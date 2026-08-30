# RF-E21 — TIR × IDT 4D Einstein-Action Selection Gate

Status: `SOURCE_BOUND_3PLUS1_CARRIER / LORENTZIAN_SIGNATURE_PARENT_EXACT / FOUR_DIMENSIONAL_LOVELOCK_SELECTION_PASS_CONDITIONAL / RF_E3_NORMALIZATION_EXACT_ON_PARENT_COUPLING / RF_E12_E13_ADM_DYNAMICS_INHERITED / NATIVE_ADMISSIBILITY_DERIVATION_OPEN`

## 1. Purpose

RF-E21 isolates the remaining action-selection step between the project-native spatial/temporal carriers and the already implemented Einstein/ADM dynamics.

The upstream repositories now supply the following typed chain:

```text
TIR rank-three positive spatial carrier
 + IDT oriented positive clock/lapse carrier
 -> RF-G0 Lorentzian 3+1 metric
 -> RF-E21 gravitational bulk-action selection
 -> RF-E3 action normalization
 -> RF-E12 Einstein equation and ADM source constraints
 -> RF-E13 ADM evolution and Bianchi constraint propagation
```

RF-E21 assigns one owner to the bulk gravitational-action selection. It keeps action selection, coupling normalization, matter composition and ADM propagation as separately auditable layers.

## 2. Source-pinned 3+1 carrier

### 2.1 TIR spatial parent

TIR main at

`3f5a08ef04ec53c1a155263d23e8b10a96404370`

contains the promoted spatial chain through the Universal-Loop torsion source and the rank-three positive spatial carrier used by the RFC geometry line.

The local spatial metric has rank

\[
\boxed{\operatorname{rank}h_\perp=3},
\]

with positive quadratic form on the admitted instantaneous distribution.

### 2.2 IDT temporal parent

IDT main at

`84ce1886175af872ae4a56ba36f7e106d8e23635`

supplies the activity-derived relational lapse

\[
\boxed{
N_R(x|r)=\frac{d\Theta_x}{d\Theta_r}
=\frac{\mathfrak a_x}{\mathfrak a_r}>0
}
\]

with exact reparameterization invariance and clock-reference composition.

The calibrated temporal one-form exported to the relativistic bridge is

\[
\boxed{\Theta_R=N_R c\,dt}.
\]

IDT also supplies the exact hyperbolic kinetic invariant

\[
\boxed{\mathfrak a^2-\mathfrak j^2=4M^2},
\]

which provides an independent temporal orientation/magnitude decomposition.

### 2.3 RF-G0 spacetime assembly

RF-G0 constructs

\[
\boxed{
g=-\Theta\otimes\Theta+h_\perp
}
\]

from one oriented temporal covector and the positive rank-three spatial form. Its temporal-reflection theorem gives

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

Thus the source-bound carrier entering RF-E21 is four-dimensional and Lorentzian.

## 3. Action admissibility surface

RF-E21 now separates the carrier theorem from the gravitational action admissibility conditions.

For the local bulk metric dynamics define the admissibility tuple

\[
\boxed{
\mathfrak A_{E21}
=
(D=4,\;
\text{Lorentzian metric},\;
\text{diffeomorphism covariance},\;
\text{local metric bulk action},\;
\text{second-order metric equations})
}.
\]

Current ownership is:

| Coordinate | Source / status |
|---|---|
| \(D=3+1=4\) | TIR spatial rank 3 + IDT temporal rank 1 — source bound |
| Lorentzian metric | RF-G0 temporal-reflection theorem — exact parent |
| diffeomorphism covariance | RFC gravitational admissibility condition — native derivation OPEN |
| local metric bulk action | RFC gravitational admissibility condition — native derivation OPEN |
| second-order metric equations | RFC gravitational admissibility condition — native derivation OPEN |

The last three coordinates are explicit theorem hypotheses at this gate. Future native derivations may promote them individually without changing the downstream algebra.

## 4. Four-dimensional Lovelock selection

External mathematical parent: the four-dimensional Lovelock uniqueness theorem.

On the complete admissibility surface \(\mathfrak A_{E21}\), the local metric field equation is generated, up to coupling constants and four-dimensional topological/boundary densities, by the cosmological and Einstein-Hilbert bulk terms.

The selected local bulk basis is therefore

\[
\boxed{
\mathcal B_{\rm grav}^{(4)}
=
\{1,\;R\}.
}
\]

Equivalently, the bulk action may be written

\[
\boxed{
S_g
=
A\int d^4x\,\sqrt{-g}\,[R-2\Lambda]
+
S_{\rm top}
+
S_{\rm boundary},
}
\]

where the four-dimensional Euler/Gauss-Bonnet density may enter \(S_{\rm top}\) while carrying no additional local bulk metric equation, and the standard boundary contribution carries the well-posed metric-variation boundary data.

This is a conditional selection theorem: the Lovelock parent closes the bulk basis once every coordinate of \(\mathfrak A_{E21}\) is admitted.

## 5. RF-E3 normalization transfer

RF-E3 fixes the Einstein-Hilbert normalization convention

\[
\boxed{
A=\frac{c^4}{16\pi G}
=\frac{1}{2\kappa_E}.
}
\]

Therefore

\[
\boxed{
\kappa_E
=\frac1{2A}
=\frac{8\pi G}{c^4}.
}
\]

With the matter definition

\[
T_{\mu\nu}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta S_m}{\delta g^{\mu\nu}},
\]

stationarity gives the RF-E12 tensor equation

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

The coefficient transfer is exact once the RF-E3 \(G\)/\(\kappa_E\) parent is admitted.

## 6. ADM inheritance

RF-E10 and RF-E12 give the Hamiltonian and momentum source constraints. For constant \(\Lambda\),

\[
\boxed{
{}^{(3)}R+K^2-K_{ij}K^{ij}-2\Lambda
=
2\kappa_E\rho
}
\]

and

\[
\boxed{
D_j(K^j{}_i-\delta^j_iK)
=
\kappa_E j_i.
}
\]

RF-E13 supplies the evolution equations

\[
\boxed{
(\partial_t-\mathcal L_\beta)h_{ij}
=
-2NK_{ij}
}
\]

and

\[
\boxed{
(\partial_t-\mathcal L_\beta)K_{ij}
=
-D_iD_jN
+
N\left[
{}^{(3)}R_{ij}
-2K_i{}^kK_{kj}
+KK_{ij}
-\kappa_ES_{ij}
+\frac{\kappa_E}{2}h_{ij}(S-\rho)
\right]
}
\]

for the zero-\(\Lambda\) displayed parent convention, with the corresponding \(\Lambda\) contribution inherited from the selected action branch.

The Bianchi/source-conservation ledger gives homogeneous propagation of the Hamiltonian and momentum residuals. Hence vanishing initial constraints remain vanishing under the admitted evolution system.

## 7. Exact closure statement

Define the parent set

\[
\mathcal P_{GR}
=
\{
\text{TIR rank-3 spatial carrier},
\text{IDT oriented lapse/clock carrier},
\text{RF-G0 Lorentz metric},
\mathfrak A_{E21},
\text{4D Lovelock theorem},
\text{RF-E3 normalization},
\text{RFC matter action}
\}.
\]

Then RF-E21 records the conditional implication

\[
\boxed{
\mathcal P_{GR}
\Longrightarrow
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}
}
\]

together with the RF-E12/RF-E13 ADM constraint, evolution and propagation system.

The remaining first-principles programme is sharply localized to the native promotion of the three action-admissibility coordinates and the independent physical determination of the project-side \(G\)/\(\kappa_E\) value.

## 8. GREMLIN audit roles

GREMLIN remains bounded to candidate/audit authority:

```text
SPIDER  dependency graph from TIR/IDT carriers to RF-E21
MOLE    coefficient and projection algebra
HOUND   premise-leak and higher-derivative counterexample audit
MANTIS  duplicate Einstein-action ownership audit
OWL     cross-repository commit/source provenance
```

Promotion authority remains theorem/validator/evidence gated.

## 9. Validation contract

Reference implementation:

`src/rfc/einstein_action_selection.py`

Reference tests:

`tests/reference/test_rfe21_einstein_action_selection.py`

Validation receipt:

`validation/RF_E21_TIR_IDT_EINSTEIN_ACTION_SELECTION_V0_1.json`

The deterministic checks cover:

1. source-typed \(3+1\) rank composition;
2. \((-+++)\) signature encoding inherited from RF-G0;
3. fail-closed Lovelock admissibility coordinates;
4. selected local bulk basis \(\{1,R\}\);
5. exact RF-E3 coefficient transfer
   \[
   c^4/(16\pi G)\mapsto8\pi G/c^4;
   \]
6. explicit separation between conditional action selection and native admissibility promotion.

## 10. Promotion frontier

```text
TIR_SPATIAL_RANK3                         SOURCE BOUND / PROMOTED PARENT
IDT_POSITIVE_RELATIONAL_LAPSE             SOURCE BOUND / EXACT RATIO
RF_G0_LORENTZIAN_SIGNATURE                PARENT EXACT
RF_E21_4D_LOVELOCK_BULK_SELECTION         PASS CONDITIONAL
RF_E3_EH_NORMALIZATION                    PARENT EXACT ON ADMITTED COUPLING
RF_E12_EINSTEIN_ADM_CONSTRAINTS           PARENT EXACT ON STATED ACTION
RF_E13_ADM_EVOLUTION_PROPAGATION           PARENT EXACT
NATIVE_DIFFEO_COVARIANCE_DERIVATION        OPEN
NATIVE_LOCAL_METRIC_ACTION_DERIVATION      OPEN
NATIVE_SECOND_ORDER_DYNAMICS_DERIVATION    OPEN
PROJECT_SIDE_G_NEWTON_UNIVERSALITY         OPEN
```

RF-E21 therefore converts the broad “Einstein closure” frontier into four explicit remaining promotion coordinates rather than one undifferentiated gap.
