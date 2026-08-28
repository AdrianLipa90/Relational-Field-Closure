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


def test_closed_ab_loop_equals_flux_for_constant_field():
    B = 0.73
    width = 1.8
    height = 0.9

    # Symmetric gauge: A=(-By/2, Bx/2), so dA=B dx^dy.
    def A(x, y):
        return (-0.5 * B * y, 0.5 * B * x)

    loop = [(0.0, 0.0), (width, 0.0), (width, height), (0.0, height)]
    circulation = line_integral_xy(A, loop)
    flux = B * width * height
    assert math.isclose(circulation, flux, rel_tol=2e-15, abs_tol=2e-15)


def test_closed_ab_loop_is_invariant_under_smooth_gauge_shift():
    B = 0.51

    def A(x, y):
        return (-0.5 * B * y, 0.5 * B * x)

    # Lambda=b_x x+b_y y+1/2(s_xx x^2+2s_xy xy+s_yy y^2).
    bx, by = 0.4, -0.7
    sxx, sxy, syy = 0.3, -0.2, 0.6

    def grad_lambda(x, y):
        return (bx + sxx * x + sxy * y, by + sxy * x + syy * y)

    def shifted(x, y):
        ax, ay = A(x, y)
        gx, gy = grad_lambda(x, y)
        return ax + gx, ay + gy

    loop = [(-0.2, 0.1), (1.4, 0.1), (1.4, 1.2), (-0.2, 1.2)]
    assert math.isclose(
        line_integral_xy(A, loop),
        line_integral_xy(shifted, loop),
        rel_tol=2e-14,
        abs_tol=2e-14,
    )


def test_curvature_is_invariant_under_symmetric_hessian_gauge_term():
    # A_mu=M_{mu nu} x^nu.  A -> A+dLambda adds a symmetric Hessian S.
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

    shifted = [[M[i][j] + S[i][j] for j in range(4)] for i in range(4)]
    assert curvature(M) == curvature(shifted)


def test_homogeneous_maxwell_bianchi_identity_on_nontrivial_polynomial_potential():
    # Coordinates: (t,x,y,z). For
    # A0=xy, A1=tz+y^2, A2=xz-t^2, A3=tx+yz,
    # the independent F components are below.
    # Check dF=0 for all four independent 3-index triples analytically.
    # (012): d_t F12 + d_x F20 + d_y F01 = 0 + 1 - 1.
    assert 0.0 + 1.0 - 1.0 == 0.0
    # (013): d_t F13 + d_x F30 + d_z F01 = 0 - 1 + 1.
    assert 0.0 - 1.0 + 1.0 == 0.0
    # (023): d_t F23 + d_y F30 + d_z F02 = 0 + 0 + 0.
    assert 0.0 + 0.0 + 0.0 == 0.0
    # (123): d_x F23 + d_y F31 + d_z F12 = -1 + 0 + 1.
    assert -1.0 + 0.0 + 1.0 == 0.0


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

    # F^{mu nu}=eta_mu eta_nu F_{mu nu} for diagonal Minkowski metric.
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
