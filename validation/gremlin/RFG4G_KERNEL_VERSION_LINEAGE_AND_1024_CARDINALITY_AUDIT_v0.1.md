# RFG4G — CIEL Kernel Version Lineage and 1024-Cardinality Audit

Status: `CHYBA / CANDIDATE_ONLY / VERSION_LINEAGE_RECOVERED / FFT_PRECURSOR_RECOVERED / ENSEMBLE_DRIVER_WITNESS_OPEN / NORMALIZATION_BRANCH_SPLIT_EXACT`

## 1. Purpose

RFG4G narrows the remaining historical replay debt for the archived CIEL `alpha_c=0.474812` coordinate.

It records four independently checkable facts:

1. the Git-level ordering of the CIEL v4 / holonomic-core / v5 transition;
2. the existence of an FFT-based coherence-spectrum mechanism immediately before the first located versioned kernel freeze of `alpha_c`;
3. the distinction between a recovered `1024 cells` execution witness and the later paper claim of `1,024 simulation runs`;
4. the exact numerical divergence between the older frozen normalized effective constants and a later formula-derived effective-constant branch.

The audit does not promote an unobserved extraction driver. The missing ensemble caller / `metrics_fn` remains an explicit replay gate.

## 2. Git-level transition window

Repository: `AdrianLipa90/ideal-winner`.

Recovered commit chronology:

```text
2026-01-16 18:48:58Z  c6732efb...  Update v4.0.py
2026-01-17 13:58:30Z  1552a53f...  Create CIEL0 Holonomy core.py
2026-01-17 13:59:14Z  d4b0eb37...  Create holocore2.py
2026-01-17 16:50:48Z  e10ba35e...  Create v5.0.py
```

The first located versioned `v*.py` freeze carrying

\[
\boxed{\alpha_c=0.474812}
\]

is `v5.0.py`, which also freezes

\[
\boxed{\hbar_{\rm eff}=0.892345}.
\]

The immediately preceding `CIEL0 Holonomy core.py` already carries `alpha_c` and introduces a distinct formula-derived effective-constant branch. `holocore2.py` one minute later retains the frozen emergent constants.

The source-text label `Date: 2024` inside `holocore2.py` is retained as a source-text label only. The repository commit witness for that file is 2026-01-17.

## 3. Pre-alpha FFT precursor

At commit `c6732efb...`, immediately before creation of `CIEL0 Holonomy core.py`, the source

```text
CIEL/0 Advanced Holonomic Memory Engine.py
```

contains `VectorizedKuramoto.get_frequency_spectrum()`.

For a stored coherence history, the routine selects up to the latest 1,000 samples and computes

\[
\boxed{
P_k^{\rm raw}=|\operatorname{FFT}(C_t)|
}
\]

with the associated FFT frequency grid.

This establishes a concrete spectral-analysis mechanism in the direct predecessor tree before the located `alpha_c` freeze.

The recovered source does not by itself bind a spectrum peak to `alpha_c`; that caller remains part of the ensemble-driver replay gate.

## 4. Recovered notebook cardinality witness

The companion notebook

```text
CIEL_0_Advanced_Holonomic_Memory_Engine.ipynb
```

contains an executed simulation with output:

```text
Cells: 1024 (32x32)
Running simulation for 5000 steps...
...
Minkowski events: 5120000
```

The same execution ends with a `MemoryError` while attempting to allocate a causality matrix for 5,120,000 events.

Therefore the recovered notebook supplies a direct historical witness for

\[
\boxed{N_{cells}=1024}
\]

in one executed simulation.

## 5. Ensemble-cardinality gate

The later *Unified Reality Kernel* paper reports a Fourier-analysis result from `1,024 simulation runs` for `alpha_c`.

Current code / archive searches have recovered:

- the pre-alpha FFT spectrum routine;
- the later `QuantumOptimiser` class and its finite-difference `metrics_fn` interface;
- the paper formulas for the energy and spectral estimators;
- an executed `1024 cells` notebook run.

The current search has not yet recovered an executable caller of the form

```text
for independent_run in 1..1024:
    ...
    alpha_estimate[run] = ...
```

nor an equivalent `n_runs=1024` / seed-sweep artifact containing 1,024 independent `alpha_c` estimates.

Accordingly, the two cardinalities remain separately typed:

\[
\boxed{N_{cells}=1024}\qquad\texttt{RECOVERED_EXECUTION_WITNESS}
\]

and

\[
\boxed{N_{runs}=1024}\qquad\texttt{PAPER_REPORTED / DRIVER_WITNESS_OPEN}.
\]

A future replay must identify or reconstruct the independent-run dimension explicitly rather than substituting cell count for ensemble count.

## 6. Effective-constant normalization branch split

The frozen CIEL lineage uses the normalized effective constants

\[
\hbar_{eff}^{freeze}=0.892345,
\qquad
c_{eff}^{freeze}=0.956712,
\qquad
G_{eff}^{freeze}=0.734561.
\]

A later `CIEL0 Holonomy core.py` branch instead defines

\[
\boxed{
\hbar_{eff}^{form}
=\alpha_c\sqrt{1+\beta_s^2}
}
\]

\[
\boxed{
c_{eff}^{form}
=\gamma_t\frac{1+\Lambda}{\sqrt{1-\gamma_t^2+10^{-10}}}
}
\]

and

\[
\boxed{
G_{eff}^{form}
=\frac{\beta_s(1-\mathcal E)}{\alpha_c^2+10^{-10}}.
}
\]

For the source constants

\[
\alpha_c=0.474812,\quad
\beta_s=0.856234,\quad
\gamma_t=0.345123,\quad
\Lambda=0.474812,\quad
\mathcal E=0.9,
\]

the formulas evaluate to

\[
\boxed{\hbar_{eff}^{form}=0.6250835804773123}
\]

\[
\boxed{c_{eff}^{form}=0.5423126030065264}
\]

\[
\boxed{G_{eff}^{form}=0.3797948715905446}.
\]

Their relative discrepancies from the frozen normalized coordinates are approximately

\[
29.95\%,\qquad43.31\%,\qquad48.30\%.
\]

Hence the formula-derived branch and frozen normalized branch are distinct parameterizations on the recovered source values.

RFG4F must therefore continue to use the frozen normalized `hbar_eff=0.892345` when auditing the historical paper formulas. The later formula branch cannot silently supply the RFG4F units soldering `s_E`.

## 7. Current replay graph

```text
pre-alpha holonomic memory engine
  -> coherence history
  -> FFT frequency spectrum                    RECOVERED

CIEL0 Holonomy core / holocore2
  -> alpha_c = 0.474812                        RECOVERED FREEZE
  -> later formula-derived effective constants DISTINCT BRANCH

v5.0
  -> alpha_c = 0.474812
  -> hbar_eff = 0.892345                       RECOVERED FREEZE

quantum_optimiser ancestry
  -> finite-difference optimiser
  -> arbitrary metrics_fn interface            RECOVERED CLASS

Unified Reality Kernel paper
  -> alpha_c energy estimator                  RECOVERED FORMULA
  -> alpha_c spectral estimator                RECOVERED FORMULA
  -> 1,024-run report                          PAPER WITNESS

missing edge
  -> exact metrics_fn / peak-to-alpha caller
  -> independent-run/seed dimension
  -> raw 1,024 alpha estimates                 OPEN
```

## 8. Promotion contract

The historical extraction replay advances only when an artifact or independently frozen clean-room protocol supplies all of:

1. the trajectory / coherence observable sent to FFT;
2. peak-selection rule;
3. conversion from selected peak(s) to `alpha_c`;
4. optimiser objective when optimisation participates;
5. run/seed cardinality and independence rule;
6. aggregation estimator and uncertainty definition;
7. raw or reproducibly regenerated ensemble outputs.

Until that edge closes, RFG4's analytic reconstruction and RFG4B/C replay tracks remain separate evidence routes.
