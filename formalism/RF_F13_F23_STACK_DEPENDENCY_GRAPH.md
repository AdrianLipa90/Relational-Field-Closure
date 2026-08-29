# RF-F13 → RF-F23 Stacked Dependency Graph

Status: `STACKED_REFERENCE_FRONTIER / NONCANONICAL / MAIN_UNCHANGED`

This sidecar records the validated stacked frontier above RFC `main` without promoting the stack into the canonical `DEPENDENCY_EXPORT.json`.

Canonical main anchor:

`58655c7fe9d25d09c13545965e951f171316e6b2`

The canonical machine export currently carries `source_commit=45659a5fbbcd0faa06ab2a7d8a81d1eb7215d4c0` and an explicit RF-F0→RF-F13 machine chain. RF-F14→RF-F23 are therefore recorded here as a noncanonical stacked frontier until the source stack is explicitly merged and a post-merge export can be regenerated against the exact resulting main commit.

## 1. Linear stacked spine

\[
\boxed{
\mathrm{RF\!\!-​F13}
\rightarrow
\mathrm{RF\!\!-​F14}
\rightarrow
\mathrm{RF\!\!-​F15}
\rightarrow
\mathrm{RF\!\!-​F16}
\rightarrow
\mathrm{RF\!\!-​F17}
\rightarrow
\mathrm{RF\!\!-​F18}
\rightarrow
\mathrm{RF\!\!-​F19}
\rightarrow
\mathrm{RF\!\!-​F20}
\rightarrow
\mathrm{RF\!\!-​F21}
\rightarrow
\mathrm{RF\!\!-​F22}
\rightarrow
\mathrm{RF\!\!-​F23}
}
\]

The branch ancestry is exact: each PR is based on the immediately preceding RF-F branch rather than directly on `main`.

## 2. Validated nodes

| Gate | Role | PR | Branch head | Hosted reference evidence |
|---|---|---:|---|---|
| RF-F13 | variational integrability / common action | #68 | `a14da535354f30ad8b0b672713863a9734970328` | suite #321 SUCCESS on `45659a5fbbcd0faa06ab2a7d8a81d1eb7215d4c0`; export head also passed suite #322 |
| RF-F14 | microscopic Noether energy / EOS compatibility | #69 | `a46315fa118da4343dd4d0310b2b6c69df6769e1` | suite #324 SUCCESS on current branch head; implementation suite #323 also passed |
| RF-F15 | microscopic scalar → phase-cell transport | #71 | `c3f7570827836e5ec071e88c72c3fc6408849dc6` | suite #326 SUCCESS |
| RF-F16 | vacuum split / dynamic-Λ common action | #72 | `42f1d7e0bb2d4c208338bac9a77cec37e36bfcf0` | suite #330 SUCCESS on `abe796f561b5235a7ba0233c3233b0fa4b081abc` |
| RF-F17 | state-dependent exchange projector | #73 | `110da304b83616fef5962413bcb21d4b59869c0b` | suite #332 SUCCESS on `f88012118a3209785a548cdc3771821a34b47ad1` |
| RF-F18 | IDT gauge-covariant phase-clock projector | #74 | `5705717e94293bba3b39719dde108eec2a3dbda8` | suite #340 SUCCESS on `f0d7d74ee3ce2a4c8a29b55faee43dc733bdab1a` |
| RF-F19 | independent rotor/lapse phase scale | #75 | `4c52bb17be0093661f20baf4e358348dcda4db25` | suite #344 SUCCESS on `c326b0ebbad2c180cfdde5ac11c157bd36d2c801` |
| RF-F20 | ABE/Euler off-shell metric-response firewall | #76 | `e537b81df0dae5d4b455e46090c61c7e4e8380b5` | suite #351 SUCCESS on `f4f22d2f77ef337768fef7ee55b185268b803dd3` |
| RF-F21 | independent IDT↔RFC phase-rate receipt | #77 | `e28584e6253507c6b5672396794cf7f1636c5513` | suite #353 SUCCESS on `71a7c1217533d4650f782d5ae01d5140c6cba98a` |
| RF-F22 | total Einstein source / Bianchi repartition | #78 | `24ff4dcbde9b5b069664f158da2661556da748fd` | suite #355 SUCCESS on `f3d7f504aa71d368b190502b85edab450558e2ab` |
| RF-F23 | phase-clock / material-congruence alignment receipt | #79 | `60c6708564083233f9579b30946673ba0c2e1c4e` before this sidecar | suite #357 SUCCESS on `241843acf8cc009d7f76a7cdb529d5615fea543a` |

## 3. Formal dependency semantics

### RF-F13 → RF-F16: action and source ledger

RF-F13 supplies the first-order/covariant common-action organization and exchange partition. RF-F14 fixes the microscopic scalar EOS and Noether energy normalization surfaces. RF-F15 transports those surfaces through the RF-F8/RF-F12 phase-cell scaling. RF-F16 joins the constant vacuum integration term, scalar potential zero point and dynamic `Lambda0` exchange on one action ledger.

### RF-F17 → RF-F20: state-dependent projector and metric response

RF-F17 gives the exact state-dependent projector theorem. RF-F18 binds it to the pre-existing IDT gauge-covariant phase one-form and isolates the self-normalization no-go. RF-F19 replaces an arbitrary projector scale with an independently evaluated rotor/lapse phase-rate calibration. RF-F20 decomposes the full ABE off-shell metric response and carries its exact stress correction without assigning an unsupported physical value to the response tensor.

### RF-F21 → RF-F23: independent receipts and Einstein assembly

RF-F21 turns the IDT↔RFC field/rotor proper-rate bridge into an independent-input zero-defect receipt. RF-F22 composes the complete source bookkeeping and proves the exact fixed-reference/dynamic-`Lambda0` Einstein residual identity and Bianchi repartition. RF-F23 turns the RF-F18 phase-clock ↔ RF-E19 material-current congruence identification into an independent-input lineage-aware receipt.

## 4. Einstein-closure statement at the stacked frontier

RF-F22 establishes

\[
T^{(0)}_{\mu\nu}-T^{(*)}_{\mu\nu}
=\widehat U_L g_{\mu\nu},
\qquad
\Lambda_0-\Lambda_*
=\kappa_E\widehat U_L,
\]

hence

\[
\boxed{
\mathcal E^{(0)}_{\mu\nu}
=\mathcal E^{(*)}_{\mu\nu}}
\]

for

\[
\mathcal E_{\mu\nu}
=G_{\mu\nu}+\Lambda g_{\mu\nu}-\kappa_E T_{\mu\nu}.
\]

It also establishes

\[
\boxed{
\kappa_E\nabla^\mu T^{(0)}_{\mu\nu}
-\nabla_\nu\Lambda_0
=
\kappa_E\nabla^\mu T^{(*)}_{\mu\nu}}
\]

so fixed-ledger action conservation and the dynamic-`Lambda0` Bianchi exchange are the same residual bookkeeping.

RF-F23 then supplies the independent local congruence audit

\[
\Delta_{\vartheta J}
=
\left|-v^{(\vartheta)}_\mu\nu_J^\mu-1\right|,
\]

with lineage and future-timelike domain firewalls.

Therefore the stacked frontier status is:

`FORMAL_ACTION_LEVEL_EINSTEIN_SOURCE_ASSEMBLY = PASS`

`REFERENCE_PHASE_CLOCK_MATERIAL_ALIGNMENT_CONTRACT = PASS`

`PHYSICAL_SOURCE_PROMOTION = CONDITIONAL / RECEIPT_GATED`

## 5. Remaining physical-promotion inputs

The stacked frontier isolates rather than hides the remaining promotion coordinates:

1. realized RF-N1B2K current/measure receipt;
2. realized local ABE off-shell response `R_mn`;
3. realized rotor/lapse phase-scale response `S_mn^(vartheta)`;
4. realized independent IDT↔RFC field/rotor rate receipt;
5. realized phase-clock/material-current alignment receipt;
6. physical state-dependent interaction profile `f(C)` and exchange allocation `eta`;
7. physical promotion/universality of `kappa_E=8 pi G/c^4` on the project-derived coupling route.

These coordinates select the realized physical source within the already closed source/repartition algebra.

## 6. Promotion rule

This sidecar has no authority to mutate canonical RFC or FPDG claims.

Canonical promotion requires, in order:

1. explicit authorization to merge the RFC stacked source branches;
2. exact post-merge RFC `main` commit;
3. regeneration of canonical `DEPENDENCY_EXPORT.json` from that exact source commit;
4. source/export freshness lock;
5. only then, corresponding FPDG federation/promotion.

Until those steps occur, this document remains the authoritative description of the validated **stacked** frontier only.