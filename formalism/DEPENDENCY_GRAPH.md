# Formal dependency graph

```text
RF-00  pinned cross-reference contract
  |
RF-01  quantum geometric tensor / relational field primitive
  |
RF-02  polyhedral metric-curvature invariants
  |\
  | RF-03 Euler-Berry reality + Poincare curvature gate
  |    |
  |    +---------------------------------------------+
  |                                                  |
  v                                                  v
RF-M0 Berry gauge seed                        RF-02H hexahedral rank-3 local metric
  |                                                  |
RF-M1 homogeneous Maxwell                            | h_H = I3/6
  |                                                  | ell_phi=c/|omega|
RF-M2 sourced/action Maxwell                         v
  |                                           RF-G0 Lorentzian signature
  |                                                  |
  |                                           RF-02I coframe connection/curvature
  |                                             |       |
  |                                             |       +-- exact negative theorem:
  |                                             |           constant lapse -> Gamma^i_tt=0
  |                                             v
  |                                           RF-N0 derive lapse / clock-rate field N
  |                                             |
  |                                           RF-N1 Newton weak-field + source law
  |                                             |
  +----------------------+----------------------+
                         |
                         v
               RF-P0 phase-energy / photoelectric bridge
                         |
                         v
              IDT 01L phase-clock length scale
          ell_phi = c/|omega| = hbar c/E
                         |
                         v
          TIR phase-clock physicalized FS/Berry area
          dA_rel = ell_phi^2 da_FS
                         |
                         v
               IDT 01K information curvature
          Xi_I = J_pi / A_rel
                         |
                         v
               RF-L0 temporal information curvature
     constant cell: Xi_I = (J_pi/a_FS)(omega/c)^2
                         |
                         v
               RF-L1 dynamic Lambda0 scalar closure
                         |
                         v
               RF-E1 Einstein-Bianchi closure
                         |
                         v
               RF-X1 unified limit audit
```

No downstream node may be promoted above the weakest unresolved prerequisite.

Exact/candidate status after RF-02I:

- `RF-02H`: LOCAL STRUCTURAL PASS. Regular six-face hexahedral dual frame gives `M_H=I3/3`, `h_H=I3/6`, exact rank three, determinant `1/216`, condition number `1`.
- `RF-G0`: exact signature theorem; RF-02H now supplies its positive rank-three local spatial prerequisite.
- `RF-02I conformal coframe connection`: LOCAL EXACT PASS. For `E^i=a vartheta^i`, `a=c/(sqrt(6)|omega|)`, the torsion-free metric connection is `omega^i_j=bar_omega^i_j+f_j E^i-f_i E^j`, with `f_i=-E_i ln|omega|`.
- `RF-02I integrable-reference curvature`: LOCAL EXACT PASS. On `vartheta^i=dx^i`, `R3=a^-2[4 Delta ln|omega|-2|grad ln|omega||^2]=(24 omega Delta omega-36|grad omega|^2)/c^2` on a sign-definite nonzero-rate patch.
- `RF-02I cell gluing`: exact `SO(3)` connection transformation law; discrete-to-continuum holonomy convergence remains a candidate/refinement gate.
- `RF-02I Newton negative theorem`: EXACT. A static metric `-c^2dt^2+h_ij(x)dx^idx^j` has `Gamma^i_tt=0`; static spatial curvature alone cannot supply the Newtonian acceleration term for a slowly moving trajectory initially at rest.
- `RF-N0 lapse kinematic bridge`: exact conditional relation `Gamma^i_tt=c^2 N h^ij partial_j N`. If a later derivation gives `N=1+Phi/c^2+...`, the slow-motion kinematic limit is `d2x^i/dt^2=-partial^i Phi+O(c^-2)`. The source equation for `Phi` remains open.
- `IDT 01L`, `TIR phase-clock area v0.2`, `IDT 01K`, `RF-L0`: retained as previously staged.
- `RF-N0 dynamical lapse derivation`, `RF-N1 source-law/Poisson closure`, `RF-E1`: OPEN.
