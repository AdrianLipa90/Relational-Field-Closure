# RF-S20 — Noether-Profile Source Reconstruction

Status: `EXACT_PROFILE_TO_OCCUPATION_RECONSTRUCTION / Q0_FREE_LOCAL_SOURCE_MAP / CURRENT_SCALE_INVARIANT`

Canonical ID: `RF-S20`. Historical pre-canonical label: `RF-S18` (profile branch).

RF-S20 branches from exact-green RF-S17. RF-N1B2K supplies a normalized conserved-current profile on a common slice and measure, RF-S16 proves equality of the conserved-current and occupation profiles on the admitted local binding surface, and RF-S17 proves that the source density is independent of the arbitrary positive carrier-unit normalization `q0`.

RF-S20 reconstructs the local orbital occupation and the relational generator source directly from the Noether-current profile plus one independently supplied total occupation.

## 1. Noether-current profile

For positive finite-cell volumes `V_a` and nonnegative local Noether densities `j_theta,a`, define

\[
\boxed{
Q_\vartheta=\sum_a V_a j_{\vartheta,a}>0
}
\]

and

\[
\boxed{
p_{\vartheta,a}=\frac{V_a j_{\vartheta,a}}{Q_\vartheta}.}
\]

Then

\[
\boxed{\sum_a p_{\vartheta,a}=1.}
\]

RF-N1B2K already gives this normalized profile on the common current/measure ledger. RF-S16 gives, on the zero-defect occupation/current binding surface,

\[
\boxed{p_{\mathcal N,a}=p_{Q,a}=p_{\vartheta,a}.}
\]

## 2. Local occupation without q0

Let the independently supplied total orbital occupation be

\[
\boxed{\mathcal N_{tot}\ge0.}
\]

Then each cell occupation is reconstructed as

\[
\boxed{\mathcal N_a=\mathcal N_{tot}p_{\vartheta,a}.}
\]

Hence the local occupation density is

\[
\boxed{
n_a:=\frac{\mathcal N_a}{V_a}
=\mathcal N_{tot}\frac{j_{\vartheta,a}}{Q_\vartheta}.}
\]

No absolute carrier quantum `q0` appears. A global positive rescaling

\[
j_{\vartheta,a}\mapsto\lambda j_{\vartheta,a}
\]

rescales `Q_theta` by the same `lambda` and leaves every `n_a` invariant.

## 3. Relational generator source

RF-S13 defines the per-occupation energy

\[
\boxed{
\epsilon_a
=B_a\omega_a(\phi_a+\kappa),
\qquad
\kappa=\frac{\ln2}{24\pi}.
}
\]

The reconstructed local source energy density is therefore

\[
\boxed{
\rho_{G,a}
=n_a\epsilon_a
=\mathcal N_{tot}
\frac{j_{\vartheta,a}}{Q_\vartheta}
B_a\omega_a(\phi_a+\kappa).
}
\]

Equivalently,

\[
\boxed{
\rho_{G,a}
=\frac{\mathcal N_a}{V_a}
B_a\omega_a(\phi_a+\kappa),
}
\]

which is exactly the RF-S13 generator applied cellwise.

Thus a physically admitted RF-N1B2K Noether-current profile supplies the spatial source shape, while `N_tot` supplies the extensive amount.

## 4. Current-normalization invariance

Under any global positive current rescaling

\[
j_{\vartheta,a}'=\lambda j_{\vartheta,a},
\qquad \lambda>0,
\]

we have

\[
Q_\vartheta'=\lambda Q_\vartheta,
\qquad
p_{\vartheta,a}'=p_{\vartheta,a},
\]

so

\[
\boxed{\mathcal N_a'=\mathcal N_a,}
\]

\[
\boxed{n_a'=n_a,}
\]

and therefore

\[
\boxed{\rho_{G,a}'=\rho_{G,a}.}
\]

This realizes RF-S17 invariance locally, without selecting an absolute carrier-charge convention.

## 5. Integrated source energy

The cell-integrated source is

\[
E_{G,a}=V_a\rho_{G,a}=\mathcal N_a\epsilon_a.
\]

Hence

\[
\boxed{
E_G=\sum_a\mathcal N_a\epsilon_a.
}
\]

For one common per-occupation energy `epsilon`,

\[
\boxed{E_G=\mathcal N_{tot}\epsilon.}
\]

Thus the current profile controls where the source lives, while total occupation and per-occupation energy control how much source exists.

## 6. Newton/Einstein insertion

RF-S13 gives

\[
\mathcal S_{R,a}=\frac{\kappa_E}{2}\rho_{G,a}
\]

on the matter/Newton branch. Therefore RF-S20 yields

\[
\boxed{
\mathcal S_{R,a}
=\frac{\kappa_E\mathcal N_{tot}}{2}
\frac{j_{\vartheta,a}}{Q_\vartheta}
B_a\omega_a(\phi_a+\kappa).
}
\]

RF-S14 separately decides whether a source contribution remains in displayed matter or is movable into dynamic `Lambda0` from its equation-of-state receipt.

## 7. Exact separation of shape and amount

The source can now be written as

\[
\boxed{
\rho_{G,a}
=\underbrace{\frac{j_{\vartheta,a}}{Q_\vartheta}}_{\text{conserved-current shape per volume}}
\underbrace{\mathcal N_{tot}}_{\text{extensive occupation}}
\underbrace{B_a\omega_a(\phi_a+\kappa)}_{\text{per-occupation energy}}.
}
\]

This is the finite-cell version of the source-carrier factorization anticipated by RF-N1B2.

## 8. Advancement

```text
Noether finite-cell normalized profile                         PASS EXACT PARENT
p_theta = p_Q = p_N on zero-defect binding surface           PASS CONDITIONAL PARENTS
N_a = N_tot p_theta,a                                         PASS EXACT
n_a = N_tot j_theta,a / Q_theta                               PASS EXACT
local source rho_G,a from Noether profile                     PASS EXACT
source invariant under global current normalization           PASS EXACT
integrated source E_G=sum N_a epsilon_a                       PASS EXACT
uniform epsilon -> E_G=N_tot epsilon                          PASS EXACT
absolute q0 required for source reconstruction                 ELIMINATED
physical RF-N1B2K local-current receipt                        OPEN INPUT
physical total orbital occupation N_tot                        OPEN INPUT
physical carrier-energy branch                                OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/noether_profile_source_reconstruction.py`.
Reference tests: `tests/reference/test_rfs20_noether_profile_source_reconstruction.py`.
Validation receipt: `validation/RF_S20_NOETHER_PROFILE_SOURCE_RECONSTRUCTION_V0_1.json`.

Historical implementation head: `f52a90a8d6c24cb4dde0cde742f2c58c34a73193`; RFC reference suite #286 SUCCESS. Canonicalization changes gate identity and file paths only; equations and executable implementation are unchanged.
