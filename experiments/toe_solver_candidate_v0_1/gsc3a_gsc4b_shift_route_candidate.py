from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Sequence

STATUS = "CANDIDATE_ONLY"
SOURCE_REPO = "AdrianLipa90/Relational-Field-Closure"
SOURCE_COMMIT = "85bbb1d0754605be2720b6bd258b486b0a072345"
SOURCE_GSC3A = "src/rfc/clock_transverse_matching_flow.py"
SOURCE_GSC4B = "src/rfc/flow_adapted_zero_shift_atlas.py"


def _v3(v: Sequence[float]):
    if len(v) != 3: raise ValueError("expected 3-vector")
    out=tuple(float(x) for x in v)
    if not all(math.isfinite(x) for x in out): raise ValueError("non-finite vector")
    return out


def _m3(a: Sequence[Sequence[float]]):
    if len(a)!=3 or any(len(r)!=3 for r in a): raise ValueError("expected 3x3")
    out=tuple(tuple(float(x) for x in r) for r in a)
    if not all(math.isfinite(x) for r in out for x in r): raise ValueError("non-finite matrix")
    return out


def matvec(a, v):
    a=_m3(a); v=_v3(v)
    return tuple(sum(a[i][k]*v[k] for k in range(3)) for i in range(3))


def expected_target_shift(spatial_jacobian, source_shift, time_drift):
    ab=matvec(spatial_jacobian, source_shift); d=_v3(time_drift)
    return tuple(ab[i]-d[i] for i in range(3))


def matching_residual(spatial_jacobian, source_shift, time_drift, target_shift):
    e=expected_target_shift(spatial_jacobian,source_shift,time_drift); t=_v3(target_shift)
    return max(abs(e[i]-t[i]) for i in range(3))


def clock_transverse_pairing_residual(shift):
    b=_v3(shift)
    spatial=tuple(-b[i]+b[i] for i in range(3))
    return max(abs(x) for x in spatial)


def zero_shift_route_status(*, product_trivialization_certified: bool,
                            interval_complete_flow_or_proper_clock_witness: bool,
                            physical_event_placement_witness: bool):
    admitted = bool(product_trivialization_certified)
    return {
        "gsc3a_local_soldering": "EXECUTABLE_CONFORMANCE_AVAILABLE",
        "interval_complete_flow_or_proper_clock_witness": bool(interval_complete_flow_or_proper_clock_witness),
        "physical_event_placement_witness": bool(physical_event_placement_witness),
        "product_trivialization_certified": admitted,
        "gsc4b_zero_shift_admitted": admitted,
        "shift_blocker_status": "ELIMINATED_BY_ADMITTED_GSC4B" if admitted else "CONDITIONALLY_ELIMINABLE_BLOCKED_WITNESS",
    }
