# Relational Field Closure

**Status:** RESEARCH_PROGRAM_BOOTSTRAP / NO_DERIVED_FIELD_EQUATIONS_YET

Relational Field Closure (RFC) is a derivation-first research repository whose purpose is to test whether Einstein, Maxwell and Newton field structures can be obtained from three pinned upstream theories:

1. **The Fundamental Theory of Informational Relations (TIR)**
2. **Secret of a Half**
3. **Informational Dynamics of Time (IDT)**

The repository also carries the dynamic \(\Lambda_0\) program as the candidate scalar closure entering the Einstein sector.

The target theories are **validation targets, not premises**. A result is admitted as DERIVED only when the target structure follows from the upstream primitives and passes the dependency, covariance, dimensional and limit gates defined here.

## Bootstrap dependency graph

```text
TIR + Secret-of-a-Half + IDT
        |
        v
RF-00 Cross-reference contract
        |
        v
RF-01 Relational field primitive
       / \
      v   v
RF-02 Local phase connection      RF-04 Local clock / metric primitive
      |                                  |
      v                                  v
RF-03 Curvature F=dA               RF-05 Metric connection / curvature
      |                                  |
      v                                  v
MAXWELL KINEMATICS                  NEWTON WEAK-FIELD GATE
      |                                  |
      +---------------+------------------+
                      v
               RF-L1 Dynamic Lambda0
                      |
                      v
              EINSTEIN-BIANCHI CLOSURE
                      |
                      v
               UNIFIED LIMIT AUDIT
```

## Repository layers

- `formalism/` — equations, operators and dependency gates
- `closure/maxwell/` — Maxwell derivation and tests
- `closure/newton/` — Newtonian limit derivation and tests
- `closure/einstein/` — Einstein/Bianchi closure and tests
- `closure/lambda0/` — dynamic \(\Lambda_0\) derivation and conservation contract
- `crossrefs/` — pinned upstream references and source contracts
- `validation/` — receipts, symbolic identities and numerical tests
- `monograph/` — derivation narrative after gates pass

## Claim firewall

No equation is promoted because it resembles a known law. Each closure must demonstrate provenance from upstream primitives, exact algebraic identities where applicable, covariance/gauge structure, dimensional consistency and the correct physical limit.
