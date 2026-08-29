from __future__ import annotations

import math
from dataclasses import dataclass


class GeneratorSourcePlacementError(ValueError):
    pass


Matrix4 = tuple[
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
]


MINKOWSKI_COV: Matrix4 = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)


@dataclass(frozen=True)
class SourcePlacementDiagnostic:
    energy_density: float
    isotropic_pressure: float
    equation_of_state_w: float | None
    vacuum_residual: float
    vacuum_defect: float
    vacuum_absorbable: bool


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise GeneratorSourcePlacementError(f"{name} must be finite")
    return value


def perfect_fluid_rest_tensor(energy_density: float, pressure: float) -> Matrix4:
    rho = _finite("energy_density", energy_density)
    p = _finite("pressure", pressure)
    return (
        (rho, 0.0, 0.0, 0.0),
        (0.0, p, 0.0, 0.0),
        (0.0, 0.0, p, 0.0),
        (0.0, 0.0, 0.0, p),
    )


def vacuum_stress_tensor(energy_density: float) -> Matrix4:
    rho = _finite("energy_density", energy_density)
    return tuple(
        tuple(-rho * MINKOWSKI_COV[i][j] for j in range(4))
        for i in range(4)
    )  # type: ignore[return-value]


def source_placement_diagnostic(
    energy_density: float,
    pressure: float,
    *,
    tolerance: float = 1.0e-12,
) -> SourcePlacementDiagnostic:
    rho = _finite("energy_density", energy_density)
    p = _finite("pressure", pressure)
    tol = _finite("tolerance", tolerance)
    if tol < 0.0:
        raise GeneratorSourcePlacementError("tolerance must be nonnegative")

    residual = rho + p
    scale = abs(rho) + abs(p)
    defect = 0.0 if scale == 0.0 else 2.0 * abs(residual) / scale
    w = None if rho == 0.0 else p / rho
    return SourcePlacementDiagnostic(
        energy_density=rho,
        isotropic_pressure=p,
        equation_of_state_w=w,
        vacuum_residual=residual,
        vacuum_defect=defect,
        vacuum_absorbable=abs(residual) <= tol,
    )


def lambda_shift_from_vacuum_energy(energy_density: float, kappa_E: float) -> float:
    rho = _finite("energy_density", energy_density)
    kappa = _finite("kappa_E", kappa_E)
    if kappa <= 0.0:
        raise GeneratorSourcePlacementError("kappa_E must be positive")
    return kappa * rho


def einstein_residual_after_lambda_move(
    energy_density: float,
    pressure: float,
    kappa_E: float,
) -> Matrix4:
    """Return the algebraic residual of moving a source into Lambda.

    Compare

        kappa_E T_{mu nu}

    against

        -DeltaLambda g_{mu nu},  DeltaLambda=kappa_E rho.

    The tensors coincide exactly iff the perfect-fluid source has p=-rho.
    """

    rho = _finite("energy_density", energy_density)
    p = _finite("pressure", pressure)
    kappa = _finite("kappa_E", kappa_E)
    if kappa <= 0.0:
        raise GeneratorSourcePlacementError("kappa_E must be positive")

    t = perfect_fluid_rest_tensor(rho, p)
    delta_lambda = lambda_shift_from_vacuum_energy(rho, kappa)
    return tuple(
        tuple(
            kappa * t[i][j] + delta_lambda * MINKOWSKI_COV[i][j]
            for j in range(4)
        )
        for i in range(4)
    )  # type: ignore[return-value]


def frobenius_norm4(matrix: Matrix4) -> float:
    return math.sqrt(sum(x * x for row in matrix for x in row))
