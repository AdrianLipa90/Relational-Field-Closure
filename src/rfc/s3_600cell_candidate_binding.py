from __future__ import annotations

from dataclasses import dataclass
import math

STATUS = "CANDIDATE"
ACTIVE_WORKING_VERSION = True
CANONICAL = False
PHYSICAL_BINDING = "OPEN"
SUPPORTED_L = tuple(range(6))
PHI = (1.0 + math.sqrt(5.0)) / 2.0

_ADJ = {
    0: 12.0,
    1: 6.0 * PHI,
    2: 4.0 * PHI,
    3: 3.0,
    4: 0.0,
    5: -2.0,
}


class RFC600CellCandidateError(ValueError):
    pass


@dataclass(frozen=True)
class S3SectorBinding:
    ell: int
    multiplicity: int
    adjacency_eigenvalue: float
    angular_eigenvalue: int
    status: str
    active_working_version: bool
    canonical: bool
    physical_binding: str


def bind_s3_sector(ell: int) -> S3SectorBinding:
    if isinstance(ell, bool) or not isinstance(ell, int) or ell not in SUPPORTED_L:
        raise RFC600CellCandidateError("ell must be an integer in [0,5]")
    return S3SectorBinding(
        ell=ell,
        multiplicity=(ell + 1) ** 2,
        adjacency_eigenvalue=_ADJ[ell],
        angular_eigenvalue=ell * (ell + 2),
        status=STATUS,
        active_working_version=ACTIVE_WORKING_VERSION,
        canonical=CANONICAL,
        physical_binding=PHYSICAL_BINDING,
    )


def working_sector_table() -> tuple[S3SectorBinding, ...]:
    return tuple(bind_s3_sector(ell) for ell in SUPPORTED_L)


def supported_dimension() -> int:
    return sum(row.multiplicity for row in working_sector_table())
