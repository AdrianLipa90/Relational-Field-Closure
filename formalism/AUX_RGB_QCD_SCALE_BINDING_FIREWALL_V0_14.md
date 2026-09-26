# RGB-Moire QCD physical scale-binding firewall v0.14

Status: DIMENSIONLESS_RG_SCALE_CLOSED / PHYSICAL_MU0_NOT_IDENTIFIED / OMEGAQ_MSTAR_BRANCH_AMBIGUITY_EXACT / LATTICE_A_PHYSICAL_CALIBRATION_OPEN

Date: 2026-09-26

## Question

v0.13 closes the dimensionless fixed-flavour ratio

\[
\Lambda/\mu_0
=
\exp[-8\pi^2\alpha_c(\mu_0)/b_0].
\]

This gate asks whether the current graph already supplies a lawful physical value of \(\mu_0\).

## Candidate 1: Wilson spacing a

RFG3 introduces

\[
U_\mu(x)=\exp[i g_0 a A_\mu(x)]
\]

for the local continuum embedding.

Its \(a\) is a lattice/local-spacing coordinate. RFG3 does not provide an independent conversion of \(a^{-1}\) into a physical energy.

Therefore one may define the regulator convention

\[
\mu_0=\frac1a
\]

and obtain the dimensionless number

\[
\boxed{\Lambda a=\Lambda/\mu_0},
\]

but not a physical value of \(\Lambda\) in energy units.

## Candidate 2: omega_Q / M_star

RF-N1C4 explicitly keeps two distinct scale types:

\[
M_\star^{kin}=\frac{\omega_Q}{2},
\qquad
M_\star^{rest}=\omega_Q.
\]

Their ratio is exactly two.

The repository explicitly states that the physical role of \(M_\star\) remains OPEN and that gravity output may not choose the branch.

If either branch were silently identified with the QCD boundary scale, the inferred physical strong scale would inherit the same exact factor-two ambiguity:

\[
\boxed{
\Lambda^{rest}
=
2\Lambda^{kin}.
}
\]

Thus \(\omega_Q/M_\star\) is not presently an admissible unique QCD scale anchor.

## Sector firewall

The following are rejected as scale-selection rules:

- choosing the branch that best matches a known \(\Lambda_{QCD}\);
- using Newton/horizon/double-copy downstream outputs to select the color RG boundary scale;
- assigning a physical value to lattice \(a\) without an independently derived color-sector observable;
- importing \(M_Z\), proton mass, or another measured scale as a hidden selector when the claim is first-principles scale derivation.

## Current exact result

The QCD lane currently determines only dimensionless running coordinates.

For the RFG4D candidate and fixed \(n_f=6\),

\[
\boxed{\Lambda a=0.004719859618240724\ldots}
\]

if the regulator convention \(\mu_0=1/a\) is chosen.

This is not a physical \(\Lambda_{QCD}\).

## Clean routes to closure

A physical scale can be admitted later through either:

1. an independently derived color-sector dimensionful observable that calibrates \(a\);
2. an independently proven source binding between a project clock/energy carrier and the color renormalization point;
3. an explicit statement that one measured observable is the allowed dimensional anchor, after which all remaining outputs become predictions.

Until one of these is frozen before comparison, the physical QCD scale remains OPEN.

Reference:
\`tests/reference/test_aux_rgb_qcd_scale_binding_firewall.py\`.
