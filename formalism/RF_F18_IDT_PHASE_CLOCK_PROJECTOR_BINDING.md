# RF-F18 — IDT Gauge-Covariant Phase-Clock Projector Binding

Status: `IDT_01AC_ONE_FORM_REUSE_PASS / IDT_01AD_CLOCK_RATE_PARENT_PASS / INDEPENDENT_PHASE_SCALE_FIREWALL_EXACT / METRIC_RESPONSE_LEDGER_EXACT / RF_E19_ALIGNMENT_GATE_DEFINED / PHYSICAL_PROJECTOR_PROMOTION_CONDITIONAL`

RF-F18 is stacked on RF-F17. Its purpose is to realize the RF-F17 projector from an already-existing IDT phase-clock field while keeping every additional physical binding explicit.

## 1. Existing IDT phase-clock one-form

IDT 01AC supplies the gauge-invariant one-form

\[
\boxed{
q_\mu:=\mathscr D_\mu\vartheta
=\partial_\mu\vartheta+\mathcal A^{ABE}_\mu.
}
\]

Under

\[
\vartheta\mapsto\vartheta+\lambda,
\qquad
\mathcal A^{ABE}\mapsto\mathcal A^{ABE}-d\lambda,
\]

one has exactly

\[
\boxed{q_\mu\mapsto q_\mu.}
\]

IDT 01AD binds the normal pullback of the same one-form to the relational-lapse proper-time phase rate,

\[
\boxed{
D_{\hat\tau}\chi
=r_n^{(\tau)}
=c\,e_{\hat0}\lrcorner\mathscr D\vartheta.
}
\]

Thus `q_mu` already carries the required gauge-covariant phase-clock lineage.

## 2. Phase-clock projector

Introduce a positive independent calibration scale `mu_vartheta` with the same norm units as `q_mu` and define

\[
\boxed{
\mathcal C_\vartheta
:=-\frac{g^{\mu\nu}q_\mu q_\nu}{\mu_\vartheta^2}.
}
\]

The RF-F17 projector surface is

\[
\boxed{\mathcal C_\vartheta=1.}
\]

On that surface define

\[
\boxed{
u^{(\vartheta)}_\mu:=\frac{q_\mu}{\mu_\vartheta}.}
\]

The intended unit-timelike condition is

\[
\boxed{u^{(\vartheta)}_\mu u_{(\vartheta)}^\mu=-1.}
\]

The projector is gauge invariant because `q_mu` is gauge invariant and `mu_vartheta` is a gauge-scalar calibration input.

## 3. Independent-scale firewall

The scale used in the stress-tensor variation is required to satisfy

\[
\boxed{
\frac{\partial\mu_\vartheta}{\partial g^{\mu\nu}}=0.
}
\]

If instead one defines the scale from the same metric norm,

\[
\mu_\vartheta^2:=-g^{\alpha\beta}q_\alpha q_\beta,
\]

then

\[
\mathcal C_\vartheta\equiv1
\]

as an off-shell identity and hence

\[
\boxed{\delta_g\mathcal C_\vartheta=0.}
\]

The corresponding RF-F17 projector stress is then identically zero. An independent `mu_vartheta` is therefore an exact nontriviality condition.

IDT 05D supplies the dimensionless relative-information clock scalar `Phi(N_R)` and its Fisher geometry. IDT 01AD supplies physical elapsed-time calibration. RF-F18 keeps `mu_vartheta` as a downstream phase-rate calibration coordinate to be fixed by an independent receipt.

## 4. Off-shell metric-response ledger

Because the ABE connection includes a geometrical Euler sector, retain the possible metric response of `q_mu` explicitly. Define

\[
\boxed{
R_{\mu\nu}
:=g^{\alpha\beta}q_\alpha
\frac{\partial q_\beta}{\partial g^{\mu\nu}}.
}
\]

With independent `mu_vartheta`, direct differentiation gives

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
=-\frac{q_\mu q_\nu+2R_{\mu\nu}}{\mu_\vartheta^2}.
}
\]

Writing

\[
u^{(\vartheta)}_\mu:=q_\mu/\mu_\vartheta,
\]

this is

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
=-u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu
-\frac{2R_{\mu\nu}}{\mu_\vartheta^2}.
}
\]

The sufficient frozen-one-form condition is

\[
\boxed{R_{\mu\nu}=0.}
\]

RF-F18 therefore does not obtain a dust tensor by silently freezing the Euler/ABE connection: the response tensor remains an explicit audit coordinate.

## 5. RF-F17 eta=1 stress

RF-F17 gives

\[
T^U_{\mu\nu}
=-2\widehat U_L f'(1)
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
\]

on the `eta=1`, `C_vartheta=1` surface. Therefore

\[
\boxed{
T^U_{\mu\nu}
=2\widehat U_L f'(1)
 u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu
+\frac{4\widehat U_L f'(1)}{\mu_\vartheta^2}R_{\mu\nu}.
}
\]

On the frozen-one-form branch,

\[
R_{\mu\nu}=0,
\]

this reduces exactly to

\[
\boxed{
T^U_{\mu\nu}
=2\widehat U_L f'(1)
 u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu.
}
\]

For

\[
\boxed{f'(1)=\frac12},
\]

one obtains

\[
\boxed{
T^U_{\mu\nu}
=\widehat U_L
u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu.
}
\]

Thus the existing IDT gauge-covariant phase one-form supplies the RF-F17 pressureless rank-one projector algebra on the independently calibrated, timelike, frozen-one-form branch. For nonzero `R_mn`, the displayed correction remains part of the source tensor.

## 6. Binding to the RF-E19 material congruence

RF-E19 supplies the future-unit-timelike material direction

\[
\boxed{
\nu_J^\mu=\frac{J^\mu}{\sqrt{-J^2}}.
}
\]

Define the local relative alignment coordinate

\[
\boxed{
\gamma_{\vartheta J}
:=-u^{(\vartheta)}_\mu\nu_J^\mu
}
\]

and defect

\[
\boxed{
\Delta_{\vartheta J}:=|\gamma_{\vartheta J}-1|.
}
\]

For future unit timelike directions,

\[
\gamma_{\vartheta J}\ge1,
\]

and the zero-defect surface

\[
\boxed{\Delta_{\vartheta J}=0}
\]

is the exact local alignment condition. Physical promotion also carries the RF-N1B2K/RF-E19 orientation, slice, measure, support and lineage receipts.

## 7. Typed IDT clock roles

```text
IDT 05D
  Phi(N_R)=N_R-1-ln N_R
  -> relative-information clock scalar / Fisher potential

IDT 01AD
  d tau_hat=N_R dt
  D_tauhat chi=c e_0 ⌟ Dvartheta
  -> lapse-calibrated proper phase-clock rate

IDT 01AC
  q_mu=D_mu vartheta
  -> gauge-invariant spacetime phase-clock one-form
```

RF-F18 consumes the 01AC one-form and 01AD rate lineage. The 05D scalar remains an upstream clock-information coordinate and a possible later constitutive/calibration input.

## 8. Promotion ledger

```text
IDT 01AC q_mu=D_mu vartheta reuse                         PASS EXACT PARENT
01AC gauge invariance of q_mu                            PASS EXACT PARENT
IDT 01AD normal pullback -> proper phase-clock rate      PASS EXACT CONDITIONAL PARENT
C_vartheta=-g^{-1}(q,q)/mu_vartheta^2                   PASS EXACT DEFINITION
projector gauge invariance                               PASS EXACT
independent mu_vartheta requirement                      PASS EXACT FIREWALL
self-normalization -> delta_g C=0                        PASS EXACT NO-GO
metric-response tensor R_mn                              PASS EXACT LEDGER
R_mn=0 -> rank-one projector derivative                 PASS EXACT CONDITIONAL
eta=1 stress including R_mn correction                   PASS EXACT
R_mn=0, f'(1)=1/2 -> T=Uhat u_theta u_theta             PASS EXACT CONDITIONAL
phase-clock/material alignment coordinate                PASS EXACT
gamma_thetaJ=1 local congruence binding                  PASS EXACT CONDITIONAL
mu_vartheta physical calibration                         OPEN PROMOTION INPUT
ABE/Euler off-shell metric-response receipt              OPEN PROMOTION INPUT
IDT phase-clock <-> RF-E19 lineage receipt               OPEN PROMOTION INPUT
RF-N1B2K current/measure physical binding                OPEN PROMOTION INPUT
physical projector profile f                             OPEN PROMOTION INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/idt_phase_clock_projector.py`.

Reference tests: `tests/reference/test_rff18_idt_phase_clock_projector.py`.

Validation receipt: `validation/RF_F18_IDT_PHASE_CLOCK_PROJECTOR_V0_1.json`.
