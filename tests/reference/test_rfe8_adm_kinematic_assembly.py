import math
import pytest


def det3(h):
    return (
        h[0][0] * (h[1][1] * h[2][2] - h[1][2] * h[2][1])
        - h[0][1] * (h[1][0] * h[2][2] - h[1][2] * h[2][0])
        + h[0][2] * (h[1][0] * h[2][1] - h[1][1] * h[2][0])
    )


def inv3(h):
    d = det3(h)
    if abs(d) < 1e-14:
        raise ValueError("singular spatial metric")
    c = [
        [h[1][1]*h[2][2]-h[1][2]*h[2][1], h[0][2]*h[2][1]-h[0][1]*h[2][2], h[0][1]*h[1][2]-h[0][2]*h[1][1]],
        [h[1][2]*h[2][0]-h[1][0]*h[2][2], h[0][0]*h[2][2]-h[0][2]*h[2][0], h[0][2]*h[1][0]-h[0][0]*h[1][2]],
        [h[1][0]*h[2][1]-h[1][1]*h[2][0], h[0][1]*h[2][0]-h[0][0]*h[2][1], h[0][0]*h[1][1]-h[0][1]*h[1][0]],
    ]
    return [[x/d for x in row] for row in c]


def matvec(a, v):
    return [sum(a[i][j]*v[j] for j in range(len(v))) for i in range(len(a))]


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def detn(a):
    m = [row[:] for row in a]
    n = len(m)
    sign = 1.0
    d = 1.0
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(m[r][i]))
        if abs(m[pivot][i]) < 1e-14:
            return 0.0
        if pivot != i:
            m[i], m[pivot] = m[pivot], m[i]
            sign *= -1.0
        p = m[i][i]
        d *= p
        for r in range(i+1, n):
            f = m[r][i] / p
            for c in range(i+1, n):
                m[r][c] -= f * m[i][c]
    return sign*d


def assert_spd3(h):
    if len(h) != 3 or any(len(row) != 3 for row in h):
        raise ValueError("h must be 3x3")
    if any(abs(h[i][j]-h[j][i]) > 1e-12 for i in range(3) for j in range(3)):
        raise ValueError("h must be symmetric")
    d1 = h[0][0]
    d2 = h[0][0]*h[1][1]-h[0][1]*h[1][0]
    d3 = det3(h)
    if min(d1, d2, d3) <= 0.0:
        raise ValueError("h must be positive definite")


def adm_metric(h, lapse, shift):
    if not math.isfinite(lapse) or lapse <= 0.0:
        raise ValueError("lapse must be positive finite")
    assert_spd3(h)
    if len(shift) != 3 or any(not math.isfinite(x) for x in shift):
        raise ValueError("shift must be finite 3-vector")
    b_cov = matvec(h, shift)
    b2 = sum(shift[i]*b_cov[i] for i in range(3))
    return [
        [-lapse*lapse+b2, b_cov[0], b_cov[1], b_cov[2]],
        [b_cov[0], h[0][0], h[0][1], h[0][2]],
        [b_cov[1], h[1][0], h[1][1], h[1][2]],
        [b_cov[2], h[2][0], h[2][1], h[2][2]],
    ]


def adm_inverse(h, lapse, shift):
    hi = inv3(h)
    n2 = lapse*lapse
    out = [[0.0]*4 for _ in range(4)]
    out[0][0] = -1.0/n2
    for i in range(3):
        out[0][i+1] = shift[i]/n2
        out[i+1][0] = shift[i]/n2
    for i in range(3):
        for j in range(3):
            out[i+1][j+1] = hi[i][j]-shift[i]*shift[j]/n2
    return out


CASES = [
    ([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]], 1.0, [0.0,0.0,0.0]),
    ([[2.0,0.2,0.1],[0.2,1.5,0.05],[0.1,0.05,0.8]], 0.7, [0.2,-0.1,0.3]),
    ([[3.0,0.4,0.0],[0.4,2.0,0.2],[0.0,0.2,1.2]], 2.3, [-0.5,0.25,0.1]),
]


@pytest.mark.parametrize("h,lapse,shift", CASES)
def test_inverse_identity(h, lapse, shift):
    g = adm_metric(h, lapse, shift)
    gi = adm_inverse(h, lapse, shift)
    prod = matmul(g, gi)
    for i in range(4):
        for j in range(4):
            assert prod[i][j] == pytest.approx(1.0 if i == j else 0.0, abs=1e-11)


@pytest.mark.parametrize("h,lapse,shift", CASES)
def test_determinant_factorization(h, lapse, shift):
    g = adm_metric(h, lapse, shift)
    assert detn(g) == pytest.approx(-lapse*lapse*det3(h), rel=1e-11, abs=1e-11)


@pytest.mark.parametrize("h,lapse,shift", CASES)
def test_unit_normal(h, lapse, shift):
    gi = adm_inverse(h, lapse, shift)
    n_cov = [-lapse, 0.0, 0.0, 0.0]
    n_contra = matvec(gi, n_cov)
    assert n_contra[0] == pytest.approx(1.0/lapse)
    for i in range(3):
        assert n_contra[i+1] == pytest.approx(-shift[i]/lapse)
    contraction = sum(n_cov[i]*n_contra[i] for i in range(4))
    assert contraction == pytest.approx(-1.0)


@pytest.mark.parametrize("h,lapse,shift", CASES)
def test_spatial_projector_recovers_h(h, lapse, shift):
    g = adm_metric(h, lapse, shift)
    n_cov = [-lapse, 0.0, 0.0, 0.0]
    gamma = [[g[i][j]+n_cov[i]*n_cov[j] for j in range(4)] for i in range(4)]
    for i in range(3):
        for j in range(3):
            assert gamma[i+1][j+1] == pytest.approx(h[i][j])


def test_zero_shift_reduction():
    h = [[2.0,0.1,0.0],[0.1,1.2,0.0],[0.0,0.0,0.7]]
    lapse = 1.7
    g = adm_metric(h, lapse, [0.0,0.0,0.0])
    assert g[0][0] == pytest.approx(-lapse*lapse)
    assert g[0][1:] == [0.0,0.0,0.0]


@pytest.mark.parametrize("lapse", [0.0, -1.0, math.nan, math.inf])
def test_nonpositive_or_nonfinite_lapse_rejected(lapse):
    with pytest.raises(ValueError):
        adm_metric([[1,0,0],[0,1,0],[0,0,1]], lapse, [0,0,0])


def test_non_spd_spatial_metric_rejected():
    with pytest.raises(ValueError):
        adm_metric([[1,0,0],[0,-1,0],[0,0,1]], 1.0, [0,0,0])
