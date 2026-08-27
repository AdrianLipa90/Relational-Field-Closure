# RF-N0 — Relational Lapse and Clock-Dynamics Bridge

Status: `EXACT_IDT_LAPSE_IMPORT / EXACT_STATIC_GEODESIC_KINEMATICS / PHYSICAL_PROPER_TIME_BINDING_CANDIDATE / SOURCE_DYNAMICS_OPEN`

Pinned stacked input:

- IDT `feat/relational-lapse-interface-v0.1`, commit `e3cbcd39f2cc9ea8f3e08f613aa5124de1c4dac4`;
- RFC RF-02H local hexahedral rank-three spatial metric;
- RFC RF-02I coframe connection and constant-lapse negative theorem.

## 1. Native IDT lapse carrier

IDT supplies two positive elapsed one-forms on a common relational patch,

\[
d\tau_x=\phi_xd\lambda,
\qquad
d\tau_{\rm ref}=\phi_{\rm ref}d\lambda,
\]

and the exact reparameterization-invariant clock ratio

\[
\boxed{
N_R
:=\frac{d\tau_x}{d\tau_{\rm ref}}
=\frac{\phi_x}{\phi_{\rm ref}}>0.
}
\]

The ratio is dimensionless, composes multiplicatively under reference changes and survives every admitted common increasing relabeling of `lambda`.

RFC therefore does not need to invent a lapse scalar. It receives one as an upstream relational clock ratio.

## 2. Temporal coframe binding candidate

After calibrating the reference elapsed clock to a physical coordinate `t`, define

\[
\boxed{
\Theta_R:=N_Rc\,dt.
}
\]

The corresponding zero-shift local spacetime metric candidate is

\[
\boxed{
g_R
=-\Theta_R\otimes\Theta_R+h_\perp
=-N_R^2c^2dt^2+h_\perp.
}
\]

Because `N_R>0` and RF-02H supplies positive rank-three `h_perp`, the metric has the same Lorentzian inertia `(-,+,+,+)` as RF-G0.

The new content of RF-N0 is not the signature. It is the nonuniform magnitude of the temporal coframe.

## 3. Exact static geodesic acceleration

On a static zero-shift patch with physical spatial metric `h_ij(X)`, let

\[
ds^2=-N_R(X)^2c^2dt^2+h_{ij}(X)dX^idX^j.
\]

Then

\[
\boxed{
\Gamma^i{}_{tt}
=c^2N_Rh^{ij}\partial_jN_R.
}
\]

For a trajectory whose spatial coordinate velocity is small compared with `c`, the leading acceleration is

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_Rh^{ij}\partial_jN_R
+O(v^2,\,v\partial h,\,\partial_t g).
}
\]

Equivalently,

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_R^2h^{ij}\partial_j\ln N_R
+\cdots.
}
\]

This is an exact kinematic consequence of the lapse-bound metric before any Newtonian potential is introduced.

## 4. Relational potential variable

Define the lapse potential variable

\[
\boxed{
\Phi_R:=c^2\ln N_R.
}
\]

Then exactly

\[
\boxed{
\partial_i\Phi_R=c^2\partial_i\ln N_R
}
\]

and the static slow-motion acceleration becomes

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-N_R^2h^{ij}\partial_j\Phi_R+\cdots.
}
\]

Near the reference clock, write

\[
N_R=1+\epsilon_N,
\qquad |\epsilon_N|\ll1.
\]

Then

\[
\Phi_R=c^2\epsilon_N+O(c^2\epsilon_N^2)
\]

and, in a local physical frame with `h_ij=delta_ij+` higher-order corrections,

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-\partial^i\Phi_R
+\text{higher-order terms}.
}
\]

This reaches the Newtonian force-law *form* without inserting a Newton potential as a primitive: `Phi_R` is defined from the independently derived IDT clock ratio.

The source equation determining `Phi_R` remains open.

## 5. Exact kinetic decomposition of the lapse

IDT 05C gives, for common local/reference activity normalization,

\[
\boxed{
N_R
=\frac{M_x\cosh(A_x/2)}
{M_{\rm ref}\cosh(A_{\rm ref}/2)}.
}
\]

For a fixed reference sector,

\[
\boxed{
\nabla_i\ln N_R
=\nabla_i\ln M
+\frac12\tanh(A/2)\nabla_iA.
}
\]

Hence the leading static acceleration has the exact relational decomposition

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_R^2h^{ij}
\left[
\partial_j\ln M
+\frac12\tanh(A/2)\partial_jA
\right]
+\cdots.
}
\]

The mobility is

\[
M
=\frac{\sqrt{\rho_R(a)\rho_R(b)}}{\eta_{ab}},
\qquad
\eta_{ab}:=\frac{\eta_R(a)+\eta_R(b)}2,
\]

so

\[
\boxed{
\partial_j\ln M
=\frac12\partial_j\ln\rho_R(a)
+\frac12\partial_j\ln\rho_R(b)
-\partial_j\ln\eta_{ab}.
}
\]

Therefore the lapse-gradient acceleration carrier decomposes into the upstream relational density, viscosity and directional-drive gradients:

\[
\boxed{
\frac{d^2X^i}{dt^2}
=-c^2N_R^2h^{ij}
\left[
\frac12\partial_j\ln\rho_R(a)
+\frac12\partial_j\ln\rho_R(b)
-\partial_j\ln\eta_{ab}
+\frac12\tanh(A/2)\partial_jA
\right]
+\cdots.
}
\]

No inverse-square force law or Poisson equation is assumed in obtaining this expression.

## 6. Relation to phase-clock spatial geometry

RF-02H/RF-02I give the local spatial coframe scale

\[
a_H=\frac{c}{\sqrt6|\omega|}.
\]

RF-N0 gives the temporal scale

\[
\Theta_R=N_Rc\,dt.
\]

The local tetrad therefore becomes

\[
\boxed{
\mathcal E^0=N_Rc\,dt,
\qquad
\mathcal E^i=\frac{c}{\sqrt6|\omega|}\vartheta^i.
}
\]

This is the first RFC tetrad in which both temporal and spatial leg magnitudes are supplied by upstream temporal dynamics:

- temporal leg magnitude from the ratio of IDT elapsed clocks;
- spatial leg magnitude from IDT phase rate combined with the hexahedral FS metric.

The two scalars `N_R` and `omega` are kept distinct. A dynamical relation between them requires its own derivation.

## 7. Static orthonormal-frame acceleration

Let `e_hat_i` be the orthonormal spatial frame dual to `E^i`. The local physical acceleration components are

\[
\boxed{
a_{\hat i}
=-c^2N_R\,e_{\hat i}(N_R)
=-c^2N_R^2\,e_{\hat i}(\ln N_R).
}
\]

Because `e_hat_i` has inverse-length type, the right-hand side has type `L T^-2` exactly.

This frame form avoids coordinate-unit ambiguity when the hexahedral reference coordinates are dimensionless.

## 8. What remains before Newton source closure

RF-N0 separates two logically different parts of Newtonian gravity:

### Kinematics

The relation

\[
\boxed{a^i\simeq-\partial^i\Phi_R}
\]

is now obtained from the derived relational lapse after physical clock binding.

### Dynamics/source law

RFC still has to derive an equation determining `N_R` or `Phi_R`. The Newton/Poisson target

\[
\nabla^2\Phi=4\pi G\rho
\]

remains outside the premise set and is reserved for RF-N1 validation.

Candidate source derivations may use an action for the temporal/lapse sector, Einstein--Bianchi closure, or an independently derived relational conservation equation. They may not insert the Poisson equation and then count its consequences as a derivation.

## 9. Promotion contract

RF-N0 records:

```text
IDT_relational_lapse_ratio        = EXACT
reparameterization_invariance     = EXACT
lapse_temporal_coframe_binding    = CANDIDATE pending physical clock calibration
static_geodesic_acceleration      = EXACT conditional on coframe binding
relational_potential_Phi_R        = DEFINITION from N_R
weak_force_law_form               = CONDITIONAL LIMIT PASS CANDIDATE
Poisson_source_equation           = OPEN
Newton_constant_normalization     = OPEN
```

The next gate is RF-N1: derive the source equation and normalization for the relational lapse potential, then test whether its weak-field limit equals the Newton/Poisson law without target leakage.
