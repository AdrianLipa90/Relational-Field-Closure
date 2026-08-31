# RF-E21 — TIR × IDT 4D Einstein-Action Selection Gate v0.2

Status: `SOURCE_BOUND_3PLUS1_CARRIER / LORENTZIAN_SIGNATURE_PARENT_EXACT / COVARIANT_ACTION_SUPPORT_PRESENT / SPIN2_4PT_5PT_SUPPORT_PRESENT / FOUR_DIMENSIONAL_LOVELOCK_SELECTION_PASS_CONDITIONAL / RF_E3_NORMALIZATION_EXACT_ON_PARENT_COUPLING / RF_E12_E13_ADM_DYNAMICS_INHERITED / THREE_NATIVE_PROMOTION_GATES_OPEN`

Supersedes the frontier classification in RF-E21 v0.1 while retaining its receipt as provenance.

## 1. Purpose

RF-E21 owns the gravitational bulk-action selection step between project-native
spatial/temporal carriers and the RFC Einstein/ADM dynamics.

The current dependency chain is

```text
TIR rank-three positive spatial carrier
 + IDT oriented positive lapse/clock carrier
 -> RF-G0 Lorentzian 3+1 metric
 -> RFC covariant/spin-2 support surfaces
 -> RF-E21 4D gravitational action-selection gate
 -> RF-E3 Einstein-Hilbert normalization
 -> RF-E12 Einstein tensor equation + ADM source constraints
 -> RF-E13 ADM evolution + Bianchi constraint propagation
```

The gate separates four logically different layers:

1. source-bound spacetime carrier;
2. evidence supporting gravitational covariance/action architecture;
3. conditional mathematical action selection;
4. physical coupling universality.

## 2. Source-bound 3+1 carrier

### 2.1 Spatial parent

TIR main parent:

`3f5a08ef04ec53c1a155263d23e8b10a96404370`

The promoted TIR spatial line supplies a positive rank-three local carrier,

\[
\boxed{\operatorname{rank}h_\perp=3}.
\]

### 2.2 Temporal parent

IDT main parent:

`84ce1886175af872ae4a56ba36f7e106d8e23635`

The relational lapse surface supplies

\[
\boxed{
N_R(x|r)
=
\frac{d\Theta_x}{d\Theta_r}
=
\frac{\mathfrak a_x}{\mathfrak a_r}>0
}
\]

with exact reparameterization invariance and clock-reference composition.  Its
relativistic export is

\[
\boxed{\Theta_R=N_Rc\,dt}.
\]

The temporal kinetic branch also carries

\[
\boxed{\mathfrak a^2-\mathfrak j^2=4M^2}.
\]

### 2.3 Lorentzian assembly

RF-G0 assembles

\[
\boxed{g=-\Theta\otimes\Theta+h_\perp}
\]

and, for one temporal direction plus the positive spatial rank-three carrier,
obtains

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

Thus RF-E21 receives a source-bound four-dimensional Lorentzian metric carrier.

## 3. Existing covariance/action support surfaces

RF-E21 v0.2 distinguishes supporting receipts from theorem promotion.

### 3.1 Covariant common-action architecture — RF-F13

RF-F13 already supplies a shared covariant action surface of the form

\[
S_{\rm common}
=
\int d^4x\,\sqrt{-g}\,\mathcal L_{\rm common},
\]

with metric variation, Bianchi/Noether bookkeeping and a common matter/source
exchange ledger.

RF-F13 therefore supports a project-compatible covariant action architecture.
Its gravitational \(R\) term enters there as an admitted parent; RF-E21 owns
the independent selection theorem for the Einstein-Hilbert term.

### 3.2 Linearized spin-2 covariance — RFG18

RFG18 passes the external-state linearized diffeomorphism Ward replacement

\[
\epsilon_{\mu\nu}
\mapsto
\epsilon_{\mu\nu}
+k_\mu\xi_\nu+k_\nu\xi_\mu
\]

on its four-point pure-spin-2 surface.

This is a direct linearized covariance witness.

### 3.3 Einstein / double-copy amplitude support

The project gravity amplitude line contains:

- `RFG20` — four-point Einstein MHV normalization firewall;
- `RFG27` — five-point project normalization firewall;
- `RFG29` — five-point BCJ root/Jacobi validation;
- `RFG30` — five-point project pre-KLT closure.

These surfaces show compatibility beyond one four-point sample and make the
spin-2/Einstein normalization line substantially more constrained.

Their publication role is finite-order support.  The all-orders nonlinear
gravitational covariance promotion is owned by its dedicated gate below.

## 4. Conditional 4D action selection

Define the Lovelock admissibility tuple

\[
\boxed{
\mathfrak A_{E21}
=
(D=4,\;
\text{Lorentzian metric},\;
\text{diffeomorphism covariance},\;
\text{local metric bulk dynamics},\;
\text{second-order metric equations})
}.
\]

The first two coordinates are source-bound by the TIR×IDT/RF-G0 chain.

For the remaining coordinates, RFC now has substantial support:
RF-F13 for covariant action architecture and RFG18/RFG20/RFG27/RFG29/RFG30
for the spin-2 covariance/Einstein amplitude line.  The project-native theorem
promoting this support to nonlinear all-orders covariance and the project
selection principle forcing local second-order metric dynamics are explicit
downstream gates.

External mathematical parent: the four-dimensional Lovelock uniqueness theorem.

On the complete admitted tuple \(\mathfrak A_{E21}\), the local metric bulk
basis affecting the four-dimensional field equations is

\[
\boxed{
\mathcal B_{\rm grav}^{(4)}
=
\{1,R\}
}
\]

up to four-dimensional topological and boundary densities.  Hence

\[
\boxed{
S_g
=
A\int d^4x\,\sqrt{-g}\,(R-2\Lambda)
+
S_{\rm top}
+
S_{\rm boundary}.
}
\]

The Euler/Gauss-Bonnet density may occur in the topological ledger while adding
no independent local four-dimensional metric equation under this gate.

This is a conditional selection theorem.  The deterministic implementation
fails closed whenever a required admissibility coordinate is absent.

## 5. Exact Einstein normalization transfer

RF-E3 owns

\[
\boxed{
A=\frac{c^4}{16\pi G}
=\frac{1}{2\kappa_E}
}.
\]

Therefore

\[
\boxed{
\kappa_E
=
\frac{1}{2A}
=
\frac{8\pi G}{c^4}.
}
\]

With

\[
T_{\mu\nu}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta S_m}{\delta g^{\mu\nu}},
\]

RF-E12 gives

\[
\boxed{
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

The coefficient transfer is exact on the admitted RF-E3 coupling parent.

## 6. ADM constraint/evolution closure

RF-E12 supplies the projected source constraints, including

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
\kappa_Ej_i.
}
\]

RF-E13 supplies

\[
\boxed{
(\partial_t-\mathcal L_\beta)h_{ij}
=
-2NK_{ij}
}
\]

and the corresponding \(K_{ij}\) evolution equation, together with homogeneous
Bianchi propagation of the Hamiltonian and momentum residuals.

Thus ADM kinematics, constraints, evolution and constraint propagation are
downstream closed once the Einstein action branch is admitted.

## 7. Reduced-gravity / Newton coupling line

RF-F25 defines the project-side reduced-gravity coordinate

\[
\boxed{
\bar M_{G,i}
=
-\frac1{\beta_W}
\ln\!\left[
\frac{|\omega_{t,i}|^2}
{16\pi\Gamma_{DC}M_\star^3}
\right].
}
\]

The reference pair gives

\[
\bar M_G=\beta_W^{-1}\ln2.
\]

RF-F26 already defines the fail-closed promotion protocol:
freeze the prerequisite normalization surfaces, admit at least two independent
nondegenerate realized pairs, and require a common \(\bar M_G\) within the
declared tolerance before promoting the physical \(G\).

The architecture of the universality test is therefore present.  The remaining
gate is the realized independent admission itself.

## 8. Three-coordinate native completion frontier

RF-E21 v0.2 reduces the broad Einstein-closure frontier to exactly three
project-native promotion coordinates:

```text
NONLINEAR_ALL_ORDERS_GRAVITATIONAL_COVARIANCE_PROMOTION
NATIVE_LOCAL_SECOND_ORDER_METRIC_GRAVITY_SELECTION
REALIZED_INDEPENDENT_REDUCED_GRAVITY_UNIVERSALITY_ADMISSION
```

### 8.1 Nonlinear all-orders covariance promotion

RF-F13 and the RFG18/RFG20/RFG27/RFG29/RFG30 sequence are strong supporting
surfaces.  The remaining promotion target is a theorem or equivalent
source-complete construction that extends the admitted gravitational covariance
from the current covariant/finite-order surfaces to the nonlinear all-orders
gravity object.

### 8.2 Native local/second-order selection principle

RF-E13 verifies that the selected Einstein system has second-order evolution.
Upstream action selection is assigned to a separate project-native principle.

The remaining target is that project-native principle selecting local,
second-order metric gravitational dynamics before the external Lovelock theorem
is invoked.

### 8.3 Realized independent reduced-gravity universality

RF-F25/RF-F26 provide the coordinate and promotion firewall.  The remaining
target is the independently sourced multi-pair realization required by that
firewall, with the prerequisite \(\beta_W,\Gamma_{DC},M_\star\) surfaces frozen.

## 9. Standard-GR boundary

For a constant cosmological term, the conditional RF-E21 → RF-E3 → RF-E12 →
RF-E13 chain already carries the standard Einstein equation and ADM system.

The independent dynamic-\(\Lambda\) action/stability programme is an extension
frontier beyond the constant-\(\Lambda\) standard-GR closure.

Additional matter species remain a matter-composition frontier alongside the
RF-E21 gravitational action-selection logic.

## 10. GREMLIN audit roles

```text
SPIDER  dependency ownership and cross-repository graph
MOLE    coefficient/projection algebra
HOUND   premise-leak, circularity and higher-derivative audit
MANTIS  duplicate action/Einstein ownership audit
OWL     source and commit provenance
```

GREMLIN is a bounded candidate/audit layer.  Promotion authority remains with
the theorem/validator/evidence gates.

## 11. Validation contract

Reference implementation:

`src/rfc/einstein_action_selection.py`

Reference tests:

`tests/reference/test_rfe21_einstein_action_selection.py`

Receipts:

- `validation/RF_E21_TIR_IDT_EINSTEIN_ACTION_SELECTION_V0_1.json`
  — historical initial classification;
- `validation/RF_E21_TIR_IDT_EINSTEIN_ACTION_SELECTION_V0_2.json`
  — refined three-gate classification.

The v0.2 deterministic checks cover:

1. source-typed \(3+1\) rank composition;
2. inherited \((-+++) \) signature encoding;
3. fail-closed 4D Lovelock admissibility;
4. selected local bulk basis \(\{1,R\}\);
5. exact RF-E3 coefficient transfer;
6. support-surface ownership with dedicated promotion boundaries;
7. exactly three project-native completion coordinates.

## 12. Closure statement

Let \(\mathcal P_{GR}\) contain the source-bound TIR/IDT 3+1 carrier, RF-G0
Lorentz metric, the complete admitted Lovelock tuple, the four-dimensional
Lovelock theorem, RF-E3 normalization and the RFC matter action.

Then

\[
\boxed{
\mathcal P_{GR}
\Longrightarrow
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}
}
\]

with the RF-E12/RF-E13 ADM constraint, evolution and propagation system.

Current classification:

```text
CONDITIONAL_STANDARD_GR_CLOSURE              PASS
PROJECT_NATIVE_FIRST_PRINCIPLES_GR_CLOSURE   THREE_NAMED_GATES_OPEN
```
