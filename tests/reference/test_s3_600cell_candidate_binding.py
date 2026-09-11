import math
import pytest

from rfc.s3_600cell_candidate_binding import (
    RFC600CellCandidateError,
    bind_s3_sector,
    supported_dimension,
    working_sector_table,
)


def test_candidate_binding_is_active_working_not_canonical():
    rows = working_sector_table()
    assert len(rows) == 6
    assert all(r.status == "CANDIDATE" for r in rows)
    assert all(r.active_working_version for r in rows)
    assert all(not r.canonical for r in rows)
    assert all(r.physical_binding == "OPEN" for r in rows)


def test_s3_sector_multiplicities_and_laplacian_eigenvalues():
    assert [r.multiplicity for r in working_sector_table()] == [1, 4, 9, 16, 25, 36]
    assert [r.angular_eigenvalue for r in working_sector_table()] == [0, 3, 8, 15, 24, 35]
    assert supported_dimension() == 91


def test_adjacency_eigenvalues_match_600cell_supported_sectors():
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    got = [r.adjacency_eigenvalue for r in working_sector_table()]
    want = [12.0, 6.0 * phi, 4.0 * phi, 3.0, 0.0, -2.0]
    assert all(math.isclose(a, b, rel_tol=0.0, abs_tol=1e-15) for a, b in zip(got, want))


@pytest.mark.parametrize("bad", [-1, 6, 7, True, 1.5, "3"])
def test_outside_verified_sector_fails_closed(bad):
    with pytest.raises(RFC600CellCandidateError):
        bind_s3_sector(bad)
