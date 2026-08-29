# RF-E18 — ADM Shift / Physical Velocity Gauge Firewall

Status: `EXACT_KINEMATIC_FIREWALL / MATERIAL_ADAPTED_BINDING_CONDITIONAL / PHYSICAL_DIRECTIONAL_CARRIER_DEFINED`

## 1. Purpose

RF-E14 derives two directional relative-information branches from the local ADM shift carrier. RF-E17 routes the resulting dimensionless clock-information potential through an admitted RFC scalar action, while leaving the physical `shift -> velocity` binding open.

RF-E18 closes the kinematic part of that question.

The ADM convention is

\[
\boxed{
 ds^2=-N^2(dx^0)^2+h_{ij}(dx^i+b^i dx^0)(dx^j+b^j dx^0),
 \qquad N>0.
}
\]

For a worldline written with coordinate spatial rate

\[
 w^i:=\frac{dx^i}{dx^0},
\]

the normal-observer relative spatial velocity coordinate is

\[
\boxed{
V^i:=\frac{w^i+b^i}{N}.
}
\]

Its physical squared speed is

\[
\boxed{
\beta_{\rm phys}^2:=h_{ij}V^iV^j,
}
\]

with `x^0=ct`, so `beta_phys=v_phys/c` in an orthonormal local frame.

## 2. Time-dependent spatial relabeling

Consider a local time-dependent spatial translation

\[
 x'^i=x^i+\xi^i(x^0).
\]

Then

\[
 dx^i=dx'^i-\dot\xi^i dx^0,
\]

and the ADM one-form block becomes

\[
 dx^i+b^i dx^0
=dx'^i+(b^i-\dot\xi^i)dx^0.
\]

Therefore

\[
\boxed{b'^i=b^i-\dot\xi^i,}
\qquad
\boxed{w'^i=w^i+\dot\xi^i.}
\]

Hence

\[
\boxed{
w'^i+b'^i=w^i+b^i,
}
\]

and therefore

\[
\boxed{V'^i=V^i}
\]

for this local translation chart change. Under a general admitted spatial diffeomorphism, `V^i` transforms as a spatial vector and `h_ij V^i V^j` is the scalar speed.

Thus `b^i` alone is not a physical velocity observable.

## 3. Null-characteristic control

In a local orthonormal `1+1` patch with `N>0`, `h=1`,

\[
 ds^2=-N^2(dx^0)^2+(dx+b\,dx^0)^2.
\]

Null propagation satisfies

\[
\boxed{
w_\pm=-b\pm N.
}
\]

The corresponding normal-relative velocities are

\[
\boxed{
V_\pm=\frac{w_\pm+b}{N}=\pm1.
}
\]

Therefore the asymmetric coordinate rates `-b+N` and `-b-N` do not imply an asymmetric locally measured speed of light. Their asymmetry is a shift-chart effect.

## 4. Consequence for RF-E14

RF-E14 uses the local coordinate traversal factors

\[
 x_s^{(b)}=\frac{1}{1-sb},
 \qquad s=\pm1,
\]

in the `N=1`, `h=1` local chart.

Because `b` changes under time-dependent spatial relabeling, the quantity

\[
\Phi\!\left(x_s^{(b)}\right),
\qquad
\Phi(x)=x-1-\ln x,
\]

is not by itself a generally physical scalar observable.

This is the RF-E18 firewall:

```text
ADM shift b alone
 -> coordinate directional rate
 -> RF-E14 chart-level Phi branch
 -> physical energy claim BLOCKED
```

until an admitted physical congruence/source binding fixes the relative velocity.

## 5. Material-adapted realization

Let a material or particle congruence be represented by a worldline field with coordinate rate `w^i`.

Its physical normal-relative speed is always determined by

\[
V^i=\frac{w^i+b^i}{N}.
\]

In a material-adapted chart in which that congruence is spatially pinned,

\[
\boxed{w^i=0,}
\]

one has

\[
\boxed{V^i=\frac{b^i}{N}.}
\]

For a local orthonormal aligned `1+1` patch with `N=1`,

\[
\boxed{b=s\beta_{\rm phys}}
\]

for the oriented material velocity.

This is a conditional source/gauge realization, not a coordinate-free identity between ADM shift and particle velocity.

## 6. Gauge-invariant directional carrier

Once an independently defined local physical speed

\[
0\le\beta_{\rm phys}<1
\]

and an orientation `s=+1` or `s=-1` are supplied, define

\[
\boxed{
x_s^{\rm phys}:=\frac{1}{1-s\beta_{\rm phys}}.}
\]

This carrier depends on the locally measured normal-relative speed rather than on the coordinate shift alone.

The IDT/RFC clock-information potential then gives

\[
\boxed{
\Phi_s^{\rm phys}
:=\Phi(x_s^{\rm phys})
=\ln(1-s\beta_{\rm phys})
+\frac{s\beta_{\rm phys}}{1-s\beta_{\rm phys}}.
}
\]

The opposite orientation obeys

\[
\boxed{
\Phi_{-s}^{\rm phys}(\beta)
=\Phi_s^{\rm phys}(-\beta).
}
\]

Its small-speed expansion is

\[
\boxed{
\Phi_s^{\rm phys}
=\frac12\beta^2
+\frac23s\beta^3
+\frac34\beta^4
+O(\beta^5).
}
\]

The universal quadratic coefficient is therefore `1/2`; the odd terms remain an orientation-sensitive physical candidate only after the material-congruence and action/observable bindings pass.

## 7. Physical promotion chain

RF-E18 replaces the shortcut `b=v/c` by the typed chain

```text
ADM (N,b,h)
 + worldline coordinate rate w
 -> V^i=(w^i+b^i)/N
 -> beta_phys^2=h_ij V^i V^j
 -> oriented beta_phys
 -> x_s^phys=1/(1-s beta_phys)
 -> Phi_s^phys
 -> RF-E17 scalar-action route
 -> energy observable / scale gates
```

A material-adapted chart may realize the special case `w=0`, `N=1`, `h=1`, so that the numerical shift coordinate equals the oriented physical speed ratio. The equality is then source- and gauge-typed.

## 8. Evidence boundary and next gate

RF-E18 establishes:

- exact ADM shift transformation under local time-dependent spatial translations;
- exact invariance of `w+b` and normal-relative velocity;
- exact null-speed control `V_null=±1` in a local orthonormal frame;
- exact material-adapted relation `V=b/N` when `w=0`;
- a gauge-invariant directional carrier built from independently measured `beta_phys`;
- parity and low-speed expansion of the physical directional information potential.

The next gates are:

1. source-bind the relevant material/particle congruence to an RFC matter sector;
2. determine whether the RF-E17 scalar-action contribution is the admitted translational kinetic observable;
3. promote the scale coordinate `E_star` through independently fixed coupling/cell geometry;
4. compare the resulting physical dispersion/energy law with standard relativistic observables.

The author/repository/formalism/code may suggest an oriented relative-information contribution to kinetic dynamics, yet does not state that contribution as an established translational energy law until these source, observable and scale gates pass.
