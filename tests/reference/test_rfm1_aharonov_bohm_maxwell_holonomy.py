import math


def line_integral_xy(A, points):
    total = 0.0
    for p0, p1 in zip(points, points[1:] + points[:1]):
        mx = 0.5 * (p0[0] + p1[0])
        my = 0.5 * (p0[1] + p1[1])
        ax, ay = A(mx, my)
        total += ax * (p1[0] - p0[0]) + ay * (p1[1] - p0[1])
    return total


def test_ab_curvature_recovers_physical_field_normalization():
    q = 1.7
    hbar = 2.3
    F = 0.41
    f_ab = (q / hbar) * F
    recovered = (hbar / q) * f_ab
    assert math.isclose(recovered, F, rel_tol=2e-15, abs_tol=2e-15)


def test_probe_charge_representations_recover_same_physical_potential():
    hbar = 1.91
    physical_A = (0.43, -0.82, 1.17, 0.09)
    recovered = []
    for q in (0.37, -1.6):
        a_ab = tuple((q / hbar) * value for value in physical_A)
        recovered.append(tuple((hbar / q) * value for value in a_ab))
    for candidate in recovered:
        for actual, expected in zip(candidate, physical_A):
            assert math.isclose(actual, expected, rel_tol=2e-15, abs_tol=2e-15)
    for x, y in zip(recovered[0], recovered[1]):
        assert math.isclose(x, y, rel_tol=2e-15, abs_tol=2e-15)


def test_closed_ab_loop_equals_flux_for_constant_field():
    B = 0.73
    width = 1.8
    height = 0.9

    def A(x, y):
        return (-0.5 * B * y, 0.5 * B * x)

    loop = [(0.0, 0.0), (width, 0.0), (width, height), (0.0, height)]
    circulation = line_integral_xy(A, loop)
    flux = B * width * height
    assert math.isclose(circulation, flux, rel_tol=2e-15, abs_tol=2e-15)


def test_closed_ab_loop_is_invariant_under_synchronized_gauge_shift():
    B = 0.51

    def A(x, y):
        return (-0.5 * B * y, 0.5 * B * x)

    bx, by = 0.4, -0.7
    sxx, sxy, syy = 0.3, -0.2, 0.6

    def grad_lambda(x, y):
        return (bx + sxx * x + sxy * y, by + sxy * x + syy * y)

    def shifted(x, y):
        ax, ay = A(x, y)
        gx, gy = grad_lambda(x, y)
        return ax - gx, ay - gy

    loop = [(-0.2, 0.1), (1.4, 0.1), (1.4, 1.2), (-0.2, 1.2)]
    assert math.isclose(
        line_integral_xy(A, loop),
        line_integral_xy(shifted, loop),
        rel_tol=2e-14,
        abs_tol=2e-14,
    )


def test_covariant_phase_one_form_matches_idt_sign_convention():
    dtheta = (0.4, -0.2, 0.7, 0.1)
    a = (-0.3, 0.5, 0.2, -0.4)
    dlambda = (0.6, -0.1, 0.8, 0.2)
    before = tuple(dtheta[i] + a[i] for i in range(4))
    after = tuple((dtheta[i] + dlambda[i]) + (a[i] - dlambda[i]) for i in range(4))
    for x, y in zip(before, after):
        assert math.isclose(x, y, rel_tol=2e-15, abs_tol=2e-15)


def test_curvature_is_invariant_under_symmetric_hessian_gauge_term():
    M = [
        [0.0, 1.0, -0.3, 0.2],
        [0.4, 0.0, 0.7, -0.5],
        [0.1, -0.2, 0.0, 0.9],
        [-0.6, 0.8, 0.3, 0.0],
    ]
    S = [
        [0.2, 0.1, -0.4, 0.3],
        [0.1, -0.5, 0.6, 0.0],
        [-0.4, 0.6, 0.7, -0.2],
        [0.3, 0.0, -0.2, 0.1],
    ]

    def curvature(matrix):
        return [[matrix[nu][mu] - matrix[mu][nu] for nu in range(4)] for mu in range(4)]

    shifted = [[M[i][j] - S[i][j] for j in range(4)] for i in range(4)]
    before = curvature(M)
    after = curvature(shifted)
    for mu in range(4):
        for nu in range(4):
            assert math.isclose(before[mu][nu], after[mu][nu], rel_tol=2e-15, abs_tol=2e-15)


def test_homogeneous_maxwell_bianchi_identity_on_nontrivial_polynomial_potential():
    b = (0.2, -0.4, 0.7, 0.1)
    M = [
        [0.1, 0.8, -0.2, 0.3],
        [-0.5, 0.2, 0.6, -0.7],
        [0.4, -0.1, 0.3, 0.9],
        [-0.6, 0.5, -0.8, 0.4],
    ]

    def hessian(nu, mu, rho):
        return ((nu + 1) * (mu + rho + 2) + (mu + 1) * (rho + 1)) / 37.0

    def potential(nu, x):
        linear = sum(M[nu][mu] * x[mu] for mu in range(4))
        quadratic = 0.5 * sum(
            hessian(nu, mu, rho) * x[mu] * x[rho]
            for mu in range(4)
            for rho in range(4)
        )
        return b[nu] + linear + quadratic

    def dA(nu, mu, x):
        return M[nu][mu] + sum(hessian(nu, mu, rho) * x[rho] for rho in range(4))

    def F(mu, nu, x):
        return dA(nu, mu, x) - dA(mu, nu, x)

    point = [0.31, -0.27, 0.44, 0.19]
    eps = 1e-6

    # Verify that the analytic first derivative really comes from the declared potential.
    for nu in range(4):
        for mu in range(4):
            xp = point.copy()
            xm = point.copy()
            xp[mu] += eps
            xm[mu] -= eps
            numeric = (potential(nu, xp) - potential(nu, xm)) / (2.0 * eps)
            assert math.isclose(numeric, dA(nu, mu, point), rel_tol=0.0, abs_tol=2e-10)

    assert max(abs(F(mu, nu, point)) for mu in range(4) for nu in range(4)) > 0.1

    def partial_F(alpha, beta, gamma):
        xp = point.copy()
        xm = point.copy()
        xp[alpha] += eps
        xm[alpha] -= eps
        return (F(beta, gamma, xp) - F(beta, gamma, xm)) / (2.0 * eps)

    for alpha, beta, gamma in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
        cyclic = (
            partial_F(alpha, beta, gamma)
            + partial_F(beta, gamma, alpha)
            + partial_F(gamma, alpha, beta)
        )
        assert math.isclose(cyclic, 0.0, rel_tol=0.0, abs_tol=5e-10)


def test_wilson_phase_tracks_flux_with_fixed_q_over_hbar():
    q = 0.37
    hbar = 1.91
    flux = -0.82
    phase = (q / hbar) * flux
    recovered_flux = (hbar / q) * phase
    assert math.isclose(recovered_flux, flux, rel_tol=2e-15, abs_tol=2e-15)


def test_em_stress_energy_trace_vanishes_in_four_dimensions():
    eta = [-1.0, 1.0, 1.0, 1.0]
    F = [
        [0.0, 0.7, -0.2, 0.1],
        [-0.7, 0.0, 0.4, -0.5],
        [0.2, -0.4, 0.0, 0.9],
        [-0.1, 0.5, -0.9, 0.0],
    ]

    F_up = [[eta[mu] * eta[nu] * F[mu][nu] for nu in range(4)] for mu in range(4)]
    F2 = sum(F[mu][nu] * F_up[mu][nu] for mu in range(4) for nu in range(4))

    T = [[0.0] * 4 for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            first = sum(F[mu][a] * eta[a] * F[nu][a] for a in range(4))
            metric = eta[mu] if mu == nu else 0.0
            T[mu][nu] = first - 0.25 * metric * F2

    trace = sum(eta[mu] * T[mu][mu] for mu in range(4))
    assert math.isclose(trace, 0.0, rel_tol=0.0, abs_tol=2e-14)


if __name__ == "__main__":
    tests = [name for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    for name in tests:
        globals()[name]()
    print(f"PASS {len(tests)}/{len(tests)}")
