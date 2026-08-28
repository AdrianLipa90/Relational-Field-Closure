import math


C = 299_792_458.0


def euler_intention_phase(*, D, epsilon_eb, phi_ab, phi_berry, phi_euler, theta_prior=0.0):
    return 2.0 * math.pi * (D + epsilon_eb) - phi_ab - phi_berry - phi_euler - theta_prior


def euler_action_charge(*, hbar, theta_i):
    return hbar * theta_i


def rotor_phase_energy(*, j_total, j_i, i_phi):
    if i_phi <= 0.0:
        raise ValueError("i_phi must be positive")
    return (j_total - j_i) ** 2 / (2.0 * i_phi)


def epsilon_after_euler(*, h_phi, j_i):
    if j_i <= 0.0 or h_phi <= 0.0:
        raise ValueError("positive non-degenerate sector required")
    return h_phi / j_i


def test_euler_closure_precedes_rfc_energy_per_charge_assignment():
    theta_i = euler_intention_phase(
        D=1,
        epsilon_eb=0.0,
        phi_ab=math.pi / 2.0,
        phi_berry=math.pi / 4.0,
        phi_euler=math.pi / 4.0,
    )
    j_i = euler_action_charge(hbar=1.0, theta_i=theta_i)
    assert math.isclose(theta_i, math.pi, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(j_i, math.pi, rel_tol=0.0, abs_tol=1e-15)


def test_rfc_epsilon_candidate_comes_from_euler_closed_rotor_ratio():
    j_i = math.pi
    h_phi = rotor_phase_energy(j_total=2.0 * math.pi, j_i=j_i, i_phi=2.0)
    epsilon_i = epsilon_after_euler(h_phi=h_phi, j_i=j_i)
    assert math.isclose(h_phi, math.pi**2 / 4.0, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(epsilon_i, math.pi / 4.0, rel_tol=0.0, abs_tol=1e-15)


def test_effective_floquet_step_is_reconstructed_from_euler_closed_sector():
    j_i = math.pi
    h_phi = math.pi**2 / 4.0
    epsilon_i = epsilon_after_euler(h_phi=h_phi, j_i=j_i)
    delta_tau_eff = 1.0 / epsilon_i
    assert math.isclose(delta_tau_eff * h_phi, j_i, rel_tol=1e-15, abs_tol=0.0)


def test_extensive_source_mass_equals_rotor_phase_energy_over_c2_in_bound_sector():
    j_i = math.pi
    h_phi = math.pi**2 / 4.0
    epsilon_i = epsilon_after_euler(h_phi=h_phi, j_i=j_i)
    m_q = epsilon_i * j_i / (C * C)
    assert math.isclose(m_q, h_phi / (C * C), rel_tol=1e-15, abs_tol=0.0)


def test_normalized_cell_mass_factorization_preserves_total_mass():
    p = [0.2, 0.3, 0.5]
    j_i = math.pi
    h_phi = math.pi**2 / 4.0
    epsilon_i = epsilon_after_euler(h_phi=h_phi, j_i=j_i)
    m_total = epsilon_i * j_i / (C * C)
    cells = [m_total * x for x in p]
    assert math.isclose(sum(cells), m_total, rel_tol=1e-15, abs_tol=0.0)


def test_degenerate_sector_does_not_force_finite_epsilon_q():
    for h_phi, j_i in ((0.0, 1.0), (1.0, 0.0), (0.0, 0.0)):
        try:
            epsilon_after_euler(h_phi=h_phi, j_i=j_i)
        except ValueError:
            pass
        else:
            raise AssertionError("degenerate sector must remain gated")


def test_rotor_inertia_must_be_positive():
    try:
        rotor_phase_energy(j_total=2.0, j_i=1.0, i_phi=0.0)
    except ValueError:
        pass
    else:
        raise AssertionError("non-positive rotor inertia must fail closed")
