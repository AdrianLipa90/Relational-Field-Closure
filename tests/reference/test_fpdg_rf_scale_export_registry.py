import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "validation" / "FPDG_RF_SCALE_EXPORT_V0_1.json"


def _load():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_rf_scale_registry_is_complete_and_source_bound():
    data = _load()
    assert data["schema"] == "RFC_FPDG_RF_SCALE_EXPORT_V0_1"
    claims = data["claims"]
    assert len(claims) == 22
    ids = [c["claim_id"] for c in claims]
    assert len(ids) == len(set(ids))
    assert {c["canonical_gate_id"] for c in claims} == {f"RF-S{i}" for i in range(1, 23)}
    for claim in claims:
        assert (ROOT / claim["source_path"]).is_file(), claim["source_path"]
        assert (ROOT / claim["validation_test"]).is_file(), claim["validation_test"]
        assert claim["status"].strip()


def test_rf_scale_registry_edges_are_internal_and_acyclic():
    data = _load()
    ids = {c["claim_id"] for c in data["claims"]}
    edges = data["local_edges"]
    assert len(edges) == 23
    assert len({(e["from"], e["to"]) for e in edges}) == len(edges)
    assert all(e["authority"] == "SOURCE_EXPLICIT" for e in edges)
    assert all(e["from"] in ids and e["to"] in ids for e in edges)

    incoming = {node: 0 for node in ids}
    outgoing = {node: [] for node in ids}
    for edge in edges:
        outgoing[edge["from"]].append(edge["to"])
        incoming[edge["to"]] += 1
    ready = [node for node, degree in incoming.items() if degree == 0]
    visited = 0
    while ready:
        node = ready.pop()
        visited += 1
        for child in outgoing[node]:
            incoming[child] -= 1
            if incoming[child] == 0:
                ready.append(child)
    assert visited == len(ids), "RF-S export graph must remain acyclic"


def test_rf_s13_s22_matches_canonical_branched_scale_index():
    data = _load()
    edges = {(e["from"], e["to"]) for e in data["local_edges"]}
    expected = {
        ("RFC.SCALE.S12", "RFC.SCALE.S13"),
        ("RFC.SCALE.S13", "RFC.SCALE.S14"),
        ("RFC.SCALE.S14", "RFC.SCALE.S15"),
        ("RFC.SCALE.S15", "RFC.SCALE.S16"),
        ("RFC.SCALE.S16", "RFC.SCALE.S17"),
        ("RFC.SCALE.S17", "RFC.SCALE.S18"),
        ("RFC.SCALE.S18", "RFC.SCALE.S19"),
        ("RFC.SCALE.S17", "RFC.SCALE.S20"),
        ("RFC.SCALE.S20", "RFC.SCALE.S21"),
        ("RFC.SCALE.S21", "RFC.SCALE.S22"),
    }
    assert expected <= edges


def test_registry_has_no_promotion_authority():
    authority = _load()["authority"]
    assert authority["source_repository_owns_claim_status"] is True
    assert authority["fpdg_may_consume_as_evidence"] is True
    assert authority["claim_promotion_authority"] is False
    assert authority["gremlin_candidate_generation_authority"] is False
