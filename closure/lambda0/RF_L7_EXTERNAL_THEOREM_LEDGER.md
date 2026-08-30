# RF-L7 External Theorem Ledger

Status: `EXTERNAL_THEOREM_DEPENDENCY_TYPED / NO_INTERNAL_PROMOTION_BY_CITATION`

## E1 — Normally hyperbolic Cauchy theorem

Reference:

C. Bär, N. Ginoux, F. Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, arXiv:0806.1036.

Imported result used by RF-L7:

- on a globally hyperbolic smooth Lorentzian spacetime, a normally hyperbolic operator has a well-posed global Cauchy problem on a smooth spacelike Cauchy hypersurface, with uniqueness and causal propagation for the standard smooth compact-support data class.

RFC-side obligations before application:

```text
operator_principal_symbol = g^{-1}                   -> RF-L7 local algebra
Lorentzian_metric         = RF-E8                    -> parent gate
positive_lapse            = IDT 05C / RF-E8          -> parent gate
spatial_metric_positive   = TIR/RF-E8                -> parent gate
normally_hyperbolic       = RF-L7                    -> exact local classification
global_Cauchy_foliation   = OPEN RFC geometric gate
regularity                = OPEN explicit domain contract
boundary/asymptotic_data  = OPEN when applicable
```

The citation supplies theorem authority only after these RFC-side premises are independently certified. It does not promote the open geometric premises.
