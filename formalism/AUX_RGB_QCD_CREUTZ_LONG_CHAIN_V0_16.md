# AUX RGB-Moire QCD long-chain Creutz pilot v0.16

Status: `FINITE_VOLUME_SMALL_LOOP_SIGNAL_POSITIVE / AUTOCORRELATION_AUDITED / CREUTZ_PLATEAU_OPEN / CONFINEMENT_NOT_PROMOTED`

Date: 2026-09-26

## 1. Relation to v0.15

v0.15 established the exact dimensionless diagnostic architecture:

- Creutz-ratio cancellation of perimeter and normalization terms;
- pure-Yang-Mills Z3 center symmetry;
- full-QCD center-breaking firewall;
- leading strong-coupling area-law coordinate;
- an initial finite-statistics Monte Carlo pilot.

That pilot was deliberately left `INCONCLUSIVE` because independent short runs disagreed on whether W22 was resolved above noise.

v0.16 does not overwrite that receipt. It executes a longer checkpointed chain designed specifically to test whether the earlier W22 failure was only a statistics/thermalization problem.

## 2. Chain

The witness uses the same dimensionless pure-SU(3) Wilson action and the same candidate coordinate

[
\beta_W=2.84903771431338\ldots.
]

No physical lattice spacing is assigned.

Parameters:

[
L^4=4^4,
\qquad
\epsilon_{proposal}=1.0,
\qquad
\text{seed}=260928.
]

The chain was thermalized for 200 full-link sweeps.

Measurements were then taken after two sweeps each, for

[
N_{meas}=150,
\qquad
N_{total\ sweeps}=500.
]

The embedded SU(2) proposals use the corrected exactly unitary form introduced after the rejected v0.15 implementation bug.

## 3. Wilson-loop means

The measured dimensionless means are

[
W_{11}=0.1934648610,
]

[
W_{12}=0.0378128421,
\qquad
W_{21}=0.0379944619,
]

[
W_{22}=0.0032026393.
]

The naive standard errors across stored measurements are approximately

[
5.53\times10^{-4},
\quad
6.11\times10^{-4},
\quad
5.53\times10^{-4},
\quad
5.21\times10^{-4},
]

respectively.

The direct small-loop Creutz coordinate is

[
\boxed{
\chi(1,1)=0.8410180524.
}
]

## 4. Autocorrelation firewall

The measurements are not independent.

Rough integrated autocorrelation times in measurement units are

[
\tau_{int}(W_{11})\approx3.09,
]

[
\tau_{int}(W_{12})\approx1.67,
\quad
\tau_{int}(W_{21})\approx1.69,
\quad
\tau_{int}(W_{22})\approx1.15.
]

Therefore the naive iid bootstrap is not used as the promotion statistic.

## 5. Non-overlapping block bootstrap

For block sizes 2, 5, 10 and 15 measurements, 10,000 deterministic bootstrap replicates were evaluated.

The conservative large-block results are:

block size 10:

[
\chi_{boot}=0.868\pm0.230,
]

with 95% interval

[
\boxed{[0.484,1.381]}.
]

block size 15:

[
\chi_{boot}=0.866\pm0.245,
]

with 95% interval

[
\boxed{[0.484,1.445]}.
]

Thus the positive small-loop Creutz signal survives an explicit autocorrelation-aware resampling stress test.

## 6. What this establishes

The current Wilson-action candidate at the dimensionless RFG4D/RFG4G coordinate produces, on this finite lattice and at these statistics,

[
\boxed{\chi(1,1)>0}
]

with a block-bootstrap interval separated from zero.

This advances the earlier pilot from `INCONCLUSIVE` to

[
\boxed{\text{FINITE-VOLUME SMALL-LOOP SIGNAL POSITIVE}.}
]

## 7. What it does not establish

This is not yet a confinement proof or a promoted nonperturbative project result.

The reasons are structural:

1. only one lattice volume has been used;
2. only the smallest Creutz ratio is resolved;
3. no plateau over increasing R,T has been demonstrated;
4. ordinary single-level sampling still suffers rapidly worsening Wilson-loop signal-to-noise;
5. no continuum-volume extrapolation has been attempted;
6. no full-QCD dynamical-quark string-breaking test is included.

Therefore the correct status remains

[
\boxed{\text{CONFINEMENT NOT PROMOTED}.}
]

## 8. Next gate

The next pure-YM gate is no longer basic Metropolis validation.

It is

[
\boxed{
\text{multilevel / variance-reduced Wilson loops}
\to
\chi(R,T)\text{ for several }R,T
\to
\text{positive plateau}
\to
\sigma a^2.
}
]

The natural external benchmark is the locality-based multilevel strategy of Luescher and Weisz, JHEP 09 (2001) 010, arXiv:hep-lat/0108014, developed specifically because ordinary Wilson-loop estimators suffer exponentially degrading signal-to-noise.

No physical metric calibration is required for this gate.
