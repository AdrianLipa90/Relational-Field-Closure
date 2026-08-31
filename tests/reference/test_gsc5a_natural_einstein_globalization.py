import pytest

from src.rfc.natural_einstein_globalization import (
    MetricAtlasOverlap,
    NaturalEinsteinGlobalizationError,
    NaturalEinsteinPatch,
    certify_natural_einstein_globalization,
)


G_P = ((-1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0))
G_Q = ((-1.0, 0.0, 0.0, 0.0), (0.0, 0.25, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0))
J_QP = ((1.0, 0.0, 0.0, 0.0), (0.0, 2.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0))
I4 = ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0))


def patch(name, metric, *, source="matter-1", receipt=None, lam=0.1, kappa=2.0, solved=True, operator="RF-E24:EINSTEIN_OPERATOR"):
    return NaturalEinsteinPatch(
        name=name,
        metric=metric,
        cosmological_constant=lam,
        kappa_e=kappa,
        source_field_lineage_id=source,
        local_solution_receipt_id=receipt or f"solution:{name}",
        local_solution_certified=solved,
        einstein_operator_lineage_id=operator,
    )


def test_smooth_shared_metric_plus_patch_solutions_derives_tensor_gluing():
    p = patch("p", G_P)
    q = patch("q", G_Q)
    cert = certify_natural_einstein_globalization(
        [p, q],
        [MetricAtlasOverlap("p", "q", J_QP)],
        shared_atlas_certified=True,
        smooth_atlas_certified=True,
        domain_coverage_certified=True,
    )
    assert cert.metric_overlap_gluing is True
    assert cert.einstein_overlap_covariance == "DERIVED_FROM_METRIC_NATURALITY"
    assert cert.stress_overlap_covariance == "DERIVED_FROM_LOCAL_EQUATION"
    assert cert.residual_overlap_covariance == "DERIVED_ZERO_TENSOR"
    assert cert.global_einstein_carrier is True
    assert cert.max_metric_overlap_residual == pytest.approx(0.0)


def test_domain_coverage_remains_separate_promotion_coordinate():
    p = patch("p", G_P)
    cert = certify_natural_einstein_globalization(
        [p],
        [],
        shared_atlas_certified=True,
        smooth_atlas_certified=True,
        domain_coverage_certified=False,
    )
    assert cert.einstein_overlap_covariance == "DERIVED_FROM_METRIC_NATURALITY"
    assert cert.global_einstein_carrier is False


def test_smoothness_parent_controls_naturality_promotion():
    p = patch("p", G_P)
    cert = certify_natural_einstein_globalization(
        [p],
        [],
        shared_atlas_certified=True,
        smooth_atlas_certified=False,
        domain_coverage_certified=True,
    )
    assert cert.einstein_overlap_covariance == "PARENT_REGULARITY_OPEN"
    assert cert.global_einstein_carrier is False


def test_metric_overlap_mismatch_fails_closed():
    p = patch("p", G_P)
    q = patch("q", G_P)
    with pytest.raises(NaturalEinsteinGlobalizationError, match="metric pullback"):
        certify_natural_einstein_globalization(
            [p, q], [MetricAtlasOverlap("p", "q", J_QP)]
        )


def test_patchwise_solution_receipt_is_required():
    p = patch("p", G_P, solved=False)
    with pytest.raises(NaturalEinsteinGlobalizationError, match="local solution receipt"):
        certify_natural_einstein_globalization([p], [])


def test_common_source_lineage_is_required():
    p = patch("p", G_P, source="matter-a")
    q = patch("q", G_P, source="matter-b")
    with pytest.raises(NaturalEinsteinGlobalizationError, match="source field lineage mismatch"):
        certify_natural_einstein_globalization(
            [p, q], [MetricAtlasOverlap("p", "q", I4)]
        )


def test_common_operator_lineage_and_constants_are_required():
    p = patch("p", G_P)
    q_bad_operator = patch("q", G_P, operator="other")
    with pytest.raises(NaturalEinsteinGlobalizationError, match="operator lineage mismatch"):
        certify_natural_einstein_globalization(
            [p, q_bad_operator], [MetricAtlasOverlap("p", "q", I4)]
        )

    q_bad_lambda = patch("q", G_P, lam=0.2)
    with pytest.raises(NaturalEinsteinGlobalizationError, match="cosmological constant mismatch"):
        certify_natural_einstein_globalization(
            [p, q_bad_lambda], [MetricAtlasOverlap("p", "q", I4)]
        )

    q_bad_kappa = patch("q", G_P, kappa=3.0)
    with pytest.raises(NaturalEinsteinGlobalizationError, match="kappa_e mismatch"):
        certify_natural_einstein_globalization(
            [p, q_bad_kappa], [MetricAtlasOverlap("p", "q", I4)]
        )


def test_disconnected_multi_patch_atlas_fails_closed():
    p = patch("p", G_P)
    q = patch("q", G_P)
    r = patch("r", G_P)
    with pytest.raises(NaturalEinsteinGlobalizationError, match="disconnected"):
        certify_natural_einstein_globalization(
            [p, q, r], [MetricAtlasOverlap("p", "q", I4)]
        )


def test_reduced_contract_contains_no_independent_einstein_stress_or_residual_matrices():
    fields = set(NaturalEinsteinPatch.__dataclass_fields__)
    assert "metric" in fields
    assert "einstein" not in fields
    assert "stress" not in fields
    assert "residual" not in fields
