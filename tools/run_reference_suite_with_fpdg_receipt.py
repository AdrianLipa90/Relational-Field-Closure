#!/usr/bin/env python3
"""Run RFC reference tests and emit an FPDG failure receipt when they fail.

The pytest exit status is preserved. The receipt records only coordinates supplied by
pytest plus explicit RFC-owned test-to-claim bindings; no equation or scientific-source
line is inferred from a test name.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
# Executing this wrapper from tools/ would otherwise make tools/ sys.path[0], unlike
# `python -m pytest` which exposes the repository root. Preserve the original import
# semantics so `src.rfc...` remains importable.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest  # noqa: E402

BINDINGS_PATH = ROOT / "validation" / "FPDG_FAILURE_BINDINGS_V0_1.json"
BUILD_DIR = ROOT / "build"
RECEIPT_PATH = BUILD_DIR / "FPDG_VALIDATION_FAILURE_RECEIPT.json"


class BindingError(RuntimeError):
    pass


def source_commit() -> str:
    value = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    if len(value) != 40:
        raise RuntimeError("git rev-parse HEAD did not return a 40-character SHA")
    return value


def load_bindings() -> dict[str, dict[str, Any]]:
    payload = json.loads(BINDINGS_PATH.read_text(encoding="utf-8"))
    if payload.get("schema") != "RFC_FPDG_FAILURE_BINDINGS_V0_1":
        raise BindingError("unexpected RFC FPDG failure binding schema")
    rows = payload.get("bindings")
    if not isinstance(rows, dict):
        raise BindingError("bindings must be an object")
    out: dict[str, dict[str, Any]] = {}
    for path, row in rows.items():
        if not isinstance(path, str) or not path or not isinstance(row, dict):
            raise BindingError("invalid binding entry")
        claim_id = row.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id.startswith("RFC."):
            raise BindingError(f"{path}: invalid RFC claim_id")
        out[path] = row
    return out


def _repo_relative(path: str) -> str:
    candidate = Path(path)
    if candidate.is_absolute():
        try:
            return candidate.resolve().relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            return candidate.as_posix()
    return candidate.as_posix()


def _node_path(report: Any) -> str:
    nodeid = str(getattr(report, "nodeid", ""))
    return _repo_relative(nodeid.split("::", 1)[0]) if nodeid else "tests/reference"


def _failure_location(report: Any) -> tuple[str, int | None]:
    """Return the finest repository source coordinate explicitly exposed by pytest."""
    longrepr = getattr(report, "longrepr", None)
    traceback = getattr(longrepr, "reprtraceback", None)
    entries = getattr(traceback, "reprentries", None)
    if entries:
        entry = entries[-1]
        fileloc = getattr(entry, "reprfileloc", None)
        path = getattr(fileloc, "path", None)
        lineno = getattr(fileloc, "lineno", None)
        if isinstance(path, str) and path:
            rel = _repo_relative(path)
            if not Path(rel).is_absolute():
                return rel, lineno if isinstance(lineno, int) and lineno > 0 else None

    location = getattr(report, "location", None)
    if isinstance(location, tuple) and len(location) >= 2:
        path, zero_line = location[0], location[1]
        if isinstance(path, str) and path:
            line = zero_line + 1 if isinstance(zero_line, int) and zero_line >= 0 else None
            return _repo_relative(path), line

    return _node_path(report), None


class FpdgFailurePlugin:
    def __init__(self, bindings: dict[str, dict[str, Any]]) -> None:
        self.bindings = bindings
        self.failures: list[dict[str, Any]] = []
        self._seen: set[tuple[str, str]] = set()

    def _record(self, report: Any, phase: str) -> None:
        nodeid = str(getattr(report, "nodeid", "")) or _node_path(report)
        key = (nodeid, phase)
        if key in self._seen:
            return
        self._seen.add(key)

        test_path = _node_path(report)
        binding = self.bindings.get(test_path)
        failure_path, line = _failure_location(report)
        locator: dict[str, Any] = {
            "path": failure_path,
            "test_id": nodeid,
        }
        if line is not None:
            locator["line_start"] = line

        refs = [f"pytest-nodeid:{nodeid}", f"pytest-phase:{phase}"]
        longreprtext = getattr(report, "longreprtext", None)
        if isinstance(longreprtext, str):
            message = longreprtext[-4000:]
        else:
            message = str(getattr(report, "longrepr", ""))[-4000:]
        row: dict[str, Any] = {
            "failure_id": f"PYTEST.{len(self.failures) + 1:04d}",
            "kind": "TEST_FAILURE",
            "message": message,
            "source_locator": locator,
            "evidence_refs": refs,
        }
        if binding is not None:
            row["claim_id"] = binding["claim_id"]
            claim_source = binding.get("claim_source")
            if isinstance(claim_source, str):
                refs.append(f"claim-source:{claim_source}")
            receipt = binding.get("validation_receipt")
            if isinstance(receipt, str):
                refs.append(f"validation-receipt:{receipt}")
        self.failures.append(row)

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.failed:
            self._record(report, str(getattr(report, "when", "call")))

    def pytest_collectreport(self, report: Any) -> None:
        if getattr(report, "failed", False):
            self._record(report, "collection")

    def pytest_sessionfinish(self, session: pytest.Session, exitstatus: int) -> None:
        if not self.failures:
            return
        BUILD_DIR.mkdir(exist_ok=True)
        payload = {
            "schema": "FPDG_VALIDATION_FAILURE_RECEIPT_V0_1",
            "repository_id": "RFC",
            "repository": "AdrianLipa90/Relational-Field-Closure",
            "source_commit": source_commit(),
            "workflow": "RFC reference suite",
            "job": "reference",
            "status": "FAIL",
            "failures": self.failures,
            "pytest_exit_status": int(exitstatus),
            "binding_schema": "RFC_FPDG_FAILURE_BINDINGS_V0_1",
            "coordinate_semantics": (
                "source_locator points to the exact pytest-observed failure/test coordinate; "
                "claim_id and claim-source evidence refs provide the scientific graph anchor"
            ),
        }
        RECEIPT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"FPDG failure receipt: {RECEIPT_PATH.relative_to(ROOT)} ({len(self.failures)} failures)")


def main() -> int:
    try:
        plugin = FpdgFailurePlugin(load_bindings())
        code = pytest.main(["-q", "tests/reference"], plugins=[plugin])
        return int(code)
    except (OSError, json.JSONDecodeError, BindingError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: unable to run RFC reference suite with FPDG receipt: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
