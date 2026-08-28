# Relational Field Closure — Canonical Dependency Graph

Status: `CURRENT_FRONTIER / CROSS_REFERENCE_LOCK_V0_25`

This graph records the current dependency spine. Historical graphs remain recoverable from Git history; this file is the active dependency view and must agree with `CROSS_REFERENCE_LOCK.json`.

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

hence

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

On the admitted same-sector normalization surface,

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

The link-orientation convention is explicit:

\[
W_\mu=\exp(i\sigma g aA_\mu),
\]

and the corresponding local nonabelian curvature uses the same fixed orientation. The four-point amplitude is orientation-even because its overall interaction power is `g^2`.

RFG15 produces, without gravity fitting,

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

The canonical numbering is unique:

```text
RFG15 project BCJ numerators
  -> RFG16 project double-copy construction + Ward gate
  -> RFG18 external tensor-product / spin-2 projector
  -> RFG19 spin-2 helicity + little-group gate
  -> RFG20 Einstein MHV normalization firewall
  -> RFG21 massless pole factorization
  -> RFG22 project four-point KLT equivalence
```

RFG20 identifies the project partial-amplitude normalization

\[
\boxed{A^{project}_{1234}=-2iA^{PT}_{1234}}.
\]

Therefore the compatible project double-copy replacement is

\[
\boxed{g\rightarrow\frac{\kappa_g}{4}},
\]

and the project-normalized four-point amplitude is

\[
\boxed{
\mathcal M_4^{project}
=-i\left(\frac{\kappa_g}{4}\right)^2
\mathcal C_{DC}^{project}
=-\frac{i\kappa_E}{4}\mathcal C_{DC}^{project}.
}
\]

This leaves the physical Einstein coupling unchanged:

\[
\boxed{\kappa_E=\frac{\kappa_g^2}{4}=8\pi G}.
\]

For the project MHV core,

\[
\boxed{\mathcal C_{--++}^{project}=-4\frac{s^3}{tu}},
\]

so

\[
\boxed{\mathcal M_{--++}^{project}=i\kappa_E\frac{s^3}{tu}}.
\]

The previous project-core coefficient `+i(kappa_g/2)^2` is rejected by the RFG20 exact factor `-4` firewall.

## 6. Pole and KLT closures

RFG21:

\[
\boxed{\lim_{t\to0}t\mathcal C_{DC}=X_t\widetilde X_t},
\]

and therefore, with RFG20 normalization,

\[
\boxed{\operatorname*{Res}_{t=0}\mathcal M_4^{project}=-\frac{i\kappa_E}{4}X_t\widetilde X_t}.
\]

RFG22 supplies the project four-point KLT core identity

\[
\boxed{\mathcal C_{DC}^{project}=-uA_{1234}\widetilde A_{1324}},
\]

hence

\[
\boxed{\mathcal M_4^{project}=+\frac{i\kappa_E}{4}uA_{1234}\widetilde A_{1324}}.
\]

## 7. G-free coupling holonomy

RFG17 connects the amplitude normalization back to the Newton/source/horizon routes:

\[
\boxed{\kappa_E=\frac1{M_HT_H}=\frac{4\Gamma_{DC}^2}{\alpha_c^2\omega_Q^2}}.
\]

Thus the same physical coupling coordinate appears in:

```text
Newton source
<-> reduced gravity scale
<-> horizon thermal product
<-> Einstein-Hilbert action
<-> project tree-level spin-2 amplitude
```

without changing the independent promotion firewalls for `M_star`, `Gamma_DC`, total matter stress-energy or cross-system universality.

## 8. Higher-point frontier

RFG23 is the first explicit higher-point gate:

```text
RFG22 four-point KLT
  -> RFG23 five-point MHV BCJ / soft-factorization reference
       |-> fundamental five-point BCJ relation        PASS REFERENCE
       |-> BCJ basis dimension (5-3)! = 2            PASS
       |-> positive-helicity soft factorization      PASS
       |-> project coupling power g_YM^3             PASS
       |-> direct project five-point vertex assembly OPEN
       |-> project five-point cubic numerators       OPEN
       `-> five-point KLT matrix                      NEXT RFG24
```

The immediate scientific frontier is therefore

\[
\boxed{\text{RFG24: five-point KLT / gravity soft-factorization normalization}}
\]

followed by direct five-point project assembly from the same RFG8/RFG13 interaction layer.

## 9. Independent open firewalls

These remain independently gated:

```text
full project five-point Feynman/Berends-Giele assembly
five-point project cubic numerator set
higher-point per-vertex normalization
internal-state / loop spectrum and pure-Einstein audit
Gamma_DC numerical promotion
M_star physical scale promotion
cross-system Mbar_G universality
universal G evidence
complete total-matter T_mn binding
dynamic Lambda_0 action closure
```

No one of these is promoted by the four-point or five-point reference gates alone.
