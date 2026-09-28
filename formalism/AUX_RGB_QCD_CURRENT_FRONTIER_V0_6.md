# AUX RGB-Moire / QCD current frontier v0.6

Date: 2026-09-28

Status: `STRUCTURAL_COLOR_GAUGE_CHAIN_ASSEMBLED / DIMENSIONLESS_CONFINEMENT_SIGNAL_POSITIVE / INDEPENDENT_EXTERNAL_STRING_BREAKING_CONSISTENCY_PASS / PHYSICAL_RENORMALIZED_QCD_OPEN`

## Delta from v0.5

v0.5 remains unchanged. v0.6 adds one externally sourced validation edge without promoting the full-QCD claim hierarchy.

The Nature Physics experiment of De et al. (2026), DOI `10.1038/s41567-026-03422-0`, experimentally observes string breaking in a `(1+1)D Z2` lattice gauge theory implemented by a 13-ion simulator. Its preprint lineage is arXiv:`2410.13815` (17 October 2024).

A project-side independent reproduction using the published Hamiltonian class, `L=13`, exponential profile `beta=0.78`, virtual static environments, and the published nine-point `(g/J,h/J)` grid passes:

- exact `2^13=8192` state-space evolution;
- positive early edge-over-centre charge excess in 9/9 parameter settings;
- perturbative Eq.(14) edge-enhanced adjacent-pair amplitudes;
- exact analytic `v_max=2g`, `A=2g/h`, and `JT=pi/(h/J)` scaling checks.

Receipt: `validation/AUX_RGB_QCD_DUKE_Z2_STRING_BREAKING_EXTERNAL_BENCHMARK_V0_17.json`.

Formal benchmark: `formalism/AUX_RGB_QCD_DUKE_Z2_STRING_BREAKING_EXTERNAL_BENCHMARK_V0_17.md`.

## Evidence classification

The result is recorded as:

`INDEPENDENT_EXTERNAL_CONSISTENCY_CONFIRMATION — MECHANISM LEVEL`.

It confirms that an independent experimental system realizes the same broad physical mechanism class required by the project frontier:

`confinement -> stored string energy -> charge-pair formation -> string breaking`.

It does **not** confirm:

- the project's full `(3+1)D SU(3)_C` construction;
- the project's coupling/scale selection;
- the project's `beta_W` value;
- PhaseNav as a physical theory;
- chronological prediction priority.

## Frontier after v0.17

The remaining physical QCD gates are:

1. physical/source selection of `g` / `alpha_c`;
2. renormalization-scale and scheme binding for `g(mu)`;
3. threshold matching and `Lambda_QCD`;
4. nonperturbative SU(3) confinement plateau with controlled continuum/volume systematics;
5. dynamical fundamental matter and SU(3) string breaking/hadronization;
6. hadron spectrum and external-data validation.

The Duke benchmark materially strengthens item 5 as a physically realized target class, while leaving the SU(3) binding itself open.
