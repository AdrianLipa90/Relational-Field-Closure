# RF-02I — Hexahedral Coframe Gluing, Connection and Phase-Rate Curvature

Status: `EXACT_LOCAL_CONNECTION_THEOREM / EXACT_INTEGRABLE_PATCH_CURVATURE / GLOBAL_CELL_GLUE_AND_DYNAMICS_OPEN`

Stacked prerequisite:

- RF-02H `feat/rf02h-hexahedral-rank3-v0.1`, head `a53f399c9b944337d5af624b3c006b279da3ce3a`;
- TIR hexahedral dual-frame theorem;
- IDT phase-clock length `ell_phi=c/|omega|`.

## 1. Local hexahedral coframe

RF-02H supplies a positive rank-three local metric. In the isotropic regular-cell sector write

\[
\boxed{
E^i=a\,\vartheta^i,
\qquad
a:=\frac{\ell_\varphi}{\sqrt6}
=\frac{c}{\sqrt6\,|\omega|},
}
\]

and

\[
\boxed{h_\perp=\delta_{ij}E^i\otimes E^j.}
\]

Here `vartheta^i` is a dimensionless reference orientation coframe carried by the hexahedral dual frame. The physical scale and the reference orientation are therefore typed separately.

## 2. Torsion-free connection under conformal physicalization

Let the reference coframe carry a torsion-free metric connection `bar omega^i_j`,

\[
d\vartheta^i+\bar\omega^i{}_j\wedge\vartheta^j=0,
\qquad
\bar\omega_{ij}=-\bar\omega_{ji}.
\]

Let `E_i` be the frame dual to `E^i` and define

\[
\boxed{f_i:=E_i(\ln a).}
\]

Then the unique torsion-free metric connection of the physicalized coframe is

\[
\boxed{
\omega^i{}_j
=\bar\omega^i{}_j
+f_jE^i-f_iE^j.
}
\]

Indeed,

\[
dE^i=d\ln a\wedge E^i-\bar\omega^i{}_j\wedge E^j
\]

and substitution gives exactly

\[
\boxed{dE^i+\omega^i{}_j\wedge E^j=0.}
\]

Thus a spatially varying phase-clock scale generates a genuine connection contribution even when the dimensionless reference frame is itself flat.

Because

\[
\ln a=\ln\!\left(\frac{c}{\sqrt6}\right)-\ln|\omega|,
\]

one has

\[
\boxed{f_i=-E_i(\ln|\omega|).}
\]

Hence the scale-induced part is

\[
\boxed{
\omega^i{}_j-\bar\omega^i{}_j
=-q_jE^i+q_iE^j,
\qquad
q_i:=E_i(\ln|\omega|).
}
\]

A uniform nonzero phase rate gives `q_i=0`, so this additional connection vanishes exactly.

## 3. Integrable reference-patch theorem

On a patch where

\[
\boxed{\vartheta^i=dx^i}
\]

with dimensionless reference coordinates `x^i`, the reference connection vanishes and

\[
\boxed{h_\perp=a(x)^2\delta_{ij}dx^idx^j.}
\]

The scalar curvature of a three-dimensional conformal Euclidean metric `h=e^{2sigma}delta`, `sigma=ln a`, is

\[
\boxed{
{}^{(3)}R
=e^{-2\sigma}
\left[-4\Delta\sigma-2|\nabla\sigma|^2\right].
}
\]

With

\[
\sigma=\ln\!\left(\frac{c}{\sqrt6}\right)-\ln|\omega|,
\]

this becomes

\[
\boxed{
{}^{(3)}R
=a^{-2}
\left[
4\Delta\ln|\omega|
-2|\nabla\ln|\omega||^2
\right].
}
\]

Using `a^{-2}=6\omega^2/c^2`, an equivalent form is

\[
\boxed{
{}^{(3)}R
=\frac{24\omega\,\Delta\omega
-36|\nabla\omega|^2}{c^2}
}
\]

on a sign-definite nonzero-`omega` patch, where the derivatives are with respect to the dimensionless reference coordinates.

This is an exact conditional curvature theorem for the integrable-reference subclass. It does not insert an Einstein or Newton field equation.

## 4. Curvature two-forms

The spatial curvature two-form is

\[
\boxed{
\Omega^i{}_j
=d\omega^i{}_j
+\omega^i{}_k\wedge\omega^k{}_j.
}
\]

The phase-clock scale therefore enters spatial curvature through first and second derivatives of `ln|omega|`. In the general hexahedral cell complex, `bar omega` additionally carries the orientation/refinement connection of the dimensionless cell frames.

The split is

```text
reference cell gluing/orientation -> bar omega
phase-clock scale gradients       -> omega - bar omega
combined curvature                -> Omega
```

This separation allows the two sources of geometric curvature to be tested independently.

## 5. Inter-cell SO(3) gluing

Let neighboring cell patches `U_A,U_B` use local orthonormal spatial coframes related on their overlap by

\[
\boxed{E_{(B)}=R_{BA}E_{(A)},\qquad R_{BA}:U_A\cap U_B\to SO(3).}
\]

Metric compatibility is automatic because `R^T R=I`. The connection transforms as

\[
\boxed{
\omega_{(B)}
=R_{BA}\omega_{(A)}R_{BA}^{-1}
-dR_{BA}\,R_{BA}^{-1}.
}
\]

Equivalently the second term may be written `+R dR^{-1}`.

On triple overlaps the ordinary bundle cocycle condition is

\[
\boxed{R_{CA}R_{BC}R_{AB}=I}
\]

for consistent frame gluing. A nontrivial ordered product around a discrete closed cell loop is a holonomy observable and becomes a curvature diagnostic in a refinement limit.

## 6. Discrete refinement connection candidate

For neighboring hexahedral cells with normalized Bloch-frame triads, define the relative best-fit orientation `R_BA in SO(3)` from their face-normal correspondences. The discrete holonomy around a closed cell sequence is

\[
\boxed{
\mathcal H_C
=R_{10}R_{21}\cdots R_{0N}.
}
\]

The exact gauge-invariant conjugacy data are supplied by quantities such as

\[
\boxed{\operatorname{tr}\mathcal H_C}
\]

or the rotation angle of `H_C`. A continuum connection is admitted only if a refinement sequence gives a stable local generator and the corresponding metric/area/Berry invariants converge.

This is a candidate discretization contract; the continuum convergence theorem remains open.

## 7. Exact negative theorem before Newton

Consider a static block-diagonal spacetime metric

\[
\boxed{
ds^2=-c^2dt^2+h_{ij}(x)dx^idx^j
}
\]

with constant temporal coefficient and no shift. Then

\[
\partial_jg_{tt}=0,
\]

so

\[
\boxed{\Gamma^i{}_{tt}=0.}
\]

For a slowly moving test trajectory initially at rest in these coordinates, the leading geodesic acceleration therefore has no Newtonian force term generated solely by a static spatial metric gradient.

Consequently:

\[
\boxed{
\text{RF-02H/RF-02I spatial curvature alone}
\not\Rightarrow
\text{Newtonian acceleration}.
}
\]

This exact negative result makes the next dependency non-optional: RFC must derive a nontrivial temporal lapse/clock-rate field or an equivalent time-space coupling before claiming a Newtonian force limit.

## 8. Lapse kinematic bridge

Introduce the still-to-be-derived temporal lapse candidate

\[
\boxed{\Theta=N(x)c\,dt}
\]

and the static zero-shift metric

\[
\boxed{
ds^2=-N(x)^2c^2dt^2+h_{ij}(x)dx^idx^j.
}
\]

Then exactly

\[
\boxed{
\Gamma^i{}_{tt}
=c^2N h^{ij}\partial_jN.
}
\]

For slow motion,

\[
\boxed{
\frac{d^2x^i}{dt^2}
=-c^2N h^{ij}\partial_jN+\text{velocity corrections}.
}
\]

If a later RF-N0 derivation produces the weak-field expansion

\[
\boxed{N=1+\frac{\Phi}{c^2}+O(c^{-4})}
\]

and `h_ij=delta_ij+O(c^-2)` in physical coordinates, the kinematic limit is

\[
\boxed{
\frac{d^2x^i}{dt^2}
=-\partial^i\Phi+O(c^{-2}).
}
\]

This derives the Newtonian *force-law kinematics* from a lapse perturbation, conditional on the lapse binding. The Poisson source equation for `Phi` remains a separate dynamical gate and is not used here.

## 9. Updated dependency frontier

RF-02I therefore changes the geometry frontier to

```text
RF-02H local rank-3 hexahedral metric
  -> RF-02I coframe connection / curvature
  -> exact negative theorem: constant lapse cannot yield Newton force
  -> RF-N0 derive temporal lapse/clock-rate dynamics
  -> RF-N1 weak-field source equation / Poisson test
```

The key open physical questions are now:

1. derive the IDT-to-lapse map `N[temporal state]`;
2. determine whether `bar omega` is torsion-free under physical cell gluing or whether a torsional sector is generated;
3. prove or falsify convergence of discrete hexahedral holonomy to the continuum connection;
4. derive the action/source equation that determines the lapse/phase-rate field;
5. test the resulting weak-field source law against the Newton/Poisson target without inserting it upstream.
