import unittest
import numpy as np


class RFG0TemporalReflectionTests(unittest.TestCase):
    def test_single_cp1_pullback_rank_bound(self):
        rng = np.random.default_rng(20260827)
        # A local chart on CP^1 is two-real-dimensional. Any pullback to a
        # four-dimensional base through one CP^1 chart has rank at most two.
        J = rng.normal(size=(2, 4))
        A = rng.normal(size=(2, 2))
        g_fs = A.T @ A + np.eye(2)
        h = J.T @ g_fs @ J
        self.assertLessEqual(np.linalg.matrix_rank(h, tol=1e-10), 2)

    def test_lorentz_signature_from_temporal_one_form(self):
        rng = np.random.default_rng(20260827)
        A = rng.normal(size=(3, 3))
        h_spatial = A.T @ A + np.eye(3)
        g = np.zeros((4, 4))
        g[0, 0] = -1.0
        g[1:, 1:] = h_spatial
        ev = np.linalg.eigvalsh(g)
        self.assertEqual(np.sum(ev < -1e-10), 1)
        self.assertEqual(np.sum(ev > 1e-10), 3)

    def test_temporal_reflection_formula(self):
        rng = np.random.default_rng(12)
        A = rng.normal(size=(3, 3))
        h_spatial = A.T @ A + np.eye(3)
        h_plus = np.zeros((4, 4))
        h_plus[0, 0] = 1.0
        h_plus[1:, 1:] = h_spatial
        theta = np.array([1.0, 0.0, 0.0, 0.0])
        g = h_plus - 2.0 * np.outer(theta, theta)
        self.assertAlmostEqual(g[0, 0], -1.0)
        self.assertTrue(np.allclose(g[1:, 1:], h_spatial))

    def test_inertia_is_coordinate_invariant(self):
        rng = np.random.default_rng(44)
        g = np.diag([-1.0, 1.0, 2.0, 3.0])
        M = rng.normal(size=(4, 4))
        while abs(np.linalg.det(M)) < 0.2:
            M = rng.normal(size=(4, 4))
        gp = M.T @ g @ M
        ev = np.linalg.eigvalsh(gp)
        self.assertEqual(np.sum(ev < -1e-10), 1)
        self.assertEqual(np.sum(ev > 1e-10), 3)

    def test_null_cone_relation(self):
        h_spatial = np.diag([1.0, 4.0, 9.0])
        v = np.array([0.3, -0.4, 0.2])
        spatial_norm_sq = float(v @ h_spatial @ v)
        a = np.sqrt(spatial_norm_sq)
        X = np.concatenate(([a], v))
        g = np.zeros((4, 4))
        g[0, 0] = -1.0
        g[1:, 1:] = h_spatial
        self.assertAlmostEqual(float(X @ g @ X), 0.0, places=12)

    def test_poincare_slice_is_positive_definite(self):
        # Poincare disk has negative Gaussian curvature but positive-definite
        # spatial metric. This separates curvature sign from metric signature.
        x, y = 0.2, -0.3
        r2 = x*x + y*y
        factor = 4.0 / (1.0 - r2)**2
        h_p = factor * np.eye(2)
        ev = np.linalg.eigvalsh(h_p)
        self.assertTrue(np.all(ev > 0.0))


if __name__ == '__main__':
    unittest.main()
