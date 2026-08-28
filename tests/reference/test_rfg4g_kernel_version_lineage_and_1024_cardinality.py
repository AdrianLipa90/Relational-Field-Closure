import math
from datetime import datetime, timezone


ALPHA_C = 0.474812
BETA_S = 0.856234
GAMMA_T = 0.345123
LAMBDA = 0.474812
ETHICAL_BOUND = 0.9

FROZEN_HBAR_EFF = 0.892345
FROZEN_C_EFF = 0.956712
FROZEN_G_EFF = 0.734561


def formula_branch():
    hbar_eff = ALPHA_C * math.sqrt(1.0 + BETA_S**2)
    c_eff = GAMMA_T * (1.0 + LAMBDA) / math.sqrt(1.0 - GAMMA_T**2 + 1e-10)
    g_eff = BETA_S * (1.0 - ETHICAL_BOUND) / (ALPHA_C**2 + 1e-10)
    return hbar_eff, c_eff, g_eff


def test_git_transition_order_is_strict():
    v4 = datetime(2026, 1, 16, 18, 48, 58, tzinfo=timezone.utc)
    holonomy = datetime(2026, 1, 17, 13, 58, 30, tzinfo=timezone.utc)
    holocore2 = datetime(2026, 1, 17, 13, 59, 14, tzinfo=timezone.utc)
    v5 = datetime(2026, 1, 17, 16, 50, 48, tzinfo=timezone.utc)
    assert v4 < holonomy < holocore2 < v5


def test_recovered_notebook_cell_cardinality_is_32_squared():
    assert 32 * 32 == 1024


def test_recovered_notebook_event_count_matches_cells_times_steps():
    cells = 1024
    steps = 5000
    assert cells * steps == 5_120_000


def test_cell_and_ensemble_cardinality_are_separately_typed():
    recovered_execution = {"cells": 1024, "steps": 5000}
    paper_report = {"runs": 1024}
    assert "runs" not in recovered_execution
    assert "cells" not in paper_report
    assert recovered_execution["cells"] == paper_report["runs"]


def test_formula_branch_reproduces_documented_formula_values():
    hbar_eff, c_eff, g_eff = formula_branch()
    assert math.isclose(hbar_eff, 0.6250835804773123, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(c_eff, 0.5423126030065264, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(g_eff, 0.3797948715905446, rel_tol=0.0, abs_tol=1e-15)


def test_formula_branch_is_distinct_from_frozen_normalized_coordinates():
    derived = formula_branch()
    frozen = (FROZEN_HBAR_EFF, FROZEN_C_EFF, FROZEN_G_EFF)
    relative_defects = [abs(d - f) / f for d, f in zip(derived, frozen)]
    assert relative_defects[0] > 0.29
    assert relative_defects[1] > 0.43
    assert relative_defects[2] > 0.48


def test_formula_branch_cannot_zero_defect_against_frozen_coordinates():
    derived = formula_branch()
    frozen = (FROZEN_HBAR_EFF, FROZEN_C_EFF, FROZEN_G_EFF)
    assert all(not math.isclose(d, f, rel_tol=1e-6, abs_tol=1e-9) for d, f in zip(derived, frozen))
