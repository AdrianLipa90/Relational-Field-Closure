# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / ACTION_LEVEL_ADM_SPINE_CLOSED_THROUGH_RF_E13`

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
 -> RF-L5A premetric dimensional calibration                       PASS
 -> IDT material clock slope Gamma_t = T_r a_r                     CROSS-REPO PASS
 -> RF-E8 ADM kinematic block assembly                             PASS
 -> RF-E9 extrinsic-curvature geometry                             PASS
 -> RF-E10 Gauss-Codazzi Einstein-tensor projections               PASS
 -> RF-E11 matter projection/source typing                         PASS
 -> RF-E12 EH-action projected ADM source constraints              PASS
 -> RF-E13 spatial evolution + Bianchi constraint propagation      PASS / MAIN
 -> physical carrier/scale/coupling promotion                      ACTIVE FRONTIER

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
 -> Gamma_DC / M_star / physical G promotion                       OPEN
```

## Information-curvature / Temporal-Wave spine

RF-L5 composes the Shannon-Onsager stiffness and information-curvature mass sector. RF-L5A separates the ordering-coordinate coefficient from physical metric-time calibration:

\[
\boxed{
\frac{M_{eff}\Gamma_x^2}{\Gamma_t^2}=c^2,
\qquad
\mu_\lambda^2=\Gamma_t^2c^2m_I^2.
}
\]

IDT now supplies the promoted temporal calibration source

\[
\boxed{
\Gamma_t=T_r\mathfrak a_r,
\qquad
\Gamma_{\tau,x|r}=T_r\mathfrak a_x=N_R\Gamma_t.
}
\]

The physical spatial scale `Gamma_x` remains an upstream TIR/RFC calibration gate.

## ADM geometry spine

RF-E8 assembles

\[
\boxed{
 ds^2=-N^2(dx^0)^2
+h_{ij}(dx^i+b^i dx^0)(dx^j+b^j dx^0),
\qquad x^0=ct.
}
\]

RF-E9 fixes

\[
\boxed{
K_{ij}=-\frac12\mathcal L_n h_{ij}
=\frac{-\partial_0h_{ij}+D_ib_j+D_jb_i}{2N}.
}
\]

RF-E10 closes the pure geometric projections

\[
\boxed{
\mathcal G_H
={} ^{(3)}R+K^2-K_{ij}K^{ij}
=2G_{nn},
}
\]

\[
\boxed{
\mathcal G_{Mi}
=D_jK^j{}_i-D_iK
=-G_{ni}.
}
\]

## Matter and action projection spine

RF-E11 decomposes the admitted RFC matter tensor as

\[
\boxed{
T_{\mu\nu}
=\rho_n n_\mu n_\nu
+n_\mu j_\nu+j_\mu n_\nu+S_{\mu\nu},
}
\]

with

\[
\rho_n=T_{nn},
\qquad
j_i=-T_{ni}.
\]

RF-E3 already supplies the stated Einstein-Hilbert + matter action and its metric variation. RF-E12 now composes that action result with RF-E10/RF-E11:

\[
\boxed{
{} ^{(3)}R+K^2-K_{ij}K^{ij}
=2\kappa_E\rho_n,
}
\]

\[
\boxed{
D_jK^j{}_i-D_iK
=\kappa_Ej_i.
}
\]

For the RF-E3 dynamic-Lambda branch,

\[
\boxed{
{} ^{(3)}R+K^2-K_{ij}K^{ij}-2\Lambda_0
=2\kappa_E\rho_n,
}
\]

while the mixed constraint is unchanged.

The action variation and ADM projection composition are exact on the stated RF-E3 action. The project-derived physical value of `kappa_E` remains conditional on the RF-E3 double-copy normalization gates.

## Evolution and propagation spine

RF-E13 closes the spatial action projection

\[
\boxed{
(\partial_0-\mathcal L_b)h_{ij}=-2NK_{ij},
}
\]

\[
\boxed{
(\partial_0-\mathcal L_b)K_{ij}
=-D_iD_jN
+N\left({}^{(3)}R_{ij}+KK_{ij}-2K_{ik}K^k{}_j\right)
+N\kappa_E\left[\frac12h_{ij}(S-\rho_n)-S_{ij}\right].
}
\]

The dynamic-Lambda branch adds `-N Lambda0 h_ij`.

For constraint residuals

\[
\mathcal H
={} ^{(3)}R+K^2-K_{ij}K^{ij}-2\kappa_E\rho_n,
\]

\[
\mathcal M_i
=D_jK^j{}_i-D_iK-\kappa_Ej_i,
\]

Bianchi plus the admitted source ledger gives the homogeneous system

\[
\boxed{
(\partial_0-\mathcal L_b)\mathcal H
=2NK\mathcal H
-2ND_i\mathcal M^i
-4\mathcal M^iD_iN,
}
\]

\[
\boxed{
(\partial_0-\mathcal L_b)\mathcal M_i
=-\frac12ND_i\mathcal H
-\mathcal H D_iN
+NK\mathcal M_i.
}
\]

For the dynamic-Lambda branch, the already-recorded exchange law

\[
\boxed{
\kappa_E\nabla^\mu T_{\mu\nu}=\nabla_\nu\Lambda_0
}
\]

restores the same divergence-free residual ledger and the same homogeneous propagation form with `H -> H_Lambda`.

## TIR affine-gluing crosslink

TIR now contains two promoted algebraic gates:

```text
SE(3) affine-holonomy algebra
 -> rotational-only transport is insufficient for affine closure
 -> anchor-source binding t_ba = Q_b^T vec(E_ba)
 -> exact pure-atlas cocycle G_cb G_ba = G_ca
 -> pure-atlas closed holonomy = identity
 -> nontrivial holonomy requires a separately source-bound connection/obstruction
```

The infinitesimal anchored affine-frame generator gives

```text
v + Omega x
```

as a precise candidate contribution to the local ADM shift. General RFC `b^i` source binding remains gated because full shift freedom extends beyond rigid affine-frame transport.

## RF-E3 coupling firewall

RF-E3 carries

\[
\boxed{
\kappa_g^2=4\kappa_E,
\qquad
\frac{2}{\kappa_g^2}=\frac1{2\kappa_E}.
}
\]

The metric variation of the stated action is already admitted. Physical promotion of the project-side value

\[
\kappa_E^{DC}
=\frac{144\Gamma_{DC}^2}{\beta_W^2\omega_Q^2}
\]

still requires the frozen RF-E3 gates for `Gamma_DC`, carrier scale, matter/source binding and cross-system Newton universality.

## GREMLIN candidate overlay

Cross-formalism discovery remains recorded in

`formalism/GREMLIN_CROSS_REPO_DEPENDENCY_OVERLAY_V0_1.md`.

The overlay remains `CANDIDATE_ONLY / CHYBA`; candidate compilation never promotes source claims by itself.

## Validation authority

- RF-L5 exact head `ceac4269a9944e1a17d3a9321ab5d7975a4ce15d`: suite **#207 SUCCESS**.
- RF-L5A exact head `08b92a7c3220844fbb63f341aa1a3974106e6ce6`: suite **#208 SUCCESS**.
- RF-E8 exact head `60b19623b5f4fb5d42128780e8c4eb8d6a1139da`: suite **#213 SUCCESS**, merge `2032129a8aba66200a3c3d87647f1dcac12b7003`.
- RF-E9 exact head `8a5f775696ea0afe634745807fe3746156d24d21`: suite **#216 SUCCESS**, merge `cc06e9f8764a6a0012b88d09c04a2183e91e463f`.
- RF-E10 exact head `1e2a9fdb64cb33a1a741d3cae95301c6b2d589e5`: suite **#218 SUCCESS**, merge `d72a1aad6b6193ef5e51d09b9818bc2fe3d816d0`.
- RF-E11 exact head `0319653c6b8401ca28d31b662b07ad86248385a9`: suite **#220 SUCCESS**, merge `b0f326608d851a443f236707f2916ca4018bb617`.
- RF-E12 corrected exact head `7a2c4b015da9e048efdaed250c4a54aed97eecc5`: suite **#223 SUCCESS**, merge `da05ebd1962bee59d50d1626affb9a178ddba676`.
- RF-E13 exact head `40f403eb89a4f0e49b9fce0c2fb92f03c7b57ac9`: suite **#225 SUCCESS**, merge `09ff66035d333960ed8260fa0fd10c0d25bdad01`.
- IDT material temporal-offset exact head `d5d5def488776c1310d83e33c639b5e3078befec`: Reference suite **#868 SUCCESS**.

## Active frontier

```text
TIR connection transport beyond pure-atlas cocycle
TIR physical curvature/torsion/coframe realization
TIR/IDT/RFC physical spatial Gamma_x / cell-width binding
TIR affine-frame generator -> general ADM shift b^i source map
RF-N1B2K physical current/measure realization
multispecies/additional matter composition
parameter-free Lambda0 calibration and global stability
RFG35 vector-polarization projected-cut Ward audit
Gamma_DC numerical/physical promotion
M_star carrier-scale promotion
cross-system physical G universality
Standard-Model dynamical action/RG/radiative closure
```
