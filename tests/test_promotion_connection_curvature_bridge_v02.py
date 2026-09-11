import numpy as np

from rfc.promotion_connection_curvature_bridge_v01 import (
    connection_defect,
    curvature_defect,
    exact_bridge,
    tangential_normal_split,
)


def _exact_embedding(dim_old: int):
    promotion = np.vstack([np.eye(dim_old), np.zeros((dim_old, dim_old))]).astype(complex)
    connection_old = 1j * np.diag(np.arange(1, dim_old + 1))
    connection_new = np.block([
        [connection_old, np.zeros((dim_old, dim_old))],
        [np.zeros((dim_old, dim_old)), np.zeros((dim_old, dim_old))],
    ])
    curvature_old = connection_old @ connection_old
    curvature_new = connection_new @ connection_new
    return promotion, connection_old, connection_new, curvature_old, curvature_new


def test_bridge_scales_across_1q_to_4q_promotion_dimensions():
    for dim_old in (2, 4, 8):
        promotion, connection_old, connection_new, curvature_old, curvature_new = _exact_embedding(dim_old)
        assert np.allclose(connection_defect(promotion, connection_old, connection_new), 0.0, atol=1e-12)
        assert np.allclose(curvature_defect(promotion, curvature_old, curvature_new), 0.0, atol=1e-12)
        verdict = exact_bridge(
            promotion,
            connection_old,
            connection_new,
            curvature_old,
            curvature_new,
            atol=1e-12,
        )
        assert verdict["accepted"]


def test_tangential_normal_split_reconstructs_for_2_4_8_complex_dimensions():
    for dim_old in (2, 4, 8):
        promotion = np.vstack([np.eye(dim_old), np.zeros((dim_old, dim_old))]).astype(complex)
        connection_old = np.zeros((dim_old, dim_old), dtype=complex)
        connection_new = np.zeros((2 * dim_old, 2 * dim_old), dtype=complex)
        derivative = np.vstack([np.zeros((dim_old, dim_old)), np.eye(dim_old)]).astype(complex)
        parallel, normal = tangential_normal_split(
            promotion,
            connection_old,
            connection_new,
            derivative,
        )
        xi = connection_defect(promotion, connection_old, connection_new, derivative)
        assert np.allclose(promotion @ parallel + normal, xi, atol=1e-12)
        assert np.linalg.norm(normal) > 0.0
