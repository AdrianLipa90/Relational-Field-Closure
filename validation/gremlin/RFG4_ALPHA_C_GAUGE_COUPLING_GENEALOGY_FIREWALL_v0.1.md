# RFG4 — alpha_c Gauge-Coupling Genealogy Firewall

Status: `CHYBA / CANDIDATE_ONLY / LEGACY_I0_OFFSET_RECOVERY_MATCH / UPSTREAM_EXPRESSION_SOURCE_OPEN / YM_PROMOTION_GATED`

RFG4 audits the archived Metatime/CIEL coordinate

\[
\alpha_c^{\rm archive}=0.474812
\]

before it enters RFG3 as a physical Yang–Mills normalization.

## 1. Archived dependency and historical normalization

The archived gluon implementation places the two coordinates

\[
\boxed{\alpha_c^{\rm archive}=0.474812},
\qquad
\boxed{I_0^{\rm legacy}=0.009}
\]

in the same constant block. The same implementation then defines

\[
\boxed{g_{\rm archive}=\frac{1}{\sqrt{\alpha_c}}}
\]

and

\[
\boxed{\alpha_s^{\rm archive}=\frac{g_{\rm archive}^2}{4\pi}.}
\]

The current canonical information constant is

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}
=0.009193150006360\ldots
\]

so the historical rounded coordinate carries the normalization displacement

\[
\boxed{\Delta I=\kappa-I_0^{\rm legacy}}
=1.9315000636\times10^{-4}.
\]

## 2. Recovered legacy-offset candidate

A previously frozen low-complexity GREMLIN candidate gave the canonical-base coordinate

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

The historical project geometry already supplies

\[
L_3=7.
\]

The newly recovered normalization-offset candidate is therefore

\[
\boxed{
\delta_{I,L_3}
=
\frac{\kappa-I_0^{\rm legacy}}{L_3}
}
\]

and

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

this gives

\[
\boxed{
\alpha_c^{\rm legacy\,rec}
=0.47481202619417856\ldots
}
\]

and therefore at the six-decimal precision carried by the archived constant,

\[
\boxed{
\operatorname{round}(\alpha_c^{\rm legacy\,rec},6)
=0.474812.
}
\]

The absolute residual against the archived decimal is

\[
\Delta_{\rm abs}=2.6194\times10^{-8},
\]

with relative residual

\[
\Delta_{\rm rel}=5.52\times10^{-8}.
\]

This is recorded as `LEGACY_I0_OFFSET_RECOVERY_MATCH`.

## 3. Canonical renormalized coordinate

Under exact replacement of the historical rounded information coordinate by the canonical one,

\[
I_0^{\rm legacy}\rightarrow\kappa,
\]

the offset term closes:

\[
\frac{\kappa-I_0}{L_3}\rightarrow0.
\]

The corresponding canonicalized coordinate is therefore

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

The archived coordinates remain

\[
g_{\rm archive}=1.4512397213\ldots,
\qquad
\beta_W^{\rm archive}=2.848872.
\]

Thus the archived/canonical difference is naturally typed as a historical information-normalization displacement rather than a free numerical retuning.

## 4. Provenance typing

The Library presently establishes three facts:

1. `alpha_c=0.474812` and `I0=0.009` coexist in the archived gluon constant block;
2. the modern phase-intention formalism fixes `kappa=ln(2)/(24pi)`;
3. the recovered offset expression reproduces the archived decimal at its stored precision.

The source document containing the historical upstream expression for `alpha_c` remains `OPEN_SOURCE_RECOVERY`.

Accordingly, the expression above is typed

`GREMLIN_RECOVERED_GENEALOGY_CANDIDATE`

with exact numerical reconstruction and open documentary provenance.

## 5. Relation to the Wilson coordinate

RFG3 uses

\[
\beta_W=\frac6{g_0^2}.
\]

For the archive relation

\[
g_0^2=\frac1{\alpha_c},
\]

one obtains

\[
\boxed{\beta_W=6\alpha_c.}
\]

RFG3/RFG5 may therefore carry two explicitly typed sensitivity coordinates:

\[
\beta_W^{\rm archive}=2.848872,
\]

and

\[
\beta_W^{\rm canonical\,cand}=2.8490377143\ldots
\]

until the upstream genealogy is recovered from source.

## 6. Falsification / promotion contract

Promotion requires all of:

1. recovery or independent derivation of the upstream expression selecting the `L3` offset structure;
2. independently typed inputs `kappa`, `I0_legacy`, `L3`, and `phi`;
3. reproduction of the archived six-decimal coordinate;
4. canonical reduction under `I0 -> kappa`;
5. separate Yang–Mills/Wilson normalization validation;
6. running-coupling validation after the bare-coordinate expression is frozen.

An adversarial sign reversal

\[
\alpha_c^{(+)}
=
\ln\varphi-\kappa\ln2
+\frac{\kappa-I_0}{L_3}
\]

must fail the six-decimal archive reconstruction gate.

## 7. GREMLIN verdict

`CHYBA / CANDIDATE_ONLY / LEGACY_I0_OFFSET_RECOVERY_MATCH`.

The current dependency graph is

```text
legacy I0 = 0.009
canonical kappa = ln(2)/(24pi)
L3 = 7
        |
        v
legacy normalization displacement
        |
        v
alpha_c legacy reconstruction candidate
        |
        +--> archive six-decimal match
        |
        +--> I0 -> kappa canonical reduction
                 |
                 v
          alpha_c canonical candidate
                 |
                 v
          g_YM / beta_W candidate
                 |
                 v
          RFG3 / RFG5 gravity gates
```
