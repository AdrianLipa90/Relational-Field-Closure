# RF-E0 — Aharonov–Bohm Maxwell Stress-Energy to Einstein–Bianchi Bridge

Status: `EXACT_BIANCHI_COMPATIBILITY / MAXWELL_STRESS_ENERGY_CONDITIONAL_PASS / DYNAMIC_LAMBDA_TRANSFER_TYPED / EINSTEIN_COUPLING_OPEN`

## 1. Purpose

RF-M1 supplies a physically typed electromagnetic curvature from the Aharonov–Bohm phase connection,

\[
\mathfrak a_{AB}=\frac{q}{\hbar}A,
\qquad
F=dA=\frac{\hbar}{q}d\mathfrak a_{AB}.
\]

RFC already carries a Lorentzian metric candidate, a torsion-free metric connection on its admitted local geometric sector, and curvature tensors. RF-E0 asks whether the electromagnetic field produced by RF-M1 is compatible with the Einstein–Bianchi source architecture.

## 2. Geometric side

For the admitted Levi-Civita sector define

\[
G_{\mu\nu}:=R_{\mu\nu}-\frac12Rg_{\mu\nu}.
\]

The contracted Bianchi identity gives

\[
\boxed{\nabla^\mu G_{\mu\nu}=0.}
\]

Metric compatibility gives

\[
\boxed{\nabla^\mu g_{\mu\nu}=0.}
\]

These are geometric identities once the Levi-Civita connection is admitted.

## 3. Electromagnetic source tensor

Conditional on the RF-M1 Maxwell action,

\[
S_{EM}=\int d^4x\sqrt{-g}
\left[-\frac{1}{4\mu_*}F_{\alpha\beta}F^{\alpha\beta}-J^\alpha A_\alpha\right],
\]

metric variation gives

\[
\boxed{
T^{EM}_{\mu\nu}
=\frac{1}{\mu_*}
\left(
F_{\mu\alpha}F_\nu{}^\alpha
-\frac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}
\right).
}
\]

The sourced Maxwell equation is

\[
\nabla_\mu F^{\mu\nu}=\mu_*J^\nu.
\]

Its stress-energy exchange law is

\[
\boxed{
\nabla^\mu T^{EM}_{\mu\nu}
=-F_{\nu\lambda}J^\lambda.
}
\]

For a charged matter sector with the complementary Lorentz-force exchange

\[
\boxed{
\nabla^\mu T^{matter}_{\mu\nu}
=+F_{\nu\lambda}J^\lambda,
}
\]

one obtains

\[
\boxed{
\nabla^\mu
\left(T^{EM}_{\mu\nu}+T^{matter}_{\mu\nu}\right)=0.
}
\]

Thus the AB-derived Maxwell sector supplies a Bianchi-compatible conserved source pair after the matter-current action is admitted.

## 4. Einstein coupling coordinate

Write the Einstein source equation with an explicit coupling coordinate

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\kappa_E T^{total}_{\mu\nu}.
}
\]

For constant `Lambda`, Bianchi compatibility requires

\[
\boxed{\nabla^\mu T^{total}_{\mu\nu}=0.}
\]

The standard physical normalization is recovered when the RFC Newton/source gate fixes

\[
\boxed{\kappa_E=\frac{8\pi G}{c^4}.}
\]

RF-E0 keeps `kappa_E` explicit until RF-N1C fixes the Newton-limit coupling.

## 5. Dynamic Lambda0 transfer identity

For the RFC dynamic scalar target

\[
G_{\mu\nu}+\Lambda_0(x)g_{\mu\nu}
=\kappa_E T^{total}_{\mu\nu},
\]

Bianchi plus metric compatibility gives exactly

\[
\boxed{
\kappa_E\nabla^\mu T^{total}_{\mu\nu}
=\nabla_\nu\Lambda_0.
}
\]

Equivalently define the bookkeeping tensor

\[
\boxed{
T^{\Lambda}_{\mu\nu}:=-\frac{\Lambda_0}{\kappa_E}g_{\mu\nu}.
}
\]

Then

\[
\nabla^\mu T^{\Lambda}_{\mu\nu}
=-\frac{1}{\kappa_E}\nabla_\nu\Lambda_0,
\]

and the combined conservation statement is

\[
\boxed{
\nabla^\mu
\left(T^{total}_{\mu\nu}+T^{\Lambda}_{\mu\nu}\right)=0.
}
\]

This matches the existing RF-L1 transfer constraint and makes the dynamic-vacuum exchange coordinate explicit.

## 6. AB → Maxwell → Einstein chain

The admitted chain is now

\[
\boxed{
\phi_{AB}[C]
\to
\mathfrak a_{AB}=\frac{q}{\hbar}A
\to
F=dA
\to
T^{EM}_{\mu\nu}
\to
T^{EM}_{\mu\nu}+T^{matter}_{\mu\nu}
\to
\text{Einstein--Bianchi source gate}.
}
\]

The first curvature/homogeneous-Maxwell part is exact at RF-M1. The stress-energy part is conditional on the admitted Maxwell/matter action. The Einstein coupling normalization remains a downstream RF-N1C result.

## 7. Promotion contract

Exact at RF-E0 after admitting the RFC Levi-Civita geometric sector:

- contracted Bianchi identity;
- metric compatibility;
- dynamic-`Lambda0` transfer identity;
- algebraic conservation of EM+matter when their Lorentz-force exchange terms are opposite.

Conditional on RF-M1 sourced action and charged-matter action:

- `T_EM` from metric variation;
- Maxwell stress-energy exchange;
- conserved EM+matter source tensor.

Open downstream coordinates:

- RFC/IDT current binding `J_Q^mu <-> J_EM^mu`;
- vacuum normalization `mu_*`;
- Newton/source determination of `G` and therefore `kappa_E`;
- complete admitted matter stress-energy;
- action-level realization of the dynamic `Lambda0` sector;
- full Einstein field-equation promotion and unified-limit audit.
