# RFC Canonical Formalization Index

Status: `FOUNDATIONAL_AND_DYNAMICAL_SPINE_AUTHORITY / DERIVATION_GATES_PRESERVED`

The RFC formalism is organized into three complementary layers.

## 1. Foundational and dynamical spine

```text
RF-F0   Primitive typed state
RF-F1   Connection-sign bridge + gauge-dressed lifted relational phase
RF-F2   Euler/Berry + Euler-root closure
RF-F3   Gauge-covariant phase rate + relational phase cell
RF-F4   Occupation + conserved four-current
RF-F5   Relational phase-energy one-form
RF-F6   Covariant relational source theorem
RF-F7   Stress-energy + Bianchi/dynamic-Lambda balance
RF-F8   Phase-cell continuity + equation-of-state theorem
RF-F9   Noether/Hamiltonian + Einstein/ADM global closure
RF-F10  Phase-energy curvature + boundary-flux theorem
RF-F11  Comoving phase-energy transport + integrated constant-w family
RF-F12  Homogeneous-isotropic phase-clock / FLRW scaling limit
```

Canonical documents:

`formalism/RF_F0_F9_FOUNDATIONAL_FORMALIZATION_SPINE.md`

`formalism/RF_F10_F12_DYNAMICAL_PHASE_TRANSPORT.md`

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

The F-series crosslinks these results while preserving their proofs and validation receipts.

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

Phase-energy curvature:

\[
\boxed{
\mathcal K_G=d\Theta_G
=(\Phi_C+\kappa)dB\wedge\mathscr D\vartheta
+B(\Phi_C+\kappa)\mathcal F_-.
}
\]

Comoving phase-energy transport:

\[
\boxed{
(\Phi_C+\kappa)(\dot B\,\omega+B\dot\omega)
+B\omega^2
=-\frac{\dot\Lambda_0}{\kappa_E n}.
}
\]

Homogeneous-isotropic phase-clock invariant:

\[
\boxed{a|\omega|=\mathrm{const}},
\qquad
\boxed{\rho_G\propto a^{-3(1+w_G)}}.
\]

## 4. Validation authority

Foundational executable formalization:

`src/rfc/foundational_phase_source_formalism.py`

Foundational reference suite:

`tests/reference/test_rff_foundational_phase_source_formalism.py`

Foundational validation ledger:

`validation/RF_F0_F9_FOUNDATIONAL_FORMALIZATION_V0_1.json`

Dynamical executable formalization:

`src/rfc/dynamical_phase_transport.py`

Dynamical reference suite:

`tests/reference/test_rff10_f12_dynamical_phase_transport.py`

Dynamical validation ledger:

`validation/RF_F10_F12_DYNAMICAL_PHASE_TRANSPORT_V0_1.json`
