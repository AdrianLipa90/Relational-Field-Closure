# RF-E23 — Conserved-Source Divergence-Free Gravitational Operator Selection

Status: `EXACT_CONSERVED_SOURCE_PARENT / UNIVERSAL_COUPLING_CONSISTENCY_SELECTION_PASS / DIVERGENCE_FREE_OPERATOR_CLASS_BOUND / DYNAMIC_LAMBDA_EXCHANGE_BRANCH_PRESERVED`

Date: 2026-08-30

## 1. Purpose

RF-E21 uses the four-dimensional Lovelock tensor classification. One of its premise classes is that the admissible geometric rank-two operator belongs to the covariantly divergence-free natural-tensor class.

RF-E23 binds that premise without naming the Einstein tensor in advance. The source is the independently established RFC matter-sector conservation law plus a universal-coupling consistency rule.

## 2. Independent conserved-source parent

RF-E6 derives the charged matter and electromagnetic stress tensors from the matter/Maxwell action on the already admitted Lorentzian background. On the matter and Maxwell equations of motion,

\[
\nabla^\mu T^{matter}_{\mu\nu}
=+F_{\nu\lambda}J_{EM}^\lambda,
\]

\[
\nabla^\mu T^{EM}_{\mu\nu}
=-F_{\nu\lambda}J_{EM}^\lambda.
\]

Therefore the admitted source tensor satisfies

\[
\boxed{
\nabla^\mu T^{source}_{\mu\nu}=0,
\qquad
T^{source}_{\mu\nu}
=T^{matter}_{\mu\nu}+T^{EM}_{\mu\nu}.
}
\]

This conservation statement is obtained from the source-sector action/equations and does not require the Einstein field equation.

Additional admitted matter sectors may be composed when their own source-conservation gates pass. The present theorem uses the already closed source class as the exact parent example and the standard universal-source rule below as the selection step.

## 3. Unknown geometric operator

Before selecting Einstein form, write the gravitational equation abstractly as

\[
\boxed{
\mathcal E_{\mu\nu}[g]
=\kappa\,T_{\mu\nu},
}
\]

where

- `mathcal E_mn[g]` is an unknown symmetric natural metric operator from the RF-E21 admissible class;
- `kappa` is a spacetime-constant universal coupling on this branch;
- `T_mn` is an independently admitted covariantly conserved source.

No formula for `mathcal E_mn` is assumed here.

## 4. Divergence consistency

Taking the covariant divergence of the abstract equation gives

\[
\nabla^\mu\mathcal E_{\mu\nu}
=\kappa\,\nabla^\mu T_{\mu\nu}.
\]

For the independently conserved source sector,

\[
\nabla^\mu T_{\mu\nu}=0,
\]

hence every admitted solution satisfies

\[
\boxed{
\nabla^\mu\mathcal E_{\mu\nu}=0.
}
\]

This is an exact consequence of constant universal coupling and source conservation.

## 5. Universal-source autonomy rule

RF-E23 now applies the following consistency selection rule:

> The fundamental gravitational operator must couple to every independently admitted covariantly conserved source without imposing an additional source-side differential law beyond that source sector's own equations of motion.

If `nabla^mu mathcal E_munu` were a nonzero independent metric expression, the coupled equation would restrict admissible source/metric pairs by an additional differential condition not supplied by the source theory.

The universal-source autonomy rule therefore selects the operator class with the geometric identity

\[
\boxed{
\nabla^\mu\mathcal E_{\mu\nu}\equiv0.
}
\]

This is the RF-E21 divergence-free premise binding.

The rule is a coupling-consistency selection, while the implication from that rule plus conserved-source universality to the divergence-free operator class is exact.

## 6. No Einstein-tensor circularity

At RF-E23 the operator remains unnamed:

\[
\mathcal E_{\mu\nu}[g].
\]

The inputs are only

```text
independent source conservation
+ constant universal coupling
+ source-autonomy consistency
+ natural symmetric local metric operator class
```

The result is only

\[
\boxed{\nabla^\mu\mathcal E_{\mu\nu}\equiv0.}
\]

The identification

\[
\mathcal E_{\mu\nu}
=A G_{\mu\nu}+B g_{\mu\nu}
\]

belongs downstream to RF-E21 after the remaining naturality/metric-jet premises are supplied.

## 7. Dynamic-Lambda branch

RFC also carries the exchange law

\[
\boxed{
\kappa_E\nabla^\mu T_{\mu\nu}
=\nabla_\nu\Lambda_0.
}
\]

This branch is consistent with

\[
\mathcal E_{\mu\nu}
+\Lambda_0 g_{\mu\nu}
=\kappa_E T_{\mu\nu}
\]

provided the base geometric operator is identically divergence-free:

\[
\nabla^\mu\mathcal E_{\mu\nu}\equiv0.
\]

Then

\[
\nabla^\mu(\Lambda_0 g_{\mu\nu})
=\nabla_\nu\Lambda_0
\]

reproduces the admitted exchange ledger exactly.

Thus RF-E23 distinguishes:

```text
bare/natural gravitational operator     -> divergence-free class
constant cosmological coefficient       -> divergence-free metric term
dynamic Lambda0                         -> separately sourced scalar exchange branch
```

## 8. Composition with TIR A4 and RF-E21

TIR Gate A4 supplies, on the leading-refinement GR sector, the local metric-jet restriction

\[
\mathcal E_{\mu\nu}
=\mathcal E_{\mu\nu}(g,\partial g,\partial^2g).
\]

RF-G0/RF-E8 supply the four-dimensional Lorentzian metric carrier. RF-E23 supplies the divergence-free operator selection.

Therefore the RF-E21 theorem premises become locally:

```text
4D Lorentzian metric carrier                         PASS
natural/covariant metric tensor construction         PASS LOCAL
metric jet order <= 2                                PASS ON TIR LRR
symmetric rank-2 gravitational operator              DECLARED EQUATION TYPE
divergence-free operator class                       PASS ON RF-E23 CONSISTENCY RULE
```

RF-E21 then selects in four dimensions

\[
\boxed{
\mathcal E_{\mu\nu}
=A G_{\mu\nu}+B g_{\mu\nu}.
}
\]

## 9. Claim ledger

| Claim | Status |
|---|---|
| RF-E6 source conservation | `PARENT EXACT ON SOURCE EOM` |
| divergence of abstract constant-coupling field equation | `EXACT` |
| conserved source implies `nabla E=0` on coupled solutions | `EXACT` |
| universal-source autonomy rule | `RFC COUPLING SELECTION RULE` |
| universal-source autonomy selects identically divergence-free operator class | `PASS EXACT CONDITIONAL` |
| Einstein tensor used as premise | `NO` |
| dynamic-Lambda exchange compatibility | `PASS EXACT` |
| Lovelock identification after A4/E23 premises | `RF-E21 DOWNSTREAM THEOREM` |
| absolute physical value of `kappa_E` | `RF-E3 SEPARATE PROMOTION LINE` |

## 10. Updated local Einstein-form dependency

```text
TIR A2 Cartan refinement                            PASS
TIR A3 zero torsion / Levi-Civita                   PASS
TIR A4 leading-loop second metric-jet selection     PASS ON LRR
IDT + RF-G0/RF-E8 Lorentzian metric carrier         PASS LOCAL
RF-E6 independently conserved source                PASS
RF-E23 divergence-free operator selection           PASS ON CONSISTENCY RULE
RF-E21 4D Lovelock uniqueness                       PASS ON COMPOSED PREMISES
 -> A G_mn + B g_mn
 -> normalize A,B and source coupling
 -> Einstein equation with cosmological term
```
