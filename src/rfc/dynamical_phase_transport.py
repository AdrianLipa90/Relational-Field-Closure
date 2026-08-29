from __future__ import annotations

import math
from dataclasses import dataclass
from collections.abc import Sequence

from src.rfc.foundational_phase_source_formalism import KAPPA_INFO


class DynamicalPhaseTransportError(ValueError):
    pass


@dataclass(frozen=True)
class BoundaryFluxIdentity:
    source_density: float
    flux_divergence: float
    B_gradient_correction: float
    current_divergence_correction: float
    reconstructed_source_density: float


@dataclass(frozen=True)
class PhaseTransportState:
    phase_factor: float
    energy_per_occupation: float
    comoving_energy_rate: float
    lambda_exchange_target: float
    transport_residual: float


@dataclass(frozen=True)
class FLRWPhaseCellScaling:
    scale_factor_ratio: float
    omega_ratio: float
    phase_clock_length_ratio: float
    projective_area_ratio: float
    relational_volume_ratio: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise DynamicalPhaseTransportError(f"{name} must be finite")
    return value


def _vector(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if len(values) < 1:
        raise DynamicalPhaseTransportError(f"{name} must be nonempty")
    return tuple(_finite(f"{name}[{i}]", x) for i, x in enumerate(values))


def phase_energy_curvature_2form(
    B_action: float,
    phase_factor: float,
    dB_covector: Sequence[float],
    phase_one_form: Sequence[float],
    curvature_2form: Sequence[Sequence[float]],
) -> tuple[tuple[float, ...], ...]:
    """RF-F10 local two-form dTheta_G on the dPhi=Dtheta branch.

    For Theta_G=B X Omega, X=Phi+kappa, Omega=Dtheta and dOmega=F,

        dTheta_G = X dB wedge Omega + B X F.

    ``curvature_2form`` is supplied as an antisymmetric matrix in one chart.
    """

    B = _finite("B_action", B_action)
    X = _finite("phase_factor", phase_factor)
    dB = _vector("dB_covector", dB_covector)
    Omega = _vector("phase_one_form", phase_one_form)
    if len(dB) != len(Omega):
        raise DynamicalPhaseTransportError("dB_covector and phase_one_form must have equal length")
    n = len(dB)
    if len(curvature_2form) != n or any(len(row) != n for row in curvature_2form):
        raise DynamicalPhaseTransportError("curvature_2form must be square with matching dimension")
    F = tuple(tuple(_finite(f"curvature_2form[{i}][{j}]", curvature_2form[i][j]) for j in range(n)) for i in range(n))
    for i in range(n):
        if abs(F[i][i]) > 1e-15:
            raise DynamicalPhaseTransportError("curvature_2form diagonal must vanish")
        for j in range(i + 1, n):
            if not math.isclose(F[i][j], -F[j][i], rel_tol=0.0, abs_tol=1e-12):
                raise DynamicalPhaseTransportError("curvature_2form must be antisymmetric")

    return tuple(
        tuple(
            X * (dB[i] * Omega[j] - dB[j] * Omega[i]) + B * X * F[i][j]
            for j in range(n)
        )
        for i in range(n)
    )


def boundary_flux_source_identity(
    B_action: float,
    phase_factor: float,
    current_phase_derivative: float,
    current_B_derivative: float,
    current_divergence: float,
) -> BoundaryFluxIdentity:
    """Pointwise divergence identity for F^mu=(B/2) X^2 J^mu.

    With X=Phi+kappa and J.Xgrad supplied as ``current_phase_derivative``,

        div F = B X J.Xgrad + 1/2 X^2 J.Bgrad + 1/2 B X^2 div J.

    Hence the RF-F6 source B X J.Xgrad is recovered by subtracting the last
    two correction terms.  On constant-B conserved-current patches it is
    exactly the divergence of the boundary-flux current.
    """

    B = _finite("B_action", B_action)
    X = _finite("phase_factor", phase_factor)
    jx = _finite("current_phase_derivative", current_phase_derivative)
    jb = _finite("current_B_derivative", current_B_derivative)
    divj = _finite("current_divergence", current_divergence)

    source = B * X * jx
    B_corr = 0.5 * X * X * jb
    div_corr = 0.5 * B * X * X * divj
    flux_div = source + B_corr + div_corr
    reconstructed = flux_div - B_corr - div_corr
    return BoundaryFluxIdentity(
        source_density=source,
        flux_divergence=flux_div,
        B_gradient_correction=B_corr,
        current_divergence_correction=div_corr,
        reconstructed_source_density=reconstructed,
    )


def phase_energy_transport_state(
    B_action: float,
    B_dot: float,
    omega: float,
    omega_dot: float,
    relational_phase: float,
    *,
    lambda_dot: float = 0.0,
    kappa_E: float = 1.0,
    proper_density: float = 1.0,
    kappa: float = KAPPA_INFO,
) -> PhaseTransportState:
    """RF-F11 comoving phase-energy transport identity.

    epsilon=B*omega*X, X=Phi+kappa, Xdot=omega, therefore

        epsilon_dot = Bdot*omega*X + B*omega_dot*X + B*omega^2.

    RF-F7 dynamic-Lambda dust balance gives

        epsilon_dot = -Lambda_dot/(kappa_E*n).

    ``transport_residual`` is epsilon_dot plus Lambda_dot/(kappa_E*n).
    """

    B = _finite("B_action", B_action)
    Bdot = _finite("B_dot", B_dot)
    w = _finite("omega", omega)
    wdot = _finite("omega_dot", omega_dot)
    phi = _finite("relational_phase", relational_phase)
    kap = _finite("kappa", kappa)
    ldot = _finite("lambda_dot", lambda_dot)
    ke = _finite("kappa_E", kappa_E)
    n = _finite("proper_density", proper_density)
    if ke <= 0.0:
        raise DynamicalPhaseTransportError("kappa_E must be positive")
    if n <= 0.0:
        raise DynamicalPhaseTransportError("proper_density must be positive")

    X = phi + kap
    epsilon = B * w * X
    epsilon_dot = Bdot * w * X + B * wdot * X + B * w * w
    target = -ldot / (ke * n)
    residual = epsilon_dot - target
    return PhaseTransportState(
        phase_factor=X,
        energy_per_occupation=epsilon,
        comoving_energy_rate=epsilon_dot,
        lambda_exchange_target=target,
        transport_residual=residual,
    )


def constant_lambda_constant_B_omega_dot(omega: float, relational_phase: float, *, kappa: float = KAPPA_INFO) -> float:
    """Solve X*omega_dot+omega^2=0 for the constant-B, constant-Lambda dust branch."""

    w = _finite("omega", omega)
    phi = _finite("relational_phase", relational_phase)
    kap = _finite("kappa", kappa)
    X = phi + kap
    if X == 0.0:
        raise DynamicalPhaseTransportError("relational_phase+kappa must be nonzero")
    return -(w * w) / X


def constant_dust_phase_energy_invariant(B_action: float, omega: float, relational_phase: float, *, kappa: float = KAPPA_INFO) -> float:
    B = _finite("B_action", B_action)
    w = _finite("omega", omega)
    phi = _finite("relational_phase", relational_phase)
    kap = _finite("kappa", kappa)
    return B * w * (phi + kap)


def constant_B_dust_phase_factor_squared(
    phase_factor_initial: float,
    omega_times_phase_factor: float,
    delta_tau: float,
) -> float:
    """Integrated RF-F11 solution X^2=X0^2+2 C DeltaTau for C=omega*X."""

    X0 = _finite("phase_factor_initial", phase_factor_initial)
    C = _finite("omega_times_phase_factor", omega_times_phase_factor)
    dt = _finite("delta_tau", delta_tau)
    return X0 * X0 + 2.0 * C * dt


def constant_w_prefactor(
    normalization: float,
    omega_abs: float,
    w_eos: float,
) -> float:
    """Integrated RF-F8 family B(Phi+kappa)=C |omega|^(3w-1)."""

    C = _finite("normalization", normalization)
    rate = _finite("omega_abs", omega_abs)
    w = _finite("w_eos", w_eos)
    if rate <= 0.0:
        raise DynamicalPhaseTransportError("omega_abs must be positive")
    return C * rate ** (3.0 * w - 1.0)


def constant_w_energy_per_occupation(
    normalization: float,
    omega: float,
    w_eos: float,
) -> float:
    """For fixed orientation, epsilon=C*sgn(omega)*|omega|^(3w)."""

    C = _finite("normalization", normalization)
    rate = _finite("omega", omega)
    w = _finite("w_eos", w_eos)
    if rate == 0.0:
        raise DynamicalPhaseTransportError("omega must be nonzero")
    return math.copysign(1.0, rate) * C * abs(rate) ** (3.0 * w)


def flrw_phase_cell_scaling(scale_factor_ratio: float) -> FLRWPhaseCellScaling:
    """RF-F12 homogeneous-isotropic consequence of theta=3H and RF-F8 continuity.

    a/a0=r implies |omega|/|omega0|=r^-1, ell/ell0=r,
    A/A0=r^2 and V/V0=r^3.
    """

    r = _finite("scale_factor_ratio", scale_factor_ratio)
    if r <= 0.0:
        raise DynamicalPhaseTransportError("scale_factor_ratio must be positive")
    return FLRWPhaseCellScaling(
        scale_factor_ratio=r,
        omega_ratio=1.0 / r,
        phase_clock_length_ratio=r,
        projective_area_ratio=r * r,
        relational_volume_ratio=r**3,
    )


def flrw_phase_rate(
    omega_initial: float,
    scale_factor_initial: float,
    scale_factor_final: float,
) -> float:
    omega0 = _finite("omega_initial", omega_initial)
    a0 = _finite("scale_factor_initial", scale_factor_initial)
    a1 = _finite("scale_factor_final", scale_factor_final)
    if omega0 == 0.0:
        raise DynamicalPhaseTransportError("omega_initial must be nonzero")
    if a0 <= 0.0 or a1 <= 0.0:
        raise DynamicalPhaseTransportError("scale factors must be positive")
    return omega0 * a0 / a1


def flrw_density_scaling(
    density_initial: float,
    scale_factor_initial: float,
    scale_factor_final: float,
    w_eos: float,
) -> float:
    rho0 = _finite("density_initial", density_initial)
    a0 = _finite("scale_factor_initial", scale_factor_initial)
    a1 = _finite("scale_factor_final", scale_factor_final)
    w = _finite("w_eos", w_eos)
    if a0 <= 0.0 or a1 <= 0.0:
        raise DynamicalPhaseTransportError("scale factors must be positive")
    return rho0 * (a0 / a1) ** (3.0 * (1.0 + w))
