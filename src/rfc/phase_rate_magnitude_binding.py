from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Sequence


C = 299_792_458.0


class PhaseMagnitudeBindingError(ValueError):
    pass


@dataclass(frozen=True)
class PhaseMagnitudePatch:
    patch_id: str
    clock_id: str
    phase_magnitude_field_id: str
    omega_t: float

    @property
    def magnitude(self) -> float:
        return abs(self.omega_t)

    @property
    def spatial_scale(self) -> float:
        return C / (math.sqrt(6.0) * self.magnitude)


@dataclass(frozen=True)
class PhaseMagnitudeOverlapResult:
    patch_p: str
    patch_q: str
    same_clock: bool
    same_magnitude_field: bool
    magnitude_defect: float
    scale_defect: float
    signed_rate_equal: bool
    spatial_scale_binding: bool


@dataclass(frozen=True)
class PhaseMagnitudeBindingCertificate:
    overlaps: tuple[PhaseMagnitudeOverlapResult, ...]
    max_magnitude_defect: float
    max_scale_defect: float
    signed_rate_identity_required: bool
    spatial_scale_binding_certified: bool
    production_status: str


def phase_magnitude_patch(
    patch_id: str,
    clock_id: str,
    phase_magnitude_field_id: str,
    omega_t: float,
) -> PhaseMagnitudePatch:
    value = float(omega_t)
    if not patch_id or not clock_id or not phase_magnitude_field_id:
        raise PhaseMagnitudeBindingError("patch, clock and magnitude-field identifiers must be non-empty")
    if not math.isfinite(value) or value == 0.0:
        raise PhaseMagnitudeBindingError("phase rate must be finite and nonzero")
    return PhaseMagnitudePatch(
        patch_id=str(patch_id),
        clock_id=str(clock_id),
        phase_magnitude_field_id=str(phase_magnitude_field_id),
        omega_t=value,
    )


def certify_phase_rate_magnitude_binding(
    patches: Sequence[PhaseMagnitudePatch],
    overlaps: Iterable[tuple[str, str]],
    *,
    tolerance: float = 1.0e-12,
) -> PhaseMagnitudeBindingCertificate:
    if not math.isfinite(tolerance) or tolerance < 0.0:
        raise PhaseMagnitudeBindingError("tolerance must be finite and nonnegative")
    by_id = {patch.patch_id: patch for patch in patches}
    if len(by_id) != len(patches):
        raise PhaseMagnitudeBindingError("patch identifiers must be unique")

    results: list[PhaseMagnitudeOverlapResult] = []
    for patch_p, patch_q in overlaps:
        if patch_p not in by_id or patch_q not in by_id:
            raise PhaseMagnitudeBindingError("overlap references unknown patch")
        p = by_id[patch_p]
        q = by_id[patch_q]
        same_clock = p.clock_id == q.clock_id
        same_field = p.phase_magnitude_field_id == q.phase_magnitude_field_id
        magnitude_defect = abs(p.magnitude - q.magnitude)
        scale_defect = abs(p.spatial_scale - q.spatial_scale)
        signed_equal = math.isclose(p.omega_t, q.omega_t, rel_tol=0.0, abs_tol=tolerance)
        spatial_binding = same_clock and same_field and magnitude_defect <= tolerance
        results.append(
            PhaseMagnitudeOverlapResult(
                patch_p=patch_p,
                patch_q=patch_q,
                same_clock=same_clock,
                same_magnitude_field=same_field,
                magnitude_defect=magnitude_defect,
                scale_defect=scale_defect,
                signed_rate_equal=signed_equal,
                spatial_scale_binding=spatial_binding,
            )
        )

    max_mag = max((r.magnitude_defect for r in results), default=0.0)
    max_scale = max((r.scale_defect for r in results), default=0.0)
    certified = all(r.spatial_scale_binding for r in results)
    return PhaseMagnitudeBindingCertificate(
        overlaps=tuple(results),
        max_magnitude_defect=max_mag,
        max_scale_defect=max_scale,
        signed_rate_identity_required=False,
        spatial_scale_binding_certified=certified,
        production_status="PRODUCTION_PHASE_MAGNITUDE_FIELD_SOURCE_OPEN",
    )


def require_spatial_scale_binding(certificate: PhaseMagnitudeBindingCertificate) -> None:
    if not certificate.spatial_scale_binding_certified:
        raise PhaseMagnitudeBindingError("phase-rate magnitude source binding is not certified")
