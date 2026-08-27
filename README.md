# Relational Field Closure

**Status:** `EARLY_FORMALISM / EXACT_LOCAL_HEXAHEDRAL_METRIC_CONNECTION_RELATIONAL_LAPSE_AND_SOURCE_OPERATOR / SOURCE_AND_FIELD_CLOSURE_OPEN`

Relational Field Closure (RFC) is a derivation-first research repository testing whether Maxwell, Newton and Einstein field structures can be obtained from three pinned upstream theories:

1. **The Fundamental Theory of Informational Relations (TIR)**
2. **Secret of a Half**
3. **Informational Dynamics of Time (IDT)**

Dynamic `Lambda0` is carried as the candidate scalar closure entering the Einstein sector.

## Current geometry

The regular hexahedral Bloch dual frame

\[
\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\}
\]

has exact second moment and aggregate Fubini--Study orbit metric

\[
\boxed{M_H=I_3/3},
\qquad
\boxed{h_H=I_3/6}.
\]

Hence `rank(h_H)=3`, `det(h_H)=1/216`, and `cond(h_H)=1`. Its integrated dual-complex invariants include

\[
\chi=2,
\qquad
a_{FS}(S^2)=\pi,
\qquad
\int F_B=\pm2\pi,
\qquad
c_1=\pm1.
\]

IDT phase-clock dynamics supplies

\[
\boxed{
\ell_\varphi=\frac{c}{|\omega|}=\frac{\hbar c}{E},
\qquad
a_H=\frac{\ell_\varphi}{\sqrt6}.
}
\]

The physicalized regular spatial metric is

\[
\boxed{h_H^{phys}=\frac{c^2}{6\omega^2}I_3.}
\]

RF-02I derives the torsion-free conformal coframe connection

\[
\boxed{
\omega^i{}_j
=\bar\omega^i{}_j+f_jE^i-f_iE^j,
\qquad
f_i=-E_i\ln|\omega|,
}
\]

and, on an integrable reference patch,

\[
\boxed{
{}^{(3)}R
=\frac{24\omega\Delta\omega-36|\nabla\omega|^2}{c^2}.
}
\]

## Relational temporal lapse

IDT now supplies the native clock ratio

\[
\boxed{
N_R
=\frac{d\tau_x}{d\tau_{ref}}
=\frac{\phi_x}{\phi_{ref}}>0,
}
\]

which is exactly invariant under a common increasing reparameterization of the ordering variable. RFC binds it, after reference-clock calibration, to

\[
\boxed{\Theta_R=N_Rc\,dt}
\]

and therefore

\[
\boxed{g_R=-N_R^2c^2dt^2+h_\perp.}
\]

For a static zero-shift sector,

\[
\boxed{\Gamma^i{}_{tt}=c^2N_Rh^{ij}\partial_jN_R.}
\]

Defining

\[
\boxed{\Phi_R=c^2\ln N_R}
\]

gives

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-N_R^2h^{ij}\partial_j\Phi_R+\cdots,
}
\]

and near the reference sector/local Euclidean frame,

\[
\boxed{
\frac{d^2X^i}{dt^2}=-\partial^i\Phi_R+\cdots.
}
\]

## RF-N1: derived source operator

IDT 01D supplies the exact symmetric Shannon--Onsager response

\[
G^{(2)}_\pi
=(\ln2)D^\top\operatorname{diag}[c_{ab}\Lambda(r_a,r_b)]D,
\]

which reduces at uniform symmetric equilibrium to a positive relational-mobility graph Laplacian.

On the six hexahedral neighbour directions RFC defines

\[
(L_Hf)(x)=\sum_{i=1}^3[2f(x)-f(x+a_He_i)-f(x-a_He_i)]
\]

and

\[
\boxed{
\Delta_H^{(a)}f=-L_Hf/a_H^2.
}
\]

The exact refinement expansion is

\[
\boxed{
\Delta_H^{(a)}f
=\Delta f+\frac{a_H^2}{12}\sum_i\partial_i^4f+O(a_H^4).
}
\]

A separate signed-permutation classification theorem shows that hexahedral/octahedral symmetry removes first-order drift and off-diagonal second derivatives, forces equal principal coefficients, and the constant-null condition removes the zeroth-order term. Thus the leading local scalar second-order operator is

\[
\boxed{\mathscr L=\alpha\Delta,}
\]

with the normalized hexahedral stencil fixing `alpha=1` in physical cell coordinates.

Therefore for

\[
u=\ln N_R
\]

the operator side of the Newton source problem is locally derived:

\[
\boxed{
\Delta_hu=\mathcal S_R,
\qquad
\Delta_h\Phi_R=c^2\mathcal S_R.
}
\]

The source functional `S_R` is **not** yet derived.

## Source-identification firewall

Because `u` is dimensionless,

\[
[\mathcal S_R]=L^{-2}.
\]

The already-derived temporal information curvature

\[
\boxed{
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{rel}},
\qquad [\Xi_I]=L^{-2}
}
\]

is retained by bounded GREMLIN only as a lowest-order independent source-basis candidate,

\[
\boxed{
\mathcal S_R=\beta_I\Xi_I+\cdots.
}
\]

No value of `beta_I` is fitted or promoted. Spatial curvature `R^(3)` is quarantined as a primary Newton source because it would recycle the geometry being solved; `|grad u|^2` is typed as a possible higher-order self-term.

The Newton/Poisson target is passed only if a later independent derivation yields

\[
\boxed{
c^2\mathcal S_R=4\pi G\rho_m}
\]

with the correct mass source and normalization. `G` is not derived by RF-N1A.

## Parallel branches

The Berry sector retains

\[
\mathcal F=d\mathcal A,
\qquad
d\mathcal F=0,
\]

with sourced Maxwell dynamics open.

The information-curvature sector retains

\[
\Lambda_I=\alpha_I\Xi_I
\]

inside dynamic `Lambda0`. This makes the next comparison precise: determine whether the same independently derived `Xi_I` contributes to both lapse-source and `Lambda0` sectors, and derive the two couplings rather than identifying them by analogy.

## Immediate frontier

1. RF-N1B: derive the independent source functional `S_R` from admitted TIR/IDT matter/information dynamics;
2. RF-N1C: derive the mass-density map and normalization and only then test `c^2 S_R = 4 pi G rho_m`;
3. prove or falsify nonuniform hexahedral refinement convergence;
4. close sourced Maxwell dynamics and physical normalization;
5. determine/bound `alpha_I` and complete dynamic `Lambda0` action variation;
6. close Einstein--Bianchi dynamics and unified limits.

## Claim firewall

Target field equations remain validation targets. Exact operator results, candidate source bases, physical bindings and empirical/limit tests remain separately typed.
