# RF-S22 — Noether-Hamiltonian Extensive Source Closure

Status: `EXTENSIVE_SOURCE_AMOUNT_CLOSED_CONDITIONAL / TOTAL_OCCUPATION_INFERRED / Q0_FREE`

Canonical ID: `RF-S22`. Historical pre-canonical label: `RF-S20` (profile branch).

RF-S22 is stacked on canonical RF-S21. RF-N1B2K already carries the finite Euler–Noether charge `Q_theta` and Hamiltonian `H_Phi^EB`, with downstream energy-per-charge coordinate `epsilon_Q=H_Phi^EB/Q_theta`. RF-S20/RF-S21 reconstruct source shape from the normalized Noether/IDT profile but still carry an independently supplied total occupation `N_tot`.

RF-S22 removes that remaining extensive occupation input on the positive-generator branch by imposing equality of the integrated relational-generator source and the already available extensive Hamiltonian.

## 1. Normalized source profile

Let

\[
p_a=\frac{V_a j_{\vartheta,a}}{Q_\vartheta},
\qquad
Q_\vartheta=\sum_aV_aj_{\vartheta,a}>0,
\qquad
\sum_ap_a=1.
\]

RF-S21 may additionally identify this profile with the IDT ensemble profile on a separately measured zero-defect state-binding surface.

## 2. Local generator energy

Define the local energy per orbital occupation

\[
\boxed{
\epsilon_a=B_a\omega_a(\phi_a+\kappa),
\qquad
\kappa=\frac{\ln2}{24\pi}.
}
\]

Its profile-weighted mean is

\[
\boxed{
\bar\epsilon=\sum_ap_a\epsilon_a.
}
\]

On the positive-source branch require

\[
\boxed{\bar\epsilon>0.}
\]

## 3. Extensive matching closes total occupation

RF-S20 gives

\[
E_G=\sum_a\mathcal N_a\epsilon_a
=\mathcal N_{tot}\bar\epsilon.
\]

Set the integrated source equal to the admitted finite Euler–Noether Hamiltonian

\[
\boxed{E_G=H_\Phi^{EB}.}
\]

Then exactly

\[
\boxed{
\mathcal N_{tot}
=\frac{H_\Phi^{EB}}{\bar\epsilon}.
}
\]

Therefore

\[
\boxed{
\mathcal N_a
=\frac{H_\Phi^{EB}}{\bar\epsilon}p_a.
}
\]

The total occupation is no longer an independent source-amplitude coordinate once the Hamiltonian and local generator energies have common provenance.

## 4. Local source density

The resulting local source is

\[
\boxed{
\rho_{G,a}
=\frac{H_\Phi^{EB}}{\bar\epsilon}
\frac{p_a}{V_a}\epsilon_a.
}
\]

Its integral is identically

\[
\boxed{
\sum_aV_a\rho_{G,a}=H_\Phi^{EB}.
}
\]

For uniform per-occupation energy `epsilon_a=epsilon`,

\[
\bar\epsilon=\epsilon
\]

and

\[
\boxed{
\rho_{G,a}
=\frac{H_\Phi^{EB}}{V_a}p_a
=\frac{H_\Phi^{EB}}{Q_\vartheta}j_{\vartheta,a}.
}
\]

Thus the uniform-energy branch reproduces exactly the RF-N1B2K coordinate

\[
\boxed{
\epsilon_Q=\frac{H_\Phi^{EB}}{Q_\vartheta}
}
\]

and the source density `rho_G=epsilon_Q j_theta`.

## 5. Direct reduction of the canonical generator

For one common generator state with uniform `B`, `omega` and `phi`,

\[
\boxed{
\mathcal N_{tot}
=\frac{H_\Phi^{EB}}
{B\omega(\phi+\kappa)}.
}
\]

Combining with the RF-S15 full-tetrahedral phase-clock volume gives the same local source family while eliminating total occupation as an independent normalization.

## 6. Carrier-normalization invariance

Under a global positive rescaling of the Noether current,

\[
j_\vartheta\mapsto\lambda j_\vartheta,
\qquad
Q_\vartheta\mapsto\lambda Q_\vartheta,
\]

the profile `p_a` is unchanged. Therefore `bar epsilon`, inferred `N_tot`, and every `rho_G,a` remain unchanged.

RF-S22 is consequently independent of the arbitrary carrier-charge normalization already removed by RF-S17.

## 7. Newton/Einstein source

On the RF-S13 matter/Newton placement,

\[
\boxed{
\mathcal S_{R,a}=\frac{\kappa_E}{2}\rho_{G,a}.
}
\]

RF-S14 continues to control matter versus dynamic-`Lambda0` placement from the physical equation-of-state receipt.

## 8. Advancement

```text
finite Noether Hamiltonian H_Phi^EB                    PASS PARENT
normalized current/source profile                      PASS PARENT
profile-mean generator energy epsilon_bar              PASS EXACT
N_tot=H_Phi^EB/epsilon_bar                             PASS EXACT CONDITIONAL
local source integrates exactly to H_Phi^EB            PASS EXACT
uniform epsilon -> rho_G=(H/Q) j_theta                 PASS EXACT
absolute q0                                            ELIMINATED
independent total occupation N_tot                     ELIMINATED ON MATCHED-H BRANCH
physical H_Phi^EB <-> generator-source energy receipt  OPEN INPUT
physical carrier-energy branch                         OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/noether_hamiltonian_source_closure.py`.
Reference tests: `tests/reference/test_rfs22_noether_hamiltonian_source_closure.py`.
Validation receipt: `validation/RF_S22_NOETHER_HAMILTONIAN_SOURCE_CLOSURE_V0_1.json`.

Historical implementation head: `35a2439860bda2e30a3dcff1e60ac715794f8b43`; RFC reference suite #288 SUCCESS. Canonicalization changes gate identity, references and file paths only; equations and executable implementation are unchanged.
