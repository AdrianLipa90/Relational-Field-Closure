# GREMLIN bounded audit — RF-N1 source-basis candidates

Status: `CANDIDATE_GENERATION_ONLY / NO_CANON_PROMOTION`

GREMLIN is used here only to generate and reject/retain candidate scalar source bases for the already-derived RF-N1 lapse operator. It has no authority to promote a source law.

Required source type:

\[
\Delta_h u=\mathcal S_R,
\qquad
u=\ln N_R,
\qquad
[\mathcal S_R]=L^{-2}.
\]

## Candidate scan

| candidate | type | independence from lapse geometry | audit disposition |
|---|---:|---|---|
| `Xi_I` temporal information curvature | `L^-2` | upstream TIR×IDT scalar; independent source-basis candidate before lapse equation | `RETAIN_CANDIDATE` |
| `R^(3)[h]` | `L^-2` | built from the spatial metric already being solved/glued | `QUARANTINE_FOR_NEWTON_SOURCE` — circular as a primary independent source |
| `|grad u|^2` | `L^-2` | self-field nonlinear invariant | `RETAIN_ONLY_AS_HIGHER_ORDER_SELF_TERM` |
| `F_{ij}F^{ij}` after physical gauge normalization | `L^-4` before a compensating scale | belongs to Maxwell branch and needs an additional scale | `DEFER_MAXWELL_CROSS_COUPLING` |
| constant `L^-2` vacuum term | `L^-2` | independent but homogeneous | `DEFER_LAMBDA0_SECTOR` |

## Minimal retained candidate

The lowest-order already-derived independent scalar with the required inverse-area type is

\[
\boxed{\Xi_I.}
\]

Therefore GREMLIN may propose, but may not promote,

\[
\boxed{
\mathcal S_R=\beta_I\Xi_I+\cdots
}
\]

with dimensionless `beta_I`.

No value of `beta_I` is generated or fitted here. No identification

\[
c^2\beta_I\Xi_I=4\pi G\rho_m
\]

is admitted. That equality remains a downstream target requiring an independent mass/source map and normalization.

## Audit conclusion

The useful candidate relation is structural rather than numerical:

```text
IDT/TIR information curvature Xi_I [L^-2]
            |
            v
candidate source basis for u = ln N_R
            |
            v
Delta_h u = beta_I Xi_I + ...
```

`R^(3)` is rejected as the primary Newton source because it would recycle the geometry being determined. `|grad u|^2` is typed as a possible nonlinear self-term, not an independent matter source. Maxwell and vacuum terms remain in their own dependency branches until cross-coupling gates are reached.
