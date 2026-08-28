import math


def mbar_dc(gamma, g2, mstar):
    return mstar / (gamma * g2)


def mbar_horizon(m_h, kappa_h):
    return math.sqrt(m_h * kappa_h / (2.0 * math.pi))


def mbar_thermal(m_h, t_h):
    return math.sqrt(m_h * t_h)


def test_rfg5_general_invariant_reduces_to_mbar_horizon_identity():
    gamma, g2, mstar = 0.83, 1.17, 2.9
    m_h = 5.4
    mbar = mbar_dc(gamma, g2, mstar)
    kappa = 2.0 * math.pi * mbar * mbar / m_h
    lhs = gamma**2 * g2**2 * m_h * kappa
    rhs = 2.0 * math.pi * mstar**2
    assert math.isclose(lhs, rhs, rel_tol=1e-14)
    assert math.isclose(mbar_horizon(m_h, kappa), mbar, rel_tol=1e-14)


def test_hawking_form_gives_mbar_squared_equals_M_T():
    m_h, kappa = 7.1, 0.42
    t = kappa / (2.0 * math.pi)
    assert math.isclose(mbar_horizon(m_h, kappa), mbar_thermal(m_h, t), rel_tol=1e-14)


def test_local_carrier_horizon_zero_G_crosscheck():
    beta, gamma, omega = 2.8, 0.94, 3.2
    mbar_local = beta * omega / (12.0 * gamma)
    m_h = 8.3
    t = (mbar_local * mbar_local) / m_h
    assert math.isclose(math.sqrt(m_h * t), mbar_local, rel_tol=1e-14)


def test_three_estimators_agree_on_closed_surface():
    beta, gamma, mstar = 3.3, 0.88, 1.9
    g2 = 6.0 / beta
    mbar1 = mbar_dc(gamma, g2, mstar)
    m_h = 4.2
    kappa = 2.0 * math.pi * mbar1 * mbar1 / m_h
    t = kappa / (2.0 * math.pi)
    mbar2 = mbar_horizon(m_h, kappa)
    mbar3 = mbar_thermal(m_h, t)
    assert math.isclose(mbar1, mbar2, rel_tol=1e-14)
    assert math.isclose(mbar2, mbar3, rel_tol=1e-14)


def test_adversarial_horizon_temperature_perturbation_is_detected():
    m_h, t = 6.0, 0.2
    mbar = math.sqrt(m_h * t)
    t_bad = t * 1.05
    defect = abs(math.sqrt(m_h * t_bad) - mbar) / mbar
    assert defect > 0.02
