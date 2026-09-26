# RGB-Moire QCD dimensionless one-loop scale ratio v0.13

Status: EXACT_FIXED_NF_RG_INTEGRATION / RFG4D_ALPHA_C_CANDIDATE_ONLY / PHYSICAL_MU0_AND_THRESHOLD_BINDING_OPEN / NOT_LAMBDA_QCD_PROMOTION

Date: 2026-09-26

## Inputs

RFG4D provides the canonical information-normalization candidate

\[
\boxed{
\alpha_c^C
=
\ln\varphi-\kappa\ln2
=
0.474839619052230\ldots
}
\]

with project convention

\[
\boxed{\alpha_c=\frac1{g^2}}.
\]

This is not the conventional QCD notation \(\alpha_s=g^2/(4\pi)\).

v0.12 gives the one-loop coefficient

\[
b_0=11-\frac23n_f
\]

conditional on the declared matter term.

## Integrated fixed-flavour flow

From

\[
\mu\frac{dg}{d\mu}
=
-\frac{b_0}{16\pi^2}g^3
\]

it follows exactly that

\[
\boxed{
\frac1{g^2(\mu)}
=
\frac1{g^2(\mu_0)}
+
\frac{b_0}{8\pi^2}
\ln\frac{\mu}{\mu_0}.
}
\]

Using the project coordinate \(\alpha_c=1/g^2\),

\[
\boxed{
\alpha_c(\mu)
=
\alpha_c(\mu_0)
+
\frac{b_0}{8\pi^2}
\ln\frac{\mu}{\mu_0}.
}
\]

Define the formal one-loop strong scale on a fixed-\(n_f\) branch by the zero of the inverse coupling:

\[
\alpha_c(\Lambda)=0.
\]

Then

\[
\boxed{
\frac{\Lambda}{\mu_0}
=
\exp\left[
-\frac{8\pi^2\alpha_c(\mu_0)}{b_0}
\right].
}
\]

## Canonical-candidate ratios

If the RFG4D canonical coordinate is provisionally used as the boundary value, then for \(n_f=6\),

\[
\boxed{
\frac{\Lambda_{(n_f=6)}}{\mu_0}
=
0.004719859618240724\ldots
}
\]

and for pure SU(3) Yang-Mills,

\[
\boxed{
\frac{\Lambda_{YM}}{\mu_0}
=
0.03309581284558998\ldots
}
\]

at one loop.

These are dimensionless consequences only.

## Firewall

Neither number is promoted to physical \(\Lambda_{\rm QCD}\).

That promotion still requires:

1. physical selection of the boundary coupling;
2. identification of the boundary scale \(\mu_0\);
3. renormalization scheme;
4. quark threshold matching and changing active \(n_f\);
5. higher-loop corrections or a nonperturbative running prescription.

The result therefore narrows the remaining problem: once a source-owned \((\mu_0,\alpha_c(\mu_0))\) pair and threshold ledger are supplied, the one-loop scale ratio is no longer ambiguous.

Reference:
\`tests/reference/test_aux_rgb_qcd_dimensionless_rg_ratio.py\`.
