# RFG4C — alpha_c Spectral Identifiability Estimator

Status: `CLEAN_ROOM_ESTIMATOR_EXACT_CONDITIONAL / SPECTRAL_INPUT_OPEN / YM_BINDING_CANDIDATE`

## 1. Purpose

RFG4C removes the historical optimizer from the minimum mathematical path required to estimate the CIEL coordinate `alpha_c` from spectral data.

The published kernel relation is

\[
\boxed{
\omega_n
=
n\alpha_c\frac{c_{\rm eff}}{\hbar_{\rm eff}}
}
\]

for integer spectral label `n`.

For known positive `c_eff` and `hbar_eff`, each nonzero labelled peak gives

\[
\boxed{
\alpha_c
=
\frac{\hbar_{\rm eff}}{c_{\rm eff}}
\frac{\omega_n}{n}.
}
\]

Thus `alpha_c` is identifiable directly from peak spacing once the effective-unit coordinates and integer peak assignment are supplied.

## 2. Multi-peak least-squares estimator

Let the observed peak set be

\[
\{(n_k,\omega_k,w_k)\}_{k=1}^{N},
\qquad n_k\in\mathbb Z_{>0},
\qquad w_k>0.
\]

Write

\[
\omega_k=s\,n_k+\varepsilon_k,
\qquad
s:=\alpha_c\frac{c_{\rm eff}}{\hbar_{\rm eff}}.
\]

The weighted least-squares estimator through the origin is

\[
\boxed{
\hat s
=
\frac{\sum_k w_k n_k\omega_k}
{\sum_k w_k n_k^2}
}
\]

and therefore

\[
\boxed{
\hat\alpha_c
=
\frac{\hbar_{\rm eff}}{c_{\rm eff}}
\frac{\sum_k w_k n_k\omega_k}
{\sum_k w_k n_k^2}.
}
\]

For exact data obeying the kernel relation, this reconstructs `alpha_c` exactly for every positive weight assignment.

## 3. Scale-free ratio audit

Before any absolute effective-unit normalization is used, the harmonic structure can be audited through

\[
\boxed{
\frac{\omega_m}{\omega_n}
=
\frac{m}{n}.
}
\]

Define

\[
\boxed{
\Delta_{harm}
=
\max_{m,n}
\left|
\frac{n\omega_m}{m\omega_n}-1
\right|.
}
\]

The exact spectral law requires

\[
\Delta_{harm}=0.
\]

This gate tests integer harmonic consistency independently of `alpha_c`, `c_eff` and `hbar_eff`.

## 4. Peakwise consistency defect

For every labelled peak define

\[
\hat\alpha_{c,k}
=
\frac{\hbar_{\rm eff}}{c_{\rm eff}}
\frac{\omega_k}{n_k}.
\]

Using the weighted estimator `hat alpha_c`, define

\[
\boxed{
\Delta_{peak}
=
\max_k
\frac{|\hat\alpha_{c,k}-\hat\alpha_c|}
{|\hat\alpha_c|}.
}
\]

Exact harmonic data give

\[
\Delta_{peak}=0.
\]

Nonzero values quantify departures from one common spectral-spacing coordinate.

## 5. Historical and analytic coordinates as blinded checks

The historical kernel paper reports

\[
\alpha_c^{hist}=0.474812\pm0.000007.
\]

RFG4 independently gives the legacy-normalization analytic candidate

\[
\alpha_c^{legacy\,rec}=0.474812026194\ldots
\]

and the canonicalized candidate

\[
\alpha_c^{canonical\,cand}
=0.474839619052\ldots
\]

A future clean-room spectral extraction must freeze the spectral preprocessing, peak assignment and effective-unit normalization before comparison with these coordinates.

The comparison order is therefore

```text
raw/declared spectrum
 -> frozen peak detector
 -> integer labels
 -> harmonic-defect audit
 -> alpha_c estimator
 -> estimator uncertainty
 -> only then compare to historical / analytic coordinates
```

## 6. Statistical uncertainty

For independent peak-frequency uncertainties `sigma_omega,k`, choose inverse-variance weights

\[
w_k=\sigma_{\omega,k}^{-2}.
\]

For the zero-intercept linear model, the slope variance is

\[
\boxed{
\operatorname{Var}(\hat s)
=
\frac{1}{\sum_k w_k n_k^2}
}
\]

when the supplied frequency variances are the full independent measurement variances.

Hence

\[
\boxed{
\sigma_{\hat\alpha_c}
=
\frac{\hbar_{\rm eff}}{c_{\rm eff}}
\frac{1}{\sqrt{\sum_k w_k n_k^2}}.
}
\]

Correlated spectral errors require the covariance-matrix generalization before promotion.

## 7. Downstream Yang–Mills coordinate

RFG3 uses the archived candidate binding

\[
\alpha_c\stackrel{?}{=}\frac{1}{g_0^2}.
\]

If that independent binding passes, then a spectral estimate produces

\[
\boxed{
\hat g_0=\hat\alpha_c^{-1/2}
}
\]

and for SU(3)

\[
\boxed{
\hat\beta_W=6\hat\alpha_c.
}
\]

RFG4C therefore separates two questions:

1. `alpha_c` spectral identifiability — exact conditional theorem;
2. `alpha_c -> 1/g_0^2` physical Yang–Mills binding — GREMLIN candidate gate.

## 8. Promotion contract

`SPECTRAL_ALPHA_C_PASS` requires:

- declared `c_eff` and `hbar_eff` with units/provenance;
- deterministic or frozen spectral preprocessing;
- deterministic peak detector;
- explicit positive integer labels;
- harmonic defect below declared tolerance;
- peakwise common-alpha defect below declared tolerance;
- estimator and uncertainty computed before target comparison;
- content-addressed input spectrum and estimator receipt.

The physical Wilson/Yang–Mills promotion remains downstream of its own independent binding gate.
