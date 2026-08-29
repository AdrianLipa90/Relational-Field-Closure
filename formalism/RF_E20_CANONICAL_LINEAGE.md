# RF-E20 — Canonical Lineage for Tetra / Phase-Clock Mass-Scale Closure

Status: `CANONICAL_NUMBERING / HISTORICAL_API_PRESERVED`

The tetra / phase-clock mass-scale line was developed through two historical branch labels:

- `feat/rfe19-tetra-clock-mass-scale-closure-v0.1`
- `feat/rfe18-tetra-clock-mass-scale-closure-v0.1`

The canonical gate is now:

`RF-E20_TETRA_CLOCK_MASS_SCALE_CLOSURE`

with authority paths:

- `closure/einstein/RF_E20_TETRA_CLOCK_MASS_SCALE_CLOSURE.md`
- `src/rfc/tetra_clock_mass_scale_closure.py`
- `tests/reference/test_rfe20_tetra_clock_mass_scale_closure.py`
- `validation/RF_E20_TETRA_CLOCK_MASS_SCALE_CLOSURE_V0_1.json`

The numbering keeps the already-promoted relativistic chain ordered as:

`RF-E18 ADM shift / velocity gauge firewall -> RF-E19 Noether-current material congruence -> RF-E20 tetra / phase-clock mass-scale closure`.

The historical physical-typing API names

- `physical_directional_phi`
- `physical_directional_energy_natural`

are preserved in the canonical RF-E20 implementation as exact aliases of the RF-E20 directional maps. This retains downstream compatibility while keeping one canonical gate number and one validation path.
