# QHTRI ToE Solver Candidate v0.1

Status: `CANDIDATE_ONLY`

This branch preserves the executable local geometry/source-closure candidate developed through the live NOEMA/PhaseNav/GREMLIN workflow. Promotion remains a separate decision.

## Executable scope

- RF-E8 ADM carrier: `(N_R, h_ij, b^i) -> g_mn`.
- Metric callable -> centered metric jet -> `G_mn`.
- RF-N0/RF-02H local metric candidate.
- QHTRI-neutrino stress/source binding candidate.
- GSC3A/GSC4B local shift-route conformance with conditional flow-adapted zero-shift route.
- Constrained local Einstein closure `G_mn + Lambda g_mn - kappa_E T_mn`.
- Multisector positive source-cone solver including massless pairs and RF-E7 amplitude-gradient stress.

## Fresh recovery revalidation

The original `/dev/shm` scratch workspace was lost during a runtime reset. Recoverable files were reconstructed from executed-command history and then rerun from scratch. `recovery_revalidation_v1.json` reports `PASS` and reproduces the archived key residuals, including:

- radiation-FLRW closure: `5.551115123125783e-17`;
- anisotropic Bianchi-I massless-only constrained residual: `0.007886680391421472`;
- massless + RF-E7 scalar residual: `0.004634958555339089`;
- residual reduction: `0.41230551698523976`;
- synthetic RF-E7 BVLS control: `8.326672684688674e-17`.

The historical V1 multisector numerical-control failure is retained alongside the repaired V2 PASS receipt.

## Open production inputs

The current ledger keeps these inputs explicit: production `N_R(x)`, production `h_ij(x)` / triad field, product-trivialization or proper-global-clock witness, physical event placement, GSC1/A5 coverage packet, and global domain coverage for E26. The physical QHTRI hardware witness remains a separate experiment.

## Recovery boundary

The pre-reset runtime inventory contained 24 files. Eighteen original-inventory files are archived here after command-history recovery and fresh revalidation. Six exploratory global-control/coverage files are inventory-confirmed but their exact source bytes have not yet been recovered; they are listed in `RECOVERY_MANIFEST.json` and are intentionally not replaced with placeholders.

Base `main`: `85bbb1d0754605be2720b6bd258b486b0a072345`.
