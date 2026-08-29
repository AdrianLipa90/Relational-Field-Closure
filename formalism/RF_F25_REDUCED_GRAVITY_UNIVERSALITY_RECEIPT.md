# RF-F25 — Reduced-Gravity Scale Cross-System Universality Receipt

Status: `RF_N1C2_C3_EXECUTABLE_UNIVERSALITY_GATE / G_FREE_ZERO_FIT_COMPARISON / HORIZON_PROVENANCE_FIREWALL / REALIZED_CROSS_SYSTEM_EVIDENCE_OPEN`

RF-F25 turns the RF-N1C / RF-N1C2 / RF-N1C3 coupling frontier into a single independent-input executable receipt. It does not select a numerical Newton constant. It tests whether independently frozen source, gauge/double-copy, carrier and optional horizon routes determine one source-independent reduced gravity scale.

The executable formulas are evaluated in the natural-unit coordinates used by RF-N1C2/RF-N1C3.

## 1. Independent per-system inputs

For each admitted weak-field system `a`, RF-F25 receives independently

\[
\beta_{W,a},
\quad
\Gamma_{DC,a},
\quad
g_{YM,a}^2,
\quad
M_{\star,a},
\quad
\omega_{Q,a},
\quad
j_{Q,a},
\quad
\mathcal S_{R,a}.
\]

It also receives explicit provenance IDs for

- RF-F24 current/measure receipt;
- RF-F21 phase-rate receipt;
- RFC source-operator receipt;
- gauge/Wilson normalization receipt;
- double-copy receipt;
- carrier-scale receipt;
- optional independent horizon provenance.

Every system carries one `gravity_sector_id`. Cross-system comparison is rejected unless all systems belong to the same declared gravity sector.

## 2. Wilson normalization audit

RFG3 supplies

\[
\boxed{g_{YM}^2=\frac6{\beta_W}.}
\]

RF-F25 keeps `g_YM^2` and `beta_W` as separate inputs and audits the symmetric defect

\[
\boxed{
\delta_W
=
\frac{2|g_{YM}^2-6/\beta_W|}
{|g_{YM}^2|+|6/\beta_W|}.}
\]

Thus the Wilson relation is tested rather than created by assignment.

## 3. General double-copy reduced scale

RF-N1C2 defines

\[
\boxed{
\bar M_G^{DC}
=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}}
\]

and

\[
\boxed{
G_{DC}
=\frac{1}{8\pi(\bar M_G^{DC})^2}.}
\]

The independent Wilson representation is

\[
\boxed{
\bar M_G^W
=\frac{\beta_WM_\star}{6\Gamma_{DC}}.}
\]

RF-F25 audits `Mbar_G^DC ↔ Mbar_G^W` independently.

## 4. Local carrier-scale candidate

The RF-N1C local candidate is

\[
\boxed{M_\star\stackrel{?}{=}\epsilon_Q=\frac12\omega_Q.}
\]

RF-F25 receives `M_star` and `omega_Q` independently and audits

\[
\boxed{
\delta_M
=
\frac{2|M_\star-\omega_Q/2|}
{|M_\star|+|\omega_Q/2|}.}
\]

On the zero-defect candidate surface,

\[
\boxed{
\bar M_G^{local}
=\frac{\beta_W\omega_Q}{12\Gamma_{DC}}.}
\]

This local representation is independently compared with `Mbar_G^DC`.

## 5. G-free source route

Before imposing the local carrier scale, RF-N1C2 gives the general source prediction

\[
\boxed{
\mathcal S_R^{general}
=
\frac{\Gamma_{DC}^2g_{YM}^4}{4M_\star^2}
\,\omega_Qj_Q.}
\]

On the local carrier/Wilson surface this reduces to

\[
\boxed{
\mathcal S_R^{local}
=
\frac{36\Gamma_{DC}^2}{\beta_W^2\omega_Q}j_Q.}
\]

The measured/promoted RFC source coordinate `S_R` remains an independent input. RF-F25 audits both source predictions separately.

No numerical `G` is used in either source comparison.

## 6. Optional independent horizon route

RF-N1C3 supplies

\[
\boxed{
\bar M_G^H
=\sqrt{\frac{M_H\kappa_H}{2\pi}}}
\]

and

\[
\boxed{
\bar M_G^T
=\sqrt{M_HT_H}.}
\]

When horizon data are supplied, RF-F25 audits

\[
\bar M_G^{DC}\leftrightarrow\bar M_G^H,
\qquad
\bar M_G^{DC}\leftrightarrow\bar M_G^T,
\]

and, when both `kappa_H` and `T_H` are supplied,

\[
\boxed{\kappa_H\leftrightarrow2\pi T_H.}
\]

The horizon route is rejected as independent evidence when its provenance ID is the same as the double-copy receipt ID. This is an executable circularity firewall; physical provenance remains a separately sourced record.

Missing optional horizon estimators are represented explicitly as `None`, never as `NaN`.

## 7. Cross-system universality theorem

For independently admitted systems `a,b`, RF-N1C2 gives

\[
G_a=G_b
\quad\Longleftrightarrow\quad
\boxed{\bar M_{G,a}=\bar M_{G,b}}
\]

on the positive reduced-scale sector.

RF-F25 evaluates the symmetric pairwise defects

\[
\boxed{
\delta_{\bar M}^{ab}
=\frac{2|\bar M_{G,a}^{DC}-\bar M_{G,b}^{DC}|}
{|\bar M_{G,a}^{DC}|+|\bar M_{G,b}^{DC}|}}
\]

and

\[
\boxed{
\delta_G^{ab}
=\frac{2|G_{DC,a}-G_{DC,b}|}
{|G_{DC,a}|+|G_{DC,b}|}.}
\]

It separately audits the local-candidate universality coordinate based on `Mbar_G^local`.

The receipt requires at least two unique system IDs. A one-system fixture cannot promote universality.

## 8. Built-in falsification coordinate

RF-N1C2 shows that fixed `beta_W` and `Gamma_DC` with a doubled `omega_Q` on the local candidate surface gives

\[
\bar M_G\mapsto2\bar M_G,
\qquad
G\mapsto\frac14G.
\]

RF-F25 includes this as an adversarial test. The receipt must fail cross-system universality even when each individual source law is algebraically satisfied.

Thus local source-law closure and universal coupling are kept as separate questions.

## 9. Zero-defect universality surface

For at least two independently sourced systems in one declared gravity sector, the reference promotion surface requires zero defects for

1. Wilson gauge normalization;
2. DC↔Wilson reduced scale;
3. independent `M_star ↔ omega_Q/2` carrier scale, when the local candidate is claimed;
4. DC↔local reduced scale;
5. general and local source routes;
6. pairwise `Mbar_G` universality;
7. pairwise `G_DC` universality;
8. optional DC↔horizon/thermal scale closure;
9. optional Hawking conversion;
10. horizon-vs-double-copy provenance independence.

A reference zero-defect fixture validates this contract. Physical promotion requires the same receipt to be populated by independently sourced realized-system inputs.

## 10. Einstein coupling consequence

Once realized cross-system evidence establishes one universal reduced scale,

\[
\boxed{
G
=\frac{1}{8\pi\bar M_G^2}}
\]

in the natural-unit RF-N1C2 coordinates.

RF-N1C then transfers this same source normalization to the Einstein equation through

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}}
\]

in SI normalization, or

\[
\boxed{\kappa_E=8\pi G}
\]

in natural units.

RF-F22 has already established the exact action-level Einstein/Bianchi source assembly for an admitted `kappa_E`. RF-F25 therefore isolates the final coupling-promotion problem as a zero-fit cross-system evidence test rather than modifying the Einstein equation.

## 11. Evidential status

The RF-N1C, RF-N1C2 and RF-N1C3 algebra is already reference-PASS. RF-F25 adds the executable universality/provenance contract.

Physical universal-`G` promotion remains conditional on realized cross-system inputs with frozen provenance. Numerical `G` is not used as a fitting or selection target in the reference gate.

## 12. Executable reference

`src/rfc/reduced_gravity_universality_receipt.py` implements:

- independent Wilson normalization audit;
- general DC, Wilson and local reduced-scale estimators;
- general and local G-free source predictions;
- natural-unit `G_DC` coordinate;
- optional horizon geometric and thermal estimators;
- horizon circularity/provenance firewall;
- pairwise cross-system `Mbar_G`, local-candidate and `G_DC` universality defects;
- minimum-two-system and same-gravity-sector domain gates;
- explicit-tolerance admission;
- no `NaN` placeholders for missing optional estimators.
