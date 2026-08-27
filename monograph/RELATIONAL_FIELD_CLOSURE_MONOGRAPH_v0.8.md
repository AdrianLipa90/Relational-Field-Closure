# Relational Field Closure
## Hexahedral Spacetime from Projective Geometry, Temporal Phase and Relational Clock Ratios

**Working monograph v0.8 — 27 August 2026**  
**Status:** `EXACT_LOCAL_METRIC_CONNECTION_AND_RELATIONAL_LAPSE_KINEMATICS / NEWTON_SOURCE_LAW_OPEN`

## Abstract

RFC has now reached a local `3+1` geometry in which neither the three positive spatial directions nor the variable temporal lapse need be inserted as free geometric functions.

The spatial sector comes from the regular hexahedral Bloch dual frame. Six oriented hexahedral face-normal rays `{±e1,±e2,±e3}` have second moment `I3/3` and aggregate Fubini--Study orbit metric `I3/6`. IDT phase-clock dynamics supplies the physical scale `ell_phi=c/|omega|`, converting that dimensionless local three-metric into a physical spatial coframe. RF-02I then derives the torsion-free connection of the physicalized coframe and, on an integrable reference patch, expresses spatial scalar curvature directly through first and second derivatives of the temporal phase rate.

The temporal sector now advances independently. IDT 05C supplies a positive, dimensionless and reparameterization-invariant relational clock ratio

\[
N_R=\frac{d\tau_x}{d\tau_{ref}}=\frac{\phi_x}{\phi_{ref}}.
\]

After physical reference-clock calibration RFC binds this ratio to the temporal coframe `Theta_R=N_R c dt`. The resulting static geodesic kinematics gives an exact acceleration driven by gradients of `N_R`. Defining `Phi_R=c^2 ln N_R` yields the Newtonian force-law form in the weak-reference limit, while the Poisson/source equation remains outside the premise set and becomes the next dedicated derivation gate.

The important change at v0.8 is therefore structural: Newtonian force kinematics is no longer waiting for an arbitrary lapse ansatz. The lapse carrier is already present in IDT as a relational clock ratio. What remains open is the field equation that determines that ratio and its normalization.

## 1. Projective origin of the spatial triad

The quantum geometric tensor is

\[
Q_{\mu\nu}=\langle D_\mu\psi|D_\nu\psi\rangle,
\]

with

\[
\boxed{\Re Q=g^{FS}},
\qquad
\boxed{2\Im Q=\Omega}.
\]

A single `CP1` ray cannot carry a rank-three pullback metric. RFC therefore uses the six-state hexahedral face-normal configuration

\[
\boxed{\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\}}.
\]

Equal weights give

\[
\boxed{M_H=I_3/3}
\]

and

\[
\boxed{h_H=\frac14(I_3-M_H)=I_3/6.}
\]

Thus

\[
\boxed{\operatorname{rank}h_H=3},
\qquad
\boxed{\det h_H=1/216},
\qquad
\boxed{\operatorname{cond}h_H=1}.
\]

The dual spherical complex also carries

\[
\chi=2,
\qquad
\sum_fa_{FS}(f)=\pi,
\qquad
\int F_B=\pm2\pi,
\qquad
c_1=\pm1.
\]

## 2. Spatial scale from IDT phase flow

IDT supplies

\[
\boxed{\ell_\varphi=\frac{c}{|\omega|}=\frac{\hbar c}{E}.}
\]

For the regular local hexahedral cell,

\[
\boxed{
h_H^{phys}=\frac{c^2}{6\omega^2}I_3.}
\]

Writing

\[
E^i=a\vartheta^i,
\qquad
a=\frac{c}{\sqrt6|\omega|},
\]

gives

\[
\boxed{h_\perp=\delta_{ij}E^i\otimes E^j.}
\]

Anisotropic paired phase rates produce the exact diagonal deformation

\[
\boxed{
h_H^{aniso}
=\frac1{12}\operatorname{diag}
(\ell_2^2+\ell_3^2,
\ell_1^2+\ell_3^2,
\ell_1^2+\ell_2^2).
}
\]

## 3. Phase-rate connection and curvature

For `E^i=a vartheta^i`, with torsion-free reference connection `bar omega`, RF-02I gives

\[
\boxed{
\omega^i{}_j
=\bar\omega^i{}_j+f_jE^i-f_iE^j,
\qquad
f_i=-E_i\ln|\omega|.
}
\]

On an integrable reference patch `vartheta^i=dx^i`,

\[
\boxed{
{}^{(3)}R
=a^{-2}\left[4\Delta\ln|\omega|-2|\nabla\ln|\omega||^2\right]
}
\]

or

\[
\boxed{
{}^{(3)}R
=\frac{24\omega\Delta\omega-36|\nabla\omega|^2}{c^2}.
}
\]

Thus nonuniform temporal phase rate generates spatial connection and curvature through exact differential geometry. The action governing `omega` remains open.

## 4. Why a temporal lapse is mandatory

For

\[
ds^2=-c^2dt^2+h_{ij}(X)dX^idX^j
\]

with static spatial geometry and zero shift,

\[
\boxed{\Gamma^i{}_{tt}=0.}
\]

Therefore spatial curvature alone cannot generate the leading Newtonian acceleration term for a slowly moving particle initially at rest.

This negative theorem fixes the next dependency: a nontrivial temporal lapse is required.

## 5. IDT relational lapse

IDT internal elapsed activity is

\[
d\tau=\phi\,d\lambda,
\qquad
\phi=\frac{\mathfrak a}{\mathfrak a_\star}>0.
\]

For a local subsystem and a reference clock,

\[
d\tau_x=\phi_xd\lambda,
\qquad
d\tau_{ref}=\phi_{ref}d\lambda.
\]

The native relational lapse is

\[
\boxed{
N_R
=\frac{d\tau_x}{d\tau_{ref}}
=\frac{\phi_x}{\phi_{ref}}>0.
}
\]

Under any common increasing reparameterization `lambda -> lambda'`, both pace densities acquire the same Jacobian and the ratio is invariant:

\[
\boxed{N_R'=N_R.}
\]

Reference changes compose multiplicatively,

\[
\boxed{N_{x|s}=N_{x|r}N_{r|s}.}
\]

This makes `N_R` a genuine relational clock-ratio invariant rather than an arbitrary coordinate scalar.

## 6. Kinetic content of the lapse

IDT gives

\[
\phi=\frac{2M}{\mathfrak a_\star}\cosh(A/2).
\]

For a common activity normalization,

\[
\boxed{
N_R
=\frac{M_x\cosh(A_x/2)}
{M_{ref}\cosh(A_{ref}/2)}.
}
\]

For a fixed reference sector,

\[
\boxed{
\nabla\ln N_R
=\nabla\ln M
+\frac12\tanh(A/2)\nabla A.
}
\]

Since

\[
M=\frac{\sqrt{\rho_R(a)\rho_R(b)}}{\eta_{ab}},
\qquad
\eta_{ab}=\frac{\eta_R(a)+\eta_R(b)}2,
\]

one has

\[
\boxed{
\nabla\ln M
=\frac12\nabla\ln\rho_R(a)
+\frac12\nabla\ln\rho_R(b)
-\nabla\ln\eta_{ab}.
}
\]

Therefore the lapse gradient is already decomposed into the upstream relational density, viscosity and directional-drive sectors.

## 7. Temporal coframe and local spacetime

After physical calibration of the reference clock,

\[
\boxed{\Theta_R=N_Rc\,dt.}
\]

The local spacetime metric is

\[
\boxed{
g_R=-N_R^2c^2dt^2+h_\perp.}
\]

The full local tetrad may be written

\[
\boxed{
\mathcal E^0=N_Rc\,dt,
\qquad
\mathcal E^i=\frac{c}{\sqrt6|\omega|}\vartheta^i.
}
\]

Both temporal and spatial leg magnitudes are therefore supplied by upstream temporal dynamics, although through two distinct functions:

\[
N_R=\text{elapsed-clock ratio},
\qquad
\omega=\text{phase rate}.
\]

No equality between these two functions is assumed.

## 8. Exact relational-lapse acceleration

For the static zero-shift metric,

\[
\boxed{
\Gamma^i{}_{tt}
=c^2N_Rh^{ij}\partial_jN_R.
}
\]

The slow-motion kinematic acceleration is

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_Rh^{ij}\partial_jN_R+\cdots
}
\]

or

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_R^2h^{ij}\partial_j\ln N_R+\cdots.
}
\]

Define

\[
\boxed{\Phi_R:=c^2\ln N_R.}
\]

Then

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-N_R^2h^{ij}\partial_j\Phi_R+\cdots.
}
\]

Near the reference sector, `N_R=1+epsilon_N` with `|epsilon_N|<<1`, and in a locally Euclidean physical frame,

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-\partial^i\Phi_R+\text{higher-order terms}.
}
\]

Thus the force-law form arises from the IDT clock ratio rather than from a gravitational-potential ansatz.

## 9. Direct upstream decomposition of the acceleration carrier

For fixed reference clock,

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_R^2h^{ij}
\left[
\partial_j\ln M
+\frac12\tanh(A/2)\partial_jA
\right]+\cdots.
}
\]

Expanding the mobility gives

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_R^2h^{ij}
\left[
\frac12\partial_j\ln\rho_R(a)
+\frac12\partial_j\ln\rho_R(b)
-\partial_j\ln\eta_{ab}
+\frac12\tanh(A/2)\partial_jA
\right]+\cdots.
}
\]

This is the current deepest Newton-facing result of RFC: a slow-motion acceleration carrier expressed entirely through the derived relational lapse and its upstream kinetic variables. It is still kinematic because the field equation determining those variables has not yet been derived.

## 10. Independent Maxwell and Lambda0 branches

The Berry sector remains

\[
\mathcal F=d\mathcal A,
\qquad
d\mathcal F=0,
\]

with sourced Maxwell dynamics open.

The information-curvature scalar remains

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}\left(\frac{\omega_P}{c}\right)^2,
\qquad [\Xi_I]=L^{-2},
}
\]

and RFC retains

\[
\Lambda_I=\alpha_I\Xi_I
\]

inside dynamic `Lambda0`.

These branches remain independently testable before their final Einstein--Bianchi coupling.

## 11. Current frontier: source dynamics

The Newton branch has now separated cleanly into:

\[
\boxed{
\text{clock-ratio lapse}
\to
\text{temporal metric coefficient}
\to
\text{geodesic acceleration}
\to
\text{weak force-law form}
}
\]

which is structurally available, and

\[
\boxed{
\text{source/action equation for }N_R
\to
\text{normalization}
\to
\text{Poisson/Newton target test}
}
\]

which remains open.

RF-N1 must therefore derive, from upstream conservation/action principles, the equation that determines the relational lapse. It may compare the resulting weak equation with

\[
\nabla^2\Phi=4\pi G\rho
\]

only after the derivation is complete; the target equation is not permitted as an input.

The same discipline continues on the Maxwell and Einstein branches. RFC now has explicit local metric, connection, curvature, lapse and force kinematics; the decisive remaining problem is dynamical source closure.
