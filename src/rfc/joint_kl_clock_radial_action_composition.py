from __future__ import annotations

import math
from collections.abc import Sequence


class JointKLCompositionError(ValueError):
    pass


def _finite(name: str, x: float) -> float:
    x = float(x)
    if not math.isfinite(x):
        raise JointKLCompositionError(f"{name} must be finite")
    return x


def _positive(name: str, x: float) -> float:
    x = _finite(name, x)
    if x <= 0.0:
        raise JointKLCompositionError(f"{name} must be positive")
    return x


def _nonnegative(name: str, x: float) -> float:
    x = _finite(name, x)
    if x < 0.0:
        raise JointKLCompositionError(f"{name} must be nonnegative")
    return x


def _prob(name: str, xs: Sequence[float], positive: bool = False) -> tuple[float, ...]:
    if not xs:
        raise JointKLCompositionError(f"{name} must be nonempty")
    out = tuple(_finite(f"{name}[{i}]", x) for i, x in enumerate(xs))
    if positive and any(x <= 0.0 for x in out):
        raise JointKLCompositionError(f"{name} entries must be positive")
    if not positive and any(x < 0.0 for x in out):
        raise JointKLCompositionError(f"{name} entries must be nonnegative")
    if not math.isclose(math.fsum(out), 1.0, abs_tol=1.0e-12, rel_tol=0.0):
        raise JointKLCompositionError(f"{name} must sum to one")
    return out


def discrete_kl(p: Sequence[float], q: Sequence[float]) -> float:
    p = _prob("p", p)
    q = _prob("q", q, positive=True)
    if len(p) != len(q):
        raise JointKLCompositionError("probability vectors must have equal length")
    value = math.fsum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0.0)
    return max(0.0, value)


def phi(x: float) -> float:
    x = _positive("x", x)
    return max(0.0, x - 1.0 - math.log(x))


def rate_kl(r_s: float, r_0: float) -> float:
    r_s = _positive("r_s", r_s)
    r_0 = _positive("r_0", r_0)
    return max(0.0, math.log(r_s / r_0) + r_0 / r_s - 1.0)


def product_kl(j_radial: float, j_clock: float) -> float:
    return _nonnegative("j_radial", j_radial) + _nonnegative("j_clock", j_clock)


def _joint(joint: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if not joint or not joint[0]:
        raise JointKLCompositionError("joint must be nonempty")
    width = len(joint[0])
    rows = []
    for i, row in enumerate(joint):
        if len(row) != width:
            raise JointKLCompositionError("joint rows must have equal length")
        checked = tuple(_finite(f"joint[{i}][{k}]", x) for k, x in enumerate(row))
        if any(x < 0.0 for x in checked):
            raise JointKLCompositionError("joint entries must be nonnegative")
        rows.append(checked)
    if not math.isclose(math.fsum(math.fsum(r) for r in rows), 1.0, abs_tol=1.0e-12, rel_tol=0.0):
        raise JointKLCompositionError("joint must sum to one")
    return tuple(rows)


def marginals(joint: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], tuple[float, ...]]:
    m = _joint(joint)
    pr = tuple(math.fsum(row) for row in m)
    pc = tuple(math.fsum(m[i][k] for i in range(len(m))) for k in range(len(m[0])))
    return pr, pc


def mutual_information(joint: Sequence[Sequence[float]]) -> float:
    m = _joint(joint)
    pr, pc = marginals(m)
    value = math.fsum(
        x * math.log(x / (pr[i] * pc[k]))
        for i, row in enumerate(m)
        for k, x in enumerate(row)
        if x > 0.0
    )
    return max(0.0, value)


def joint_kl_product_reference(joint: Sequence[Sequence[float]], pi_r: Sequence[float], pi_c: Sequence[float]) -> float:
    m = _joint(joint)
    qr = _prob("pi_r", pi_r, positive=True)
    qc = _prob("pi_c", pi_c, positive=True)
    if len(m) != len(qr) or len(m[0]) != len(qc):
        raise JointKLCompositionError("joint shape must match product reference")
    value = math.fsum(
        x * math.log(x / (qr[i] * qc[k]))
        for i, row in enumerate(m)
        for k, x in enumerate(row)
        if x > 0.0
    )
    return max(0.0, value)


def chain_components(joint: Sequence[Sequence[float]], pi_r: Sequence[float], pi_c: Sequence[float]) -> tuple[float, float, float, float]:
    pr, pc = marginals(joint)
    return (
        joint_kl_product_reference(joint, pi_r, pi_c),
        discrete_kl(pr, pi_r),
        discrete_kl(pc, pi_c),
        mutual_information(joint),
    )


def xi(j_nats: float, area_rel: float) -> float:
    return _nonnegative("j_nats", j_nats) / _positive("area_rel", area_rel)


def joint_potential(alpha_joint: float, kappa_e: float, xi_r: float, xi_c: float, xi_x: float = 0.0) -> float:
    return _finite("alpha_joint", alpha_joint) * (
        _nonnegative("xi_r", xi_r) + _nonnegative("xi_c", xi_c) + _nonnegative("xi_x", xi_x)
    ) / _positive("kappa_e", kappa_e)


def decomposed_potential(alpha_i: float, alpha_clk: float, alpha_x: float, kappa_e: float, xi_r: float, xi_c: float, xi_x: float = 0.0) -> float:
    kappa_e = _positive("kappa_e", kappa_e)
    return (
        _finite("alpha_i", alpha_i) * _nonnegative("xi_r", xi_r)
        + _finite("alpha_clk", alpha_clk) * _nonnegative("xi_c", xi_c)
        + _finite("alpha_x", alpha_x) * _nonnegative("xi_x", xi_x)
    ) / kappa_e


def basis_residuals(alpha_joint: float, alpha_i: float, alpha_clk: float, alpha_x: float, kappa_e: float) -> tuple[float, float, float]:
    k = _positive("kappa_e", kappa_e)
    aj = _finite("alpha_joint", alpha_joint)
    return ((aj - _finite("alpha_i", alpha_i)) / k, (aj - _finite("alpha_clk", alpha_clk)) / k, (aj - _finite("alpha_x", alpha_x)) / k)


def coupling_ratio(alpha_clk: float, alpha_i: float) -> float:
    ai = _finite("alpha_i", alpha_i)
    if ai == 0.0:
        raise JointKLCompositionError("alpha_i must be nonzero for a ratio")
    return _finite("alpha_clk", alpha_clk) / ai


def additivity_defect(j_joint: float, j_r: float, j_c: float, j_x: float) -> float:
    vals = tuple(_nonnegative(name, value) for name, value in (("j_joint", j_joint), ("j_r", j_r), ("j_c", j_c), ("j_x", j_x)))
    denom = math.fsum(vals)
    if denom <= 0.0:
        raise JointKLCompositionError("additivity defect requires information support")
    return abs(vals[0] - vals[1] - vals[2] - vals[3]) / denom


def factorization_defect(j_x: float) -> float:
    j_x = _nonnegative("j_x", j_x)
    return j_x / (1.0 + j_x)


def c_delta_fs() -> float:
    return 8.0 / (9.0 * math.sqrt(3.0) * math.pi)


def zeta_unity_coupling() -> float:
    return (1.0 / c_delta_fs()) ** (1.0 / 3.0)
