# RF-E24 — Local Einstein-Form Closure from TIR × IDT × RFC

Status: `LOCAL_EINSTEIN_FORM_CLOSURE_PASS_ON_DECLARED_SELECTION_RULES / STANDARD_KAPPA_NORMALIZATION_TRANSFER_PASS / ADM_CONSTRAINT_EVOLUTION_PARENT_PASS / GLOBAL_SMOOTH_REALIZATION_OPEN / PROJECT_ABSOLUTE_G_PROMOTION_OPEN / HKT_CROSSCHECK_OPEN`

Date: 2026-08-30

## 1. Purpose

RF-E24 composes the now separately gated local geometry, locality and source-consistency results into the local metric field-equation form of general relativity.

The logical direction is

```text
TIR Cartan refinement + zero-torsion Levi-Civita sector
+ TIR Leading Refinement Rule (LRR)
+ IDT temporal orientation/lapse
+ RFC Lorentzian/ADM carrier
+ RFC universal-source autonomy rule
+ four-dimensional Lovelock uniqueness theorem
-> local Einstein tensor form
-> RF-E3 coupling normalization
-> RF-E12/RF-E13 ADM constraints, evolution and propagation
```

RF-E24 does not use the Einstein-Hilbert action as the premise selecting the tensor form. RF-E3 is consumed downstream for the independently established normalization transfer.

## 2. Exact pinned parents

### 2.1 TIR local spatial-GR geometry

Source repository:

`AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations`

Validated feature line:

`feat/tir-cartan-refinement-v0.1`

Gate A2/A3 hosted exact head:

`59b820e74c3b7be0e4cd81aa95ec0a23184e4f24`

Gate A4 hosted exact head:

`0ec6190f54a5bc64c5dfb89bdc77b48c6c144828`

The composed local spatial result is

\[
T^a=0,
\qquad
Dh=0,
\qquad
D=D^{LC},
\]

with nonzero curvature retained. Gate A4 supplies the leading-refinement metric-jet restriction

\[
\boxed{
\mathcal E_{\mu\nu}
=\mathcal E_{\mu\nu}(g,\partial g,\partial^2g)
}
\]

for the leading GR-selection sector under the explicitly declared TIR Leading Refinement Rule.

### 2.2 Four-dimensional Lorentzian carrier

RF-G0 and RF-E8, with the IDT temporal orientation and positive lapse, supply a local four-dimensional metric with

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

RF-E22 binds the TIR Cartan/Levi-Civita gates into this RFC carrier and records the remaining global-refinement firewall.

### 2.3 Conserved-source operator class

RF-E6 independently supplies conserved admitted matter/source tensors on their source equations of motion. RF-E23 applies the universal-source autonomy rule to the abstract gravitational equation and selects

\[
\boxed{
\nabla^\mu\mathcal E_{\mu\nu}\equiv0
}
\]

before the geometric operator is identified with the Einstein tensor.

## 3. Abstract local field equation

Write the local universal metric/source equation before tensor-form selection as

\[
\boxed{
\mathcal E_{\mu\nu}[g]
=C\,T_{\mu\nu},
}
\]

where `C` is a spacetime-constant coupling coordinate and `mathcal E_mn` is a symmetric natural rank-two metric operator in the leading local class selected above.

At this stage no Einstein tensor formula is inserted.

## 4. Four-dimensional uniqueness step

The RF-E21 four-dimensional Lovelock tensor theorem applies to the composed local premise set:

```text
four-dimensional Lorentzian metric carrier       PASS LOCAL
natural/covariant metric construction             PASS LOCAL
metric derivative order <= 2                     PASS ON TIR LRR
symmetric rank-two equation type                  DECLARED
identically divergence-free operator class        PASS ON RF-E23 RULE
```

Therefore

\[
\boxed{
\mathcal E_{\mu\nu}
=A\,G_{\mu\nu}+B\,g_{\mu\nu}
}
\]

for constants `A,B` on the selected local branch.

Substitution into the abstract source equation gives

\[
A G_{\mu\nu}+B g_{\mu\nu}
=C T_{\mu\nu}.
\]

For the nondegenerate dynamical branch `A != 0`, divide by `A` and define

\[
\boxed{
\Lambda:=\frac BA,
\qquad
\kappa_E:=\frac CA.
}
\]

Then

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\kappa_E T_{\mu\nu}.
}
\]

This is the local Einstein field-equation form, obtained after the project-owned local selection rules have supplied the Lovelock premise class.

## 5. Coupling normalization

RF-E3 independently carries the exact conventional/Newton-Einstein normalization transfer

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}.
}
\]

Hence the normalized local field equation is

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

The algebraic transfer and SI normalization are exact on the stated convention. The project-internal derivation of the absolute physical value of `G` from the double-copy/carrier line retains the RF-E3 promotion gates and is not needed to establish the tensor form itself.

## 6. Einstein-Hilbert action as downstream representative

Once the local tensor form has been selected, the action-side Lovelock cross-check in RF-E21 shows that in four dimensions the corresponding leading local metric action is represented, up to boundary/topological terms, by

\[
\boxed{
S_g
=\frac{1}{2\kappa_E}
\int d^4x\sqrt{-g}\,(R-2\Lambda).
}
\]

Thus the Einstein-Hilbert form now appears downstream as the action representative of the selected local dynamics rather than as the premise that chooses the field tensor.

## 7. ADM dynamical closure roundtrip

RF-E12 and RF-E13 already supply the 3+1 projections and evolution system for this tensor equation. In particular, for constant `Lambda` the Hamiltonian and momentum constraints are

\[
\boxed{
{}^{(3)}R+K^2-K_{ij}K^{ij}-2\Lambda
=2\kappa_E\rho_n,
}
\]

\[
\boxed{
D_jK^j{}_i-D_iK
=\kappa_Ej_i.
}
\]

RF-E13 supplies

\[
\boxed{
(\partial_0-\mathcal L_b)h_{ij}=-2NK_{ij}
}
\]

and the corresponding `K_ij` evolution equation, together with homogeneous Bianchi propagation of the Hamiltonian/momentum residuals.

Therefore RF-E24 does not stop at a covariant tensor identity: it roundtrips to the already validated ADM constraint/evolution closure on the same admitted local smooth sector.

## 8. Dynamic-Lambda branch

RFC separately carries the scalar exchange branch

\[
\kappa_E\nabla^\mu T_{\mu\nu}=\nabla_\nu\Lambda_0.
\]

RF-E23 shows that an identically divergence-free base geometric operator remains compatible with

\[
G_{\mu\nu}+\Lambda_0 g_{\mu\nu}=\kappa_E T_{\mu\nu}
\]

when the scalar exchange law is used. Independent `Lambda0` dynamics and its physical calibration retain their dedicated RFC gates.

## 9. Global and independent-cross-check frontier

The local Einstein-form theorem is distinct from two downstream promotions.

### Global realization

TIR Gate A3 keeps open the global existence/stability theorem for a smooth compatible refinement across the full relational complex. RF-E24 therefore promotes the equation on the admitted local/regular continuum sector and leaves global realization as a separate topology/refinement problem.

### HKT cross-check

RF-E21 retains Hojman-Kuchar-Teitelboim as an independent route. A project-owned gravitational canonical momentum `pi^{ij}` and independently derived hypersurface-deformation algebra remain to be constructed before HKT can serve as a non-circular second proof.

## 10. Claim ledger

| Claim | Status |
|---|---|
| TIR Cartan curvature/torsion refinement | `PARENT HOSTED PASS` |
| local zero-torsion metric-compatible Levi-Civita sector | `PARENT HOSTED PASS` |
| leading metric-jet order <= 2 | `PASS ON TIR LRR / HOSTED GATE` |
| local Lorentzian 4D carrier | `PARENT PASS` |
| independently conserved admitted source | `PARENT PASS` |
| divergence-free unknown operator class | `PASS ON RFC UNIVERSAL-SOURCE AUTONOMY RULE` |
| 4D Lovelock form `A G_mn + B g_mn` | `STANDARD EXACT THEOREM ON COMPOSED PREMISES` |
| `Lambda=B/A`, `kappa_E=C/A` for `A!=0` | `EXACT ALGEBRA` |
| local Einstein form `G_mn+Lambda g_mn=kappa_E T_mn` | `PASS ON DECLARED TIR/RFC SELECTION RULES` |
| `kappa_E=8 pi G/c^4` normalization transfer | `RF-E3 EXACT CONVENTIONAL TRANSFER` |
| ADM constraint/evolution/propagation roundtrip | `RF-E12/RF-E13 PARENT PASS` |
| global smooth relational realization | `OPEN` |
| project-derived absolute physical `G` | `OPEN SEPARATE RF-E3 COUPLING LINE` |
| independent HKT proof | `OPEN CROSS-CHECK` |

## 11. Result

Within the declared TIR Leading Refinement Rule and RFC universal-source autonomy rule, the local TIR × IDT continuum carrier satisfies the RF-E21 Lovelock premise set. Therefore the leading local metric field equation is selected to

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}
}
\]

with RF-E12/RF-E13 supplying the corresponding ADM constraints, evolution and constraint propagation.

Validation authority:

`tests/reference/test_rfe24_local_einstein_form_closure.py`

`validation/RF_E24_LOCAL_EINSTEIN_FORM_CLOSURE_V0_1.json`

Verdict target:

`PASS_RF_E24_LOCAL_EINSTEIN_FORM_CLOSURE`.
