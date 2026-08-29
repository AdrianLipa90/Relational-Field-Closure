# RFC Canonical Formalization Index

Status: `FOUNDATIONAL_SPINE_AUTHORITY / DERIVATION_GATES_PRESERVED`

The RFC formalism is organized into three complementary layers.

## 1. Foundational spine

```text
RF-F0  Primitive typed state
RF-F1  Connection-sign bridge + gauge-dressed lifted relational phase
RF-F2  Euler/Berry + Euler-root closure
RF-F3  Gauge-covariant phase rate + relational phase cell
RF-F4  Occupation + conserved four-current
RF-F5  Relational phase-energy one-form
RF-F6  Covariant relational source theorem
RF-F7  Stress-energy + Bianchi/dynamic-Lambda balance
RF-F8  Phase-cell continuity + equation-of-state theorem
RF-F9  Noether/Hamiltonian + Einstein/ADM global closure
```

Canonical document:

`formalism/RF_F0_F9_FOUNDATIONAL_FORMALIZATION_SPINE.md`

The F-series provides the compact theorem-level statement of the system.

## 2. Derivation gates

The existing detailed gate families remain the derivation authority:

```text
RF-01...       state-space/QGT/Berry geometry
RF-N1...       lapse/source/current/phase-energy derivations
RF-L...        dynamic Lambda0 and Temporal-Wave closure
RF-E...        Lorentzian action, stress-energy, ADM and Bianchi closure
RF-S13-S22     relational generator, source geometry, current, tensor and profile closure
RFG...         double-copy / coupling-normalization program
```

The F-series crosslinks these results without replacing their proofs or validation receipts.

## 3. Central canonical equations

Gauge-dressed lifted relational phase:

\[
\boxed{
\Phi_C
=\widetilde\vartheta(x)-\widetilde\vartheta(x_0)
+\int_C\mathcal A_-.
}
\]

Gauge-covariant phase rate:

\[
\boxed{\omega=u^\mu\mathscr D_\mu\vartheta.}
\]

Relational phase-cell volume:

\[
\boxed{V_R=a_{FS}c^3/|\omega|^3.}
\]

Energy per occupation:

\[
\boxed{\epsilon_G=B\omega(\Phi_C+\kappa).}
\]

Covariant source:

\[
\boxed{
\rho_G
=B(\Phi_C+\kappa)J^\mu\mathscr D_\mu\vartheta
=n\epsilon_G.
}
\]

Dust tensor branch:

\[
\boxed{
T_{\mu\nu}=\epsilon_G\frac{J_\mu J_\nu}{n}.
}
\]

Einstein closure:

\[
\boxed{
G_{\mu\nu}+\Lambda_0g_{\mu\nu}=\kappa_ET_{\mu\nu}.
}
\]

Comoving phase-cell equation-of-state theorem:

\[
\boxed{
 w_G
=\frac13\frac{d\ln|\epsilon_G|}{d\ln|\omega|}
=\frac13\left[
1+\frac{d\ln|B(\Phi_C+\kappa)|}{d\ln|\omega|}
\right]
}
\]

on the separately conserved perfect-fluid branch specified by RF-F8.

## 4. Validation authority

Executable formalization:

`src/rfc/foundational_phase_source_formalism.py`

Reference suite:

`tests/reference/test_rff_foundational_phase_source_formalism.py`

Validation ledger:

`validation/RF_F0_F9_FOUNDATIONAL_FORMALIZATION_V0_1.json`
