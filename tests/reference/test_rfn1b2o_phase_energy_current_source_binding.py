import math


def phase_current_density(amplitude, r_n):
    if amplitude < 0 or r_n <= 0:
        raise ValueError("positive-source sector requires A>=0 and r_n>0")
    return 2.0 * amplitude**2 * r_n


def phase_energy_density(amplitude, r_n):
    if amplitude < 0 or r_n <= 0:
        raise ValueError("positive-source sector requires A>=0 and r_n>0")
    return amplitude**2 * r_n**2


def epsilon_local(r_n):
    if r_n <= 0:
        raise ValueError("positive normal phase rate required")
    return 0.5 * r_n


def test_local_energy_current_factorization():
    a, r = 1.7, 3.4
    j = phase_current_density(a, r)
    e = phase_energy_density(a, r)
    assert math.isclose(e, epsilon_local(r) * j, rel_tol=1e-15)


def test_mass_density_is_energy_density_over_c_squared():
    a, r, c = 0.81, 2.3, 299792458.0
    rho_from_energy = phase_energy_density(a, r) / c**2
    rho_from_carrier = epsilon_local(r) * phase_current_density(a, r) / c**2
    assert math.isclose(rho_from_energy, rho_from_carrier, rel_tol=1e-15)


def test_local_identity_survives_nonuniform_cells():
    amplitudes = [0.4, 0.9, 1.3, 0.7]
    rates = [1.2, 2.1, 0.8, 3.3]
    volumes = [0.5, 1.1, 0.7, 0.9]
    lhs = sum(phase_energy_density(a, r) * v for a, r, v in zip(amplitudes, rates, volumes))
    rhs = sum(epsilon_local(r) * phase_current_density(a, r) * v for a, r, v in zip(amplitudes, rates, volumes))
    assert math.isclose(lhs, rhs, rel_tol=1e-15)


def test_collective_common_rate_recovers_rotor_ratio():
    amplitudes = [0.5, 1.0, 1.4]
    volumes = [0.8, 0.6, 1.2]
    r = 2.7
    q_theta = sum(phase_current_density(a, r) * v for a, v in zip(amplitudes, volumes))
    h_phase = sum(phase_energy_density(a, r) * v for a, v in zip(amplitudes, volumes))
    assert math.isclose(h_phase / q_theta, r / 2.0, rel_tol=1e-15)


def test_lapse_form_matches_rfn1b2n():
    a, r_t, n_r = 1.1, 4.8, 1.6
    r_n = r_t / n_r
    e = phase_energy_density(a, r_n)
    j = phase_current_density(a, r_n)
    assert math.isclose(e / j, r_t / (2.0 * n_r), rel_tol=1e-15)


def test_additional_energy_sector_is_separate_coordinate():
    a, r = 1.2, 1.9
    e_phase = phase_energy_density(a, r)
    extra_sector = 0.37
    e_total = e_phase + extra_sector
    assert not math.isclose(e_total, epsilon_local(r) * phase_current_density(a, r), rel_tol=1e-12)


def test_positive_source_sector_is_fail_closed():
    for a, r in ((1.0, 0.0), (1.0, -0.2), (-1.0, 1.0)):
        try:
            phase_current_density(a, r)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid positive-source inputs must be rejected")
