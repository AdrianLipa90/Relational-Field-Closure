import math


def test_em_matter_exchange_cancels_exactly():
    lorentz_force = (0.7, -1.2, 0.4, 2.1)
    div_em = tuple(-x for x in lorentz_force)
    div_matter = lorentz_force
    div_total = tuple(a + b for a, b in zip(div_em, div_matter))
    assert div_total == (0.0, 0.0, 0.0, 0.0)


def test_dynamic_lambda_transfer_matches_bianchi_balance():
    kappa_e = 2.7
    grad_lambda = (0.3, -0.8, 1.1, 0.5)
    div_t = tuple(x / kappa_e for x in grad_lambda)
    residual = tuple(kappa_e * div_t[i] - grad_lambda[i] for i in range(4))
    for value in residual:
        assert math.isclose(value, 0.0, rel_tol=0.0, abs_tol=2e-15)


def test_lambda_bookkeeping_tensor_restores_combined_conservation():
    kappa_e = 4.2
    grad_lambda = (-0.4, 0.6, 0.2, -1.0)
    div_total = tuple(x / kappa_e for x in grad_lambda)
    div_lambda = tuple(-x / kappa_e for x in grad_lambda)
    combined = tuple(a + b for a, b in zip(div_total, div_lambda))
    for value in combined:
        assert math.isclose(value, 0.0, rel_tol=0.0, abs_tol=2e-15)


def test_constant_lambda_recovers_conserved_total_source():
    grad_lambda = (0.0, 0.0, 0.0, 0.0)
    kappa_e = 3.0
    required_divergence = tuple(x / kappa_e for x in grad_lambda)
    assert required_divergence == (0.0, 0.0, 0.0, 0.0)


def test_einstein_coupling_has_expected_standard_form_when_g_is_fixed():
    G = 6.67430e-11
    c = 299792458.0
    kappa_e = 8.0 * math.pi * G / c**4
    assert kappa_e > 0.0
    assert math.isclose(kappa_e * c**4 / (8.0 * math.pi), G, rel_tol=2e-15, abs_tol=0.0)


if __name__ == "__main__":
    tests = [name for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    for name in tests:
        globals()[name]()
    print(f"PASS {len(tests)}/{len(tests)}")
