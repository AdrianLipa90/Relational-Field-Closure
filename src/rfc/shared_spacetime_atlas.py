"""RF-E25 shared-spacetime atlas/coframe compatibility certifier.

On an overlap p -> q the convention is
    dx_q = J_{q<-p} dx_p,
    theta_q = Lambda_{q<-p} theta_p,
so the executable coframe compatibility equation is
    E_q J_{q<-p} = Lambda_{q<-p} E_p.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable, Mapping, Sequence


class SharedSpacetimeAtlasError(ValueError):
    """Raised when declared patch/overlap data fail the RF-E25 gate."""


Matrix = tuple[tuple[float, ...], ...]
ETA: Matrix = (
    (-1.0, 0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0, 1.0),
)


def _finite(value: float, label: str) -> float:
    out = float(value)
    if not isfinite(out):
        raise SharedSpacetimeAtlasError(f"{label} must be finite")
    return out


def _matrix(value: Sequence[Sequence[float]], n: int, label: str) -> Matrix:
    if len(value) != n:
        raise SharedSpacetimeAtlasError(f"{label} must be {n}x{n}")
    rows: list[tuple[float, ...]] = []
    for i, row in enumerate(value):
        if len(row) != n:
            raise SharedSpacetimeAtlasError(f"{label} must be {n}x{n}")
        rows.append(tuple(_finite(x, f"{label}[{i}]") for x in row))
    return tuple(rows)


def _vector(value: Sequence[float], n: int, label: str) -> tuple[float, ...]:
    if len(value) != n:
        raise SharedSpacetimeAtlasError(f"{label} must have length {n}")
    return tuple(_finite(x, label) for x in value)


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b or len(a[0]) != len(b):
        raise SharedSpacetimeAtlasError("matrix dimensions do not compose")
    return tuple(
        tuple(
            sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def _minor(a: Matrix, row: int, col: int) -> Matrix:
    return tuple(
        tuple(x for j, x in enumerate(r) if j != col)
        for i, r in enumerate(a)
        if i != row
    )


def det(a: Matrix) -> float:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise SharedSpacetimeAtlasError("determinant requires a square matrix")
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return sum(((-1.0) ** j) * a[0][j] * det(_minor(a, 0, j)) for j in range(n))


def max_abs(a: Matrix) -> float:
    return max((abs(x) for row in a for x in row), default=0.0)


def subtract(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise SharedSpacetimeAtlasError("matrix shapes differ")
    return tuple(tuple(x - y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def _close_matrix(a: Matrix, b: Matrix, atol: float) -> float:
    residual = max_abs(subtract(a, b))
    scale = 1.0 + max(max_abs(a), max_abs(b))
    if residual > atol * scale:
        raise SharedSpacetimeAtlasError(
            f"matrix compatibility residual {residual:.17g} exceeds tolerance"
        )
    return residual


@dataclass(frozen=True)
class ADMPatch:
    name: str
    lapse: float
    triad: Sequence[Sequence[float]]
    shift: Sequence[float]

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise SharedSpacetimeAtlasError("patch name must be a non-empty string")
        lapse = _finite(self.lapse, f"{self.name}.lapse")
        if lapse <= 0.0:
            raise SharedSpacetimeAtlasError("ADM lapse must be strictly positive")
        triad = _matrix(self.triad, 3, f"{self.name}.triad")
        shift = _vector(self.shift, 3, f"{self.name}.shift")
        if abs(det(triad)) <= 1.0e-14:
            raise SharedSpacetimeAtlasError("spatial triad must be invertible")
        object.__setattr__(self, "lapse", lapse)
        object.__setattr__(self, "triad", triad)
        object.__setattr__(self, "shift", shift)

    @property
    def coframe(self) -> Matrix:
        rows: list[tuple[float, ...]] = [(self.lapse, 0.0, 0.0, 0.0)]
        for a in range(3):
            temporal = sum(self.triad[a][i] * self.shift[i] for i in range(3))
            rows.append((temporal, *self.triad[a]))
        return tuple(rows)

    @property
    def metric(self) -> Matrix:
        e = self.coframe
        return matmul(transpose(e), matmul(ETA, e))


@dataclass(frozen=True)
class AtlasOverlap:
    source: str
    target: str
    jacobian: Sequence[Sequence[float]]
    lorentz: Sequence[Sequence[float]]

    def __post_init__(self) -> None:
        if not isinstance(self.source, str) or not self.source:
            raise SharedSpacetimeAtlasError("overlap source must be a non-empty string")
        if not isinstance(self.target, str) or not self.target:
            raise SharedSpacetimeAtlasError("overlap target must be a non-empty string")
        if self.source == self.target:
            raise SharedSpacetimeAtlasError("self overlap is not an atlas transition")
        object.__setattr__(self, "jacobian", _matrix(self.jacobian, 4, "jacobian"))
        object.__setattr__(self, "lorentz", _matrix(self.lorentz, 4, "lorentz"))


@dataclass(frozen=True)
class SharedAtlasCertificate:
    compatible: bool
    patch_count: int
    overlap_count: int
    triangle_count: int
    max_coframe_residual: float
    max_lorentz_residual: float
    max_metric_residual: float
    max_jacobian_cocycle_residual: float
    max_lorentz_cocycle_residual: float
    production_input_status: str = "OPEN_INPUT"


def _validate_overlap(
    patches: Mapping[str, ADMPatch],
    overlap: AtlasOverlap,
    atol: float,
) -> tuple[float, float, float]:
    if overlap.source not in patches or overlap.target not in patches:
        raise SharedSpacetimeAtlasError("overlap references an unknown patch")

    j = overlap.jacobian
    lam = overlap.lorentz

    if det(j) <= atol:
        raise SharedSpacetimeAtlasError("overlap Jacobian must preserve atlas orientation")
    if abs(j[0][0] - 1.0) > atol or any(abs(j[0][i]) > atol for i in range(1, 4)):
        raise SharedSpacetimeAtlasError(
            "time-adapted overlap must preserve the shared scalar clock differential"
        )

    lorentz_residual = _close_matrix(
        matmul(transpose(lam), matmul(ETA, lam)),
        ETA,
        atol,
    )
    if det(lam) <= 0.0:
        raise SharedSpacetimeAtlasError("Lorentz transition must be proper")
    if lam[0][0] < 1.0 - atol:
        raise SharedSpacetimeAtlasError("Lorentz transition must preserve time orientation")

    ep = patches[overlap.source].coframe
    eq = patches[overlap.target].coframe
    coframe_residual = _close_matrix(matmul(eq, j), matmul(lam, ep), atol)

    gp = patches[overlap.source].metric
    gq = patches[overlap.target].metric
    metric_residual = _close_matrix(
        matmul(transpose(j), matmul(gq, j)),
        gp,
        atol,
    )
    return coframe_residual, lorentz_residual, metric_residual


def _connected(names: set[str], overlaps: Sequence[AtlasOverlap]) -> bool:
    if len(names) <= 1:
        return True
    adjacency = {name: set() for name in names}
    for item in overlaps:
        if item.source in names and item.target in names:
            adjacency[item.source].add(item.target)
            adjacency[item.target].add(item.source)
    root = next(iter(names))
    seen = {root}
    stack = [root]
    while stack:
        current = stack.pop()
        for nxt in adjacency[current] - seen:
            seen.add(nxt)
            stack.append(nxt)
    return seen == names


def certify_shared_spacetime_atlas(
    patches: Sequence[ADMPatch],
    overlaps: Sequence[AtlasOverlap],
    *,
    triangles: Iterable[tuple[str, str, str]] = (),
    atol: float = 1.0e-10,
) -> SharedAtlasCertificate:
    """Validate a shared time-oriented Lorentzian atlas on supplied patch data.

    A declared triangle (p,q,r) requires direct overlaps p->q, q->r and p->r
    and certifies both coordinate and orthonormal-frame cocycle laws.
    """

    atol = _finite(atol, "atol")
    if atol < 0.0:
        raise SharedSpacetimeAtlasError("atol must be non-negative")
    if not patches:
        raise SharedSpacetimeAtlasError("at least one ADM patch is required")

    patch_map: dict[str, ADMPatch] = {}
    for patch in patches:
        if not isinstance(patch, ADMPatch):
            raise SharedSpacetimeAtlasError("all patches must be ADMPatch instances")
        if patch.name in patch_map:
            raise SharedSpacetimeAtlasError(f"duplicate patch name {patch.name!r}")
        patch_map[patch.name] = patch

    overlap_map: dict[tuple[str, str], AtlasOverlap] = {}
    max_coframe = max_lorentz = max_metric = 0.0
    for overlap in overlaps:
        if not isinstance(overlap, AtlasOverlap):
            raise SharedSpacetimeAtlasError("all overlaps must be AtlasOverlap instances")
        key = (overlap.source, overlap.target)
        if key in overlap_map:
            raise SharedSpacetimeAtlasError(f"duplicate overlap {key!r}")
        overlap_map[key] = overlap
        c_res, l_res, m_res = _validate_overlap(patch_map, overlap, atol)
        max_coframe = max(max_coframe, c_res)
        max_lorentz = max(max_lorentz, l_res)
        max_metric = max(max_metric, m_res)

    if not _connected(set(patch_map), tuple(overlaps)):
        raise SharedSpacetimeAtlasError("declared atlas overlap graph must be connected")

    max_j_cocycle = max_l_cocycle = 0.0
    triangle_count = 0
    for p, q, r in triangles:
        triangle_count += 1
        try:
            pq = overlap_map[(p, q)]
            qr = overlap_map[(q, r)]
            pr = overlap_map[(p, r)]
        except KeyError as exc:
            raise SharedSpacetimeAtlasError(
                f"triangle {(p, q, r)!r} requires direct p->q, q->r and p->r overlaps"
            ) from exc

        j_residual = _close_matrix(
            pr.jacobian,
            matmul(qr.jacobian, pq.jacobian),
            atol,
        )
        l_residual = _close_matrix(
            pr.lorentz,
            matmul(qr.lorentz, pq.lorentz),
            atol,
        )
        max_j_cocycle = max(max_j_cocycle, j_residual)
        max_l_cocycle = max(max_l_cocycle, l_residual)

    for patch in patch_map.values():
        if abs(det(patch.coframe)) <= atol:
            raise SharedSpacetimeAtlasError("assembled ADM coframe lost rank four")

    return SharedAtlasCertificate(
        compatible=True,
        patch_count=len(patch_map),
        overlap_count=len(overlap_map),
        triangle_count=triangle_count,
        max_coframe_residual=max_coframe,
        max_lorentz_residual=max_lorentz,
        max_metric_residual=max_metric,
        max_jacobian_cocycle_residual=max_j_cocycle,
        max_lorentz_cocycle_residual=max_l_cocycle,
    )
