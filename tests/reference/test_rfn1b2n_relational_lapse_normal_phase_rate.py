import math


def normal_rate(r_t, n_r):
    if n_r <= 0:
        raise ValueError("N_R must be positive")
    return r_t / n_r


def epsilon_n(r_t, n_r):
    return 0.5 * normal_rate(r_t, n_r)


def test_lapse_rate_identity():
    r_t, n_r = 7.5, 1.25
    r_n = normal_rate(r_t, n_r)
    assert math.isclose(r_t, n_r * r_n, rel_tol=1e-15)


def test_proper_time_rotor_rate_equals_normal_rate():
    r_t, n_r = 3.2, 0.8
    d_tau_chi = r_t / n_r
    assert math.isclose(d_tau_chi, normal_rate(r_t, n_r), rel_tol=1e-15)


def test_epsilon_is_half_normal_rate():
    r_t, n_r = 9.1, 1.3
    assert math.isclose(epsilon_n(r_t, n_r), 0.5 * normal_rate(r_t, n_r), rel_tol=1e-15)


def test_generator_equality_on_common_inertia_surface():
    i_a = i_phi = 4.7
    r_t, n_r = 5.4, 0.9
    r_n = normal_rate(r_t, n_r)
    q_theta = i_a * r_n
    p_phi = i_phi * r_n
    assert math.isclose(q_theta, p_phi, rel_tol=1e-15)


def test_positive_lapse_is_fail_closed():
    for bad in (0.0, -1.0):
        try:
            normal_rate(1.0, bad)
        except ValueError:
            pass
        else:
            raise AssertionError("non-positive lapse must be rejected")
