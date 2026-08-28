# RF-E2 — Horizon Spin-1/2 Thermal Holonomy

Status: `EXACT_NEAR_HORIZON_SPIN_CONNECTION / EXACT_FRAME_WINDING / SPIN_HALF_ANTIPERIODICITY_PASS / HAWKING_MODE_BINDING_OPEN`

RF-E2 mirrors IDT 01AI on the Einstein-facing horizon boundary. It derives the Euclidean horizon phase one-form from the local Levi-Civita spin connection and evaluates the primitive winding in integer-spin and spin-`1/2` representations.

## 1. Near-horizon orthonormal frame

For

\[
 ds_E^2=d\rho^2+\rho^2d\Theta_H^2,
 \qquad
 \Theta_H=\kappa_H\tau_E,
\]

choose

\[
 e^{\hat\rho}=d\rho,
 \qquad
 e^{\hat\theta}=\rho d\Theta_H.
\]

The torsion-free Cartan equation yields, for the selected orientation,

\[
\boxed{
\omega^{\hat\theta}{}_{\hat\rho}
=d\Theta_H
=\kappa_Hd\tau_E.
}
\]

Thus the RF-E1 horizon holonomy one-form is the Euclidean polar-frame spin connection.

## 2. Primitive Euler rotation

With

\[
\beta_H=\frac{2\pi}{\kappa_H},
\]

one obtains

\[
\boxed{
\oint_{C_H}\omega^{\hat\theta}{}_{\hat\rho}=2\pi.
}
\]

The horizon thermal circle therefore carries one primitive frame winding.

## 3. Integer-spin and half-integer-spin representations

For integer spin weight,

\[
\boxed{e^{i2\pi m}=1.}
\]

For spin `1/2`,

\[
\boxed{
e^{i(2\pi)/2}=e^{i\pi}=-1.
}
\]

Hence the thermal-circle boundary conditions are

\[
\boxed{
\phi(\tau_E+\beta_H)=\phi(\tau_E),
}
\]

and

\[
\boxed{
\psi(\tau_E+\beta_H)=-\psi(\tau_E).
}
\]

## 4. Thermal frequencies

The primitive period therefore gives

\[
\omega_n^B=\frac{2\pi n}{\beta_H}=n\kappa_H,
\]

and

\[
\boxed{
\omega_n^F=\frac{(2n+1)\pi}{\beta_H}
=\left(n+\frac12\right)\kappa_H.
}
\]

RF-E2 thus gives an exact representation-theoretic bridge from Euclidean horizon winding to bosonic/fermionic thermal mode spacing.

## 5. Einstein-facing use

RF-E1 fixes the thermal period and Hawking temperature. RF-E2 fixes the spin structure around the same contractible Euclidean circle. A later black-hole matter/radiation calculation can use

\[
\boxed{
\kappa_H\beta_H=2\pi,
\qquad
W_{integer}=+1,
\qquad
W_{1/2}=-1
}
\]

as exact horizon boundary data.

## 6. Frontier

Exact:

- Levi-Civita spin connection of the Euclidean near-horizon polar frame;
- one primitive `2π` frame winding;
- periodic integer-spin sector;
- antiperiodic spin-`1/2` sector;
- Matsubara spacing derived from the same `beta_H`.

Open downstream binding:

- mode occupation and greybody transfer;
- interacting field content;
- evaporation/backreaction.
