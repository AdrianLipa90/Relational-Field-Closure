# RF-F18 — IDT Gauge-Covariant Phase-Clock Projector Binding

Status: `IDT_01AC_ONE_FORM_REUSE_PASS / IDT_01AD_CLOCK_RATE_PARENT_PASS / INDEPENDENT_PHASE_SCALE_FIREWALL_EXACT / METRIC_RESPONSE_LEDGER_EXACT / RF_E19_ALIGNMENT_GATE_DEFINED / PHYSICAL_PROJECTOR_PROMOTION_CONDITIONAL`

RF-F18 is stacked on RF-F17. It audits whether the RF-F17 state-dependent exchange projector can be realized from an already-existing IDT field rather than by introducing an additional clock degree of freedom.

The selected upstream object is the IDT 01AC gauge-invariant phase one-form

\[
\boxed{
q_\mu
:=
\mathscr D_\mu\vartheta
=
\partial_\mu\vartheta+\mathcal A^{ABE}_\mu.
}
\]

IDT 01AC gives the gauge transformation

\[
\vartheta\mapsto\vartheta+\lambda,
\qquad
\mathcal A^{ABE}\mapsto\mathcal A^{ABE}-d\lambda,
\]

and therefore

\[
\boxed{q_\mu\mapsto q_\mu.}
\]

IDT 01AD independently binds the normal pullback of this same one-form to the relational-lapse proper-time phase rate,

\[
\boxed{
D_{\hat\tau}\chi
=
r_n^{(\tau)}
=
c\,e_{\hat0}\lrcorner\mathscr D\vartheta.
}
\]

Thus `q_mu` already has the required phase-clock lineage.

---

## 1. Projector definition

Introduce one positive independent phase-clock norm scale `mu_vartheta` with the same norm units as `q_mu`, and define

\[
\boxed{
\mathcal C_\vartheta
:=
-\frac{g^{\mu\nu}q_\mu q_\nu}{\mu_\vartheta^2}.
}
\]

The RF-F17 projector surface is

\[
\boxed{\mathcal C_\vartheta=1.}
\]

On this surface define

\[
\boxed{
u^{(\vartheta)}_\mu:=\frac{q_\mu}{\mu_\vartheta}.}
\]

Then

\[
\boxed{
u^{(\vartheta)}_\mu u_{(\vartheta)}^\mu=-1.}
\]

The projector is gauge invariant because `q_mu` is gauge invariant and `mu_vartheta` is a gauge-scalar calibration input.

---

## 2. Independent-scale firewall

The normalization scale must be independent under the metric variation used to define the stress tensor:

\[
\boxed{
\frac{\partial\mu_\vartheta}{\partial g^{\mu\nu}}=0.
}
\]

A self-normalized definition

\[
\mu_\vartheta^2
:=
-g^{\alpha\beta}q_\alpha q_\beta
\]

would give

\[
\mathcal C_\vartheta\equiv1
\]

as an off-shell identity and therefore

\[
\boxed{
\delta_g\mathcal C_\vartheta=0.
}
\]

That surface produces no RF-F17 state-dependent projector stress. The independent phase-clock calibration is therefore an exact integrability condition for a nontrivial realization.

IDT 05D supplies the dimensionless relative-information clock potential `Phi(N_R)` and delegates physical action/Hamiltonian/energy scaling downstream. IDT 01AD supplies the reference-clock calibration into physical elapsed time. RF-F18 consequently leaves `mu_vartheta` as an explicit downstream phase-rate calibration coordinate rather than constructing it from the same metric norm being varied.

---

## 3. Metric-response ledger for the ABE connection

The simple frozen-one-form variation is valid only on a surface where `q_mu` is held independent in the metric variation.

Define the possible connection/one-form metric-response contraction

\[
\boxed{
R_{\mu\nu}
:=
g^{\alpha\beta}q_\alpha
\frac{\partial q_\beta}{\partial g^{\mu\nu}}.
}
\]

With independent `mu_vartheta`, direct differentiation gives

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
=
-\frac{q_\mu q_\nu+2R_{\mu\nu}}
{\mu_\vartheta^2}.
}
\]

Equivalently,

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
=
-u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu
-
\frac{2R_{\mu\nu}}{\mu_\vartheta^2}.
}
\]

The frozen-one-form branch is the sufficient condition

\[
\boxed{R_{\mu\nu}=0.}
\]

RF-F18 keeps `R_mn` explicit because the ABE connection includes a geometrical Euler sector whose off-shell metric typing must be audited independently.

---

## 4. RF-F17 eta=1 stress

RF-F17 gives, at `eta=1`,

\[
T^U_{\mu\nu}
=
-2\widehat U_L f'(1)
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}.
\]

Therefore

\[
\boxed{
T^U_{\mu\nu}
=
2\widehat U_L f'(1)
 u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu
+
\frac{4\widehat U_L f'(1)}{\mu_\vartheta^2}
R_{\mu\nu}.
}
\]

This is the exact metric-response ledger.

On the frozen-one-form branch,

\[
R_{\mu\nu}=0,
\]

one obtains

\[
\boxed{
T^U_{\mu\nu}
=
2\widehat U_L f'(1)
 u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu.
}
\]

For

\[
\boxed{f'(1)=\frac12},
\]

this reduces to

\[
\boxed{
T^U_{\mu\nu}
=
\widehat U_L
u^{(\vartheta)}_\mu u^{(\vartheta)}_\nu.
}
\]

Thus the already-existing IDT gauge-covariant phase one-form supplies the exact RF-F17 pressureless rank-one projector algebra on the independently calibrated, timelike, frozen-one-form branch.

If `R_mn` is nonzero, its tensor correction remains explicit and the resulting stress is classified by the measured/calculated response tensor rather than by the frozen-one-form reduction.

---

## 5. Material-congruence binding to RF-E19

RF-E19 supplies the normalized future-timelike material congruence from the admitted Noether current,

\[
\boxed{
\nu_J^\mu
=
\frac{J^\mu}{\sqrt{-J^2}}.
}
\]

On the RF-F18 unit phase-clock surface define the relative alignment coordinate

\[
\boxed{
\gamma_{\vartheta J}
:=-u^{(\vartheta)}_\mu\nu_J^\mu.
}
\]

For two future unit timelike directions,

\[
\gamma_{\vartheta J}\ge1.
\]

Define

\[
\boxed{
\Delta_{\vartheta J}
:=
|\gamma_{\vartheta J}-1|.
}
\]

Then

\[
\boxed{
\Delta_{\vartheta J}=0
}
\]

is the exact local alignment surface on the future-unit-timelike sector.

The physical binding target is therefore

\[
\boxed{
 u^{(\vartheta)\mu}
\stackrel{?}{\longleftrightarrow}
\nu_J^\mu
}
\]

with the same orientation, slice, measure, support and lineage receipts already required by RF-N1B2K/RF-E19.

---

## 6. Relation to IDT 05D and 01AD

The three IDT clock surfaces now have separate typed roles:

```text
IDT 05D:
  Phi(N_R)=N_R-1-ln N_R
  role: relative-information clock scalar / Fisher potential

IDT 01AD:
  d tau_hat=N_R dt
  D_tauhat chi = c e_0 ⌟ Dvartheta
  role: lapse-calibrated proper phase-clock rate

IDT 01AC:
  q_mu=D_mu vartheta
  role: gauge-invariant spacetime phase-clock one-form
```

RF-F18 consumes the 01AC one-form and the 01AD clock-rate lineage. The 05D information scalar remains a compatible upstream clock-information coordinate and a possible later calibration/constitutive input.

---

## 7. Promotion ledger

```text
IDT 01AC q_mu=D_mu vartheta reuse                         PASS EXACT PARENT
01AC gauge invariance of q_mu                            PASS EXACT PARENT
IDT 01AD q_mu normal pullback -> proper phase-clock rate PASS EXACT CONDITIONAL PARENT
C_vartheta=-g^{-1}(q,q)/mu_vartheta^2                   PASS EXACT DEFINITION
projector gauge invariance                               PASS EXACT
independent mu_vartheta requirement                      PASS EXACT FIREWALL
self-normalized mu^2=-g^{-1}(q,q) -> delta_g C=0        PASS EXACT NO-GO
metric-response tensor R_mn ledger                       PASS EXACT
R_mn=0 -> rank-one projector derivative                 PASS EXACT CONDITIONAL
eta=1 stress with R_mn correction                        PASS EXACT
R_mn=0 and f'(1)=1/2 -> T=Uhat u_theta u_theta          PASS EXACT CONDITIONAL
phase-clock/material alignment gamma_thetaJ              PASS EXACT COORDINATE
Delta_thetaJ=0 local congruence binding                  PASS EXACT CONDITIONAL
mu_vartheta physical calibration                         OPEN PROMOTION INPUT
ABE/Euler off-shell metric-response receipt              OPEN PROMOTION INPUT
IDT phase-clock <-> RF-E19 material lineage receipt      OPEN PROMOTION INPUT
RF-N1B2K current/measure physical binding                OPEN PROMOTION INPUT
physical projector profile f                             OPEN PROMOTION INPUT
```

## 8. Validation authority

Reference implementation:

`src/rfc/idt_phase_clock_projector.py`

Reference tests:

`tests/reference/test_rff18_idt_phase_clock_projector.py`

Validation receipt:

`validation/RF_F18_IDT_PHASE_CLOCK_PROJECTOR_V0_1.json`
