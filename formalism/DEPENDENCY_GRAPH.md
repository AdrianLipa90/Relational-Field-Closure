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
  |                         +------------------------+-------------------+
  |                         |                                            |
  |                         v                                            v
  |                 IDT 01D Shannon-Onsager                    TIR RF-02H six-ray symmetry
  |                 G~D^T W D                                  {+/-e1,+/-e2,+/-e3}
  |                         |                                            |
  |                         +------------------------+-------------------+
  |                                                  |
  |                                                  v
  |                                      RF-N1A source-operator theorem
  |                                      -L_H/a_H^2 -> Delta_h
  |                                      octahedral symmetry -> Laplace
  |                                                  |
  |                                                  v
  |                                      RF-N1B source identification
  |                                      Delta_h ln N_R = S_R
  |                                      S_R [L^-2] : OPEN
  |                                                  |
  |                                                  v
  |                                      RF-N1C Newton normalization audit
  |                                      c^2 S_R ?= 4 pi G rho_m
  |                                      TARGET ONLY / OPEN
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
                         +------------------------+
                         |                        |
                         v                        |
               RF-L0 temporal information        |
               curvature                         |
                         |                        |
                         v                        |
               RF-L1 dynamic Lambda0             |
                         |                        |
                         +----------+             |
                                    |             |
                                    v             v
                              RF-E1 Einstein   RF-N1B source-basis candidate
                              Bianchi closure  S_R = beta_I Xi_I + ...
                                    |             |
                                    +------+------+ 
                                           |
                                           v
                                  RF-X1 unified limit audit
```

No downstream node may be promoted above the weakest unresolved prerequisite.

Exact/candidate status after RF-N1A:

- `RF-02H`: LOCAL STRUCTURAL PASS. Regular hexahedral dual frame supplies `h_H=I3/6`, six signed axis directions and exact octahedral isotropy.
- `RF-G0`: exact Lorentzian signature theorem; positive rank-three prerequisite satisfied locally by RF-02H.
- `RF-02I`: LOCAL EXACT CONNECTION PASS. Phase-clock gradients enter the spatial connection and curvature; constant lapse gives exact `Gamma^i_tt=0` negative theorem.
- `IDT 05C`: EXACT CLOCK-RATIO PASS. `N_R=phi_x/phi_ref>0` is dimensionless, reparameterization invariant and compositional.
- `RF-N0`: exact conditional geodesic kinematics after the temporal-coframe binding. `Phi_R=c^2 ln N_R`; near the reference sector `a^i=-partial^i Phi_R+...`.
- `IDT 01D`: exact detailed-balance Shannon-Onsager operator `G=(ln2)D^T diag[c Lambda]D`; at uniform equilibrium it reduces to the positive relational-mobility graph Laplacian `(ln2/m)K_0`.
- `RF-N1A six-neighbour operator`: LOCAL EXACT PASS. The positive hexahedral graph Laplacian `L_H` has constant null and normalized continuum-sign operator `-L_H/a_H^2 = Delta + (a_H^2/12) sum_i partial_i^4 + O(a_H^4)`.
- `RF-N1A symmetry classification`: LOCAL EXACT PASS. Signed permutations remove first-order drift and off-diagonal second derivatives; axis permutations force equal diagonal coefficients; constant-null removes the zeroth-order term. The leading local second-order scalar operator is therefore proportional to `Delta`, with normalized hexahedral stencil fixing the principal coefficient to one in physical cell coordinates.
- `RF-N1B source functional`: OPEN. `Delta_h ln N_R=S_R` is only a typed balance until `S_R` is independently derived. `Xi_I` is retained by bounded GREMLIN only as a lowest-order `L^-2` source-basis candidate, `S_R=beta_I Xi_I+...`; no promotion and no fitted `beta_I`.
- `RF-N1C Newton normalization`: OPEN. The target `c^2 S_R = 4 pi G rho_m` is not used as an input. `G` is not derived by RF-N1A.
- `IDT 01L`, `TIR phase-clock area v0.2`, `IDT 01K`, `RF-L0`: retained.
- `RF-M2`, `RF-N1B`, `RF-N1C`, `RF-E1`: OPEN.
