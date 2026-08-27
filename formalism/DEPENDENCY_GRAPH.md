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
  |                                           RF-G0 Lorentzian signature gate
  |                                                  |
  |                                           RF-02I coframe gluing/integrability
  |                                                  |
  |                                           RF-N0 clock-rate / lapse dynamics
  |                                                  |
  |                                           RF-N1 Newton weak-field gate
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

Exact/candidate status after RF-02H:

- `RF-02H hexahedral dual frame`: LOCAL STRUCTURAL PASS. Six oriented hexahedral face normals `{±e1,±e2,±e3}` have second moment `I3/3` and aggregate FS orbit metric `I3/6`, hence exact rank three, determinant `1/216`, condition number `1`.
- `RF-02H topology/refinement invariants`: exact for the regular dual complex: `chi=2`, total FS area `pi`, Berry flux magnitude `2pi`, first Chern number magnitude `1`, octant FS area `pi/8`, octant Berry phase magnitude `pi/4`.
- `RF-02H phase-clock physicalization`: candidate physical binding `h_phys=(ell_phi^2/6)I3=c^2 I3/(6 omega^2)`; rank remains three for finite nonzero phase rate.
- `RF-G0 signature theorem`: its positive rank-three local spatial prerequisite is now satisfied by RF-02H. Global spatial coframe integrability and physical displacement binding remain open.
- `IDT 01L`: exact phase-clock length identity `ell_phi = c/|omega| = hbar c/E` on nonzero-rate patches.
- `TIR phase-clock area v0.2`: exact dimensional reduction and candidate physicalization `dA_rel = ell_phi^2 da_FS`.
- `IDT 01K`: exact constant-rate reduction `Xi_I = (J_pi/a_FS)(omega/c)^2` once the TIR area binding is admitted.
- `RF-L0`: exact TIR×IDT algebraic interface with `Lambda_I = alpha_I Xi_I`.
- `RF-02I`, `RF-N0`, `RF-N1`, `RF-E1`: OPEN.
