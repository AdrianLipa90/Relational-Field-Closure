import cmath
import itertools
import math


def omega():
    return cmath.exp(2j * math.pi / 3.0)


def z_nu(state):
    w = omega()
    se, sm, st = state
    return se + w * sm + (w ** 2) * st


def matmul(A, B):
    rows, inner, cols = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def dagger(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]


def max_defect(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def test_three_neutrino_flavour_bipolar_channels_give_eight_sectors():
    sectors = list(itertools.product((1, -1), repeat=3))
    assert len(sectors) == 8


def test_neutrino_root_of_unity_frame_closes():
    w = omega()
    assert abs(1 + w + w ** 2) < 1e-12


def test_aligned_neutrino_bipolar_sectors_are_projection_zero():
    assert abs(z_nu((1, 1, 1))) < 1e-12
    assert abs(z_nu((-1, -1, -1))) < 1e-12


def test_six_non_aligned_sectors_have_equal_magnitude():
    sectors = list(itertools.product((1, -1), repeat=3))
    excited = [s for s in sectors if s not in ((1, 1, 1), (-1, -1, -1))]
    assert len(excited) == 6
    assert all(math.isclose(abs(z_nu(s)), 2.0, rel_tol=1e-12, abs_tol=1e-12) for s in excited)


def test_unitary_flavour_rotation_preserves_total_norm():
    c = math.cos(0.43)
    s = math.sin(0.43)
    U = [[c, s, 0.0], [-s, c, 0.0], [0.0, 0.0, 1.0]]
    a = [0.4 + 0.2j, -0.1 + 0.3j, 0.2 - 0.6j]
    ap = [sum(U[i][j] * a[j] for j in range(3)) for i in range(3)]
    assert math.isclose(sum(abs(x) ** 2 for x in a), sum(abs(x) ** 2 for x in ap), rel_tol=1e-12, abs_tol=1e-12)


def test_neutrino_charge_zero_is_exact_null_control_for_any_rotation():
    c = math.cos(0.52)
    s = math.sin(0.52)
    U = [[1.0, 0.0, 0.0], [0.0, c, s], [0.0, -s, c]]
    Qnu = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    transformed = matmul(matmul(dagger(U), Qnu), U)
    assert max_defect(transformed, Qnu) == 0.0


def test_charge_degenerate_flavour_subspace_preserves_em_source_operator():
    c = math.cos(0.31)
    s = math.sin(0.31)
    U = [[c, s, 0.0], [-s, c, 0.0], [0.0, 0.0, 1.0]]
    q = -1.0
    Q = [[q, 0.0, 0.0], [0.0, q, 0.0], [0.0, 0.0, q]]
    transformed = matmul(matmul(dagger(U), Q), U)
    assert max_defect(transformed, Q) < 1e-12


def test_mixing_across_different_charges_fails_source_preservation_gate():
    c = math.cos(0.39)
    s = math.sin(0.39)
    U = [[c, s, 0.0], [-s, c, 0.0], [0.0, 0.0, 1.0]]
    Q = [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]
    transformed = matmul(matmul(dagger(U), Q), U)
    assert max_defect(transformed, Q) > 1e-6
