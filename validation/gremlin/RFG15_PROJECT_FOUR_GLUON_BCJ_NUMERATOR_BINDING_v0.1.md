# RFG15 — Project Four-Gluon BCJ Numerator Binding

Status: `PROJECT_A4_CUBICIZATION_PASS / MATCHED_COLOR_KINEMATICS_JACOBI_PASS / NO_GRAVITY_FIT / FOUR_POINT_SCOPE`

RFG15 consumes the actual RFG14 exchange-plus-contact amplitude. It does not import a target gravity amplitude and it does not choose numerators by fitting a desired double-copy output.

For each channel define the cubic-exchange kinematic numerator `X_i`, propagator denominator `D_i`, and the coefficient `K_i` multiplying the same color factor in the quartic contact term. The RFG14 amplitude can then be written

\[
\mathcal A_4
=g^2\sum_{i=s,t,u} c_i\left(\frac{X_i}{D_i}+K_i\right).
\]

Define the project numerators

\[
\boxed{n_i:=X_i+D_iK_i.}
\]

Then

\[
\boxed{\mathcal A_4=g^2\left(\frac{c_sn_s}{s}+\frac{c_tn_t}{t}+\frac{c_un_u}{u}\right).}
\]

With the channel orientation inherited from RFG14, the SU(3) color factors obey

\[
\boxed{c_s-c_t+c_u=0.}
\]

For on-shell transverse four-gluon external states with momentum conservation, the project numerators obey the matched identity

\[
\boxed{n_s-n_t+n_u=0.}
\]

The quartic contact is essential to this cubic representation. The exchange-only objects `X_s,X_t,X_u` do not generally satisfy the matched Jacobi relation; the distributed contact terms `D_i K_i` close the defect.

The reference gate verifies:

1. color Jacobi over all `8^4 = 4096` external SU(3) color assignments;
2. matched kinematic Jacobi over 500 deterministic random on-shell transverse states;
3. exact reconstruction of the full RFG14 amplitude from the cubicized numerators across multiple nonzero color sectors;
4. a witness where exchange-only Jacobi fails while the full project numerators close;
5. independence of the kinematic numerators from the chosen external color labels;
6. no gravity target or Newton coupling is used in numerator construction.

Local result:

```text
6 passed, 0 failed
```

The admitted four-point project chain is therefore

```text
holonomic SU(3) links
 -> normalized local A_mu^a
 -> cubic vertex + quartic contact
 -> gauge-invariant project A4
 -> project n_s,n_t,n_u
 -> matched color/kinematics Jacobi
```

The next gate is a double-copy amplitude built directly from these project numerators, with gravitational Ward tests performed independently in both kinematic copies.
