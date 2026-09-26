# AUX RGB / QCD typed-provenance erratum v0.1

Date: 2026-09-26

Status: ERRATUM / TYPE_CORRECTION / PRIOR_NUMERICAL_RESULTS_PRESERVED

## Error identified

The earlier candidate receipt
`AUX_RGB_TETRA_TRIPLET_C3_INTERTWINER_V0_1`
contains the statement

`aux_is_generic_three_channel_carrier = true`.

That statement is too broad and conflicts with RF-M2.

RF-M2 explicitly types current AUX RGB as an implementation alias for the three neutrino-flavour AUX channels and defines the full bipolar AUX state space as

\[
\mathcal H_{\nu,AUX}
=\mathbb C^2_{\nu_e}\otimes
 \mathbb C^2_{\nu_\mu}\otimes
 \mathbb C^2_{\nu_\tau},
\qquad \dim=8.
\]

The independent color carrier is instead

\[
\mathcal H_C\cong\mathbb C^3_C.
\]

Therefore the full AUX state is not the color triplet and is not a generic \(\mathbb C^3\) carrier.

## Corrected statement

What is reusable across sectors is the abstract three-channel root-of-unity / C3 phase template

\[
(1,\omega,\omega^2),\qquad \omega=e^{2\pi i/3},
\]

together with its cyclic shift representation.

A separately typed copy of that template may act on the independent color carrier \(\mathbb C^3_C\). The v0.2 adapter formalizes exactly this copy without identifying the neutrino-flavour AUX Hilbert space with color.

Thus the corrected chain is

\[
\text{RF-M2 AUX flavour state}
\neq
\text{color triplet},
\]

while

\[
\text{abstract RGB/C3 phase template}
\xrightarrow{\text{typed color copy}}
\mathbb C^3_C
\to
\mathfrak{su}(3)_C
\]

is valid.

## Preservation

The earlier numerical C3 intertwiner, Weyl closure, Gell-Mann reconstruction and structure-tensor results are not invalidated. Their interpretation is narrowed from a direct full-AUX identification to a typed phase-template representation bridge.

Authoritative continuation:

- `AUX_RGB_TEMPLATE_COLOR_SU3_ADAPTER_V0_2`
- `AUX_RGB_COLOR_QUARK_LINK_COUPLING_V0_3`
- `AUX_RGB_QCD_RUNNING_INVARIANTS_V0_4`
