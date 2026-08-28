# RF-M4 — Charge-Projected Noether Current as the Maxwell Source

Status: `EXACT_VARIATION_LEVEL_SOURCE_FACTORIZATION_CONDITIONAL_ON_FIELD_MULTIPLET / EXACT_SINGLE_CHARGE_REDUCTION / RF_E6_SIGNATURE_ALIGNMENT_PASS / RFC_MEASURED_CURRENT_PROMOTION_TYPED`

RF-M4 closes the variation-level interface between the charged flavour/phase matter current and the electromagnetic Maxwell source. RF-E6 fixes the action sign to the canonical RFC metric signature `(-,+,+,+)` and thereby fixes the current sign used below.

## 1. Charged flavour multiplet

Let

\[
\Psi(x)\in\mathbb C^N
\]

be a local complex flavour multiplet with Hermitian electric-charge operator `Q`. Use

\[
\boxed{
\Psi'=e^{iQ\Lambda/\hbar}\Psi,
\qquad
A'=A-d\Lambda,
}
\]

and

\[
\boxed{
\mathcal D_\mu\Psi
=\nabla_\mu\Psi+\frac{i}{\hbar}A_\mu Q\Psi.
}
\]

## 2. Lorentzian matter action and charge compatibility

With the canonical RFC signature `(-,+,+,+)`, use the energy-positive action density

\[
\boxed{
\mathcal L_m
=-(\mathcal D_\mu\Psi)^\dagger\mathcal D^\mu\Psi
-\Psi^\dagger\mathcal M^2\Psi
-V_{inv}(\Psi).
}
\]

Gauge compatibility requires

\[
\boxed{[\mathcal M^2,Q]=0.}
\]

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
\boxed{\mathcal J_Q^\mu=qJ_\vartheta^\mu.}
\]

## 4. Variation with respect to the AB potential

For the RF-E6-aligned matter action,

\[
\boxed{
\frac{1}{\sqrt{-g}}\frac{\delta S_m}{\delta A_\mu}
=-\frac{1}{\hbar}\mathcal J_Q^\mu.
}
\]

Combining this microscopic matter variation with

\[
S_F=-\frac{1}{4\mu_*}\int d^4x\sqrt{-g}\,F_{\alpha\beta}F^{\alpha\beta}
\]

gives

\[
\boxed{
\nabla_\mu F^{\mu\nu}=\mu_*J_{EM}^\nu,
\qquad
J_{EM}^\nu=\frac{1}{\hbar}\mathcal J_Q^\nu.
}
\]

For one charge eigenvalue,

\[
\boxed{
J_{EM}^\mu=\frac q\hbar J_\vartheta^\mu.
}
\]

The same source equation is obtained in the effective external-current representation with source term `-J_EM^mu A_mu`; RF-E6 keeps the microscopic and external-current action ledgers separately typed.

## 5. Current conservation and sourced Maxwell compatibility

On the gauge-invariant matter equations, with

\[
[\mathcal M^2,Q]=0,
\]

Noether conservation gives

\[
\boxed{\nabla_\mu\mathcal J_Q^\mu=0,}
\qquad
\boxed{\nabla_\mu J_{EM}^\mu=0.}
\]

## 6. Neutral control

For

\[
Q_\nu=0,
\]

one gets

\[
\boxed{\mathcal J_{Q_\nu}^\mu=0,}
\qquad
\boxed{J_{EM}^\mu[\nu]=0.}
\]

The unweighted matter carrier and stress-energy remain separately typed by RF-N1B2O/RF-E6.

## 7. Equal-charge flavour sector

For

\[
Q=qI_N,
\]

\[
\mathcal J_Q^\mu=qJ_{flavour-sum}^\mu,
\qquad
J_{EM}^\mu=\frac q\hbar J_{flavour-sum}^\mu.
\]

## 8. Relation to the RFC conserved carrier

RF-N1B2P composes RF-M4 with the independently audited RFC carrier. On the RF-N1B2K zero-defect surface,

\[
\boxed{
J_{EM}^\mu
=\frac1\hbar\Pi_Q[J_{RFC}]^\mu.
}
\]

For a single charged phase field,

\[
\boxed{
J_{EM}^\mu
=\frac q\hbar J_{RFC,\vartheta}^\mu.
}
\]

The proportionality factor is inherited from the Aharonov–Bohm charge normalization.

## 9. Executable defects

Reference gates audit

\[
\Delta_{MQ}=\|[\mathcal M^2,Q]\|,
\]

\[
\Delta_{var}
=\left\|
\frac{\delta\mathcal L_m}{\delta A_\mu}
+\frac{1}{\hbar}\mathcal J_Q^\mu
\right\|,
\]

\[
\Delta_{single}=\|\mathcal J_Q^\mu-qJ_\vartheta^\mu\|,
\]

and

\[
\Delta_{source}=\|J_{EM}^\mu-\mathcal J_Q^\mu/\hbar\|.
\]

RF-E6 additionally audits energy positivity, source-ledger uniqueness, EM/matter stress-energy exchange and `mu_*` unit normalization.
