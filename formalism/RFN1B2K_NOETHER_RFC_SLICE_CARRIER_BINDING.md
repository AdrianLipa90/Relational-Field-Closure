# RF-N1B2K — Noether ↔ RFC Slice-Carrier Binding Gate

Status: `EXACT_DEFECT_THEOREM_PASS / COMMON_SLICE_BINDING_CONDITIONAL / PHYSICAL_CURRENT_IDENTITY_OPEN`

RF-N1B2K consumes IDT 01AA and tests whether the RFC extensive carrier

\[
Q_\Sigma=\int_{\Sigma_t}j_Q\,dV_h
\]

is the same finite conserved carrier as the Euler–Noether phase charge

\[
Q_\vartheta=\int_{\Sigma_t}n_\mu J_\vartheta^\mu\,dV_h.
\]

The gate is downstream of RF-N1B2J and upstream of source-density promotion.

## 1. Common cell/slice contract

Choose one indexed partition

\[
\Sigma=\bigcup_{a=1}^N C_a
\]

with the same normal orientation on both representations. Let

\[
j_{\vartheta,a},\quad V_a^{(\vartheta)}>0
\]

be the Noether slice density and measure, and

\[
j_{Q,a},\quad V_a^{(Q)}>0
\]

be the RFC carrier density and measure.

Then

\[
\boxed{
Q_\vartheta=\sum_a V_a^{(\vartheta)}j_{\vartheta,a},
\qquad
Q_\Sigma=\sum_a V_a^{(Q)}j_{Q,a}.
}
\]

The reference carrier sector requires

\[
Q_\vartheta>0.
\]

## 2. Measured binding defects

Define

\[
\boxed{
\Delta_J
=
\frac{\sum_aV_a^{(Q)}|j_{Q,a}-j_{\vartheta,a}|}{Q_\vartheta}
}
\]

for local current mismatch,

\[
\boxed{
\Delta_V
=
\frac{\sum_a|V_a^{(Q)}-V_a^{(\vartheta)}|\,|j_{\vartheta,a}|}{Q_\vartheta}
}
\]

for measure mismatch, and

\[
\boxed{
\Delta_\Sigma
=
\frac{|Q_\Sigma-Q_\vartheta|}{Q_\vartheta}
}
\]

for the integrated extensive-carrier mismatch.

## 3. Exact bound

Using

\[
V_a^{(Q)}j_{Q,a}-V_a^{(\vartheta)}j_{\vartheta,a}
=
V_a^{(Q)}(j_{Q,a}-j_{\vartheta,a})
+(V_a^{(Q)}-V_a^{(\vartheta)})j_{\vartheta,a},
\]

the triangle inequality gives the exact finite-cell theorem

\[
\boxed{
\Delta_\Sigma\le\Delta_J+\Delta_V.
}
\]

Therefore exact local current and measure binding,

\[
\Delta_J=0,
\qquad
\Delta_V=0,
\]

implies

\[
\boxed{Q_\Sigma=Q_\vartheta.}
\]

This is the conditional carrier-identity closure needed by RF-N1B2J.

## 4. Integrated equality does not close the local gate

A vanishing extensive defect can occur through cancellation of local current errors. Hence

\[
\boxed{
\Delta_\Sigma=0
\not\Rightarrow
\Delta_J=0.
}
\]

RF-N1B2K therefore does not promote a current identity from total-charge equality alone.

## 5. Normalized carrier profile

On positive sectors,

\[
p_{\vartheta,a}
=\frac{V_a^{(\vartheta)}j_{\vartheta,a}}{Q_\vartheta},
\qquad
p_{Q,a}
=\frac{V_a^{(Q)}j_{Q,a}}{Q_\Sigma}.
\]

Under exact local current/measure binding,

\[
\boxed{p_{Q,a}=p_{\vartheta,a}.}
\]

Thus the same gate that closes the extensive carrier also supplies the phase-current normalized profile needed by the later IDT shape cross-binding.

## 6. Consequence for epsilon_Q and source mass

RF-N1B2J supplies

\[
\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{Q_\vartheta^{EB}}.
\]

Once the current/measure gate admits

\[
Q_\Sigma=Q_\vartheta^{EB},
\]

the RFC continuous conversion becomes

\[
\boxed{
\epsilon_Q=\epsilon_N^{EB}
}
\]

on that bound carrier sector, and

\[
\boxed{
M_Q
=\frac{\epsilon_QQ_\Sigma}{c^2}
=\frac{H_\Phi^{EB}}{c^2}.
}
\]

The local mass-density candidate is then

\[
\rho_Q(x)
=\frac{\epsilon_N^{EB}}{c^2}j_\vartheta(x)
\]

once the same local current representation is admitted.

## 7. Persistence across slices

The binding is evaluated on one pinned slice. Persistence to another slice additionally requires conserved currents and the same side-boundary convention:

\[
\nabla_\mu J_Q^\mu=0,
\qquad
\nabla_\mu J_\vartheta^\mu=0,
\]

with vanishing side flux, periodic boundary conditions, or sufficient decay.

## 8. Gate state

```text
same cell IDs / partition                  REQUIRED
same slice normal orientation              REQUIRED
positive cell measures                     REQUIRED
Q_theta > 0                                REQUIRED
Delta_J                                    MEASURED
Delta_V                                    MEASURED
Delta_Sigma                                MEASURED
Delta_Sigma <= Delta_J + Delta_V           PASS EXACT
Delta_J=Delta_V=0 -> Q_Sigma=Q_theta       PASS CONDITIONAL
Q_Sigma=Q_theta alone -> local identity     INSUFFICIENT
physical J_Q^mu <-> J_theta^mu             OPEN measured binding
cross-slice persistence                    BOUNDARY-CONDITIONED
```

## 9. Advancement

```text
RF-N1B2J finite Noether carrier                   PASS_CONDITIONAL
Noether/RFC cell-charge construction              PASS
current/measure defect decomposition              PASS EXACT
integrated carrier defect bound                   PASS EXACT
Q_Sigma <-> Q_theta physical carrier identity    OPEN measured binding
epsilon_Q <-> epsilon_N^EB after carrier gate    PASS CONDITIONAL
p_Q <-> p_theta after local binding               PASS CONDITIONAL
p_IDT <-> p_theta physical state-space binding   OPEN
RF-N1C coupling/universality                      OPEN
```

The next PNCS executable edge is the closed Noether ↔ RFC slice-carrier loop carrying `Delta_J`, `Delta_V`, `Delta_Sigma`, and inverse lineage.
