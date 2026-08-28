# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_26`

This graph is the active dependency view and is synchronized with `CROSS_REFERENCE_LOCK.json`.

## 1. Geometric / temporal base

```text
TIR information geometry
 -> RF01 relational field primitive
 -> RF02H rank-3 spatial metric
 -> RF02I coframe + metric-compatible torsion-free connection
 -> Lorentzian / Riemann / Ricci / Einstein geometry

IDT phase clock / relational lapse
 -> RFN0 relational lapse clock dynamics
 -> RFN1 hexahedral source operator
 -> RFN1B source-type firewall
 -> RFN1B2 conserved source carrier
 -> RFN1B2N normal phase rate
 -> RFN1B2O phase-energy/current source binding
```

\[
\omega_Q=D_{\hat\tau}\chi=\frac{D_t\chi}{N_R},\quad
\epsilon_N=\frac{\omega_Q}{2},\quad
j_\vartheta=2A^2\omega_Q,\quad
\rho_\vartheta=\frac{A^2\omega_Q^2}{c^2}.
\]

## 2. Newton → Einstein coupling branch

```text
RFN1B2O
 -> RFN1C three-route coupling holonomy
    |-> RFN1C1 local phase-source specialization
    |-> RFN1C2 carrier-scale universality firewall
    |-> RFN1C3 horizon reduced-gravity-scale closure
    `-> RFN1C4 double-copy carrier energy-type firewall
 -> RF-E3 Einstein-Hilbert normalization
 -> RF-E4 phase kinetic stress-energy firewall
 -> RF-E5 on-shell scalar carrier-energy firewall
```

\[
\boxed{\bar M_G=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}=\frac{2}{\kappa_g}},\qquad
\boxed{\kappa_E=\frac{\kappa_g^2}{4}=8\pi G=\frac1{\bar M_G^2}},\qquad
\boxed{\bar M_G^2=M_HT_H}.
\]

## 3. Holonomic Yang–Mills normalization

```text
Metatime W_ij
 -> RFG3 Wilson continuum
 -> RFG4/RFG4B/RFG4C/RFG4D alpha_c genealogy
 -> RFG4E Wilson coefficient
 -> RFG4F link-rescale firewall
 -> RFG4G holonomy/continuum/Wilson transfer
```

\[
\boxed{g_{YM}^2=1/\alpha_c},\qquad \boxed{\beta_W=6\alpha_c}.
\]

## 4. Project interaction branch

```text
RFG4G
 -> RFG8 cubic Yang-Mills vertex
 -> RFG10 link -> A_mu -> momentum/polarization
 -> RFG11 noncommuting SU(3) curvature
 -> RFG12 color/momentum convolution
 -> RFG13 quartic contact normalization
 -> RFG14 complete four-gluon Ward amplitude
 -> RFG15 project four-point BCJ numerators
```

RFG15 supplies

\[
\boxed{c_s-c_t+c_u=0},\qquad
\boxed{n_s-n_t+n_u=0},\qquad
\boxed{n_i=X_i+D_iK_i}.
\]

## 5. Four-point gauge → gravity branch

```text
RFG15
 -> RFG16 project double-copy + Ward
 -> RFG18 transverse tensor product / spin-2 projector
 -> RFG19 spin-2 helicity / little-group gate
 -> RFG20 Einstein MHV normalization firewall
 -> RFG21 massless pole factorization
 -> RFG22 project four-point KLT equivalence
```

RFG20 fixes the project four-point conversion:

\[
A_{1234}^{project}=-2iA_{1234}^{PT},\qquad
\boxed{g\to\kappa_g/4},
\]

\[
\boxed{\mathcal M_4^{project}=-\frac{i\kappa_E}{4}\mathcal C_{DC}^{project}},\qquad
\boxed{\mathcal C_{--++}^{project}=-4\frac{s^3}{tu}},
\]

so

\[
\boxed{\mathcal M_{--++}^{project}=i\kappa_E\frac{s^3}{tu}}.
\]

RFG21 and RFG22 then give

\[
\boxed{\operatorname*{Res}_{t=0}\mathcal M_4^{project}=-\frac{i\kappa_E}{4}X_t\widetilde X_t},
\]

\[
\boxed{\mathcal C_{DC}^{project}=-uA_{1234}\widetilde A_{1324}}.
\]

## 6. G-free coupling holonomy

RFG17 closes the common coupling coordinate

\[
\boxed{\kappa_E=\frac1{M_HT_H}=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}}.
\]

## 7. Higher-point tree spine

Canonical numbering is dependency-ordered and unique:

```text
RFG22 four-point KLT
 -> RFG23 five-point MHV BCJ / momentum-conserving soft reference
 -> RFG24 five-point KLT kernel / reduced-scale coordinate
 -> RFG25 direct project five-point Berends-Giele / BCJ
 -> RFG26 direct project five-point KLT gravity core
 -> RFG27 five-point project-to-Einstein normalization firewall   NEXT
 -> five-point multi-particle pole residue audit                  AFTER RFG27
```

RFG23 establishes the two-amplitude BCJ basis and soft reference. RFG24 establishes the `2 x 2` KLT kernel and exact reduced-scale coordinate

\[
P_5=\left(\frac{\kappa_g}{2}\right)^3=\frac1{\bar M_G^3}=\frac{\kappa_E}{\bar M_G}.
\]

RFG25 promotes the Yang–Mills side to direct project amplitudes from the inherited cubic/quartic interaction layer. RFG26 promotes the gravity **core** to

\[
\boxed{\mathcal C_5^{project}=\mathbf A_L^{project\,T}S_5\mathbf A_R^{project}}.
\]

The overall five-point amplitude is typed as

\[
\boxed{\mathcal M_5^{project}=\zeta_5P_5\mathcal C_5^{project}},
\]

with `zeta_5` determined only by RFG27. This firewall prevents automatic transfer of a conventional higher-point prefactor across a project normalization surface already known to be nontrivial at four points.

## 8. Independent open firewalls

```text
RFG27 five-point project-to-Einstein normalization
five-point multi-particle pole residue audit
explicit 15-cubic-graph project BCJ numerator representation
higher-point per-vertex normalization
internal-state / loop spectrum and pure-Einstein audit
Gamma_DC numerical promotion
M_star physical-scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```
