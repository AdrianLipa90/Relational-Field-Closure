# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_27`

## 1. Source and geometry spine

```text
TIR geometry -> RF02H/RF02I -> Lorentzian/Riemann/Einstein geometry
IDT phase clock -> RFN0 -> RFN1 -> RFN1B2 -> RFN1B2O phase-energy source
RFN1B2O -> RFN1C -> RFN1C1/C2/C3/C4 -> RF-E3/E4/E5
```

\[
\omega_Q=D_{\hat\tau}\chi=\frac{D_t\chi}{N_R},\quad
\epsilon_N=\omega_Q/2,\quad
j_\vartheta=2A^2\omega_Q,\quad
\rho_\vartheta=A^2\omega_Q^2/c^2.
\]

\[
\bar M_G=\frac{2}{\kappa_g},\qquad
\kappa_E=\frac{\kappa_g^2}{4}=8\pi G=\frac1{\bar M_G^2},\qquad
\bar M_G^2=M_HT_H.
\]

## 2. Yang–Mills / four-point gravity spine

```text
RFG3 -> RFG4G -> RFG8/RFG10/RFG11/RFG12/RFG13
 -> RFG14 complete A4 Ward gate
 -> RFG15 matched-Jacobi project numerators
 -> RFG16 project double copy
 -> RFG18 spin-2 projector
 -> RFG19 helicity/little-group
 -> RFG20 Einstein MHV normalization
 -> RFG21 pole factorization
 -> RFG22 four-point KLT
```

RFG20 fixes

\[
A_4^{project}=2A_4^{PT(raw)},\qquad
\mathcal M_4^{project}=-\frac{i}{4}\left(\frac{\kappa_g}{2}\right)^2\mathcal C_4^{project}.
\]

RFG17 simultaneously supplies

\[
\kappa_E=\frac1{M_HT_H}=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}.
\]

## 3. Higher-point tree spine

```text
RFG22 four-point KLT
 -> RFG23 five-point BCJ / conserved gauge soft reference
 -> RFG24 five-point KLT kernel / reduced-scale coordinate
 -> RFG25 direct vertex Berends-Giele / BCJ
 -> RFG26 direct BG x BG KLT gravity core
 -> RFG27 project normalization + conserved gravity soft transport
 -> RFG28 five-point multi-particle pole residue audit          NEXT
```

RFG27 identifies the color-order basis map

\[
\boxed{\eta_A=2},\qquad
\boxed{A_5^{project}=2A_5^{BG}},
\]

so the KLT bilinear maps as

\[
\boxed{\mathcal C_5^{project}=4\mathcal C_5^{BG}}.
\]

For the reduced-scale coordinate

\[
P_5=\left(\frac{\kappa_g}{2}\right)^3=\frac1{\bar M_G^3},
\]

the momentum-conserving gravity soft gate gives

\[
\boxed{\frac{\mathcal C_5^{project}}{S_5^+\mathcal C_4^{project}}\to1},
\]

and therefore

\[
\boxed{\mathcal M_5^{project}=-\frac{i}{4}P_5\mathcal C_5^{project}=-iP_5\mathcal C_5^{BG}}.
\]

The previous `+i P5 C5_BG` expression is rejected by an exact soft-limit phase ratio `-1`.

## 4. Current open firewalls

```text
RFG28 five-point multi-particle pole residue audit
explicit 15-cubic-graph project BCJ numerator representation
higher-point per-vertex normalization beyond the pinned color-order map
internal-state / loop spectrum and pure-Einstein audit
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```
