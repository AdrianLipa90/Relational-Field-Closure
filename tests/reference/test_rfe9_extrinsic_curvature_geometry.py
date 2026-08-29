import pytest


def det3(h):
    return (
        h[0][0]*(h[1][1]*h[2][2]-h[1][2]*h[2][1])
        - h[0][1]*(h[1][0]*h[2][2]-h[1][2]*h[2][0])
        + h[0][2]*(h[1][0]*h[2][1]-h[1][1]*h[2][0])
    )


def inv3(h):
    d = det3(h)
    return [
        [(h[1][1]*h[2][2]-h[1][2]*h[2][1])/d, (h[0][2]*h[2][1]-h[0][1]*h[2][2])/d, (h[0][1]*h[1][2]-h[0][2]*h[1][1])/d],
        [(h[1][2]*h[2][0]-h[1][0]*h[2][2])/d, (h[0][0]*h[2][2]-h[0][2]*h[2][0])/d, (h[0][2]*h[1][0]-h[0][0]*h[1][2])/d],
        [(h[1][0]*h[2][1]-h[1][1]*h[2][0])/d, (h[0][1]*h[2][0]-h[0][0]*h[2][1])/d, (h[0][0]*h[1][1]-h[0][1]*h[1][0])/d],
    ]


def extrinsic(hdot, sym_shift_grad, lapse):
    if lapse <= 0:
        raise ValueError("lapse must be positive")
    return [[(-hdot[i][j] + sym_shift_grad[i][j])/(2.0*lapse) for j in range(3)] for i in range(3)]


def trace(h, k):
    hi = inv3(h)
    return sum(hi[i][j]*k[i][j] for i in range(3) for j in range(3))


def shear(h, k):
    tr = trace(h, k)
    return [[k[i][j]-h[i][j]*tr/3.0 for j in range(3)] for i in range(3)]


def trace_tensor(h, a):
    hi = inv3(h)
    return sum(hi[i][j]*a[i][j] for i in range(3) for j in range(3))


def test_static_zero_shift_gives_zero_extrinsic_curvature():
    z = [[0.0]*3 for _ in range(3)]
    k = extrinsic(z, z, 1.0)
    assert k == z


def test_killing_shift_control_gives_zero_for_static_metric():
    hdot = [[0.0]*3 for _ in range(3)]
    sym_killing = [[0.0]*3 for _ in range(3)]
    assert extrinsic(hdot, sym_killing, 2.0) == [[0.0]*3 for _ in range(3)]


def test_isotropic_expansion_certificate():
    a = 2.5
    aprime = 0.2
    lapse = 1.25
    h = [[a*a if i == j else 0.0 for j in range(3)] for i in range(3)]
    hdot = [[2.0*a*aprime if i == j else 0.0 for j in range(3)] for i in range(3)]
    z = [[0.0]*3 for _ in range(3)]
    k = extrinsic(hdot, z, lapse)
    expected_diag = -(a*aprime)/lapse
    for i in range(3):
        for j in range(3):
            assert k[i][j] == pytest.approx(expected_diag if i == j else 0.0)
    assert trace(h, k) == pytest.approx(-3.0*aprime/(a*lapse))
    aij = shear(h, k)
    assert max(abs(x) for row in aij for x in row) < 1e-12


def test_trace_free_shear_identity_for_generic_symmetric_k():
    h = [[2.0,0.2,0.0],[0.2,1.4,0.1],[0.0,0.1,0.9]]
    k = [[0.5,0.1,-0.2],[0.1,-0.3,0.05],[-0.2,0.05,0.7]]
    aij = shear(h, k)
    assert trace_tensor(h, aij) == pytest.approx(0.0, abs=1e-12)


def test_reconstruction_from_trace_and_shear():
    h = [[1.3,0.1,0.0],[0.1,1.1,0.0],[0.0,0.0,0.8]]
    k = [[0.2,0.03,0.0],[0.03,-0.1,0.02],[0.0,0.02,0.4]]
    tr = trace(h, k)
    aij = shear(h, k)
    for i in range(3):
        for j in range(3):
            reconstructed = aij[i][j] + h[i][j]*tr/3.0
            assert reconstructed == pytest.approx(k[i][j])


def test_shift_gradient_enters_symmetrically():
    hdot = [[0.0]*3 for _ in range(3)]
    sym = [[1.0,0.4,0.0],[0.4,-0.2,0.3],[0.0,0.3,0.5]]
    k = extrinsic(hdot, sym, 2.0)
    for i in range(3):
        for j in range(3):
            assert k[i][j] == pytest.approx(k[j][i])
            assert k[i][j] == pytest.approx(sym[i][j]/4.0)


def test_nonpositive_lapse_rejected():
    z = [[0.0]*3 for _ in range(3)]
    with pytest.raises(ValueError):
        extrinsic(z, z, 0.0)
