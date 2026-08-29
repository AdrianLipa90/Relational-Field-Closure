# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / MAIN_PROMOTED_THROUGH_RF_L5 / CROSS_REFERENCE_LOCK_V0_38`

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
 -> RF-L5 Shannon-Onsager Temporal-Wave Klein-Gordon bridge        PASS / MAIN
 -> RF-L5A premetric dimensional calibration                       NEXT STACKED GATE
 -> calibrated metric-time / light-cone binding                    OPEN
 -> parameter-free Lambda0 calibration / global stability          OPEN
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

## Dynamic Lambda0 action spine

RF-L2 introduces a canonical real scalar `phi_L` with potential `U_L`. The action split defines

\[
\boxed{\Lambda_0(x)=\Lambda_{ref}+\kappa_EU_L(\phi_L(x)).}
\]

while retaining

\[
\boxed{
T^{kin}_{\mu\nu}
=\nabla_\mu\phi_L\nabla_\nu\phi_L
-\frac12g_{\mu\nu}(\nabla\phi_L)^2
}
\]

as an explicit source contribution. On the scalar equation of motion,

\[
\boxed{
\kappa_E\nabla^\mu
\left(T^{base}_{\mu\nu}+T^{kin}_{\mu\nu}\right)
=\nabla_\nu\Lambda_0.
}
\]

At a stationary point `grad(phi_L)=0`, `U_L'=0`, the kinetic tensor vanishes and `Lambda0` is constant. Linear stability is typed by

\[
\boxed{m_L^2=U_L''(\phi_{L0})\ge0.}
\]

## Information-curvature / Temporal-Wave spine

RF-L3 reconstructs the scalar potential from the admitted information carrier. RF-L4 supplies the canonical information-curvature pullback. RF-L4A binds the local quadratic curvature to the Shannon-Fisher normalization. RF-L5 then composes the normalized curvature with the conservative IDT Temporal-Wave operator.

At uniform equilibrium,

\[
\boxed{
G_u^{(2)}(u)=\frac{\ln2}{N_s}K_0,
\qquad
K_0=\frac{N_s}{\ln2}G_u^{(2)}(u).
}
\]

With

\[
\boxed{m_I^2=\frac{\alpha_I}{\kappa_E},}
\]

the finite-graph conservative field equation is

\[
\boxed{
\ddot\phi_I+(K_0+m_I^2 I)\phi_I=0.
}
\]

For `K0 v_r=lambda_r v_r`,

\[
\boxed{\omega_r^2=\lambda_r+m_I^2.}
\]

RF-L5 is the current promoted `main` boundary. RF-L5A owns the next dimensional-typing step, introducing the premetric homogeneous coefficient `mu_lambda^2` and the calibrated relations

\[
\boxed{
\frac{M_{eff}\Gamma_x^2}{\Gamma_t^2}=c^2,
\qquad
\mu_\lambda^2=\Gamma_t^2c^2m_I^2.
}
\]

That RF-L5A surface remains the next stacked gate.

## GREMLIN candidate overlay

Cross-formalism discovery is recorded separately in

`formalism/GREMLIN_CROSS_REPO_DEPENDENCY_OVERLAY_V0_1.md`.

The overlay is typed `CANDIDATE_ONLY / CHYBA`. GREMLIN candidate classes organize theorem targets and source bindings; canonical RFC promotion remains controlled by source pins, typed realization maps, falsification gates, deterministic validators, and receipts.

## Validation authority

- RF-E6 PR #16: final head `e9d665c0b3b31719868d92bfd30631ba540a9a83`, run `33207702078`, **470/470 PASS**.
- RF-E7 PR #17: final head `ab433a32a8271ac629ef7c0863e3eaec9ee50ffd`, final run `33208035997`, **479/479 PASS**.
- RF-L2 PR #18: tested commit `38c9589608abe77bdcf05d46e997731ef5d6e430`, run `33208242527`, job `98974734417`, **489/489 PASS**.
- RF-L5 integrated head `ceac4269a9944e1a17d3a9321ab5d7975a4ce15d`: RFC reference suite run **#207 SUCCESS**; this exact head was promoted to `main` by non-force fast-forward on 2026-08-29.

## Open firewalls

```text
RF-N1B2K physical current/measure realization
multispecies/additional matter composition
IDT-01AG reciprocal Lorentzian current-sign alignment
RF-L5A premetric dimensional calibration                         NEXT LAMBDA/TIME FRONTIER
physical cell-width / clock-lapse source binding
parameter-free Lambda0 calibration
global/nonlinear Lambda-sector stability
first-principles alpha_EM gate if pursued
RFG35 vector-polarization projected-cut Ward audit
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system physical G universality
ADM Hamiltonian and momentum constraint derivation
constraint propagation
full Einstein/unified-limit audit
```
