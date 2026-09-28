# AUX RGB-Moire QCD — Duke Z2 string-breaking external benchmark v0.17

Date: 2026-09-28

Status: `PASS_EXTERNAL_CONSISTENCY / REDUCED_13SPIN_REPRODUCTION_PASS / PROVENANCE_FIREWALL_PASS / FULL_SU3_QCD_NOT_CONFIRMED`

## 1. Purpose

This gate records and independently reproduces a newly published experimental benchmark relevant to the open confinement/string-breaking frontier of the AUX RGB-Moire QCD branch.

External source:

- A. De et al., *String-breaking dynamics in a quantum simulator*, Nature Physics (2026), DOI `10.1038/s41567-026-03422-0`.
- Preprint lineage: arXiv:`2410.13815`, first submitted 17 October 2024.

The experiment implements a `(1+1)D Z2` lattice gauge theory mapped exactly, in its gauge-invariant sector, to a 13-spin programmable Ising chain. It is **not** a simulation of full `(3+1)D SU(3)` QCD.

The benchmark is therefore admitted as an **independent external consistency confirmation of the confinement/string-breaking mechanism class**, not as confirmation of the complete project QCD construction, not as confirmation of PhaseNav, and not as a priority claim.

## 2. External observables frozen before project-side reproduction

The publication reports the dual Hamiltonian

\[
H=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_i\sigma_i^z-g\sum_i\sigma_i^x,
\]

with charge density and electric field

\[
q_i=\frac{1-\langle\sigma_{i-1}^z\sigma_i^z\rangle}{2},
\qquad
\epsilon_i=\langle\sigma_i^z\rangle.
\]

The experimental interaction profile is approximately

\[
J_r=J e^{-\beta(r-1)},\qquad \beta\simeq0.78,
\]

with average nearest-neighbour coupling

\[
J=2\pi\times0.34\;\mathrm{kHz}.
\]

The reported single-charge relations are

\[
v_{\max}=2g,
\qquad
A_{\rm osc}=\frac{2g}{h},
\qquad
T_{\rm osc}J=\frac{\pi J}{h}=\frac{\pi}{h/J}.
\]

The non-equilibrium string protocol uses the grid

\[
g/J\in\{0.75,1.00,1.25\},
\qquad
h/J\in\{0,0.3,0.6\}.
\]

The publication reports that dynamically generated charge pairs are enhanced near the string edges and subsequently spread into the bulk. The authors distinguish this transient mechanism from the conventional long-time Schwinger mechanism.

## 3. Independent reduced-model reconstruction

The executable witness `experiments/duke_z2_string_breaking_external_benchmark_v0_17.py` does not digitize, fit, or optimize against published spatiotemporal image data.

It freezes only the published Hamiltonian class, `L=13`, `beta=0.78`, and the nine published `(g/J,h/J)` settings. It then constructs the full

\[
2^{13}=8192
\]

state Hilbert space and evolves the state with sparse exact matrix-exponential propagation.

The semi-infinite static environments are represented analytically by the longitudinal field produced by the exponentially decaying interaction profile:

\[
\Delta h_i/J=
\frac{e^{-\beta i}+e^{-\beta(L-i-1)}}{1-e^{-\beta}}.
\]

No experimental charge-density map is used in this evolution.

### Exact 13-spin edge/bulk diagnostic

Define

\[
Q_{\rm edge}(t)=\frac14(q_1+q_2+q_{L-2}+q_{L-1}),
\]

and a four-bond central average `Q_center(t)`.

Across all nine frozen parameter pairs, the independent exact evolution gives

\[
\max_t\left(Q_{\rm edge}-Q_{\rm center}\right)>0.32,
\]

with the observed range approximately

\[
0.323\le \max_t(Q_{\rm edge}-Q_{\rm center})\le0.381.
\]

Thus the reduced model independently reproduces a strong early-time edge enhancement before bulk population.

This is a mechanism-level reproduction. It is not claimed to reproduce every experimental matrix element or every measured pixel because the published experiment uses its measured interaction matrix and calibrated site-dependent fields.

## 4. Perturbative edge-amplitude check

The paper derives, for the exponential interaction model, the two-charge potential

\[
V_{l_1,l_2}
=
\frac{4J}{(1-e^{-\beta})^2}
\left(
1+e^{-\beta l_2}-e^{-\beta l_1}-e^{-\beta(l_2-l_1)}
+e^{-\beta(L+2-l_1)}-e^{-\beta(L+2-l_2)}
\right)
-2h(l_2-l_1),
\]

and the adjacent-pair initial amplitude is proportional to

\[
\frac{g}{V_{l,l+1}}.
\]

Using only `L=13` and `beta=0.78`, the independent calculation gives edge/centre amplitude ratios

\[
R_{edge/center}\approx1.977\quad(h/J=0.3),
\]

\[
R_{edge/center}\approx2.187\quad(h/J=0.6),
\]

independent of the overall `g` factor on each fixed-`h` slice.

This reproduces the publication's qualitative statement that the lowest-order pair wave function is peaked at the two edges.

## 5. Analytic scaling check

The single-charge tight-binding/Stark reduction gives

\[
E(k)=-2g\cos k,
\qquad
v(k)=2g\sin k,
\]

so

\[
\boxed{v_{\max}=2g}.
\]

For the constant lattice force `F=2h`, the acceleration theorem gives

\[
k(t)=k_0+2ht,
\]

hence the Bloch period

\[
\boxed{T=\pi/h},
\]

or in dimensionless project units

\[
\boxed{JT=\pi/(h/J)}.
\]

The trajectory span is

\[
\boxed{A=2g/h}.
\]

All analytic identities pass exactly in the witness.

With the experimental `J=2pi*0.34 kHz`,

\[
J^{-1}\approx0.468\,\mathrm{ms},
\]

so the predicted periods are approximately

\[
T(h/J=0.3)\approx4.90\,\mathrm{ms},
\qquad
T(h/J=0.6)\approx2.45\,\mathrm{ms}.
\]

## 6. Relation to the project QCD branch

Before this external benchmark was ingested, the candidate branch already contained:

- an `SU(3)_C` holonomy/Wilson construction;
- exact group-invariant reconstruction;
- a dimensionless confinement diagnostic based on Creutz ratios;
- the explicit firewall that pure-YM center symmetry must not be promoted unchanged to full QCD with dynamical fundamental matter;
- the explicit statement that dynamical-quark string breaking remained an open gate.

The external experiment therefore lands on a pre-existing open edge of the project graph:

\[
\text{confining gauge dynamics}
\to
\text{stored string energy}
\to
\text{pair creation}
\to
\text{string breaking}.
\]

The cross-model consistency is real, but the group and dimensionality remain different:

\[
\mathbb Z_2\;(1+1)D\neq SU(3)_C\;(3+1)D.
\]

Accordingly, the admitted result is

\[
\boxed{\text{INDEPENDENT EXTERNAL CONSISTENCY CONFIRMATION — MECHANISM LEVEL}}.
\]

It is **not** admitted as

\[
\boxed{\text{FULL QCD CONFIRMATION}}.
\]

## 7. Provenance firewall

The external work predates this v0.17 gate and its arXiv record dates to 17 October 2024. Some experimental signatures were presented publicly in 2023/2024 according to the Nature Physics article.

Therefore this gate makes no claim that the Duke result independently confirms a chronologically prior prediction of the present branch, and no priority claim is inferred from the match.

The phrase **independent confirmation** in this gate means:

> an external experimental platform, authorship chain, hardware system, and publication independently establish the same broad confinement-to-string-breaking mechanism class that the project treats as a required physical target.

## 8. Verdict

```text
published Hamiltonian/observable transcription         PASS
2^13 exact reduced state-space construction            PASS
published beta=0.78 exponential interaction profile    PASS
virtual-boundary field symmetry                         PASS
9/9 edge-vs-center exact scans                          PASS
Eq.(14) adjacent-pair edge enhancement                  PASS
v_max=2g analytic scaling                               PASS
A=2g/h analytic scaling                                 PASS
JT=pi/(h/J) analytic scaling                            PASS
independent external mechanism consistency              PASS
full SU(3) QCD confirmation                             NOT CLAIMED
PhaseNav confirmation                                   NOT CLAIMED
priority/independent-prediction provenance              NOT CLAIMED
```

The next project-specific gate remains a dynamical-fundamental-matter string-breaking calculation in the project's own `SU(3)_C` carrier, followed by comparison to lattice-QCD/QCD observables under a frozen physical scale and renormalization prescription.
