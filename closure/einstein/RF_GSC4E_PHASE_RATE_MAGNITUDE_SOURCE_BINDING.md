# RF-GSC4E — Phase-Rate Magnitude Source-Binding Firewall

Status: `EXACT_SPATIAL_SCALE_QUOTIENT / EXECUTABLE_MAGNITUDE_BINDING_CERTIFIER / PRODUCTION_MAGNITUDE_FIELD_OPEN`

Date: 2026-08-31

## 1. Purpose

RF-GSC4D constructs the rigid-route spatial coframe scale from the local phase rate,

\[
 s=\frac{c}{\sqrt6\,|\omega_t|},
 \qquad e=sI_3.
\]

Its spatial overlap theorem requires `s_q=s_p`. RF-GSC4E isolates the exact information content of that condition.

## 2. Magnitude quotient

For finite nonzero phase rates define

\[
\boxed{\nu:=|\omega_t|>0.}
\]

Then

\[
\boxed{s=\frac{c}{\sqrt6\,\nu}.}
\]

Because `nu -> c/(sqrt(6) nu)` is injective on the positive reals,

\[
\boxed{s_q=s_p\iff \nu_q=\nu_p.}
\]

Therefore the GSC4D spatial scale depends on the quotient

\[
\boxed{\omega_t\sim-\omega_t}
\]

rather than on the signed phase rate itself.

A sign reversal

\[
\omega_{t,q}=-\omega_{t,p}
\]

preserves `nu`, `s`, the physical coframe scale, and the GSC4D spatial compatibility equation.

## 3. Source-binding witness

The minimal overlap witness for the GSC4D spatial scale is therefore:

1. one common `clock_id` / temporal calibration;
2. one common `phase_magnitude_field_id` for the represented physical scalar `nu`;
3. finite nonzero local phase-rate representatives;
4. overlap equality
   \[
   \boxed{|\omega_{t,q}|=|\omega_{t,p}|}
   \]
   within the declared numerical tolerance.

A signed phase-rate identity is a stronger input than this spatial gate requires.

## 4. Firewall

The magnitude binding is limited to the RF-GSC4D spatial physicalization seam.

- It does not identify the phase-rate sign across patches.
- It does not construct the IDT relational lapse `N_R`.
- It does not construct the 05H event clock.
- It does not close production provenance for the magnitude field.
- Other dynamical sectors may retain signed `omega_t` information independently.

## 5. Executable certifier

Implementation:

`src/rfc/phase_rate_magnitude_binding.py`

Reference tests:

`tests/reference/test_gsc4e_phase_rate_magnitude_binding.py`

The certifier separates:

- valid finite nonzero phase-rate representatives;
- common clock provenance;
- common magnitude-field provenance;
- magnitude agreement;
- signed-rate agreement.

The final spatial-scale binding can pass while signed-rate agreement is false.

## 6. Claim ledger

| Statement | Status |
|---|---|
| `s=c/(sqrt6 |omega_t|)` factors through `nu=|omega_t|` | `EXACT` |
| `s_q=s_p iff nu_q=nu_p` for finite nonzero rates | `EXACT` |
| sign reversal preserves the GSC4D spatial scale | `EXACT` |
| executable magnitude-binding certifier | `VALIDATION TARGET` |
| production `phase_magnitude_field_id` and overlap values | `OPEN SOURCE INPUT` |
| signed phase-rate equality | `SEPARATE STRONGER INPUT` |
| IDT lapse binding | `SEPARATE TEMPORAL INPUT` |

## 7. Live 36D boundary

The reduction was independently audited through the active

`GREMLIN -> Terminal36D -> PhaseNav36D -> GREMLIN`

surface with `CANDIDATE_ONLY` authority. Runtime evidence does not promote source data or canonical claims.
