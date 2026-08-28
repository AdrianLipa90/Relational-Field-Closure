import math


def test_em_matter_exchange_cancels_exactly():
    lorentz_force = (0.7, -1.2, 0.4, 2.1)
    div_em = tuple(-x for x in lorentz_force)
    div_matter = lorentz_force
    div_total = tuple(a + b for a, b in zip(div_em, div_matter))
    assert div_total == (0.0, 0.0, 0.0, 0.0)


def _plane_wave_field(t, x, amplitude=0.7, wave_number=1.3):
    phase = wave_number * (t - x)
    f02 = -amplitude * wave_number * math.sin(phase)
    field = [[0.0] * 4 for _ in range(4)]
    field[0][2] = f02
    field[2][0] = -f02
    field[1][2] = -f02
    field[2][1] = f02
    return field


def _em_stress_energy_up(t, x, mu_star=1.0):
    eta = (-1.0, 1.0, 1.0, 1.0)
    field = _plane_wave_field(t, x)
    field_up = [
        [eta[mu] * eta[nu] * field[mu][nu] for nu in range(4)]
        for mu in range(4)
    ]
    field2 = sum(
        field[mu][nu] * field_up[mu][nu]
        for mu in range(4)
        for nu in range(4)
    )
    t_cov = [[0.0] * 4 for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            first = sum(field[mu][a] * eta[a] * field[nu][a] for a in range(4))
            metric = eta[mu] if mu == nu else 0.0
            t_cov[mu][nu] = (first - 0.25 * metric * field2) / mu_star
    return [
        [eta[mu] * eta[nu] * t_cov[mu][nu] for nu in range(4)]
        for mu in range(4)
    ]


def test_vacuum_plane_wave_em_stress_energy_has_zero_divergence():
    t0, x0 = 0.43, -0.21
    tensor = _em_stress_energy_up(t0, x0)
    assert tensor[0][0] > 0.0
    assert math.isclose(tensor[0][0], tensor[0][1], rel_tol=2e-15, abs_tol=2e-15)
    assert math.isclose(tensor[0][0], tensor[1][1], rel_tol=2e-15, abs_tol=2e-15)

    step = 1e-6
    for nu in range(4):
        dt = (
            _em_stress_energy_up(t0 + step, x0)[0][nu]
            - _em_stress_energy_up(t0 - step, x0)[0][nu]
        ) / (2.0 * step)
        dx = (
            _em_stress_energy_up(t0, x0 + step)[1][nu]
            - _em_stress_energy_up(t0, x0 - step)[1][nu]
        ) / (2.0 * step)
        assert math.isclose(dt + dx, 0.0, rel_tol=0.0, abs_tol=2e-9)


def test_flat_flrw_einstein_tensor_satisfies_contracted_bianchi_identity():
    # ds^2 = -dt^2 + a(t)^2 d\vec{x}^2 with a nontrivial polynomial scale factor.
    for t in (0.2, 0.7, 1.1):
        a = 1.0 + 0.4 * t + 0.2 * t * t
        adot = 0.4 + 0.4 * t
        addot = 0.4
        hubble = adot / a
        dhubble = (addot * a - adot * adot) / (a * a)

        # G^0_0 and isotropic spatial Einstein tensor encoded as effective rho_G, p_G.
        rho_g = 3.0 * hubble * hubble
        p_g = -(2.0 * dhubble + 3.0 * hubble * hubble)
        drho_g = 6.0 * hubble * dhubble
        contracted_bianchi = drho_g + 3.0 * hubble * (rho_g + p_g)

        assert abs(hubble) > 0.1
        assert abs(rho_g) > 0.1
        assert math.isclose(contracted_bianchi, 0.0, rel_tol=0.0, abs_tol=2e-14)


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
