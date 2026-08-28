# RFG4B — alpha_c Historical Extraction Replay Contract

Status: `CHYBA / CANDIDATE_ONLY / PAPER_METHOD_RECOVERED / OPTIMISER_ANCESTRY_RECOVERED / HISTORICAL_DRIVER_COORDINATES_OPEN / EXACT_REPLAY_GATED`

## 1. Purpose

RFG4B defines the minimum provenance and numerical coordinates required to replay the historical CIEL/0 extraction of

\[
\alpha_c=0.474812.
\]

It preserves two recovered algorithmic routes as separately typed objects:

1. the published October 2025 constant-extraction method;
2. the archived `ciel_quantum_optimiser` ancestry recovered through `ext2.py`.

The replay gate opens only when the historical driver coordinates connecting the published method to an executable run are supplied.

## 2. Published extraction route

The October 2025 *Unified Reality Kernel* source gives the iterative coordinate update

\[
\boxed{
\alpha_c^{(n+1)}
=
\alpha_c^{(n)}
+\eta_n\frac{\partial\mathcal L}{\partial\alpha_c}
}
\]

with coherence functional

\[
\boxed{
\mathcal L
=\int_M
\left[
|\nabla\Psi|^2
+\alpha_c|\Psi|^4
+\beta_s|S-\Psi|^2
-\gamma_t\tau|\Psi|^2
\right]d^4x
}
\]

and adaptive step coordinate

\[
\boxed{
\eta_n
=
\frac{0.01}{1+\sqrt{\sum_i(\partial\mathcal L/\partial\theta_i)^2}}
}.
\]

The spectral estimator is

\[
\boxed{
P(\omega)
=
\left|
\int\Psi(x,t)e^{-i\omega t}dt
\right|^2
}
\]

with peak spacing

\[
\boxed{
\omega_n
=n\alpha_c\frac{c_{\rm eff}}{\hbar_{\rm eff}}.
}
\]

The source reports

\[
\boxed{
N_{\rm runs}=1024,
\qquad
\alpha_c=0.474812\pm0.000007.
}
\]

It also specifies the numerical-method family: fourth-order spatial finite differences, a symplectic time integrator, adaptive time stepping and perfectly matched boundary layers.

This route is typed

`PAPER_METHOD_RECOVERED`.

## 3. Archived optimiser ancestry

The recovered CIEL batch source `ext2.py` preserves a class explicitly labelled `Quantum Optimiser — bez zmian`, corresponding to the earlier source name `ciel_quantum_optimiser.py`.

Its executable update uses the loss

\[
\boxed{
\mathcal J
=(1-C)^2+(1-F)^2+P_{ethics}
}
\]

where the ethics penalty is zero for an admitted state and `0.1 * ethical_weight` otherwise.

For every supplied constant `theta_k`, the implementation estimates

\[
\boxed{
\partial_k\mathcal J
\approx
\frac{
\mathcal J(\theta_k+10^{-3})-\mathcal J(\theta_k)
}{10^{-3}}
}
\]

and performs

\[
\boxed{
\theta_k\leftarrow\theta_k-0.05\,\partial_k\mathcal J
}
\]

for 50 default optimiser steps.

This is typed

`OPTIMISER_ANCESTRY_RECOVERED`.

The published update and the archived generic optimiser remain separately typed because their objective coordinates, step rules and update signs are different objects in the recovered sources.

## 4. Historical driver coordinates

An exact historical replay requires a driver packet containing all of the following coordinates.

### Field initialization

- initial `Psi` construction;
- initial symbolic field `S` construction;
- initial temporal field `tau` construction;
- field dimensionality and component count;
- spatial domain and coordinate units;
- grid resolution and spacing;
- random-seed schedule or deterministic seed rule.

### Constant initialization

- initial `alpha_c` per run;
- initial `beta_s` per run;
- initial `gamma_t` per run;
- complete list of simultaneously optimized coordinates `theta_i`;
- fixed versus optimized status of every constant.

### Integrator realization

- exact fourth-order finite-difference stencil;
- symplectic update map;
- initial timestep;
- adaptive timestep law and bounds;
- total integration horizon or accepted-step count;
- PML width, profile and strength.

### Optimization realization

- exact objective used for the reported `alpha_c` extraction;
- optimizer iteration count per simulation run;
- stopping criterion;
- gradient realization;
- treatment of coupled constants during each alpha update;
- acceptance/rejection policy for unstable runs.

### Spectral extraction

- sampled observable entering the Fourier transform;
- sampling cadence;
- windowing/detrending rule;
- frequency-grid construction;
- spectral peak detector;
- integer assignment rule for `n`;
- estimator converting peak spacing into one run-level `alpha_c`.

### Ensemble aggregation

- exact meaning of the reported 1,024 runs;
- run-to-run seed/initial-condition schedule;
- aggregation estimator for the reported central value;
- uncertainty estimator producing `±0.000007`;
- outlier and failed-run policy.

Until these coordinates are recovered or independently frozen for a new clean-room protocol, the historical replay status remains

`HISTORICAL_DRIVER_COORDINATES_OPEN / EXACT_REPLAY_GATED`.

## 5. 1,024-run versus 1,024-sample firewall

A later CIEL Batch-17 experiment `exp_47fdb331` uses

\[
n_{sample}=1024
\]

samples for one Schumann-harmonic signal.

RFG4B keeps this coordinate distinct from the published

\[
N_{runs}=1024
\]

ensemble count. Replay provenance therefore carries explicit typed fields

`simulation_run_count`

and

`time_series_sample_count`.

Equality of their integer values carries zero authority to identify the two coordinates.

## 6. Relation to the modern analytic reconstruction

RFG4 independently records

\[
\alpha_c^{\rm legacy\,rec}
=
\ln\varphi
-\kappa\ln2
-\frac{\kappa-I_0^{legacy}}{L_3}
=0.474812026194\ldots
\]

for

\[
I_0^{legacy}=0.009,
\qquad
L_3=7.
\]

The historical paper reports the interval

\[
0.474805\le\alpha_c\le0.474819
\]

from its stated `±0.000007` coordinate. The analytic reconstruction lies inside this interval.

This agreement is an independent cross-route constraint. Its status remains

`GREMLIN_ANALYTIC_RECONSTRUCTION_CANDIDATE`.

## 7. Replay promotion states

RFG4B uses the following monotonic states:

```text
PAPER_METHOD_RECOVERED
  -> OPTIMISER_ANCESTRY_RECOVERED
  -> HISTORICAL_DRIVER_COORDINATES_RECOVERED
  -> CLEAN_ROOM_REPLAY_EXECUTED
  -> ENSEMBLE_STATISTICS_REPRODUCED
  -> EXTRACTION_REPLAY_PASS
```

Promotion to `EXTRACTION_REPLAY_PASS` requires a clean-room execution that reproduces the declared run count, estimator and uncertainty procedure from a content-addressed driver packet.

## 8. Current verdict

`CHYBA / CANDIDATE_ONLY`.

Current evidence closes the published-method source and recovers a real CIEL optimiser ancestor. The remaining root gate is the historical driver packet that instantiates initial conditions, numerical realization, optimizer binding, spectral estimator and ensemble aggregation.