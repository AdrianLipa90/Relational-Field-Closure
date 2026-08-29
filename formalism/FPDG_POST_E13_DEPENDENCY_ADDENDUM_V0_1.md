# RFC post-E13 dependency addendum — RF-E14 through RF-E20

Status: `SOURCE_DEPENDENCY_SYNC / POST_E13_INFORMATION_CLOCK_BRANCH`

This addendum exposes the source-local dependency structure required by the Fundamental-Physics-Dependency-Graph without rewriting the older ADM spine in `formalism/DEPENDENCY_GRAPH.md`.

The action-level ADM spine remains closed through RF-E13. RF-E14–RF-E20 form a distinct information/clock/material-congruence branch rooted in RF-E8 kinematics, the IDT 05D local-clock relative-entropy potential, and the RFC Noether/current carrier.

```text
IDT 05D local-clock relative entropy
              |
RFC RF-E8 ----+----> RF-E14 directional relative-entropy potential
                         |
                         +----> RF-E15 Legendre/Hamiltonian audit
                         |               |
                         +---------------+----> RF-E17 scalar-action potential

RFC RF-E8 ---------------------------> RF-E16 shift/Noether identification firewall
RFC Noether/current carrier ----------> RF-E16
RF-E17 -------------------------------> RF-E18 shift/physical-velocity gauge firewall
RF-E16 -------------------------------> RF-E18
RFC RF-E8 ----------------------------> RF-E18
RF-E18 -------------------------------> RF-E19 Noether-current material congruence
RFC current/measure carrier -----------> RF-E19
RF-E17 -------------------------------> RF-E20 tetra-clock mass-scale closure
RF-E19 -------------------------------> RF-E20
TIR regular-tetrahedron carrier -------> RF-E20
RF-E20 -------------------------------> physical scale/coupling frontier
```

## Typed source states

- `RF-E14`: `EXACT_ADM_RECIPROCAL_RATIO / CONDITIONAL_IDT_PARENT / SCALE_UNFIXED`
- `RF-E15`: `LEGENDRE_TRANSFORM_EXACT / HAMILTONIAN_IDENTIFICATION_CONDITIONAL / DYNAMICAL_CARRIER_UNFIXED`
- `RF-E16`: `ADM_SHIFT_TENSORIAL / NOETHER_SECTOR_TYPED / IDENTIFICATION_REJECTED`
- `RF-E17`: `COVARIANT_ACTION_TEMPLATE / NORMALIZATION_CONDITIONAL / POTENTIAL_SHAPE_BOUND`
- `RF-E18`: `SHIFT_GAUGE_TRANSFORMATION_EXACT / PHYSICAL_VELOCITY_CARRIER_BOUND / BETA_SHIFT_IDENTIFICATION_REJECTED`
- `RF-E19`: `EXACT_TIMELIKE_CURRENT_DECOMPOSITION / MATERIAL_FLOW_BINDING_CONDITIONAL / BETA_PHYS_SOURCE_PASS_CONDITIONAL`
- `RF-E20`: `TETRA_CLOCK_DIMENSIONAL_CLOSURE / MASS_FORMULA_EXACT_CONDITIONAL / SCALE_SOLVE_DEPENDENT`

## Cross-repository parent boundaries

RF-E14 uses the exact IDT 05D generator

\[
\Phi(N)=N-1-\ln N,
\]

as a conditional parent. The IDT source keeps this object dimensionless and assigns physical action/Hamiltonian/energy binding downstream.

RF-E20 uses the regular tetrahedral carrier from TIR together with a physical SI edge scale `ell_*`. The regular tetrahedron supplies the geometric carrier; RF-E20 keeps the SI scale selector explicit. Its mass relation

\[
m_{\rm eff}=\sigma_{\rm tet}\frac{\hbar}{c\ell_*}
\]

is therefore exact conditional on the declared scale inputs and does not by itself close the physical scale/coupling frontier.

## Dependency semantics

RF-E14–RF-E20 are not represented as a false linear continuation of RF-E13. The branch dependencies above follow the explicit parent surfaces used by the individual closure documents. RF-E16 and RF-E18 are firewalls that reject the naive identification of coordinate ADM shift with material velocity and force the material-congruence route used by RF-E19.
