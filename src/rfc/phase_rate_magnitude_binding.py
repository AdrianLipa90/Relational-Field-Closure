from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence


C = 299_792_458.0


class PhaseMagnitudeBindingError(ValueError):
    pass


@dataclass(frozen=True)
class PhaseMagnitudeOverlapSample:
    source_patch: str
    target_patch: str
    sample_id: str
    clock_id: str
    phase_magnitude_field_id: str
    source_omega_t: float
    target_omega_t: float

    @property
    def source_magnitude(self) -> float:
        return abs(self.source_omega_t)

    @property
    def target_magnitude(self) -> float:
        return abs(self.target_omega_t)

    @property
    def source_spatial_scale(self) -> float:
        return C / (math.sqrt(6.0) * self.source_magnitude)

    @property
    def target_spatial_scale(self) -> float:
        return C / (math.sqrt(6.0) * self.target_magnitude)


@dataclass(frozen=True)
class PhaseMagnitudeOverlapResult:
    source_patch: str
    target_patch: str
    sample_id: str
    clock_id: str
    phase_magnitude_field_id: str
    magnitude_defect: float
    scale_defect: float
    signed_rate_equal: bool
    spatial_scale_binding: bool


@dataclass(frozen=True)
class PhaseMagnitudeBindingCertificate:
    samples: tuple[PhaseMagnitudeOverlapResult, ...]
    max_magnitude_defect: float
    max_scale_defect: float
    signed_rate_identity_required: bool
    overlap_local_field_semantics: bool
    spatial_scale_binding_certified: bool
    production_status: str


def phase_magnitude_overlap_sample(
    source_patch: str,
    target_patch: str,
    sample_id: str,
    clock_id: str,
    phase_magnitude_field_id: str,
    source_omega_t: float,
    target_omega_t: float,
) -> PhaseMagnitudeOverlapSample:
    source = str(source_patch).strip()
    target = str(target_patch).strip()
    sid = str(sample_id).strip()
    clock = str(clock_id).strip()
    field_id = str(phase_magnitude_field_id).strip()
    if not source or not target or source == target:
        raise PhaseMagnitudeBindingError("sample must reference two distinct non-empty patch ids")
    if not sid or not clock or not field_id:
        raise PhaseMagnitudeBindingError("sample, clock and magnitude-field identifiers must be non-empty")
    source_rate = float(source_omega_t)
    target_rate = float(target_omega_t)
    if not math.isfinite(source_rate) or source_rate == 0.0:
        raise PhaseMagnitudeBindingError("source phase rate must be finite and nonzero")
    if not math.isfinite(target_rate) or target_rate == 0.0:
        raise PhaseMagnitudeBindingError("target phase rate must be finite and nonzero")
    return PhaseMagnitudeOverlapSample(
        source_patch=source,
        target_patch=target,
        sample_id=sid,
        clock_id=clock,
        phase_magnitude_field_id=field_id,
        source_omega_t=source_rate,
        target_omega_t=target_rate,
    )


def certify_phase_rate_magnitude_binding(
    samples: Sequence[PhaseMagnitudeOverlapSample],
    *,
    tolerance: float = 1.0e-12,
) -> PhaseMagnitudeBindingCertificate:
    if not math.isfinite(tolerance) or tolerance < 0.0:
        raise PhaseMagnitudeBindingError("tolerance must be finite and nonnegative")
    seen: set[tuple[str, str, str]] = set()
    results: list[PhaseMagnitudeOverlapResult] = []
    for sample in samples:
        key = (sample.source_patch, sample.target_patch, sample.sample_id)
        if key in seen:
            raise PhaseMagnitudeBindingError("overlap sample identifiers must be unique per directed overlap")
        seen.add(key)
        magnitude_defect = abs(sample.source_magnitude - sample.target_magnitude)
        scale_defect = abs(sample.source_spatial_scale - sample.target_spatial_scale)
        signed_equal = math.isclose(
            sample.source_omega_t,
            sample.target_omega_t,
            rel_tol=0.0,
            abs_tol=tolerance,
        )
        results.append(
            PhaseMagnitudeOverlapResult(
                source_patch=sample.source_patch,
                target_patch=sample.target_patch,
                sample_id=sample.sample_id,
                clock_id=sample.clock_id,
                phase_magnitude_field_id=sample.phase_magnitude_field_id,
                magnitude_defect=magnitude_defect,
                scale_defect=scale_defect,
                signed_rate_equal=signed_equal,
                spatial_scale_binding=magnitude_defect <= tolerance,
            )
        )

    max_mag = max((r.magnitude_defect for r in results), default=0.0)
    max_scale = max((r.scale_defect for r in results), default=0.0)
    certified = all(r.spatial_scale_binding for r in results)
    return PhaseMagnitudeBindingCertificate(
        samples=tuple(results),
        max_magnitude_defect=max_mag,
        max_scale_defect=max_scale,
        signed_rate_identity_required=False,
        overlap_local_field_semantics=True,
        spatial_scale_binding_certified=certified,
        production_status="PRODUCTION_OVERLAP_LOCAL_PHASE_MAGNITUDE_FIELD_SOURCE_OPEN",
    )


def require_spatial_scale_binding(certificate: PhaseMagnitudeBindingCertificate) -> None:
    if not certificate.spatial_scale_binding_certified:
        raise PhaseMagnitudeBindingError("phase-rate magnitude source binding is not certified")
