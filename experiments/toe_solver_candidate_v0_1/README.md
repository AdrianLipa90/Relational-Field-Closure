# QHTRI ToE Solver Candidate v0.11

Status: `CANDIDATE_RELEASE_READY`

Authority: `CANDIDATE_ONLY`  
Canon: `false`  
Physical-production claim: `false`

This branch contains the executable geometry/source-closure stack developed through the live NOEMA → GREMLIN/Phase36D → QHTRI workflow. The current candidate is complete for bounded-domain reference E2E and for one archived same-realization observational E2E. Merge to `main` remains an explicit operator decision.

## Executable closure stack

The branch provides the complete candidate path

`source observations -> precision clock / lapse -> spatial carrier -> inter-leaf matching -> RF-E8 ADM metric -> metric jets -> Ricci / Einstein tensor -> source closure -> Bianchi gates`.

Implemented components include:

- precision-safe `DECIMAL_LOG_N` clock/lapse handling;
- RF-E8 ADM carrier `(N_R, h_ij, b^i) -> g_mn`;
- metric callable -> metric jet -> `G_mn`;
- GSC3A/GSC4B matching/shift route;
- QHTRI-neutrino and multisector source bindings;
- constrained local Einstein closure and positive source-cone falsification;
- bounded-domain RF-E25/RF-E26 carrier checks;
- observational same-realization E2E with analytic contracted-Bianchi sweep.

## Candidate release evidence

### 1. Empirically calibrated bounded-domain Rindler route

Source: optical-clock process data, DOI `10.5281/zenodo.8184043` (`Fig3.csv`).

The measured clock gradient calibrates a bounded Rindler reference field. The route validates:

- precision retention below float64 endpoint resolution;
- analytic Rindler curvature-null control;
- RF-E25 single-patch shared atlas;
- explicit bounded-domain coverage;
- RF-E26 global carrier on that covered domain;
- QHTRI model-state validation.

Current release receipt:

`validation/toe_solver_candidate_v0_1/CANDIDATE_RELEASE_GATE_V0_11.json`

Verdict: `PASS_REPOSITORY_BOUNDED_DOMAIN_E2E_REFERENCE_COMPLETE`.

### 2. Archived same-realization observational route

Source dataset: `RT218283.SP3@8013`, epochs `2015-01-21T00:01:00Z` and `2015-01-21T00:03:00Z`, satellites `G01..G05`.

Frozen source digest:

`e6c18e85a6f2b62c6820258b7ecfc514f8a177f1c2eaff54d6a5ff0b8fab2399`

The executable route validates:

- precision clock inverse cycles;
- deterministic five-node tetrahedral boundary closure with full A5 closed-3-manifold / vertex-link checks;
- inter-leaf matching with maximum residual `6.938893903907228e-17`;
- derived RF-E8 shift;
- finite Lorentzian ADM metric;
- Einstein tensor construction;
- analytic contracted-Bianchi sweep from approximately `3.08e-24` to `1.89e-21`.

Validation: `7/7 PASS`.  
Adversarial suite: `5/5 PASS`.  
Reproducibility release gate: `10/10 PASS`.

Current ledger:

`experiments/toe_solver_candidate_v0_1/CONCEPTNAV_CLOSURE_LEDGER_V0_11.json`

Status: `PASS_CANDIDATE_REPO_COMPLETE_OBSERVATIONAL_E2E`.

Evidence class: `MODEL_LEVEL_EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED`. Full physical 3+1 production capture remains an external-evidence expansion route.

## Retained failures and repairs

Failures remain part of provenance.

- Multisector V1 TRF numerical-control failure is retained beside the BVLS V2 repair.
- Precision v0.8 retains the Decimal-context negation failure that exposed loss below endpoint float64 resolution.
- v0.11 retains the `numpy.bool_` receipt-serialization failure; the repair was an explicit `bool(...)` cast, with source data and physics thresholds unchanged.

## Automated gates

`.github/workflows/toe-candidate-v0-11-release.yml` runs:

1. empirical bounded-domain E2E validation;
2. bounded-domain candidate release gate with archived QHTRI receipt;
3. observational same-realization validation;
4. observational adversarial suite;
5. observational reproducibility release gate.

## Release boundary

Candidate software operators missing: `0`.  
Candidate source-wiring operators missing: `0`.  
Candidate release ready: `true`.

Promotion to `main` or canon requires an explicit operator instruction.

Base `main` at candidate inception: `85bbb1d0754605be2720b6bd258b486b0a072345`.
