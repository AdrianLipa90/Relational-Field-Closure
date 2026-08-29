import math

import pytest

from src.rfc.idt_phase_clock_projector import (
    PhaseClockProjectorError,
    connection_response_stress_correction,
    eta_one_projector_stress,
    frozen_one_form_dust_stress,
    gauge_covariant_phase_covector,
    gauge_transform_pair,
    material_alignment_defect,
    material_alignment_gamma,
    normalized_phase_covector,
    phase_clock_projector,
    projector_metric_derivative,
    response_is_zero,
    unit_surface_defect,
)


MINKOWSKI_INV = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)

ZERO4 = tuple(tuple(0.0 for _ in range(4)) for _ in range(4))


def test_idt_01ac_gauge_covariant_one_form_is_invariant():
    dtheta = (2.0, -1.0, 0.5, 3.0)
    connection = (-0.25, 0.4, 1.5, -2.0)
    dlam = (10.0, -4.0, 2.0, 0.75)
    q0 = gauge_covariant_phase_covector(dtheta, connection)
    dtheta_p, connection_p = gauge_transform_pair(dtheta, connection, dlam)
    q1 = gauge_covariant_phase_covector(dtheta_p, connection_p)
    assert q1 == pytest.approx(q0)


def test_phase_clock_projector_unit_timelike_surface():
    mu = 2.5
    q = (-mu, 0.0, 0.0, 0.0)
    assert phase_clock_projector(MINKOWSKI_INV, q, mu) == pytest.approx(1.0)
    assert unit_surface_defect(MINKOWSKI_INV, q, mu) == pytest.approx(0.0)


def test_independent_calibration_scale_is_not_tautological():
    q = (-2.0, 0.0, 0.0, 0.0)
    assert phase_clock_projector(MINKOWSKI_INV, q, 2.0) == pytest.approx(1.0)
    assert phase_clock_projector(MINKOWSKI_INV, q, 4.0) == pytest.approx(0.25)


def test_frozen_one_form_metric_derivative_is_rank_one():
    mu = 3.0
    q = (-mu, 0.0, 0.0, 0.0)
    derivative = projector_metric_derivative(q, mu)
    assert derivative[0][0] == pytest.approx(-1.0)
    assert sum(abs(v) for row in derivative for v in row) == pytest.approx(1.0)


def test_frozen_one_form_fprime_half_gives_dust_stress():
    mu = 4.0
    U = 7.0
    q = (-mu, 0.0, 0.0, 0.0)
    T = frozen_one_form_dust_stress(U, q, mu)
    assert T[0][0] == pytest.approx(U)
    assert T[1][1] == pytest.approx(0.0)
    assert T[2][2] == pytest.approx(0.0)
    assert T[3][3] == pytest.approx(0.0)


def test_connection_metric_response_is_kept_as_explicit_tensor_correction():
    mu = 2.0
    U = 5.0
    fp = 0.5
    q = (-mu, 0.0, 0.0, 0.0)
    response = (
        (0.2, 0.0, 0.0, 0.0),
        (0.0, -0.1, 0.0, 0.0),
        (0.0, 0.0, 0.3, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    )
    frozen = eta_one_projector_stress(U, fp, q, mu)
    full = eta_one_projector_stress(
        U,
        fp,
        q,
        mu,
        connection_metric_response_contraction=response,
    )
    correction = connection_response_stress_correction(U, fp, mu, response)
    for i in range(4):
        for j in range(4):
            assert full[i][j] - frozen[i][j] == pytest.approx(correction[i][j])


def test_response_zero_gate():
    assert response_is_zero(ZERO4)
    response = [list(row) for row in ZERO4]
    response[1][1] = 1e-8
    assert not response_is_zero(response)
    assert response_is_zero(response, atol=1e-7)


def test_phase_clock_material_congruence_alignment_zero_defect():
    u_cov = (-1.0, 0.0, 0.0, 0.0)
    nu_contra = (1.0, 0.0, 0.0, 0.0)
    assert material_alignment_gamma(u_cov, nu_contra) == pytest.approx(1.0)
    assert material_alignment_defect(u_cov, nu_contra) == pytest.approx(0.0)


def test_boosted_material_congruence_has_positive_alignment_defect():
    beta = 0.6
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    u_cov = (-1.0, 0.0, 0.0, 0.0)
    nu_contra = (gamma, gamma * beta, 0.0, 0.0)
    assert material_alignment_gamma(u_cov, nu_contra) == pytest.approx(gamma)
    assert material_alignment_defect(u_cov, nu_contra) == pytest.approx(gamma - 1.0)


def test_normalized_phase_covector_uses_independent_mu_phase():
    assert normalized_phase_covector((-6.0, 0.0, 0.0, 0.0), 3.0) == pytest.approx(
        (-2.0, 0.0, 0.0, 0.0)
    )


def test_fail_closed_inputs():
    with pytest.raises(PhaseClockProjectorError):
        phase_clock_projector(MINKOWSKI_INV, (-1.0, 0.0, 0.0, 0.0), 0.0)
    with pytest.raises(PhaseClockProjectorError):
        gauge_covariant_phase_covector((1.0,), (0.0, 0.0, 0.0, 0.0))
    with pytest.raises(PhaseClockProjectorError):
        response_is_zero(((0.0,),))
    with pytest.raises(PhaseClockProjectorError):
        response_is_zero(ZERO4, atol=-1.0)
