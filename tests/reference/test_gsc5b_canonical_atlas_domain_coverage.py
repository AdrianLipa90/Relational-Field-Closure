import pytest

from src.rfc.canonical_atlas_domain_coverage import (
    CanonicalAtlasCoverageError,
    certify_canonical_atlas_domain_coverage,
)


PATCHES = ("star:0", "star:1", "star:2", "star:3")


def test_complete_patchwise_solution_set_derives_atlas_domain_coverage():
    cert = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=reversed(PATCHES),
        target_domain_id="product-domain-1",
        atlas_domain_id="product-domain-1",
        canonical_atlas_coverage_certified=True,
    )
    assert cert.every_atlas_patch_has_local_solution is True
    assert cert.no_unmatched_solution_patch_ids is True
    assert cert.target_equals_atlas_domain is True
    assert cert.domain_coverage_derived is True
    assert cert.production_status == "PASS_GSC5B_CANONICAL_ATLAS_DOMAIN_COVERAGE_DERIVED"


def test_missing_one_local_solution_patch_keeps_coverage_open():
    cert = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=PATCHES[:-1],
        target_domain_id="product-domain-1",
        atlas_domain_id="product-domain-1",
        canonical_atlas_coverage_certified=True,
    )
    assert cert.every_atlas_patch_has_local_solution is False
    assert cert.domain_coverage_derived is False


def test_extra_unknown_solution_patch_is_lineage_mismatch_for_this_route():
    cert = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=PATCHES + ("foreign:9",),
        target_domain_id="product-domain-1",
        atlas_domain_id="product-domain-1",
        canonical_atlas_coverage_certified=True,
    )
    assert cert.every_atlas_patch_has_local_solution is True
    assert cert.no_unmatched_solution_patch_ids is False
    assert cert.domain_coverage_derived is False


def test_target_domain_larger_or_different_from_atlas_domain_remains_open():
    cert = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=PATCHES,
        target_domain_id="larger-target-domain",
        atlas_domain_id="product-domain-1",
        canonical_atlas_coverage_certified=True,
    )
    assert cert.target_equals_atlas_domain is False
    assert cert.domain_coverage_derived is False


def test_reference_patch_index_equality_does_not_replace_atlas_coverage_parent():
    cert = certify_canonical_atlas_domain_coverage(
        atlas_patch_ids=PATCHES,
        local_solution_patch_ids=PATCHES,
        target_domain_id="product-domain-1",
        atlas_domain_id="product-domain-1",
        canonical_atlas_coverage_certified=False,
    )
    assert cert.every_atlas_patch_has_local_solution is True
    assert cert.domain_coverage_derived is False


def test_duplicate_or_empty_patch_ids_fail_closed():
    with pytest.raises(CanonicalAtlasCoverageError):
        certify_canonical_atlas_domain_coverage(
            atlas_patch_ids=("star:0", "star:0"),
            local_solution_patch_ids=("star:0",),
            target_domain_id="d",
            atlas_domain_id="d",
            canonical_atlas_coverage_certified=True,
        )
    with pytest.raises(CanonicalAtlasCoverageError):
        certify_canonical_atlas_domain_coverage(
            atlas_patch_ids=("star:0", ""),
            local_solution_patch_ids=("star:0",),
            target_domain_id="d",
            atlas_domain_id="d",
            canonical_atlas_coverage_certified=True,
        )
