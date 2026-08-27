# Relational Field Closure
## From Spinorial Information Geometry to Hexahedral Coframes, Gauge Curvature and Dynamical Spacetime

**Working monograph v0.7 — 27 August 2026**  
**Status:** `EARLY_FORMALISM / EXACT_LOCAL_HEXAHEDRAL_METRIC_CONNECTION_AND_LORENTZ_RESULTS / NEWTON_SOURCE_DYNAMICS_OPEN`

## Abstract

Relational Field Closure (RFC) is a derivation-first programme asking whether Maxwell, Newton and Einstein structures can emerge from a common relational information geometry while the target laws remain outside the premise set.

The current construction begins with spin-1/2 projective geometry on `CP1`, decomposes the quantum geometric tensor into Fubini--Study metric and Berry-curvature sectors, and then passes from a single-ray rank-two geometry to a six-ray hexahedral dual frame. The six oriented face normals `{±e1,±e2,±e3}` have exact second moment `I3/3` and aggregate Fubini--Study orbit metric `I3/6`, giving a positive rank-three local spatial metric. IDT phase-clock dynamics supplies the physical scale `ell_phi=c/|omega|`, so the local hexahedral coframe becomes a physical length coframe. Together with the IDT temporal covector this yields exact Lorentzian signature.

RF-02I now advances the construction from a metric at one cell to its differential geometry. For a physicalized coframe `E^i=a vartheta^i` with `a=c/(sqrt(6)|omega|)`, the torsion-free metric connection is obtained exactly. On an integrable reference patch, the spatial scalar curvature becomes an explicit functional of first and second derivatives of the temporal phase rate. The same gate proves an exact negative result: spatial curvature with constant temporal lapse cannot by itself generate the Newtonian acceleration term. A nontrivial lapse/clock-rate field is therefore a mathematically mandatory next dependency. The Newtonian force-law kinematics follows conditionally from a weak lapse perturbation, while the Poisson source equation remains a separate dynamical derivation target.

## 1. Dependency firewall

The present stacked foundation is:

- TIR hexahedral Bloch branch: `agent/hexahedral-bloch-frame-v0.1`;
- IDT phase-clock branch: `feat/phase-clock-length-scale-v0.1`;
- Secret of a Half: pinned spinorial interface;
- RFC RF-02H: local rank-three hexahedral metric;
- RFC RF-02I: coframe connection and curvature.

The target equations of Maxwell, Newton and Einstein are used only as downstream validation oracles. A result is admitted because it follows from the declared geometry and passes its own checks, not because it resembles a known law.

## 2. Projective seed

A normalized spinor defines a ray

\[
[\psi]\in\mathbb{CP}^1\simeq S^2_{\rm Bloch}.
\]

For the quantum geometric tensor

\[
Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle,
\]

RFC uses the fixed convention

\[
\boxed{\Re Q_{\mu\nu}=g^{FS}_{\mu\nu}},
\qquad
\boxed{2\Im Q_{\mu\nu}=\Omega_{\mu\nu}}.
\]

The first projection supplies projective metric data; the second supplies Berry-curvature data.

A single `CP1` pullback has rank at most two. Three local spatial directions therefore require a multi-state configuration.

## 3. Hexahedral dual frame

Represent a regular hexahedral cell by its six oriented face normals,

\[
\boxed{\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\}}.
\]

The six Bloch representatives form the octahedral dual. Equal weights give

\[
\boxed{M_H=\frac13I_3}
\]

for the Bloch second moment. The aggregate FS orbit metric is

\[
\boxed{
h_H=\frac14(I_3-M_H)=\frac16I_3.
}
\]

Consequently,

\[
\boxed{
\operatorname{rank}h_H=3,
\quad
\det h_H=\frac1{216},
\quad
\operatorname{cond}h_H=1.
}
\]

The local spatial-rank prerequisite of the Lorentzian gate is therefore explicitly realized.

## 4. Integrated hexahedral invariants

The dual complex contains eight spherical octants. Each carries

\[
\Omega_{\rm oct}=\frac\pi2,
\qquad
a_{FS,\rm oct}=\frac\pi8,
\qquad
|\gamma_{B,\rm oct}|=\frac\pi4.
\]

The complete complex gives

\[
\boxed{
\chi=2,
\quad
\sum_fa_{FS}(f)=\pi,
\quad
\int_{S^2}\mathcal F_B=\pm2\pi,
\quad
c_1=\pm1.
}
\]

These quantities provide discrete-to-continuum refinement invariants independent of a particular drawing of the hexahedron.

## 5. Phase-clock physicalization

IDT supplies the calibrated phase rate

\[
\omega=\frac{d\varphi}{dt}
\]

and the exact local length carrier

\[
\boxed{
\ell_\varphi=\frac{c}{|\omega|}=\frac{\hbar c}{E}.
}
\]

For the regular isotropic hexahedral cell,

\[
\boxed{
h_H^{\rm phys}
=\frac{\ell_\varphi^2}{6}I_3
=\frac{c^2}{6\omega^2}I_3.
}
\]

Write the physical spatial coframe as

\[
\boxed{
E^i=a\,\vartheta^i,
\qquad
a=\frac{\ell_\varphi}{\sqrt6}
=\frac{c}{\sqrt6|\omega|}.
}
\]

Then

\[
\boxed{h_\perp=\delta_{ij}E^i\otimes E^j.}
\]

The reference orientation `vartheta^i` and the physical phase-clock scale `a` remain separately typed.

## 6. Anisotropic temporal rates and spatial metric

If the three antipodal face pairs carry scales

\[
\ell_i=\frac{c}{|\omega_i|},
\]

then the exact paired-rate metric is

\[
\boxed{
h_H^{\rm aniso}
=\frac1{12}
\operatorname{diag}
(\ell_2^2+\ell_3^2,
\ell_1^2+\ell_3^2,
\ell_1^2+\ell_2^2).
}
\]

Thus finite nonzero anisotropic phase rates preserve rank three while deforming the local spatial eigenvalues. This is a structural geometry result; the phase-rate evolution law remains a downstream dynamical problem.

## 7. Lorentzian local tetrad

Let IDT supply a nonvanishing temporal covector `Theta`. RF-G0 then gives

\[
\boxed{
g_L=-\Theta\otimes\Theta+h_\perp}
\]

with exact signature

\[
\boxed{(-,+,+,+)}.
\]

The local tetrad is

\[
\boxed{\{\Theta,E^1,E^2,E^3\}}.
\]

RF-02H therefore resolves the existence of a local positive three-dimensional spatial carrier. RF-02I asks how this tetrad changes from point to point and from cell to cell.

## 8. RF-02I torsion-free connection

Assume the dimensionless reference coframe has a torsion-free metric connection

\[
d\vartheta^i+\bar\omega^i{}_j\wedge\vartheta^j=0.
\]

For

\[
E^i=a\vartheta^i
\]

define

\[
f_i=E_i(\ln a).
\]

The physical torsion-free metric connection is exactly

\[
\boxed{
\omega^i{}_j
=\bar\omega^i{}_j+f_jE^i-f_iE^j.
}
\]

Because

\[
\ln a=\ln\!\left(\frac{c}{\sqrt6}\right)-\ln|\omega|,
\]

we have

\[
\boxed{f_i=-E_i\ln|\omega|.}
\]

Hence a nonuniform temporal phase rate contributes directly to the spatial connection. A uniform phase rate makes this scale-induced connection contribution vanish.

This is the first point in RFC where the temporal phase field enters a spatial connection through an exact differential relation rather than only through dimensional scaling.

## 9. Curvature generated by phase-rate gradients

The curvature two-form is

\[
\boxed{
\Omega^i{}_j
=d\omega^i{}_j+\omega^i{}_k\wedge\omega^k{}_j.
}
\]

On an integrable reference patch

\[
\vartheta^i=dx^i,
\qquad
\bar\omega^i{}_j=0,
\]

the spatial metric is conformally Euclidean,

\[
h_\perp=a(x)^2\delta_{ij}dx^idx^j.
\]

Its exact three-dimensional scalar curvature is

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

With

\[
a^{-2}=\frac{6\omega^2}{c^2},
\]

this is equivalently

\[
\boxed{
{}^{(3)}R
=\frac{24\omega\Delta\omega
-36|\nabla\omega|^2}{c^2}.
}
\]

Thus a spatially varying calibrated temporal phase rate produces a curvature scalar with the correct inverse-length-squared type through the already-derived physicalization map.

This is a conditional theorem for the integrable-reference subclass. It does not yet supply the dynamical equation determining `omega`.

## 10. Cell gluing as an SO(3) connection

Let neighboring hexahedral patches use coframes related by

\[
\boxed{E_{(B)}=R_{BA}E_{(A)},\qquad R_{BA}\in SO(3).}
\]

Metric compatibility follows from `R^T R=I`. The connection transforms as

\[
\boxed{
\omega_{(B)}
=R_{BA}\omega_{(A)}R_{BA}^{-1}
-dR_{BA}R_{BA}^{-1}.
}
\]

On consistent triple overlaps,

\[
\boxed{R_{CA}R_{BC}R_{AB}=I.}
\]

For a discrete closed cell sequence, the ordered product

\[
\boxed{\mathcal H_C=R_{10}R_{21}\cdots R_{0N}}
\]

is a discrete holonomy carrier. Its conjugacy invariants, such as `tr H_C`, are independent of the local frame labeling. A continuum connection requires a convergent refinement limit; that convergence is a dedicated evidence gate.

## 11. Exact negative theorem: spatial curvature is insufficient for Newton

Consider

\[
\boxed{
ds^2=-c^2dt^2+h_{ij}(x)dx^idx^j
}
\]

with static spatial geometry, zero shift and constant temporal coefficient. Since

\[
\partial_jg_{tt}=0,
\]

we obtain

\[
\boxed{\Gamma^i{}_{tt}=0.}
\]

Therefore a slowly moving test trajectory initially at rest has no leading Newtonian acceleration term generated solely by the static spatial metric gradient.

This is an exact negative result:

\[
\boxed{
\text{spatial phase-rate curvature alone}
\not\Rightarrow
\text{Newtonian acceleration}.
}
\]

The temporal sector must participate dynamically.

## 12. Mandatory RF-N0 lapse gate

The next temporal object is therefore a nontrivial lapse candidate

\[
\boxed{\Theta=N(x)c\,dt.}
\]

For

\[
\boxed{
ds^2=-N(x)^2c^2dt^2+h_{ij}(x)dx^idx^j
}
\]

with zero shift, one obtains exactly

\[
\boxed{
\Gamma^i{}_{tt}
=c^2N h^{ij}\partial_jN.
}
\]

The slow-motion kinematic acceleration is

\[
\boxed{
\frac{d^2x^i}{dt^2}
=-c^2N h^{ij}\partial_jN
+\text{velocity corrections}.
}
\]

If IDT later derives

\[
N=1+\frac{\Phi}{c^2}+O(c^{-4})
\]

and the spatial metric tends to the Euclidean limit, then

\[
\boxed{
\frac{d^2x^i}{dt^2}
=-\partial^i\Phi+O(c^{-2}).
}
\]

This is the Newtonian force-law kinematic form, conditional on the lapse derivation. The Poisson source equation remains outside the derivation at this stage.

## 13. Maxwell branch remains independent

The imaginary QGT sector gives the Berry connection and curvature,

\[
\mathcal F=d\mathcal A,
\qquad
d\mathcal F=0.
\]

This independently closes the homogeneous gauge-curvature identity. Sourced Maxwell dynamics still requires the source/action gate and physical electromagnetic normalization.

The separation is now sharp:

```text
Re Q + hexahedral configuration + phase clock -> spatial metric / connection / curvature
Im Q + Berry connection                     -> gauge curvature
```

Both sectors originate in the same projective state geometry but require independent physical closure tests.

## 14. Temporal information curvature and Lambda0

The information-area scalar remains

\[
\mathcal J_\pi=(\ln2)\mathcal I_\pi
\]

and, under phase-clock area physicalization,

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{\omega_P}{c}\right)^2,
\qquad
[\Xi_I]=L^{-2}.
}
\]

Using

\[
\kappa=\frac{\ln2}{24\pi},
\]

full CP1 gives

\[
\boxed{
\Xi_I=24\kappa\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2.
}
\]

RFC retains the information contribution

\[
\boxed{\Lambda_I=\alpha_I\Xi_I}
\]

inside the dynamic scalar sector. Phase-rate gradients now appear in two distinct places: spatial connection/curvature through RF-02I and inverse-area information curvature through RF-L0. Their action-level relation remains to be derived rather than identified by notation.

## 15. Current exact results and open dynamics

At v0.7, the following are exact within their declared classes:

1. QGT decomposition into FS metric and Berry curvature;
2. single-CP1 rank-at-most-two firewall;
3. hexahedral dual-frame rank-three local metric `h_H=I3/6`;
4. hexahedral Euler/FS/Berry/Chern integrated invariants;
5. Lorentzian signature from one temporal leg plus the positive hexahedral spatial triad;
6. phase-clock length `ell_phi=c/|omega|`;
7. torsion-free conformal coframe connection;
8. integrable-patch scalar curvature as a functional of `omega`;
9. SO(3) metric-compatible cell-gluing law;
10. constant-lapse negative theorem;
11. nontrivial-lapse Newtonian force-law kinematic bridge.

The active derivation frontier is now

\[
\boxed{
\mathrm{IDT}\to\mathrm{RF\!-\!N0:\ derive}\ N
\to\mathrm{RF\!-\!N1:\ derive\ source\ law}
\to\mathrm{Newton\ limit}.
}
\]

In parallel:

\[
\boxed{
\mathrm{Berry}\to\mathrm{sourced\ Maxwell}
}
\]

and then

\[
\boxed{
(g,\,F,\,T,\,\Lambda_0)
\to\mathrm{Einstein-Bianchi\ action\ closure}.
}
\]

The programme has therefore reached a useful negative as well as positive milestone: the spatial geometry is locally available, but the formalism itself shows that Newton cannot emerge until the temporal clock sector becomes a dynamical lapse. That result fixes the next dependency rather than allowing the derivation to choose it by resemblance to general relativity.
