# RFG4 — alpha_c Gauge-Coupling Genealogy Firewall

Status: `CHYBA / CANDIDATE_ONLY / HISTORICAL_NUMERICAL_EXTRACTION_SOURCE_RECOVERED / LEGACY_I0_OFFSET_ANALYTIC_MATCH / EXTRACTION_REPLAY_OPEN / ANALYTIC_SOURCE_OPEN / YM_PROMOTION_GATED`

RFG4 audits the archived Metatime/CIEL coordinate

\[
\alpha_c^{\rm archive}=0.474812
\]

before it enters RFG3 as a physical Yang–Mills normalization.

## 1. Historical constant lineage

The archived gluon implementation places

\[
\boxed{\alpha_c^{\rm archive}=0.474812},
\qquad
\boxed{I_0^{\rm legacy}=0.009}
\]

in the same constant block and then defines

\[
\boxed{g_{\rm archive}=\alpha_c^{-1/2}},
\qquad
\boxed{\alpha_s^{\rm archive}=\frac{g_{\rm archive}^2}{4\pi}}.
\]

The October 11, 2025 paper *Unified Reality Kernel: Mathematical Foundation of Consciousness-Matter Unification* (SSRN 5591492; ResearchGate DOI 10.13140/RG.2.2.17107.85287) supplies the recovered historical extraction provenance for the same coordinate. It records

\[
\boxed{\alpha_c=0.474812}
\]

as the Consciousness Quantum and gives an iterative constant-extraction scheme

\[
\boxed{
\alpha_c^{(n+1)}
=
\alpha_c^{(n)}
+\eta\frac{\partial\mathcal L}{\partial\alpha_c}
}
\]

with a coherence functional containing the quartic coordinate

\[
\mathcal L
=\int
\left[
|\nabla\Psi|^2
+\alpha_c|\Psi|^4
+\beta_s|S-\Psi|^2
-\gamma_t\tau|\Psi|^2
\right]d^4x.
\]

The same source gives the power-spectrum extraction

\[
P(\omega)
=
\left|
\int\Psi(x,t)e^{-i\omega t}dt
\right|^2
\]

and spectral spacing

\[
\omega_n
=n\alpha_c\frac{c_{\rm eff}}{\hbar_{\rm eff}},
\]

then reports the 1024-run result

\[
\boxed{\alpha_c=0.474812\pm0.000007}.
\]

This closes the historical *method/document* source for the archived decimal. The exact executable artifact reproducing those 1024 historical runs is typed `EXTRACTION_REPLAY_OPEN`.

The later `definitekernel.py` kernel freezes the extracted coordinate as both `CONSCIOUSNESS_QUANTUM` and `LIPA_CONSTANT`; the current CIEL repository exposes the same value through model-tuning aliases.

## 2. Canonical information normalization

The current canonical information constant is

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}
=0.009193150006360\ldots
\]

while the historical rounded coordinate is

\[
I_0^{\rm legacy}=0.009.
\]

Their displacement is

\[
\boxed{\Delta I=\kappa-I_0^{\rm legacy}}
=1.9315000636\times10^{-4}.
\]

The historical project geometry supplies

\[
\boxed{L_3=7}.
\]

## 3. Independent analytic reconstruction candidate

A frozen low-complexity GREMLIN search produced the canonical-base coordinate

\[
\boxed{
\alpha_c^{(\kappa,0)}
=
\ln\varphi-\kappa\ln2
}
\]

with

\[
\alpha_c^{(\kappa,0)}
=0.474839619052230\ldots
\]

The old rounded information normalization generates the candidate correction

\[
\boxed{
\delta_{I,L_3}
=
\frac{\kappa-I_0^{\rm legacy}}{L_3}
}
\]

and hence

\[
\boxed{
\alpha_c^{\rm legacy\,rec}
=
\ln\varphi
-\kappa\ln2
-\frac{\kappa-I_0^{\rm legacy}}{L_3}.
}
\]

For

\[
I_0^{\rm legacy}=0.009,
\qquad L_3=7,
\]

this evaluates to

\[
\boxed{
\alpha_c^{\rm legacy\,rec}
=0.47481202619417856\ldots
}
\]

and therefore

\[
\boxed{
\operatorname{round}(\alpha_c^{\rm legacy\,rec},6)
=0.474812.
}
\]

The absolute residual against the historical extracted mean is

\[
\boxed{\Delta_{\rm abs}=2.6194\times10^{-8}},
\]

and the relative residual is

\[
\boxed{\Delta_{\rm rel}=5.52\times10^{-8}}.
\]

The historical paper contains the numerical extraction route. The analytic expression above is therefore typed independently as

`GREMLIN_ANALYTIC_RECONSTRUCTION_CANDIDATE`.

Its six-decimal agreement with the historical simulation-extracted coordinate is recorded as

`LEGACY_I0_OFFSET_ANALYTIC_MATCH`.

## 4. Canonical renormalized coordinate

Under the exact normalization replacement

\[
I_0^{\rm legacy}\rightarrow\kappa,
\]

the correction coordinate closes:

\[
\frac{\kappa-I_0}{L_3}\rightarrow0.
\]

The corresponding canonicalized candidate is

\[
\boxed{
\alpha_c^{\rm canonical\,cand}
=
\ln\varphi-\kappa\ln2
=0.474839619052230\ldots
}
\]

with downstream candidate coordinates

\[
\boxed{
g_{\rm canonical\,cand}
=(\alpha_c^{\rm canonical\,cand})^{-1/2}
=1.4511975150\ldots}
\]

and, for the SU(3) Wilson convention,

\[
\boxed{
\beta_W^{\rm canonical\,cand}
=6\alpha_c^{\rm canonical\,cand}
=2.8490377143\ldots
}.
\]

The historical coordinates are

\[
g_{\rm archive}=1.4512397213\ldots,
\qquad
\beta_W^{\rm archive}=2.848872.
\]

The two coordinates are retained simultaneously for sensitivity tests until the canonical Yang–Mills binding is independently admitted.

## 5. Provenance split

RFG4 now has two explicitly separated provenance routes.

### Route H — historical numerical extraction

```text
Unified Reality Kernel (11 Oct 2025)
  -> iterative alpha_c update
  -> consciousness-field power spectrum
  -> 1024 reported simulation runs
  -> alpha_c = 0.474812 ± 0.000007
  -> definitekernel.py frozen coordinate
  -> archived gluon alpha_c
```

Status:

`HISTORICAL_NUMERICAL_EXTRACTION_SOURCE_RECOVERED / EXTRACTION_REPLAY_OPEN`.

### Route A — analytic information-normalization reconstruction

```text
phi
kappa = ln(2)/(24pi)
legacy I0 = 0.009
L3 = 7
  -> (kappa-I0)/L3
  -> ln(phi)-kappa ln(2)-(kappa-I0)/L3
  -> 0.474812026194...
  -> six-decimal match to historical extracted alpha_c
```

Status:

`GREMLIN_ANALYTIC_RECONSTRUCTION_CANDIDATE / ANALYTIC_SOURCE_OPEN`.

The agreement of these routes is a cross-route consistency observation. Promotion requires independent closure of the remaining replay/derivation gates.

## 6. Relation to the Wilson coordinate

RFG3 uses

\[
\beta_W=\frac6{g_0^2}.
\]

For

\[
g_0^2=\frac1{\alpha_c},
\]

this gives

\[
\boxed{\beta_W=6\alpha_c.}
\]

RFG3/RFG5 therefore carry the explicitly typed sensitivity coordinates

\[
\beta_W^{\rm archive}=2.848872,
\]

and

\[
\beta_W^{\rm canonical\,cand}=2.8490377143\ldots
\]

until the physical Yang–Mills normalization gate closes.

## 7. Falsification / promotion contract

Promotion requires all of:

1. executable replay or equivalent independent reconstruction of the historical numerical extraction;
2. independent derivation/source selection of the analytic `L3` offset structure;
3. independently typed inputs `kappa`, `I0_legacy`, `L3`, and `phi`;
4. reproduction of the archived six-decimal coordinate;
5. canonical reduction under `I0 -> kappa`;
6. separate Yang–Mills/Wilson normalization validation;
7. running-coupling validation after the bare-coordinate expression is frozen.

The adversarial sign reversal

\[
\alpha_c^{(+)}
=
\ln\varphi-\kappa\ln2
+\frac{\kappa-I_0}{L_3}
\]

must fail the six-decimal archive reconstruction gate.

## 8. GREMLIN verdict

`CHYBA / CANDIDATE_ONLY`.

The genealogy is now more strongly constrained because the historical decimal has a recovered published numerical-extraction route and an independent modern analytic reconstruction candidate that agrees at the archived six-decimal precision. The next root gates are the historical extraction replay and the analytic source/derivation of the `L3` normalization correction.
