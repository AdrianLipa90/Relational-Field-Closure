import math


C = 299_792_458.0


def intention_charge(hbar, rhythm, intention):
    return hbar * rhythm * intention


def phase_energy(hbar, delta_tau, rhythm, intention):
    return hbar * rhythm * intention / delta_tau


def test_phase_intention_energy_is_linear_in_action_charge():
    hbar = 2.5
    rhythm = 1.4
    intention = -0.6
    delta_tau = 0.25
    j_i = intention_charge(hbar, rhythm, intention)
    h_phi = phase_energy(hbar, delta_tau, rhythm, intention)
    assert delta_tau * h_phi == j_i
    assert h_phi == j_i / delta_tau


def test_bound_rfc_epsilon_q_is_inverse_floquet_time_step():
    for delta_tau in (2.0, 0.5, 0.125):
        epsilon_q = 1.0 / delta_tau
        assert epsilon_q > 0.0
        assert math.isfinite(epsilon_q)


def test_extensive_source_mass_equals_phase_energy_over_c2_in_bound_sector():
    hbar = 1.0
    rhythm = 3.0
    intention = 0.75
    delta_tau = 0.2
    q_sigma = intention_charge(hbar, rhythm, intention)
    epsilon_q = 1.0 / delta_tau
    h_phi = phase_energy(hbar, delta_tau, rhythm, intention)
    m_q = epsilon_q * q_sigma / (C * C)
    assert math.isclose(m_q, h_phi / (C * C), rel_tol=1e-15, abs_tol=0.0)


def test_normalized_cell_mass_factorization_preserves_total_mass():
    p = [0.2, 0.3, 0.5]
    q_sigma = 4.0
    delta_tau = 0.25
    m_total = q_sigma / (C * C * delta_tau)
    cells = [m_total * x for x in p]
    assert math.isclose(sum(cells), m_total, rel_tol=1e-15, abs_tol=0.0)


def test_zero_intention_charge_maps_to_zero_phase_energy_without_ratio():
    delta_tau = 0.4
    j_i = intention_charge(1.0, 2.0, 0.0)
    h_phi = phase_energy(1.0, delta_tau, 2.0, 0.0)
    assert j_i == 0.0
    assert h_phi == 0.0
    assert delta_tau * h_phi == j_i
