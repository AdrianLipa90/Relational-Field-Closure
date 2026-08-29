import pytest


def inv_matrix(a):
    n = len(a)
    aug = [
        [float(x) for x in row] + [1.0 if i == j else 0.0 for j in range(n)]
        for i, row in enumerate(a)
    ]
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(aug[r][i]))
        aug[i], aug[pivot] = aug[pivot], aug[i]
        p = aug[i][i]
        if abs(p) < 1e-14:
            raise ValueError("singular")
        aug[i] = [x / p for x in aug[i]]
        for r in range(n):
            if r == i:
                continue
            f = aug[r][i]
            aug[r] = [aug[r][c] - f * aug[i][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def adm_metric(h, lapse, shift):
    b_cov = [sum(h[i][j] * shift[j] for j in range(3)) for i in range(3)]
    b2 = sum(shift[i] * b_cov[i] for i in range(3))
    return [
        [-lapse*lapse+b2, b_cov[0], b_cov[1], b_cov[2]],
        [b_cov[0], h[0][0], h[0][1], h[0][2]],
        [b_cov[1], h[1][0], h[1][1], h[1][2]],
        [b_cov[2], h[2][0], h[2][1], h[2][2]],
    ]


def project_matter(g, lapse, T):
    gi = inv_matrix(g)
    n_cov = [-lapse, 0.0, 0.0, 0.0]
    n_up = matvec(gi, n_cov)

    # h_mu^alpha = delta_mu^alpha + n_mu n^alpha
    proj = [[(1.0 if mu == a else 0.0) + n_cov[mu] * n_up[a] for a in range(4)] for mu in range(4)]

    rho = sum(T[m][n] * n_up[m] * n_up[n] for m in range(4) for n in range(4))
    t_n = [sum(T[a][b] * n_up[b] for b in range(4)) for a in range(4)]
    j = [-sum(proj[mu][a] * t_n[a] for a in range(4)) for mu in range(4)]
    S = [[sum(proj[mu][a] * proj[nu][b] * T[a][b] for a in range(4) for b in range(4)) for nu in range(4)] for mu in range(4)]
    return n_cov, n_up, proj, rho, j, S


def reconstruct(n_cov, rho, j, S):
    return [[rho*n_cov[m]*n_cov[n] + n_cov[m]*j[n] + j[m]*n_cov[n] + S[m][n] for n in range(4)] for m in range(4)]


def max_error(a, b):
    return max(abs(a[i][j]-b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def test_adapted_orthonormal_frame_signs():
    g = [[-1.0,0,0,0],[0,1.0,0,0],[0,0,1.0,0],[0,0,0,1.0]]
    T = [
        [2.5, -0.3, 0.7, -0.1],
        [-0.3, 1.2, 0.2, 0.0],
        [0.7, 0.2, 0.8, -0.4],
        [-0.1, 0.0, -0.4, 1.7],
    ]
    n_cov, n_up, _, rho, j, S = project_matter(g, 1.0, T)
    assert n_up == pytest.approx([1.0,0.0,0.0,0.0])
    assert rho == pytest.approx(T[0][0])
    for i in range(3):
        assert j[i+1] == pytest.approx(-T[0][i+1])
        for k in range(3):
            assert S[i+1][k+1] == pytest.approx(T[i+1][k+1])
    assert max_error(reconstruct(n_cov, rho, j, S), T) < 1e-12


def test_generic_adm_reconstruction_and_spatiality():
    h = [[2.0,0.2,0.1],[0.2,1.4,0.05],[0.1,0.05,0.9]]
    lapse = 0.8
    shift = [0.25,-0.1,0.2]
    g = adm_metric(h, lapse, shift)
    T = [
        [3.0, 0.4, -0.2, 0.1],
        [0.4, 1.1, 0.15, -0.05],
        [-0.2, 0.15, 0.7, 0.12],
        [0.1, -0.05, 0.12, 1.4],
    ]
    n_cov, n_up, _, rho, j, S = project_matter(g, lapse, T)
    assert max_error(reconstruct(n_cov, rho, j, S), T) < 2e-12
    assert sum(n_up[mu] * j[mu] for mu in range(4)) == pytest.approx(0.0, abs=1e-12)
    for nu in range(4):
        assert sum(n_up[mu] * S[mu][nu] for mu in range(4)) == pytest.approx(0.0, abs=2e-12)


def test_trace_identity():
    h = [[1.5,0.1,0.0],[0.1,1.2,0.05],[0.0,0.05,0.8]]
    lapse = 1.3
    shift = [-0.15,0.3,0.05]
    g = adm_metric(h, lapse, shift)
    gi = inv_matrix(g)
    T = [
        [1.7,-0.2,0.1,0.3],
        [-0.2,0.9,0.04,0.0],
        [0.1,0.04,1.3,-0.1],
        [0.3,0.0,-0.1,0.6],
    ]
    n_cov, n_up, _, rho, _, S = project_matter(g, lapse, T)
    trace_T = sum(gi[m][n]*T[m][n] for m in range(4) for n in range(4))
    # h^mn = g^mn + n^m n^n
    h_up = [[gi[m][n] + n_up[m]*n_up[n] for n in range(4)] for m in range(4)]
    trace_S = sum(h_up[m][n]*S[m][n] for m in range(4) for n in range(4))
    assert trace_T == pytest.approx(-rho + trace_S, abs=2e-12)


def test_projection_linearity():
    g = [[-1.0,0,0,0],[0,1.0,0,0],[0,0,1.0,0],[0,0,0,1.0]]
    A = [[0.2*(i+1)*(j+1) for j in range(4)] for i in range(4)]
    A = [[0.5*(A[i][j]+A[j][i]) for j in range(4)] for i in range(4)]
    B = [[(-0.07)*(i+j+1) for j in range(4)] for i in range(4)]
    B = [[0.5*(B[i][j]+B[j][i]) for j in range(4)] for i in range(4)]
    C = [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
    pa = project_matter(g, 1.0, A)
    pb = project_matter(g, 1.0, B)
    pc = project_matter(g, 1.0, C)
    assert pc[3] == pytest.approx(pa[3]+pb[3])
    for mu in range(4):
        assert pc[4][mu] == pytest.approx(pa[4][mu]+pb[4][mu])
        for nu in range(4):
            assert pc[5][mu][nu] == pytest.approx(pa[5][mu][nu]+pb[5][mu][nu])
