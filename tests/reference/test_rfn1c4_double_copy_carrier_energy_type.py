import math


def kappa(alpha, omega, gamma, scale_factor):
    Mstar = scale_factor * omega / 2
    Mbar = alpha * Mstar / gamma
    return 1 / (Mbar * Mbar)


def test_kinetic_carrier_scale_reproduces_rfg17_expression():
    a, w, g = 0.47, 1.3, 0.8
    assert math.isclose(kappa(a, w, g, 1), 4 * g * g / (a * a * w * w), rel_tol=1e-15)


def test_total_rest_scale_gives_quarter_kappa():
    a, w, g = 0.51, 0.9, 1.2
    kkin = kappa(a, w, g, 1)
    krest = kappa(a, w, g, 2)
    assert math.isclose(krest, kkin / 4, rel_tol=1e-15)


def test_total_rest_expression():
    a, w, g = 0.61, 1.7, 0.73
    assert math.isclose(kappa(a, w, g, 2), g * g / (a * a * w * w), rel_tol=1e-15)


def test_reduced_gravity_scale_doubles_between_type_surfaces():
    a, w, g = 0.48, 1.1, 0.92
    mkin = a * (w / 2) / g
    mrest = a * w / g
    assert math.isclose(mrest, 2 * mkin, rel_tol=1e-15)


def test_horizon_holonomy_discriminates_scale_type_when_gamma_is_fixed():
    a, w, g = 0.55, 1.25, 0.88
    kh = kappa(a, w, g, 2)
    MHT = 1 / kh
    assert math.isclose(g * g / (a * a * w * w), 1 / MHT, rel_tol=1e-15)
    assert not math.isclose(4 * g * g / (a * a * w * w), 1 / MHT, rel_tol=1e-12)


def test_scale_type_coordinate_is_one_or_two_on_defined_surfaces():
    omega = 1.4
    eps = omega / 2
    assert math.isclose(eps / eps, 1.0)
    assert math.isclose(omega / eps, 2.0)
