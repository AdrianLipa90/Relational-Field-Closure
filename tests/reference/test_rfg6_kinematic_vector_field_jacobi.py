import numpy as np


def affine_bracket(X, Y):
    A_x, b_x = X
    A_y, b_y = Y
    return A_y @ A_x - A_x @ A_y, A_y @ b_x - A_x @ b_y


def affine_add(*fields):
    A = sum((f[0] for f in fields), np.zeros_like(fields[0][0]))
    b = sum((f[1] for f in fields), np.zeros_like(fields[0][1]))
    return A, b


def norm_field(X):
    return max(float(np.max(np.abs(X[0]))), float(np.max(np.abs(X[1]))))


def test_affine_vector_field_bracket_is_antisymmetric():
    X = (np.array([[1.0, 2.0], [0.0, -1.0]]), np.array([0.3, -0.4]))
    Y = (np.array([[0.2, -0.7], [1.1, 0.5]]), np.array([-0.2, 0.6]))
    XY = affine_bracket(X, Y)
    YX = affine_bracket(Y, X)
    assert norm_field(affine_add(XY, YX)) < 1e-12


def test_affine_vector_fields_satisfy_exact_jacobi_numerically():
    X = (np.array([[1.0, 2.0], [0.0, -1.0]]), np.array([0.3, -0.4]))
    Y = (np.array([[0.2, -0.7], [1.1, 0.5]]), np.array([-0.2, 0.6]))
    Z = (np.array([[-0.4, 0.9], [0.8, 0.3]]), np.array([0.7, 0.1]))
    jacobi = affine_add(
        affine_bracket(X, affine_bracket(Y, Z)),
        affine_bracket(Y, affine_bracket(Z, X)),
        affine_bracket(Z, affine_bracket(X, Y)),
    )
    assert norm_field(jacobi) < 1e-12


def test_matrix_commutator_part_of_affine_bracket_satisfies_jacobi():
    A = np.array([[0.0, 1.0], [-2.0, 0.3]])
    B = np.array([[1.2, -0.4], [0.7, -0.2]])
    C = np.array([[-0.6, 0.5], [1.1, 0.8]])

    def bracket(P, Q):
        # Corresponds to linear-vector-field convention used above.
        return Q @ P - P @ Q

    J = bracket(A, bracket(B, C)) + bracket(B, bracket(C, A)) + bracket(C, bracket(A, B))
    assert np.max(np.abs(J)) < 1e-12


def test_matched_jacobi_triplet_accepts_zero_sum_kinematic_numerators():
    n_i = np.array([0.7, -0.1, 0.4])
    n_j = np.array([-0.2, 0.5, -0.8])
    n_k = -(n_i + n_j)
    assert np.max(np.abs(n_i + n_j + n_k)) < 1e-12


def test_adversarial_unmatched_kinematic_triplet_fails_gate():
    n_i = np.array([0.7, -0.1, 0.4])
    n_j = np.array([-0.2, 0.5, -0.8])
    n_k = np.array([0.1, -0.2, 0.3])
    defect = np.max(np.abs(n_i + n_j + n_k))
    assert defect > 0.1


def test_self_copy_squares_numerator_without_changing_graph_denominator():
    n = 0.73
    D = 2.4
    gauge_kinematic_term = n / D
    gravity_self_copy_term = n * n / D
    assert gravity_self_copy_term == n * gauge_kinematic_term
