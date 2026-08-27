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
RF-M1 homogeneous Maxwell                            | h_H=I3/6
  |                                                  | ell_phi=c/|omega|
RF-M2 sourced/action Maxwell                         v
  |                                           RF-G0 Lorentzian signature
  |                                                  |
  |                                           RF-02I coframe connection/curvature
  |                                                  |
  |                                       exact negative theorem:
  |                                       constant lapse -> Gamma^i_tt=0
  |                                                  |
  |                                                  v
  |                                  IDT 05C relational clock ratio
  |                                  N_R=phi_x/phi_ref > 0
  |                                                  |
  |                                                  v
  |                                           RF-N0 relational lapse
  |                                     Theta=N_R c dt
  |                                     Phi_R=c^2 ln N_R
  |                                     a^i~-grad^i Phi_R
  |                                                  |
  |                                                  v
  |                                           RF-N1 source law / Poisson test
  |                                                  |
  +----------------------+---------------------------+
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

Exact/candidate status after RF-N0:

- `RF-02H`: LOCAL STRUCTURAL PASS. Regular hexahedral dual frame supplies the positive rank-three local metric `h_H=I3/6`.
- `RF-G0`: exact Lorentzian signature theorem; positive rank-three prerequisite satisfied locally by RF-02H.
- `RF-02I`: LOCAL EXACT CONNECTION PASS. Phase-clock gradients enter the spatial connection and curvature; constant temporal lapse gives exact `Gamma^i_tt=0` negative theorem.
- `IDT 05C relational lapse`: EXACT CLOCK-RATIO PASS. `N_R=phi_x/phi_ref>0` is dimensionless, reparameterization invariant and compositional. For common normalization, `N_R=M_x cosh(A_x/2)/[M_ref cosh(A_ref/2)]`.
- `RF-N0 temporal coframe binding`: CANDIDATE physical binding `Theta_R=N_R c dt` after reference-clock calibration.
- `RF-N0 static geodesic kinematics`: EXACT conditional on the temporal-coframe binding. `Gamma^i_tt=c^2N_R h^ij partial_j N_R`; `Phi_R=c^2 ln N_R`; slow local acceleration is `a^i=-N_R^2 h^ij partial_j Phi_R+...`.
- `RF-N0 relational-gradient decomposition`: EXACT under fixed reference and admitted IDT kinetic realization. `partial ln N_R=partial ln M+1/2 tanh(A/2) partial A`, with `partial ln M` decomposing into density and viscosity gradients.
- `RF-N0 weak force-law form`: CONDITIONAL LIMIT PASS CANDIDATE. Near `N_R=1` and locally Euclidean physical `h`, `a^i=-partial^i Phi_R+...`.
- `RF-N1 source equation / Newton constant normalization`: OPEN. No Poisson equation is used upstream.
- `IDT 01L`, `TIR phase-clock area v0.2`, `IDT 01K`, `RF-L0`: retained.
- `RF-M2`, `RF-N1`, `RF-E1`: OPEN.
