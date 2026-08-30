# RF-E21 — Einstein Tensor Uniqueness Selection from TIR × IDT Geometry

Status: `EXACT_LOVELOCK_SELECTION_THEOREM_ON_DECLARED_PREMISES / TIR_IDT_4D_CARRIER_PRESENT / LEVI_CIVITA_GLOBAL_PROMOTION_OPEN / SECOND_ORDER_NATURALITY_GATE_OPEN / HKT_INDEPENDENT_ROUTE_OPEN`

## 1. Purpose

RF-E21 removes the remaining circularity between the already assembled TIR × IDT spacetime carrier and RF-E3.

RF-E3 proves the coefficient transfer and standard metric variation once the Einstein–Hilbert action is written. RF-E21 asks the logically prior question:

\[
\boxed{\text{Why is the metric-side local curvature tensor }G_{\mu\nu}+\Lambda g_{\mu\nu}\text{ selected?}}
\]

The answer is recorded as a theorem gate rather than an imported definition.

Two independent uniqueness routes are kept separately typed:

1. the four-dimensional Lovelock tensor/action route;
2. the Hojman–Kuchař–Teitelboim (HKT) hypersurface-deformation route.

GREMLIN may compare the two dependency graphs, but neither route is promoted by GREMLIN itself.

## 2. Upstream TIR × IDT spacetime carrier

The current repository graph already supplies the following components.

### 2.1 Spatial rank

RF-02H constructs a local positive rank-three metric from the hexahedral multi-state projective carrier,

\[
h_\perp>0,\qquad \operatorname{rank}h_\perp=3.
\]

### 2.2 Temporal orientation and Lorentzian reflection

RF-G0 takes one nonzero oriented IDT temporal covector \(\Theta\) and the positive spatial metric on \(\ker\Theta\), and defines

\[
g=-\Theta\otimes\Theta+h_\perp.
\]

Its temporal-reflection theorem gives

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

IDT 05C additionally supplies a positive relational lapse \(N_R>0\), while RF-E8 assembles the ADM block metric.

### 2.3 Connection and curvature

RF-02I proves the unique torsion-free metric connection of the physicalized coframe on the declared torsion-free reference-coframe surface. Its global cell-refinement and torsion-selection promotion remains separately gated.

Thus RF-E21 distinguishes:

```text
local Lorentzian metric carrier                 PRESENT
local spatial metric-compatible connection      PRESENT ON RF-02I PREMISE SURFACE
global/refinement Levi-Civita promotion          OPEN
```

## 3. Tensor-side Lovelock selection

Use the standard four-dimensional Lovelock uniqueness theorem in its tensor-concomitant form.

On a smooth four-dimensional metric manifold, consider a symmetric rank-two geometric tensor \(E_{\mu\nu}[g]\) satisfying the standard Lovelock naturality/regularity hypotheses and depending locally on the metric and its derivatives through at most second differential order. Require

\[
\boxed{\nabla^\mu E_{\mu\nu}\equiv0.}
\]

Then in four dimensions the metric-side tensor is restricted to

\[
\boxed{
E_{\mu\nu}
=A\,G_{\mu\nu}+B\,g_{\mu\nu}.
}
\]

For \(A\ne0\), define

\[
\kappa_E:=A^{-1},
\qquad
\Lambda:=\frac{B}{A}.
\]

Coupling to an admitted conserved matter/source tensor gives

\[
E_{\mu\nu}=\kappa_E^{-1}\kappa_E T_{\mu\nu}
\]

or equivalently

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\kappa_E T_{\mu\nu}.
}
\]

The role of RF-E21 is the selection of the tensor form. RF-E3 owns the independent normalization transfer

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}
}
\]

after its Newton/double-copy promotion gates are satisfied.

## 4. Action-side cross-check

If the additional action-principle hypothesis is admitted, the four-dimensional Lovelock action classification gives

\[
\mathcal L_g
=\sqrt{-g}\left(c_0+c_1R+c_2\mathcal G\right)
\]

up to a boundary term, where

\[
\mathcal G
=R^2-4R_{\mu\nu}R^{\mu\nu}
+R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
\]

is the Gauss–Bonnet density.

In \(D=4\),

```text
curvature order 0    cosmological term     DYNAMIC
curvature order 1    Ricci scalar R        DYNAMIC
curvature order 2    Gauss–Bonnet          TOPOLOGICAL
curvature order >=3  Lovelock density      ZERO in D=4
```

so the local metric dynamics reduce to

\[
\boxed{
S_g
=\frac1{2\kappa_E}
\int d^4x\,\sqrt{-g}\,(R-2\Lambda)
}
\]

up to boundary/topological terms.

This makes RF-E3's Einstein–Hilbert action a downstream representative of the selected four-dimensional local second-order metric dynamics rather than the source of that selection.

## 5. Project premise ledger

RF-E21 is fail-closed. The mathematical selection theorem is exact on its declared premises; project-side promotion requires the premises to be supplied by the dependency graph.

| Premise | Current project source | Status |
|---|---|---|
| one temporal direction + rank-3 positive spatial carrier | RF-G0 + RF-02H + IDT | `PASS_LOCAL_CARRIER` |
| Lorentzian signature | RF-G0 temporal reflection | `PASS_THEOREM_ON_CARRIER` |
| positive lapse / ADM block metric | IDT 05C + RF-E8 | `PASS_KINEMATIC` |
| metric-compatible torsion-free connection | RF-02I | `PASS_LOCAL_ON_REFERENCE_TORSION_FREE_SURFACE` |
| global/refinement Levi-Civita promotion | TIR/RF-02I continuum line | `OPEN` |
| full 4D tensor naturality / diffeomorphism covariance | TIR × IDT × RFC join | `OPEN` |
| metric-side locality through at most second differential order | continuum closure principle | `OPEN` |
| symmetric divergence-free geometric source operator | conservation/Bianchi compatibility target | `OPEN_SELECTION_BINDING` |
| tensor Lovelock theorem once premises are admitted | standard theorem | `PASS_EXTERNAL_THEOREM` |
| RF-E3 coupling normalization | RF-N1C/RF-E3 | `PASS_ALGEBRA / PHYSICAL_VALUE_CONDITIONAL` |

Accordingly, RF-E21 advances the dependency graph to

```text
TIR rank-3 spatial carrier
 + IDT temporal orientation/lapse
 -> RF-G0 / RF-E8 four-metric
 -> RF-02I local metric connection
 -> [global Levi-Civita + 4D naturality + second-order locality]
 -> LOVELOCK UNIQUE TENSOR FORM
 -> G_mn + Lambda g_mn
 -> RF-E3 normalization
 -> RF-E12 ADM projections
 -> RF-E13 constraint/evolution propagation
```

## 6. HKT independent route

The Hojman–Kuchař–Teitelboim route is retained as a logically independent cross-check.

For a spatial metric \(h_{ij}\) and an independently derived gravitational canonical momentum \(\pi^{ij}\), define the smeared normal and tangential deformation generators \(H[N]\) and \(H_i[N^i]\).

The target hypersurface-deformation algebra is

\[
\{H_i[N^i],H_j[M^j]\}
=
H_k[N^i\partial_iM^k-M^i\partial_iN^k],
\]

\[
\{H_i[N^i],H[M]\}
=
H[\mathcal L_N M],
\]

and

\[
\boxed{
\{H[N],H[M]\}
=
H_i\!\left[
h^{ij}(N\partial_jM-M\partial_jN)
\right].
}
\]

Under the standard HKT hypotheses, the representation is the ADM geometrodynamics of general relativity.

Current independent HKT ledger:

```text
h_ij spatial metric                         PRESENT
N_R lapse                                   PRESENT
b^i shift                                   PRESENT AS TYPED RFC INPUT
independent gravitational pi^ij             OPEN
independent HDA derivation                   OPEN
HKT no-circularity cross-check               OPEN
```

Existing RF-E12/RF-E13 constraints cannot be used as the independent HKT proof because they are downstream of RF-E3. RF-E21 therefore keeps HKT as a future falsification/cross-check route.

## 7. Minimal remaining theorem frontier

The Einstein-form frontier is now reduced to three project-owned promotion questions:

\[
\boxed{
\text{GLOBAL LEVI-CIVITA}
\quad+\quad
\text{4D NATURALITY / COVARIANCE}
\quad+\quad
\text{SECOND-ORDER LOCALITY}
}
\]

Once these are promoted on the TIR × IDT carrier, the tensor-side Lovelock theorem selects

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
}
\]

before RF-E3 supplies its coupling normalization.

A second, independent closure can later be obtained by deriving the HDA from relational slice gluing and constructing the gravitational canonical pair.

## 8. Falsification rules

RF-E21 fails promotion if any of the following occurs:

1. the continuum carrier has dimension other than four;
2. the admitted connection has physical torsion/non-metricity on the target GR sector;
3. the geometric field operator requires independent higher-than-second-order metric derivatives;
4. extra gravitational fields are required inside the metric-side uniqueness sector without a separately typed extension;
5. the selected source operator is not covariantly divergence-free on the conserved-source branch;
6. the HKT cross-check is claimed using RF-E12/RF-E13 as premises rather than an independent HDA derivation.

## 9. Claim ledger

| Claim | Status |
|---|---|
| 4D Lovelock dynamic orders are \(0,1\) | `EXACT STANDARD THEOREM CONSEQUENCE` |
| Gauss–Bonnet is topological in \(D=4\) | `EXACT STANDARD THEOREM CONSEQUENCE` |
| tensor form \(A G_{\mu\nu}+B g_{\mu\nu}\) on Lovelock premises | `EXACT STANDARD THEOREM` |
| RF-G0 local Lorentzian signature | `PARENT EXACT THEOREM` |
| RF-E8 ADM block algebra | `PARENT EXACT KINEMATIC` |
| RF-02I local torsion-free metric connection | `PARENT EXACT ON DECLARED REFERENCE SURFACE` |
| global project Levi-Civita promotion | `OPEN` |
| full 4D naturality/covariance promotion | `OPEN` |
| second-order locality promotion | `OPEN` |
| Einstein tensor form after all project premises pass | `CONDITIONAL PROMOTION TARGET` |
| \(\kappa_E=8\pi G/c^4\) project value | `RF-E3 PHYSICAL PROMOTION CONDITIONAL` |
| HKT independent cross-check | `OPEN` |

## 10. Validation authority

Reference implementation:

`src/rfc/einstein_uniqueness_selection.py`

Reference tests:

`tests/reference/test_rfe21_einstein_uniqueness_selection.py`

Validation receipt:

`validation/RF_E21_EINSTEIN_UNIQUENESS_SELECTION_V0_1.json`

External theorem anchors:

- D. Lovelock, *The Einstein tensor and its generalizations*, Journal of Mathematical Physics 12 (1971).
- D. Lovelock, *The four-dimensionality of space and the Einstein tensor*, Journal of Mathematical Physics 13 (1972).
- S. A. Hojman, K. Kuchař, C. Teitelboim, *Geometrodynamics Regained*, Annals of Physics 96 (1976).

Verdict target:

`PASS_RF_E21_SELECTION_THEOREM_WITH_PROJECT_PREMISES_OPEN`.
