# RF-S19 — IDT ↔ Noether Profile Source Binding

Status: `EXACT_PROFILE_DEFECT / ZERO_DEFECT_SOURCE_EQUIVALENCE / PHYSICAL_STATE_BINDING_OPEN`

RF-S19 is stacked on exact-green RF-S18. RF-S18 reconstructs the local relational-generator source from the normalized Noether-current profile plus total occupation. IDT independently supplies a normalized finite ensemble profile `p_a`. RF-S19 places those two normalized state descriptions on one explicit comparison surface.

## 1. Two normalized profiles

Let

\[
\boxed{p_a^{IDT}\ge0,\qquad \sum_a p_a^{IDT}=1}
\]

be the IDT ensemble profile on an ordered finite cell ledger.

For the same ordered cells and physical measure, RF-N1B2K/RF-S18 supplies

\[
\boxed{
p_a^{\vartheta}=\frac{V_a j_{\vartheta,a}}{Q_\vartheta},
\qquad
Q_\vartheta=\sum_aV_aj_{\vartheta,a}>0,
}
\]

with

\[
\sum_ap_a^{\vartheta}=1.
\]

## 2. Exact binding defects

Define the squared Hellinger defect

\[
\boxed{
H^2(p^{IDT},p^\vartheta)
=1-\sum_a\sqrt{p_a^{IDT}p_a^\vartheta}.
}
\]

For normalized nonnegative finite profiles,

\[
\boxed{0\le H^2\le1}
\]

and

\[
\boxed{H^2=0\iff p^{IDT}=p^\vartheta.}
\]

RF-S19 also records

\[
\boxed{
D_1=\sum_a|p_a^{IDT}-p_a^\vartheta|
}
\]

and

\[
\boxed{
D_\infty=\max_a|p_a^{IDT}-p_a^\vartheta|.
}
\]

The executable zero-defect rule uses an explicitly supplied finite-precision tolerance on `D_infinity`.

## 3. Source equivalence on the zero-defect surface

RF-S18 gives, from the Noether profile,

\[
\mathcal N_a
=\mathcal N_{tot}p_a^\vartheta.
\]

If RF-S19 closes with

\[
\boxed{p_a^{IDT}=p_a^\vartheta,}
\]

then exactly

\[
\boxed{
\mathcal N_a
=\mathcal N_{tot}p_a^{IDT}.
}
\]

Therefore the local source becomes

\[
\boxed{
\rho_{G,a}
=\frac{\mathcal N_{tot}p_a^{IDT}}{V_a}
B_a\omega_a(\phi_a+\kappa),
\qquad
\kappa=\frac{\ln2}{24\pi}.
}
\]

This is identical to the RF-S18 Noether reconstruction on the zero-defect profile-binding surface.

## 4. Current-normalization invariance

A global positive rescaling

\[
j_{\vartheta,a}\mapsto\lambda j_{\vartheta,a}
\]

rescales `Q_theta` by the same factor and leaves `p_theta` unchanged. Consequently

\[
\boxed{
H^2,D_1,D_\infty
}
\]

are all invariant under the RF-S17 carrier/current normalization freedom.

Thus the IDT↔Noether comparison is performed entirely on normalization-independent state shapes.

## 5. Source mismatch control

Let the magnitude of every local per-occupation energy satisfy

\[
|\epsilon_a|\le E_{max},
\qquad
\epsilon_a=B_a\omega_a(\phi_a+\kappa).
\]

Then the integrated source-energy difference between an IDT-profile reconstruction and a Noether-profile reconstruction obeys

\[
\boxed{
|\Delta E_G|
\le
\mathcal N_{tot}E_{max}D_1.
}
\]

Hence the profile-binding defect has a direct source-level error bound rather than serving only as an abstract state-space metric.

## 6. Zero-support robustness

The Hellinger defect remains finite when one or more cell probabilities vanish. This avoids introducing a KL singularity solely for the cross-profile equality test. IDT's own relative-information/KL dynamics remain independently preserved in their existing gates.

## 7. Source chain after RF-S19

On a physical zero-defect receipt the source chain is

\[
\boxed{
 p^{IDT}
 =p^\vartheta
 \to
 \mathcal N_a=\mathcal N_{tot}p_a
 \to
 \rho_{G,a}
 \to
 \mathcal S_{R,a}=\frac{\kappa_E}{2}\rho_{G,a}
 \to
 T_{\mu\nu}
 \to
 G_{\mu\nu}.
}
\]

RF-S14 separately controls whether a given source contribution stays in displayed matter or is represented on the dynamic-`Lambda0` side.

## 8. Advancement

```text
IDT normalized finite profile                                PASS PARENT TYPE
Noether normalized finite profile                            PASS PARENT TYPE
Hellinger/L1/Linf defects                                    PASS EXACT
zero defect iff normalized profiles agree                    PASS EXACT
profile defects invariant under current normalization        PASS EXACT
zero-defect IDT source = RF-S18 Noether source               PASS EXACT
source-energy mismatch bounded by N_tot Emax D1              PASS EXACT
physical IDT <-> Noether state-space identity                OPEN RECEIPT
common ordered cell/support/measure identity                 OPEN PHYSICAL INPUT
physical total occupation N_tot                              OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/idt_noether_profile_binding.py`.
Reference tests: `tests/reference/test_rfs19_idt_noether_profile_binding.py`.
Validation receipt: `validation/RF_S19_IDT_NOETHER_PROFILE_BINDING_V0_1.json`.

Stack parent: RF-S18 exact-green head `f52a90a8d6c24cb4dde0cde742f2c58c34a73193`, RFC reference suite #286 SUCCESS.
