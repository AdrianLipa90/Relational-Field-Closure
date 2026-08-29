from __future__ import annotations

import math
from collections.abc import Sequence


class CommonProjectiveCellAreaError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise CommonProjectiveCellAreaError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise CommonProjectiveCellAreaError(f"{name} must be positive")
    return value


def constant_cell_area(a_fs: float, omega: float, c: float = 1.0) -> float:
    a_fs = _positive("a_fs", a_fs)
    omega = _positive("omega", omega)
    c = _positive("c", c)
    return (c * c / (omega * omega)) * a_fs


def area_ratio(a_fs_radial: float, a_fs_clock: float, omega_radial: float, r_0: float) -> float:
    a_fs_radial = _positive("a_fs_radial", a_fs_radial)
    a_fs_clock = _positive("a_fs_clock", a_fs_clock)
    omega_radial = _positive("omega_radial", omega_radial)
    r_0 = _positive("r_0", r_0)
    return (a_fs_radial / a_fs_clock) * (r_0 / omega_radial) ** 2


def area_defect(area_radial: float, area_clock: float) -> float:
    area_radial = _positive("area_radial", area_radial)
    area_clock = _positive("area_clock", area_clock)
    return abs(area_radial - area_clock) / (area_radial + area_clock)


def area_defect_from_ratio(chi_a: float) -> float:
    chi_a = _positive("chi_a", chi_a)
    return abs(chi_a - 1.0) / (chi_a + 1.0)


def same_source_ledger(
    radial_cell_id: str,
    clock_cell_id: str,
    radial_area_carrier_id: str,
    clock_area_carrier_id: str,
    radial_clock_carrier_id: str,
    clock_clock_carrier_id: str,
) -> bool:
    ids = (
        radial_cell_id,
        clock_cell_id,
        radial_area_carrier_id,
        clock_area_carrier_id,
        radial_clock_carrier_id,
        clock_clock_carrier_id,
    )
    if any(not isinstance(value, str) or not value for value in ids):
        raise CommonProjectiveCellAreaError("source-ledger IDs must be nonempty strings")
    return (
        radial_cell_id == clock_cell_id
        and radial_area_carrier_id == clock_area_carrier_id
        and radial_clock_carrier_id == clock_clock_carrier_id
    )


def admitted_common_area(
    radial_cell_id: str,
    clock_cell_id: str,
    radial_area_carrier_id: str,
    clock_area_carrier_id: str,
    radial_clock_carrier_id: str,
    clock_clock_carrier_id: str,
    a_fs_radial: float,
    a_fs_clock: float,
    omega_radial: float,
    r_0: float,
    c: float = 1.0,
) -> float:
    if not same_source_ledger(
        radial_cell_id,
        clock_cell_id,
        radial_area_carrier_id,
        clock_area_carrier_id,
        radial_clock_carrier_id,
        clock_clock_carrier_id,
    ):
        raise CommonProjectiveCellAreaError("radial and clock consumers do not share one source ledger")

    a_fs_radial = _positive("a_fs_radial", a_fs_radial)
    a_fs_clock = _positive("a_fs_clock", a_fs_clock)
    omega_radial = _positive("omega_radial", omega_radial)
    r_0 = _positive("r_0", r_0)
    c = _positive("c", c)

    if not math.isclose(a_fs_radial, a_fs_clock, rel_tol=0.0, abs_tol=1.0e-12):
        raise CommonProjectiveCellAreaError("shared area carrier has inconsistent a_FS values")
    if not math.isclose(omega_radial, r_0, rel_tol=0.0, abs_tol=1.0e-12):
        raise CommonProjectiveCellAreaError("shared phase-clock carrier has inconsistent rates")

    area_r = constant_cell_area(a_fs_radial, omega_radial, c)
    area_c = constant_cell_area(a_fs_clock, r_0, c)
    if not math.isclose(area_r, area_c, rel_tol=1.0e-12, abs_tol=1.0e-12):
        raise CommonProjectiveCellAreaError("same-source ledger failed area equality")
    return 0.5 * (area_r + area_c)


def nonuniform_cell_area(
    da_fs_weights: Sequence[float],
    omega_values: Sequence[float],
    c: float = 1.0,
) -> float:
    if not da_fs_weights or len(da_fs_weights) != len(omega_values):
        raise CommonProjectiveCellAreaError("weights and phase rates must be nonempty and aligned")
    c = _positive("c", c)
    weights = tuple(_finite(f"da_fs_weights[{i}]", x) for i, x in enumerate(da_fs_weights))
    rates = tuple(_positive(f"omega_values[{i}]", x) for i, x in enumerate(omega_values))
    if any(x < 0.0 for x in weights) or math.fsum(weights) <= 0.0:
        raise CommonProjectiveCellAreaError("projective area weights must be nonnegative with positive total")
    return math.fsum((c * c / (omega * omega)) * weight for weight, omega in zip(weights, rates))
