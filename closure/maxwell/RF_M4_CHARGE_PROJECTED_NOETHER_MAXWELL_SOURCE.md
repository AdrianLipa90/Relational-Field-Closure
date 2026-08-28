# RF-M4 — Charge-Projected Noether Current as the Maxwell Source

Status: `EXACT_VARIATION_LEVEL_SOURCE_FACTORIZATION_CONDITIONAL_ON_FIELD_MULTIPLET / EXACT_SINGLE_CHARGE_REDUCTION / RFC_MEASURED_CURRENT_PROMOTION_OPEN`

RF-M4 follows RF-M1 through RF-M3 and closes the variation-level interface between the flavour/phase matter current and the electromagnetic Maxwell source.

## 1. Charged flavour multiplet

Let

\[
\Psi(x)\in\mathbb C^N
\]

be a local complex flavour multiplet with Hermitian electric-charge operator `Q`. Use the synchronized RFC/IDT convention

\[
\boxed{
\Psi'=e^{iQ\Lambda/\hbar}\Psi,
\qquad
A'=A-d\Lambda.
}
\]

Define

\[
\boxed{
\mathcal D_\mu\Psi
=\nabla_\mu\Psi+\frac{i}{\hbar}A_\mu Q\Psi.
}
\]

## 2. Matter action and charge compatibility

Admit

\[
\boxed{
\mathcal L_m
=(\mathcal D_\mu\Psi)^\dagger\mathcal D^\mu\Psi
-\Psi^\dagger\mathcal M^2\Psi
-V_{inv}(\Psi),
}
\]

with gauge-invariant `V_inv`. Gauge compatibility of the flavour/mass operator requires

\[
\boxed{[\mathcal M^2,Q]=0.}
\]

This is the local-field counterpart of the RF-M3 condition `[H_f,Q]=0`.

## 3. Charge-projected Noether current

Define

\[
\boxed{
\mathcal J_Q^\mu
=i\left[
(\mathcal D^\mu\Psi)^\dagger Q\Psi
-\Psi^\dagger Q\mathcal D^\mu\Psi
\right].
}
\]

For a single component with `Q=q`,

\[
\boxed{\mathcal J_Q^\mu=qJ_\vartheta^\mu,}
\]

where `J_theta` is the gauge-covariant phase current used by IDT 01AC.

## 4. Variation with respect to the AB potential

Since

\[
\delta_A(\mathcal D_\mu\Psi)
=\frac{i}{\hbar}Q\Psi\,\delta A_\mu,
\]

and

\[
\delta_A(\mathcal D_\mu\Psi)^\dagger
=-\frac{i}{\hbar}\Psi^\dagger Q\,\delta A_\mu,
\]

the matter variation is

\[
\boxed{
\delta_A\mathcal L_m
=\frac{1}{\hbar}\mathcal J_Q^\mu\delta A_\mu.
}
\]

Therefore

\[
\boxed{
\frac{1}{\sqrt{-g}}\frac{\delta S_m}{\delta A_\mu}
=\frac{1}{\hbar}\mathcal J_Q^\mu.
}
\]

RF-M1 defines the source term with

\[
S_{EM}\supset-\int d^4x\sqrt{-g}\,J_{EM}^\mu A_\mu.
\]

Thus the matter contribution to the Maxwell source is

\[
\boxed{
J_{EM}^\mu=-\frac{1}{\hbar}\mathcal J_Q^\mu.
}
\]

For one charge eigenvalue,

\[
\boxed{
J_{EM}^\mu=-\frac q\hbar J_\vartheta^\mu.
}
\]

The source conversion uses the same `q/hbar` already fixed by the Aharonov–Bohm connection and introduces no additional current scaling parameter.

## 5. Current conservation and sourced Maxwell compatibility

On the gauge-invariant matter equations, with

\[
[\mathcal M^2,Q]=0,
\]

Noether conservation gives

\[
\boxed{\nabla_\mu\mathcal J_Q^\mu=0.}
\]

Hence

\[
\boxed{\nabla_\mu J_{EM}^\mu=0.}
\]

This is the compatibility condition for

\[
\boxed{
\nabla_\mu F^{\mu\nu}=\mu_*J_{EM}^\nu.
}
\]

## 6. Neutrino null-control

For

\[
Q_\nu=0,
\]

one gets identically

\[
\boxed{\mathcal J_{Q_\nu}^\mu=0,}
\qquad
\boxed{J_{EM}^\mu[\nu]=0.}
\]

The internal neutrino-flavour evolution described by RF-M2/RF-M3 may remain nontrivial while the direct electromagnetic source current is exactly zero.

## 7. Equal-charge flavour sector

For

\[
Q=qI_N,
\]

\[
\mathcal J_Q^\mu=qJ_{flavour-sum}^\mu.
\]

Charge-compatible flavour dynamics may redistribute the internal flavour amplitudes while preserving the total electric `U(1)` source current.

## 8. Relation to the RFC conserved carrier

RF-M4 replaces the earlier untyped current-promotion target by a charge-projected target. The remaining measured closure gate is

\[
\boxed{
J_Q^{RFC\,\mu}
\stackrel{?}{=}J_{EM}^\mu
=-\frac{1}{\hbar}\mathcal J_Q^\mu.
}
\]

For a single charged phase field this becomes

\[
\boxed{
J_Q^{RFC\,\mu}
\stackrel{?}{=}
-\frac q\hbar J_\vartheta^\mu.
}
\]

The proportionality factor is inherited from AB normalization rather than fitted at the RFC current gate.

## 9. Executable defects

The reference interface should audit

\[
\Delta_{MQ}=\|[\mathcal M^2,Q]\|,
\]

\[
\Delta_{var}
=\left\|
\frac{\delta\mathcal L_m}{\delta A_\mu}
-\frac{1}{\hbar}\mathcal J_Q^\mu
\right\|,
\]

\[
\Delta_{single}=\|\mathcal J_Q^\mu-qJ_\vartheta^\mu\|,
\]

and

\[
\Delta_{source}=\|J_{EM}^\mu+\mathcal J_Q^\mu/\hbar\|.
\]

A mass/flavour operator mixing different electric-charge eigenspaces must fail the charge-compatibility gate.
