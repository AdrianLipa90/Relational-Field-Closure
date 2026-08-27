import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PAIR = ROOT / "validation" / "IDT_RFC_PNCS_SOURCE_HOLONOMY_PAIR_V0_1.json"
LOCK = ROOT / "CROSS_REFERENCE_LOCK.json"
EXPECTED_PNCS = "fa517208e40873523d1c2a5b7fdb852092421afa"
EXPECTED_LOOPS = [
    "SOURCE.CARRIER.NORMALIZATION.ROUNDTRIP",
    "SOURCE.CARRIER.Q0_OCCUPATION.ROUNDTRIP",
    "SOURCE.CARRIER.EPSILON_MASS_DENSITY.ROUNDTRIP",
    "SOURCE.PHASE_INTENTION.EULER_CHARGE_ENERGY.ROUNDTRIP",
    "SOURCE.PHASE_NOETHER.COLLECTIVE_CARRIER.ROUNDTRIP",
]


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_pair_receipt_matches_rfc_cross_reference_lock():
    pair = _load(PAIR)
    lock = _load(LOCK)
    assert pair["schema"] == "IDT_RFC_PNCS_SOURCE_HOLONOMY_PAIR_V0_1"
    assert pair["local_repository"] == "AdrianLipa90/Relational-Field-Closure"
    pncs_upstream = next(
        row for row in lock["upstreams"]
        if row["role"] == "gremlin_pnv_candidate_authoring_information_holonomy_and_source_loop_contracts"
    )
    assert pair["pncs"]["code_commit"] == EXPECTED_PNCS
    assert pncs_upstream["commit"] == EXPECTED_PNCS
    assert pair["pncs"]["loops"] == EXPECTED_LOOPS
    assert lock["pncs_source_holonomy_loops"] == EXPECTED_LOOPS


def test_pair_receipt_records_executed_peer_reference_gates():
    pair = _load(PAIR)
    assert pair["idt"]["status"] == "PASS"
    assert pair["idt"]["passed"] >= 356
    assert pair["idt"]["failed"] == 0
    assert pair["rfc"]["status"] == "PASS"
    assert pair["rfc"]["passed"] >= 48
    assert pair["rfc"]["failed"] == 0
    assert pair["pncs"]["native_ci"]["classification"] == "CI_EXECUTION_UNRESOLVED_PRE_TEST"
    assert pair["pncs"]["native_ci"]["code_test_failure_observed"] is False


def test_noether_carrier_is_distinct_from_intention_charge_and_rotor_coordinate():
    pair = _load(PAIR)
    interface = pair["interface"]
    assert interface["euler_closed_intention_charge"] == "J_I^EB=hbar*theta_I^EB"
    assert interface["rotor_kinetic_carrier"] == "P_Phi^EB=J-J_I^EB"
    assert interface["noether_collective_charge"] == "Q_theta=I_A*(P_Phi^EB/I_phi)"
    assert interface["energy_per_finite_noether_carrier"] == "epsilon_N^EB=H_Phi^EB/Q_theta"
    assert interface["exact_inertia_binding_reduction"] == (
        "I_A=I_phi => Q_theta=P_Phi^EB and epsilon_N^EB=P_Phi^EB/(2 I_phi)=(1/2)D_tau_chi"
    )


def test_inertia_binding_defect_remains_explicit():
    pair = _load(PAIR)
    assert pair["interface"]["inertia_binding_defect"] == "Delta_I=abs(I_A/I_phi-1)"
    assert pair["interface"]["physical_cross_binding"] == "OPEN"
