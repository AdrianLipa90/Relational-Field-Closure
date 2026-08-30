# Spacetime-dimension candidate chain

Status: `CANDIDATE_ONLY`

This directory preserves the staged pre-RF-G0 dimension derivation and its promotion order.

## Candidate lineage

1. `PRE_RF_G0_SPACETIME_RANK_GATE_V0_4.md`
   - established the premetric four-volume factorization;
   - isolated `PREMETRIC_TEMPORAL_SPATIAL_TRANSVERSALITY` as the next algebraic gate.

2. `PREMETRIC_TEMPORAL_SPATIAL_TRANSVERSALITY_V0_5.md`
   - closes the v0.4 transversality gate;
   - proves the trace/traceless direct sum
     `Herm(2) = R I ⊕ Herm_0(2)`;
   - proves the canonical dual evaluation matrix is `I4`;
   - establishes carrier/coframe transversality at premetric level;
   - keeps worldline motion as an independent dynamical coordinate.

3. Cross-repository IDT candidate `IDT_TEMPORAL_TRACE_UNIQUENESS_V0_6.md`
   - proves that an additive positive `SU(2)`-invariant temporal scalar on the primitive Hermitian carrier is
     `T(X) = alpha Tr(X)`, `alpha > 0`;
   - leaves one positive reference-clock calibration constant.

4. `TIR_IDT_RFC_DIMENSION_CLOSURE_V0_7.md`
   - combines TIR spatial rank 3, IDT temporal rank 1 and RFC premetric transversality;
   - proves the exact local-carrier dimension
     `D_local_carrier = 4`;
   - supplies the four-rank carrier to RF-G0 before Lorentzian signature/field closure.

## Current frontier

Candidate-level results:

```text
TIR spatial carrier rank                     = 3
IDT invariant temporal scalar class          = trace up to positive calibration
RFC premetric temporal/spatial transversality = PASS
local Hermitian carrier dimension             = 4
Lorentzian determinant inertia                = EXACT ALGEBRA
```

The active downstream gate is:

`PHYSICAL_SPACETIME_SOLDERING_AND_FIELD_REALIZATION`

Canon authority follows explicit theory-admission and merge decisions.
