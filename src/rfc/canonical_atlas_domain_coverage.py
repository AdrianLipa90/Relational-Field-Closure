from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


class CanonicalAtlasCoverageError(ValueError):
    """Raised when a declared GSC5B coverage packet fails closed."""


def _normalize_ids(values: Iterable[str], label: str) -> tuple[str, ...]:
    out: list[str] = []
    seen: set[str] = set()
    for raw in values:
        value = str(raw).strip()
        if not value:
            raise CanonicalAtlasCoverageError(f"{label} contains an empty patch id")
        if value in seen:
            raise CanonicalAtlasCoverageError(f"{label} contains duplicate patch id {value!r}")
        seen.add(value)
        out.append(value)
    if not out:
        raise CanonicalAtlasCoverageError(f"{label} must be nonempty")
    return tuple(sorted(out))


@dataclass(frozen=True)
class CanonicalAtlasDomainCoverageCertificate:
    atlas_patch_ids: tuple[str, ...]
    local_solution_patch_ids: tuple[str, ...]
    target_domain_id: str
    atlas_domain_id: str
    canonical_atlas_coverage_certified: bool
    target_equals_atlas_domain: bool
    every_atlas_patch_has_local_solution: bool
    no_unmatched_solution_patch_ids: bool
    domain_coverage_derived: bool
    production_status: str


def certify_canonical_atlas_domain_coverage(
    *,
    atlas_patch_ids: Iterable[str],
    local_solution_patch_ids: Iterable[str],
    target_domain_id: str,
    atlas_domain_id: str,
    canonical_atlas_coverage_certified: bool,
) -> CanonicalAtlasDomainCoverageCertificate:
    """Derive target-domain coverage from canonical atlas coverage + patch completeness.

    This is the GSC5B sufficient route.  The admitted atlas is already known to
    cover its own domain (for the flow-adapted product route this is the product
    of the GSC3 interval with the GSC4C vertex-star cover of the A5 spatial
    carrier).  If the declared RF-E24 local-solution receipt set is exactly the
    atlas patch-id set and the requested target domain is that atlas domain, an
    independent W7 domain-coverage witness is a derived coordinate.
    """

    atlas = _normalize_ids(atlas_patch_ids, "atlas_patch_ids")
    solutions = _normalize_ids(local_solution_patch_ids, "local_solution_patch_ids")

    target = str(target_domain_id).strip()
    domain = str(atlas_domain_id).strip()
    if not target:
        raise CanonicalAtlasCoverageError("target_domain_id must be nonempty")
    if not domain:
        raise CanonicalAtlasCoverageError("atlas_domain_id must be nonempty")

    atlas_set = set(atlas)
    solution_set = set(solutions)
    every_patch = atlas_set.issubset(solution_set)
    no_unmatched = solution_set.issubset(atlas_set)
    same_domain = target == domain

    derived = bool(
        canonical_atlas_coverage_certified
        and same_domain
        and every_patch
        and no_unmatched
    )

    return CanonicalAtlasDomainCoverageCertificate(
        atlas_patch_ids=atlas,
        local_solution_patch_ids=solutions,
        target_domain_id=target,
        atlas_domain_id=domain,
        canonical_atlas_coverage_certified=bool(canonical_atlas_coverage_certified),
        target_equals_atlas_domain=same_domain,
        every_atlas_patch_has_local_solution=every_patch,
        no_unmatched_solution_patch_ids=no_unmatched,
        domain_coverage_derived=derived,
        production_status=(
            "PASS_GSC5B_CANONICAL_ATLAS_DOMAIN_COVERAGE_DERIVED"
            if derived
            else "DOMAIN_COVERAGE_PARENT_OR_PATCH_COMPLETENESS_OPEN"
        ),
    )
