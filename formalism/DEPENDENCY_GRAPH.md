# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_37_STACKED`

```text
TIR/IDT -> RFC conserved carrier / phase-energy source
 -> RF-N1B2K RFC↔Noether current/measure audit
 -> RF-N1B2O phase-energy matter-source factorization
 -> RF-N1B2P charge-projected RFC↔Maxwell intertwiner
 -> RF-E4 phase stress-energy / pressure firewall
 -> RF-E5 on-shell scalar carrier-energy firewall
 -> RF-E6 canonical Lorentzian action/source bookkeeping           PASS STACKED
 -> RF-E7 exact scalar T decomposition/recomposition               PASS STACKED
 -> single-complex-scalar total matter T_mn                        CLOSED
 -> multispecies/additional matter composition                     OPEN
 -> Einstein source closure / physical G universality
 -> dynamic Lambda0 independent action                             NEXT ACTION FRONTIER

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

RF-G0 fixes

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

RF-E6 aligns the matter action to

\[
\boxed{\mathcal L_m=-(D_\mu\Psi)^\dagger D^\mu\Psi-U(\Psi)}
\]

and fixes the charge-projected Maxwell source

\[
\boxed{J_{EM}^{\mu}=\hbar^{-1}\Pi_Q[J_{RFC}]^{\mu}.}
\]

RF-E7 writes one complex scalar as

\[
\psi=Ae^{i\vartheta},
\qquad
q_\mu=\partial_\mu\vartheta+\frac q\hbar A_\mu^{EM},
\]

so

\[
\boxed{
(D_\mu\psi)^*D^\mu\psi
=(\partial A)^2+A^2q^2.
}
\]

The mixed amplitude/phase terms cancel exactly, giving

\[
\boxed{
T_{\mu\nu}^{scalar}
=T_{\mu\nu}^{amp}
+T_{\mu\nu}^{phase}
+T_{\mu\nu}^{pot}.
}
\]

with

\[
T_{\mu\nu}^{amp}
=2\partial_\mu A\partial_\nu A-g_{\mu\nu}(\partial A)^2,
\]

\[
T_{\mu\nu}^{phase}
=2A^2q_\mu q_\nu-g_{\mu\nu}A^2q^2,
\]

\[
T_{\mu\nu}^{pot}=-g_{\mu\nu}V.
\]

The synchronized AB gauge shift leaves `q_mu` invariant, so the decomposition is gauge covariant.

For the homogeneous phase limit,

\[
\boxed{\varepsilon=K+V,\qquad p=K-V,\qquad \varepsilon+3p=4K-2V.}
\]

For the homogeneous quadratic on-shell scalar,

\[
\boxed{V=K,\qquad p=0,\qquad \varepsilon=2K.}
\]

A pure spatial amplitude gradient `partial_hat A=(0,g,0,0)` gives

\[
\boxed{T_{\hat a\hat b}^{amp}=\operatorname{diag}(g^2,g^2,-g^2,-g^2),}
\]

so gradient energy and anisotropic stress enter the Einstein source explicitly.

For the admitted single-scalar electromagnetic system,

\[
\boxed{
T_{\mu\nu}^{source}
=T_{\mu\nu}^{EM}+T_{\mu\nu}^{scalar},
}
\]

and RF-E6 supplies the on-shell exchange closure

\[
\boxed{\nabla^\mu T_{\mu\nu}^{source}=0.}
\]

## Validation authority

RF-E6 correction authority:

- PR #16;
- final head `e9d665c0b3b31719868d92bfd30631ba540a9a83`;
- final run `33207702078`, job `98972879666`;
- `470/470 PASS`.

RF-E7 stacked gate:

- PR #17;
- tested commit `904d641948b48ca564dbbfb38a9442e7ca6ab078`;
- run `33207870117`, job `98973459240`;
- `479/479 PASS`;
- receipt `validation/RFE7_TOTAL_SCALAR_STRESS_ENERGY_COMPOSITION_V0_1.json`.

## Open firewalls

```text
RF-N1B2K physical current/measure realization
multispecies/additional matter composition
IDT-01AG reciprocal Lorentzian current-sign alignment
first-principles alpha_EM gate if pursued
RFG35 vector-polarization projected-cut Ward audit
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system physical G universality
dynamic Lambda0 independent action and stability             NEXT ACTION FRONTIER
full Einstein/unified-limit audit
```
