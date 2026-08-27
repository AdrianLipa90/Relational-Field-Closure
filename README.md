# Relational Field Closure

**Status:** `EARLY_FORMALISM / EXACT_QGT_HEXAHEDRAL_RANK3_LORENTZ_AND_LOCAL_CONNECTION_RESULTS / NEWTON_SOURCE_DYNAMICS_OPEN`

Relational Field Closure (RFC) is a derivation-first research repository testing whether Maxwell, Newton and Einstein field structures can be obtained from three pinned upstream theories:

1. **The Fundamental Theory of Informational Relations (TIR)**
2. **Secret of a Half**
3. **Informational Dynamics of Time (IDT)**

The repository carries dynamic `Lambda0` as the candidate scalar closure entering the Einstein sector.

## Projective and hexahedral core

For a projective state,

\[
Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle,
\qquad
\Re Q=g^{FS},
\qquad
2\Im Q=\Omega.
\]

A single `CP1` pullback has rank at most two. RF-02H therefore uses the six oriented face-normal Bloch rays of a regular hexahedron,

\[
\boxed{\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\}.}
\]

With equal weights,

\[
\boxed{M_H=\frac13I_3},
\qquad
\boxed{h_H=\frac14(I_3-M_H)=\frac16I_3}.
\]

Hence

\[
\boxed{
\operatorname{rank}h_H=3,
\qquad
\det h_H=\frac1{216},
\qquad
\operatorname{cond}h_H=1.
}
\]

The exact integrated dual-complex invariants include

\[
\boxed{
\chi=2,
\qquad
\sum_fa_{FS}(f)=\pi,
\qquad
\int_{S^2}F_B=\pm2\pi,
\qquad
c_1=\pm1.
}
\]

## Phase-clock physicalized spatial metric

IDT supplies

\[
\boxed{
\ell_\varphi=\frac{c}{|\omega|}=\frac{\hbar c}{E}.
}
\]

For a common local phase rate,

\[
\boxed{
h_H^{\rm phys}=\frac{c^2}{6\omega^2}I_3.}
\]

Write

\[
\boxed{
E^i=a\vartheta^i,
\qquad
a=\frac{c}{\sqrt6|\omega|},
\qquad
h_\perp=\delta_{ij}E^i\otimes E^j.
}
\]

With the temporal covector `Theta`,

\[
\boxed{g_L=-\Theta\otimes\Theta+h_\perp}
\]

has exact signature `(-,+,+,+)`.

## RF-02I coframe connection

If the dimensionless reference coframe is torsion-free with connection `bar_omega`, the physicalized torsion-free metric connection is

\[
\boxed{
\omega^i{}_j
=\bar\omega^i{}_j+f_jE^i-f_iE^j,
\qquad
f_i=E_i\ln a=-E_i\ln|\omega|.
}
\]

Thus spatial gradients of the calibrated temporal phase rate contribute directly to the spatial connection.

On an integrable reference patch `vartheta^i=dx^i`, the three-dimensional scalar curvature is

\[
\boxed{
{}^{(3)}R
=a^{-2}
\left[4\Delta\ln|\omega|-2|\nabla\ln|\omega||^2\right]
}
\]

or equivalently

\[
\boxed{
{}^{(3)}R
=\frac{24\omega\Delta\omega-36|\nabla\omega|^2}{c^2}.
}
\]

Neighboring spatial coframes glue by `SO(3)` transition maps,

\[
E_{(B)}=R_{BA}E_{(A)},
\]

with connection law

\[
\boxed{
\omega_{(B)}
=R_{BA}\omega_{(A)}R_{BA}^{-1}
-dR_{BA}R_{BA}^{-1}.
}
\]

Discrete closed products of the cell rotations are the refinement-holonomy carriers.

## Exact Newton dependency result

For a static constant-lapse metric

\[
\boxed{ds^2=-c^2dt^2+h_{ij}(x)dx^idx^j,}
\]

one has

\[
\boxed{\Gamma^i{}_{tt}=0.}
\]

Therefore static spatial curvature alone cannot generate the leading Newtonian acceleration term for a slowly moving test trajectory initially at rest.

The next temporal gate is consequently mandatory. With

\[
\boxed{\Theta=N(x)c\,dt}
\]

and zero shift,

\[
\boxed{\Gamma^i{}_{tt}=c^2N h^{ij}\partial_jN.}
\]

If RF-N0 later derives

\[
N=1+\frac{\Phi}{c^2}+O(c^{-4}),
\]

then the slow-motion kinematic limit is

\[
\boxed{
\frac{d^2x^i}{dt^2}=-\partial^i\Phi+O(c^{-2}).
}
\]

The Poisson/source equation for `Phi` remains a separate dynamical derivation target.

## Temporal information curvature and dynamic Lambda0

With

\[
\mathcal J_\pi=(\ln2)\mathcal I_\pi=24\pi\kappa\mathcal I_\pi,
\]

RFC uses

\[
\boxed{
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}},
\qquad [\Xi_I]=L^{-2}.
}
\]

For a constant-rate cell,

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}\left(\frac{\omega_P}{c}\right)^2.
}
\]

RFC retains

\[
\boxed{\Lambda_I=\alpha_I\Xi_I}
\]

inside the dynamic scalar basis for `Lambda0`.

## Maxwell branch

The imaginary QGT sector supplies

\[
\mathcal F=d\mathcal A,
\qquad
d\mathcal F=0.
\]

Sourced Maxwell dynamics and physical normalization remain dedicated downstream gates.

## Immediate frontier

1. derive the IDT-to-lapse map `N[temporal state]` in RF-N0;
2. prove or falsify global hexahedral coframe/refinement convergence and classify possible torsion;
3. derive the full tetrad connection and curvature including the temporal leg;
4. derive the weak-field source equation and test the Newton/Poisson target;
5. close sourced Maxwell dynamics;
6. determine or bound `alpha_I` and complete dynamic `Lambda0` action variation;
7. close Einstein--Bianchi dynamics and unified limits.

## Claim firewall

Target equations remain validation targets. A closure is promoted only after upstream provenance, covariance, dimensional and physical-limit gates pass.
