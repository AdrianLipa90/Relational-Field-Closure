# RGB-Moire color triplet quark-link coupling v0.3

Status: EXACT_DISCRETE_COLOR_MATTER_GAUGE_COVARIANCE / EXACT_ADJOINT_CURRENT / CONTINUUM_DIRAC_AND_RUNNING_OPEN

Date: 2026-09-26

## Scope

The v0.2 typed adapter reconstructs the full color \(\mathfrak{su}(3)_C\) algebra on the independent Stage-25 color triplet without identifying the existing neutrino-flavour AUX state with color.

This gate asks the next QCD-specific question: does the same reconstructed color algebra couple covariantly to a quark color triplet?

## Quark color carrier

Use

\[
q_i\in\mathbb C^3_C,
\qquad
G_i\in SU(3)_C,
\qquad
q_i\mapsto G_iq_i.
\]

For a holonomic color link

\[
W_{ij}:q_j\to q_i,
\qquad
W_{ij}\in SU(3)_C,
\]

use the existing v4.0 transformation

\[
W_{ij}\mapsto G_iW_{ij}G_j^\dagger.
\]

Then

\[
W_{ij}q_j\mapsto G_i(W_{ij}q_j),
\]

so transported quark color transforms covariantly.

The link bilinear

\[
\boxed{q_i^\dagger W_{ij}q_j}
\]

is exactly gauge invariant.

## Adjoint color current

With the Weyl-reconstructed generators \(T_a=\lambda_a/2\), define

\[
J_i^a=q_i^\dagger T_aq_i.
\]

Under \(q_i\mapsto G_iq_i\),

\[
J_i^a\mapsto R(G_i)^a{}_bJ_i^b,
\]

where

\[
R(G)^a{}_b=2\operatorname{Tr}(T_aGT_bG^\dagger).
\]

Thus the matter color current transforms in the same adjoint eight reconstructed in v0.2.

## Fundamental Casimir

The same generators satisfy

\[
\boxed{\sum_{a=1}^8T_aT_a=\frac43 I_3}.
\]

Therefore the reconstructed color triplet has the standard SU(3) fundamental Casimir

\[
C_F=\frac43.
\]

Together with v0.2 \(C_A=3\), the group invariants needed by perturbative QCD are present without inserting a separate generator basis.

## Family firewall

On the Stage-25 carrier

\[
V_Q=\mathbb C^3_C\otimes\mathbb C^2_L\otimes\mathbb C^3_F,
\]

color-link and family transformations remain on separate tensor factors and commute identically.

## Boundary

This closes a discrete holonomic matter-coupling theorem:

\[
\boxed{
\mathbf3_C
+W_{ij}\in SU(3)_C
\Rightarrow
\text{gauge-covariant quark transport}
+\text{adjoint color current}.
}
\]

It does not yet derive the continuum Dirac kinetic term, renormalized coupling, QCD beta function from project dynamics, confinement, or hadron spectrum.

Reference:
`tests/reference/test_aux_rgb_color_quark_link_coupling.py`.
