# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_26`

This graph is the active dependency view and must agree with `CROSS_REFERENCE_LOCK.json`.

## 1. Geometric / temporal base

```text
TIR information geometry
  -> RF01 relational field primitive
  -> RF02H rank-3 spatial metric
  -> RF02I coframe + metric-compatible torsion-free connection
  -> Lorentzian closure
  -> Riemann / Ricci / Einstein geometry

IDT phase-clock / relational lapse
  -> RFN0 relational lapse clock dynamics
  -> RFN1 hexahedral source operator
  -> RFN1B source-type firewall
  -> RFN1B2 conserved source carrier
  -> RFN1B2N normal phase rate
  -> RFN1B2O phase-energy/current source binding
```

The source-side local carrier chain is

\[
\omega_Q=D_{\hat\tau}\chi=\frac{D_t\chi}{N_R},
\qquad
\epsilon_N=\frac{\omega_Q}{2},
\]

\[
j_\vartheta=2A^2\omega_Q,
\qquad
\rho_\vartheta=\frac{A^2\omega_Q^2}{c^2}.
\]

## 2. Newton → Einstein coupling branch

```text
RFN1B2O phase source
  -> RFN1C three-route coupling holonomy
      |-> RFN1C1 local phase-source specialization
      |-> RFN1C2 carrier-scale universality firewall
      |-> RFN1C3 horizon reduced-gravity-scale closure
      `-> RFN1C4 double-copy carrier energy-type firewall
  -> RF-E3 Einstein-Hilbert normalization
  -> RF-E4 phase kinetic stress-energy firewall
  -> RF-E5 on-shell scalar carrier-energy firewall
```

Key reduced scale:

\[
\boxed{\bar M_G=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}=\frac{2}{\kappa_g}},
\]

\[
\boxed{G=\frac{1}{8\pi\bar M_G^2}},
\qquad
\boxed{\kappa_E=\frac{\kappa_g^2}{4}=8\pi G=\frac1{\bar M_G^2}}.
\]

The horizon route supplies

\[
\boxed{\bar M_G^2=M_HT_H}.
\]

## 3. Holonomic Yang–Mills normalization

```text
Metatime W_ij holonomy
  -> RFG3 Wilson continuum normalization
  -> RFG4 / RFG4B / RFG4C / RFG4D alpha_c genealogy
  -> RFG4E Wilson action coefficient firewall
  -> RFG4F link-coupling rescaling firewall
  -> RFG4G holonomy -> continuum -> Wilson transfer
```

On the admitted same-sector surface,

\[
\boxed{g_{YM}^2=\frac1{\alpha_c}},
\qquad
\boxed{C_p=2\alpha_c},
\qquad
\boxed{\beta_W=6\alpha_c}.
\]

## 4. Project field / interaction branch

```text
RFG4G
  -> RFG8 oriented cubic Yang-Mills vertex
  -> RFG10 link bytes -> A_mu^a -> momentum/polarization
  -> RFG11 noncommuting SU(3) principal-log curvature
  -> RFG12 nonabelian color/momentum convolution
  -> RFG13 quartic Yang-Mills contact normalization
  -> RFG14 complete exchange + contact A4 Ward gate
  -> RFG15 project four-point BCJ numerators
```

RFG15 gives

\[
\boxed{c_s-c_t+c_u=0},
\qquad
\boxed{n_s-n_t+n_u=0},
\]

with

\[
\boxed{n_i=X_i+D_iK_i}.
\]

## 5. Four-point gauge → gravity branch

Canonical four-point chain:

```text
RFG15 project BCJ numerators
  -> RFG16 project double-copy construction + Ward gate
  -> RFG18 external tensor-product / spin-2 projector
  -> RFG19 spin-2 helicity + little-group gate
  -> RFG20 Einstein MHV normalization firewall
  -> RFG21 massless pole factorization
  -> RFG22 project four-point KLT equivalence
```

RFG20 identifies

\[
\boxed{A^{project}_{1234}=-2iA^{PT}_{1234}},
\]

so the project-normalized transfer is

\[
\boxed{g\rightarrow\frac{\kappa_g}{4}}.
\]

Hence

\[
\boxed{
\mathcal M_4^{project}
=-i\left(\frac{\kappa_g}{4}\right)^2
\mathcal C_{DC}^{project}
=-\frac{i\kappa_E}{4}\mathcal C_{DC}^{project}.
}
\]

The physical Einstein coupling remains

\[
\boxed{\kappa_E=\frac{\kappa_g^2}{4}=8\pi G}.
\]

RFG21 supplies

\[
\boxed{\operatorname*{Res}_{t=0}\mathcal M_4^{project}
=-\frac{i\kappa_E}{4}X_t\widetilde X_t},
\]

and RFG22 supplies

\[
\boxed{\mathcal C_{DC}^{project}=-uA_{1234}\widetilde A_{1324}}.
\]

## 6. G-free coupling holonomy

RFG17 closes the same physical coupling coordinate across the source/horizon and amplitude routes:

\[
\boxed{
\kappa_E
=\frac1{M_HT_H}
=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}.
}
\]

Thus

```text
Newton source
<-> reduced gravity scale
<-> horizon thermal product
<-> Einstein-Hilbert action
<-> project spin-2 tree amplitude
```

share one admitted physical coupling coordinate, while their independent promotion firewalls remain intact.

## 7. Higher-point Yang–Mills branch

RFG23 is the five-point reference gate:

```text
RFG22 four-point KLT
  -> RFG23 five-point MHV BCJ / soft reference
       |-> fundamental five-point BCJ               PASS REFERENCE
       |-> BCJ basis dimension (5-3)! = 2           PASS
       `-> momentum-conserving soft factorization   PASS
```

RFG24 then builds the five-point amplitude directly from project currents:

```text
RFG8 cubic + RFG13 quartic
  -> RFG24 Berends-Giele project A5
       |-> five-leg Ward identities                 PASS
       |-> direct five-point BCJ                    PASS
       |-> reflection / insertion identities        PASS
       `-> g_YM^3 coupling power                    PASS
```

## 8. RFG26 project-current normalization firewall

The initial BG stripped-current coefficients were

\[
V_3^{base}:V_4^{base}=\sqrt2:1.
\]

RFG26 compares the resulting four-point BG amplitude directly with RFG15 and finds

\[
\boxed{A_4^{BG,base}=\frac12A_4^{RFG15}}.
\]

A common interaction normalization

\[
c=\sqrt2
\]

gives the project-consistent coefficients

\[
\boxed{V_3^{project}:V_4^{project}=2:2},
\]

while the gauge-coupling coordinate remains fixed. Then

\[
\boxed{A_4^{BG,project}=A_4^{RFG15}}.
\]

Tree scaling gives and the executable gate verifies

\[
\boxed{A_4^{project}=2A_4^{base}},
\qquad
\boxed{A_5^{project}=2\sqrt2\,A_5^{base}}.
\]

RFG24 consumes this corrected project-current convention.

## 9. Five-point KLT gravity branch

RFG23 supplies the two-amplitude BCJ basis. RFG25 constructs the \(2\times2\) momentum kernel directly and evaluates

\[
\boxed{
\mathcal C_5^{project}
=\mathbf A_L^{project\,T}S_5\mathbf A_R^{project}.
}
\]

RFG26 proves

\[
\boxed{\mathcal C_5^{project}=8\mathcal C_5^{base}}.
\]

The project-normalized gravity transfer therefore is

\[
\boxed{
\mathcal M_5^{project}
=i\left(\frac{\kappa_g}{4}\right)^3\mathcal C_5^{project}.
}
\]

Because

\[
\left(\frac{\kappa_g}{4}\right)^3
=\frac18\left(\frac{\kappa_g}{2}\right)^3,
\]

the physical product is unchanged:

\[
\boxed{
i\left(\frac{\kappa_g}{4}\right)^3\mathcal C_5^{project}
=
i\left(\frac{\kappa_g}{2}\right)^3\mathcal C_5^{base}.
}
\]

Reduced-scale form:

\[
\boxed{
\left(\frac{\kappa_g}{4}\right)^3
=\frac1{8\bar M_G^3}
=\frac{\kappa_E}{8\bar M_G}
=\frac1{8(M_HT_H)^{3/2}}.
}
\]

Corrected local replay:

```text
RFG24  6/6 PASS
RFG25  6/6 PASS
RFG26  6/6 PASS
TOTAL 18/18 PASS
```

## 10. Current frontier

The immediate next higher-point gate is

\[
\boxed{\text{RFG27: five-point multi-particle pole residue audit}}.
\]

It should test whether the direct RFG25 project KLT amplitude factorizes on a five-point multi-particle pole into admitted lower-point project amplitudes with the RFG26 normalization carried through exactly.

Parallel open gate:

```text
explicit 15-cubic-graph project numerator representation
```

Independent open firewalls:

```text
internal-state / loop spectrum and pure-Einstein audit
Gamma_DC numerical promotion
M_star physical scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```
