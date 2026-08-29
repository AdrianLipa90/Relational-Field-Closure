# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / MAIN_PROMOTED_THROUGH_RF_E8`

```text
TIR/IDT -> RFC conserved carrier / phase-energy source
 -> RF-N1B2K RFC↔Noether current/measure audit
 -> RF-N1B2O phase-energy matter-source factorization
 -> RF-N1B2P charge-projected RFC↔Maxwell intertwiner
 -> RF-E4 phase stress-energy / pressure firewall
 -> RF-E5 on-shell scalar carrier-energy firewall
 -> RF-E6 canonical Lorentzian action/source bookkeeping           PASS
 -> RF-E7 exact scalar T decomposition/recomposition               PASS
 -> single-complex-scalar total matter T_mn                        CLOSED
 -> RF-L1 dynamic Lambda0 target                                   ADMITTED
 -> RF-L2 dynamic Lambda0 action + stability                       PASS
 -> RF-L3 information-scalar potential reconstruction              PASS
 -> RF-L4 information-curvature canonical pullback                 PASS
 -> RF-L4A Shannon-Fisher local normalization                      PASS
 -> RF-L5 Shannon-Onsager Temporal-Wave Klein-Gordon bridge        PASS
 -> RF-L5A premetric dimensional calibration                       PASS / MAIN
 -> IDT material clock slope Gamma_t = T_r a_r                     CROSS-REPO PASS
 -> RF-E8 ADM kinematic block assembly                             PASS / MAIN
 -> RF-E9 extrinsic-curvature geometry                             NEXT EINSTEIN-GEOMETRY GATE
 -> RF-E10 Gauss-Codazzi Einstein-tensor projections               OPEN
 -> matter projections / constraint source binding                 OPEN
 -> constraint propagation                                         OPEN
 -> Einstein/unified-limit audit                                   OPEN

Parallel coupling line:
project Yang-Mills normalization and BCJ
 -> four-point double copy / spin-2 / Einstein normalization
 -> five-point BG / KLT / project normalization / pole
 -> RFG29 explicit 15-graph BCJ
 -> RFG30 explicit 15-graph double-copy <-> KLT
 -> RFG31 matched-helicity internal tree spin-2 factorization
 -> RFG32 raw-loop mixed internal-state spectrum firewall
 -> RFG33 explicit pure-spin2 internal-state projector
 -> RFG34 projected s/t/u loop-cut channel covariance              PASS
 -> RFG35 vector-polarization projected-cut Ward audit             NEXT COUPLING FRONTIER
```

## Lorentzian matter spine

RF-G0 fixes `(-,+,+,+)`. RF-E6 fixes the canonical matter action and charge-projected Maxwell current,

\[
\boxed{J_{EM}^{\mu}=\hbar^{-1}\Pi_Q[J_{RFC}]^{\mu}.}
\]

RF-E7 closes the complete one-complex-scalar matter tensor,

\[
\boxed{T_{\mu\nu}^{scalar}=T_{\mu\nu}^{amp}+T_{\mu\nu}^{phase}+T_{\mu\nu}^{pot}.}
\]

Together with the Maxwell tensor,

\[
\boxed{T_{\mu\nu}^{base}=T_{\mu\nu}^{EM}+T_{\mu\nu}^{scalar}}
\]

is conserved on the admitted coupled equations.

## Information-curvature / Temporal-Wave spine

RF-L3 reconstructs the scalar potential from the admitted information carrier. RF-L4 supplies the canonical information-curvature pullback. RF-L4A binds the local quadratic curvature to the Shannon-Fisher normalization. RF-L5 composes the normalized curvature with the conservative IDT Temporal-Wave operator.

At uniform equilibrium,

\[
\boxed{
G_u^{(2)}(u)=\frac{\ln2}{N_s}K_0,
\qquad
K_0=\frac{N_s}{\ln2}G_u^{(2)}(u).
}
\]

RF-L5A then separates the premetric ordering-coordinate mass coefficient from the physical inverse-length mass coordinate:

\[
\boxed{
\frac{M_{eff}\Gamma_x^2}{\Gamma_t^2}=c^2,
\qquad
\mu_\lambda^2=\Gamma_t^2c^2m_I^2.
}
\]

IDT material temporal-offset binding supplies the typed time-slope source on the shared affine ordering patch,

\[
\boxed{
\Gamma_t=T_r\mathfrak a_r,
\qquad
\Gamma_{\tau,x|r}=T_r\mathfrak a_x=N_R\Gamma_t.
}
\]

The physical spatial scale `Gamma_x` remains a separate source/calibration gate.

## ADM kinematic spine

RF-E8 composes the TIR spatial metric and IDT positive lapse into the exact ADM block metric. With `x^0=ct` and typed shift `b^i`,

\[
\boxed{
 ds^2=-N_R^2(dx^0)^2
+h_{ij}(dx^i+b^i dx^0)(dx^j+b^j dx^0).
}
\]

The exact inverse and determinant are

\[
\boxed{
 g^{00}=-N_R^{-2},
\quad
g^{0i}=b^iN_R^{-2},
\quad
g^{ij}=h^{ij}-b^ib^jN_R^{-2},
}
\]

\[
\boxed{
\det g=-N_R^2\det h,
\qquad
\sqrt{-g}=N_R\sqrt h.
}
\]

This closes kinematic assembly. The next gate is the purely geometric definition and dimensional typing of the extrinsic curvature `K_ij` before any ADM constraint equation is admitted.

## TIR affine-gluing crosslink

TIR now carries an exact `SE(3)` affine-holonomy gate. Its main algebraic conclusion is that rotational `W_ij/SO(3)` data alone cannot determine translational affine loop closure. The RFC shift-source relation is therefore typed as

```text
TIR SE(3) affine local-frame transport
 -> local-frame displacement rate
 -> b^i
```

with the final source realization still gated. RF-E8 accepts `b^i` as a typed kinematic carrier and does not promote this candidate source map by itself.

## GREMLIN candidate overlay

Cross-formalism discovery is recorded separately in

`formalism/GREMLIN_CROSS_REPO_DEPENDENCY_OVERLAY_V0_1.md`.

The overlay remains `CANDIDATE_ONLY / CHYBA`; candidate compilation does not promote source claims.

## Validation authority

- RF-E6 PR #16: **470/470 PASS**.
- RF-E7 PR #17: **479/479 PASS**.
- RF-L2 PR #18: **489/489 PASS**.
- RF-L5 exact integrated head `ceac4269a9944e1a17d3a9321ab5d7975a4ce15d`: RFC reference suite **#207 SUCCESS**.
- RF-L5A exact head `08b92a7c3220844fbb63f341aa1a3974106e6ce6`: RFC reference suite **#208 SUCCESS**; merged through commit `4aa0e108846743e71f9d76f7f17c6e098d75293d`.
- RF-E8 exact head `60b19623b5f4fb5d42128780e8c4eb8d6a1139da`: RFC reference suite **#213 SUCCESS**; merged through commit `2032129a8aba66200a3c3d87647f1dcac12b7003`.
- IDT material temporal-offset binding exact head `d5d5def488776c1310d83e33c639b5e3078befec`: Reference suite **#868 SUCCESS**; cross-repository source pin `Gamma_t=T_r a_r` promoted to IDT main.

## Open firewalls

```text
RF-N1B2K physical current/measure realization
multispecies/additional matter composition
IDT-01AG reciprocal Lorentzian current-sign alignment
physical spatial Gamma_x / cell-width binding
TIR SE(3) gluing-rate -> ADM shift b^i source binding
RF-E9 extrinsic-curvature geometric definition                    NEXT
RF-E10 Gauss-Codazzi Einstein-tensor projection identities
matter energy/momentum projections into ADM source variables
Hamiltonian constraint source closure
momentum constraint source closure
constraint propagation
parameter-free Lambda0 calibration
global/nonlinear Lambda-sector stability
first-principles alpha_EM gate if pursued
RFG35 vector-polarization projected-cut Ward audit
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system physical G universality
full Einstein/unified-limit audit
```
