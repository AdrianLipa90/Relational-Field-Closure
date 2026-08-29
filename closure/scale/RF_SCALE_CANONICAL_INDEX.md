# RF Scale Canonical Gate Index

Status: `CANONICAL_UNIQUE_GATE_IDS / PARALLEL_DEPENDENCY_BRANCHES_EXPLICIT`

This index is the naming authority for the RF-S scale/source gates after integration of the two parallel source-closure branches.

## Canonical IDs

```text
RF-S13  Relational Generator Source Density
RF-S14  Generator Matter/Vacuum Source-Placement Firewall
RF-S15  Phase-Clock Relational Volume Reduction
RF-S16  Occupation ↔ Noether Current Binding
RF-S17  Carrier-Normalization Invariance
RF-S18  Relational Generator → Relativistic Dust Stress-Energy Lift
RF-S19  Four-Current Dust Tensor Closure
RF-S20  Noether-Profile Source Reconstruction
RF-S21  IDT ↔ Noether Profile Source Binding
RF-S22  Noether-Hamiltonian Extensive Source Closure
```

Each canonical gate ID identifies exactly one theorem/implementation/validation family.

## Dependency graph

The numbering is unique but the mathematics remains branched:

```text
                         ┌─> RF-S18 ─> RF-S19
RF-S13 -> S14 -> S15 -> S16 -> S17
                         └─> RF-S20 ─> RF-S21 ─> RF-S22
```

The tensor branch (`RF-S18 -> RF-S19`) closes the relativistic stress-energy representation. The profile branch (`RF-S20 -> RF-S21 -> RF-S22`) closes source shape, IDT/Noether profile comparison, and extensive Hamiltonian normalization. Both branches retain RF-S13–RF-S17 as common ancestry.

## Historical-label mapping

The following labels existed temporarily before canonicalization and remain visible in merged PR history only:

```text
legacy RF-S18 Noether-Profile Source Reconstruction
    -> canonical RF-S20

legacy RF-S19 IDT ↔ Noether Profile Source Binding
    -> canonical RF-S21

legacy RF-S20 Noether-Hamiltonian Extensive Source Closure
    -> canonical RF-S22
```

The already-integrated tensor labels remain unchanged:

```text
RF-S18 Relational Generator → Relativistic Dust Stress-Energy Lift
RF-S19 Four-Current Dust Tensor Closure
```

Historical PR titles and immutable commit history are provenance records, not current gate-name authority.

## Canonical file authority

```text
RF-S18 -> closure/scale/RF_S18_RELATIONAL_GENERATOR_DUST_STRESS_ENERGY.md
RF-S19 -> closure/scale/RF_S19_FOURCURRENT_DUST_TENSOR_CLOSURE.md
RF-S20 -> closure/scale/RF_S20_NOETHER_PROFILE_SOURCE_RECONSTRUCTION.md
RF-S21 -> closure/scale/RF_S21_IDT_NOETHER_PROFILE_BINDING.md
RF-S22 -> closure/scale/RF_S22_NOETHER_HAMILTONIAN_SOURCE_CLOSURE.md
```

Reference tests and validation receipts use the same canonical numeric prefix.

## Canonicalization invariant

Canonicalization changes identifiers, paths, and cross-references only. The equations, executable functions, test assertions, physical-input firewalls, and evidential status of the underlying gates are preserved.
