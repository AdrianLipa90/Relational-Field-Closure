# RF-S7 — Noether–Shannon Radial Source-Binding Gate

Status: `EXACT_CROSS_OBSERVABLE_REDUCTION / EXECUTABLE_RADIAL_SOURCE_DEFECT / LOCAL_FISHER_LIMIT_PASS / PHYSICAL_ZERO_DEFECT_PROMOTION_OPEN`

RF-S7 follows RF-S4 and RF-S5 and consumes the IDT 01C/01K Shannon-relative-information lineage. Its purpose is to turn the remaining `RADIAL_INFORMATION_SOURCE_BINDING` into one directly auditable equality between independently supplied probability-state data and Noether-current data.

The gate keeps the baseline-resolved information curvature explicit and promotes the RF-S4 radial source surface only when the cross-observable defect vanishes on supplied data.

## 1. Independent Shannon/KL input

IDT 01C supplies an admitted relational probability state

\[
p=(p_1,\ldots,p_m),
\qquad
\pi=(\pi_1,\ldots,\pi_m),
\qquad
\pi_a>0,
\]

with natural-log relative information

\[
\boxed{
\mathcal J_\pi[p]
=\sum_{a:p_a>0}p_a\ln\frac{p_a}{\pi_a}.
}
\]

IDT 01K supplies the positive relational area

\[
\mathcal A_{\rm rel}>0
\]

and the exact inverse-area scalar

\[
\boxed{
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}}.
}
\]

RF-L4 carries a constant reference coordinate `Xi_star`. Define

\[
\boxed{
\bar\Xi_I
:=\Xi_I-\Xi_\star
=\frac{
\mathcal J_\pi-\Xi_\star\mathcal A_{\rm rel}
}{\mathcal A_{\rm rel}}.
}
\]

On the admitted positive radial chart,

\[
\bar\Xi_I\ge0.
\]

The Shannon/KL side is therefore computable from the tuple

```text
(p, pi, A_rel, Xi_star)
```

without using the matter-scalar amplitude as an input.

## 2. Independent Noether input

RF-S5/RF-E16 supplies the positive-carrier relation

\[
\boxed{
j_\vartheta=2A^2r_s,}
\]

with

\[
r_s>0,
\qquad
j_\vartheta>0.
\]

Therefore the matter radial amplitude is reconstructed as

\[
\boxed{
A_N^2
:=\frac{j_\vartheta}{2r_s}.
}
\]

The Noether side is computable from the tuple

```text
(j_vartheta, r_s)
```

independently of the probability-state inputs.

## 3. Exact radial source-binding residual

RF-S4 defines the radial information/matter source surface by

\[
A^2=\bar\Xi_I.
\]

Using the two independent reconstructions above, define

\[
\boxed{
R_{N\!S}
:=
\mathcal A_{\rm rel}j_\vartheta
-2r_s\left(
\mathcal J_\pi-\Xi_\star\mathcal A_{\rm rel}
\right).
}
\]

Since

\[
\mathcal A_{\rm rel}j_\vartheta
=2r_s\mathcal A_{\rm rel}A_N^2
\]

and

\[
2r_s\left(
\mathcal J_\pi-\Xi_\star\mathcal A_{\rm rel}
\right)
=2r_s\mathcal A_{\rm rel}\bar\Xi_I,
\]

one obtains exactly

\[
\boxed{
R_{N\!S}=0
\Longleftrightarrow
A_N^2=\bar\Xi_I
}
\]

for positive `A_rel` and `r_s`.

Thus the RF-S4 source-binding surface is equivalent to one cross-observable equality.

## 4. Normalized source-binding defect

For nondegenerate combined support define

\[
\boxed{
\Delta_{N\!S}
:=
\frac{|A_N^2-\bar\Xi_I|}
{A_N^2+\bar\Xi_I}.
}
\]

Substitution gives the observable form

\[
\boxed{
\Delta_{N\!S}
=
\frac{
\left|
\mathcal A_{\rm rel}j_\vartheta
-2r_s(\mathcal J_\pi-\Xi_\star\mathcal A_{\rm rel})
\right|
}
{
\mathcal A_{\rm rel}j_\vartheta
+2r_s(\mathcal J_\pi-\Xi_\star\mathcal A_{\rm rel})
}.
}
\]

Hence

\[
\boxed{
0\le\Delta_{N\!S}\le1.
}
\]

The RF-S4 radial source-binding surface is

\[
\boxed{
\Delta_{N\!S}=0.
}
\]

For positive `barXi_I`, define also the ratio

\[
\boxed{
\chi_{N\!S}
:=\frac{A_N^2}{\bar\Xi_I}
=
\frac{
\mathcal A_{\rm rel}j_\vartheta
}
{
2r_s(\mathcal J_\pi-\Xi_\star\mathcal A_{\rm rel})
}.
}
\]

The binding surface is equivalently `chi_NS=1`.

## 5. Stationary zero-baseline specialization

On the stationary-reference zero-baseline branch

\[
\Xi_\star=0,
\]

RF-S7 reduces to

\[
\boxed{
R_{N\!S}
=\mathcal A_{\rm rel}j_\vartheta
-2r_s\mathcal J_\pi.
}
\]

Therefore

\[
\boxed{
\Delta_{N\!S}=0
\Longleftrightarrow
\mathcal A_{\rm rel}j_\vartheta
=2r_s\mathcal J_\pi.
}
\]

This is the minimal exact measurement equation for the local RF-S4 radial source surface.

## 6. Local Shannon–Fisher limit

RF-L4A supplies, near the stationary reference,

\[
\mathcal J_\pi
=\frac12s_F^2+O(\|\delta p\|^3)
\]

and

\[
\mathcal A_{\rm rel}
=\mathcal A_\star+O(\|\delta p\|).
\]

At quadratic order,

\[
\boxed{
\bar\Xi_I^{(2)}
=\frac{s_F^2}{2\mathcal A_\star}
}
\]

on the stationary zero-baseline branch.

Matching the independent Noether reconstruction gives

\[
\frac{j_\vartheta}{2r_s}
=\frac{s_F^2}{2\mathcal A_\star}
\]

or equivalently

\[
\boxed{
\mathcal A_\star j_\vartheta
=r_ss_F^2.
}
\]

Define the quadratic Fisher residual

\[
\boxed{
R_F^{(2)}
:=\mathcal A_\star j_\vartheta-r_ss_F^2.
}
\]

This is the local Hessian-limit form of the exact Noether–Shannon equality.

## 7. RF-S4 promotion consequence

RF-S4 proves on its radial zero-defect action-reclassification surface that

\[
\phi_A=\phi_I
\]

and, for nonzero radial support on the positive-mass branch,

\[
\boxed{m_\Psi=m_I.}
\]

RF-S7 supplies an independently evaluable admission coordinate for that source surface:

\[
\boxed{
\Delta_{N\!S}=0
\Longrightarrow
\Delta_{A\Xi}=0
}
\]

when the RF-S4 and RF-S7 radial coordinates refer to the same selected cell, support and baseline.

Consequently, measured zero defect admits the RF-S4 chain

\[
\Delta_{N\!S}=0
\to
A^2=\bar\Xi_I
\to
\phi_A=\phi_I
\to
m_\Psi=m_I
\to
\rho_\omega=1.
\]

The equality is therefore attached to a concrete cross-observable receipt rather than a field-name assignment.

## 8. Cell/support ledger

The comparison requires a shared physical support ledger:

```text
same selected RFC matter mode
same spatial/projective cell
same A_rel used in Xi_I
same slice/current density convention
same positive normal phase rate r_s
same Xi_star baseline
same ordered measurement event
```

Define a support-admission flag only after those identifiers agree. A source-binding receipt records the identifiers together with `J_pi`, `A_rel`, `Xi_star`, `j_vartheta`, `r_s`, `R_NS` and `Delta_NS`.

## 9. Dynamical continuation

IDT 01C supplies monotonic contraction of `J_pi` under the admitted stationary relational kernel. RF-E16 supplies the matter-phase Noether current/rate pair. Preservation or evolution of `Delta_NS` under joint dynamics is a separate dynamical gate.

RF-S7 therefore isolates the next question sharply:

\[
\boxed{
D_\tau\Delta_{N\!S}
}
\]

under synchronized Shannon–Onsager and matter/Noether evolution.

A dynamically invariant zero-defect surface would promote the pointwise source-binding equality into a transported source-binding relation.

## 10. Promotion ledger

Promoted parents:

```text
IDT 01C J_pi[p] from p,pi                               PASS EXACT
IDT 01K Xi_I=J_pi/A_rel                                PASS EXACT
RF-L4 baseline barXi_I=Xi_I-Xi_star                    PASS EXACT
RF-L4A local Fisher Hessian normalization              PASS LOCAL
RF-S5 A^2=j_vartheta/(2r_s)                            PASS EXACT
RF-S4 action consequences on Delta_AXi=0               PASS CONDITIONAL
```

RF-S7 outputs:

```text
Noether radial reconstruction A_N^2                    PASS EXACT
Shannon radial reconstruction barXi_I                  PASS EXACT
R_NS observable residual                               PASS EXACT
R_NS=0 <-> A_N^2=barXi_I                               PASS EXACT
normalized Delta_NS                                    PASS EXACT
stationary zero-baseline measurement equation          PASS EXACT
local Fisher residual A_star j = r_s s_F^2             PASS QUADRATIC
RF-S4 source-surface admission from Delta_NS=0          PASS GIVEN SHARED SUPPORT LEDGER
```

Remaining gates:

```text
PHYSICAL_RADIAL_ZERO_DEFECT_DATA
RADIAL_BINDING_DYNAMICAL_TRANSPORT
CLOCK_RADIAL_ACTION_COMPOSITION
CLOCK_ALPHA_BINDING
TIR_RFC_CELL_SOURCE_BINDING
TRANSLATIONAL_OBSERVABLE
DIRECTIONAL_CUBIC_TEST
GENERAL_MATTER_MULTIPLET
GLOBAL_INFORMATION_GEODESIC_EXTENSION
```

## 11. Validation authority

Reference implementation: `src/rfc/noether_shannon_radial_source_binding.py`.
Reference tests: `tests/reference/test_rfs7_noether_shannon_radial_source_binding.py`.
Validation receipt: `validation/RF_S7_NOETHER_SHANNON_RADIAL_SOURCE_BINDING_V0_1.json`.

Parent RFC main at branch creation: `466d364f3d903215b94e2ba66e1fd1fac23e7a30`.
