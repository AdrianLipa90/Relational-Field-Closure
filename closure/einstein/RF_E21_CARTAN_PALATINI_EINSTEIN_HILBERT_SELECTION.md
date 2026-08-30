# RF-E21 — Cartan–Palatini Einstein–Hilbert Selection

Status: `EXACT_CONDITIONAL_ACTION_FORM_SELECTION / TORSION_FREE_VARIATION_PASS / RF_E3_NORMALIZATION_REUSED / PRIMITIVE_ASSUMPTION_PROMOTION_OPEN`

## 1. Purpose

RF-E21 closes the action-form gap between the already assembled TIR×IDT Lorentzian carrier and RF-E3.

RF-E8 supplies the four-dimensional coframe/metric assembly from the TIR spatial carrier and the IDT relational lapse. RF-E3 supplies the independently gated gravitational coupling normalization. RF-E12 and RF-E13 already consume the resulting Einstein tensor equation in the ADM constraint/evolution chain.

The present gate selects the Einstein–Hilbert bulk form from the admitted Cartan carrier under an explicit minimal structural class rather than introducing `sqrt(-g) R` as a free action ansatz.

## 2. Frozen source lock

```text
TIR main  = 3f5a08ef04ec53c1a155263d23e8b10a96404370
IDT main  = 84ce1886175af872ae4a56ba36f7e106d8e23635
RFC main  = 63418a88d686021c2a6fe6ab159d6152db303c19
```

Source surfaces:

```text
TIR/foundations/TIR_DISCRETE_SOLDER_FORM_V0_1.md
IDT formalism/05C_relational_lapse_interface.md
RFC closure/einstein/RF_E8_ADM_KINEMATIC_ASSEMBLY_FIREWALL.md
RFC formalism/RF02I_HEXAHEDRAL_COFRAME_CONNECTION.md
RFC closure/einstein/RF_E3_DOUBLE_COPY_EINSTEIN_HILBERT_NORMALIZATION.md
RFC closure/einstein/RF_E12_ACTION_PROJECTED_ADM_SOURCE_CONSTRAINTS.md
RFC closure/einstein/RF_E13_CONSTRAINT_PROPAGATION_BIANCHI_LEDGER.md
```

## 3. TIR×IDT four-coframe

TIR supplies a rank-three spatial coframe in the continuum target,

\[
e^a=e^a{}_i\,dx^i,
\qquad
h_{ij}=\delta_{ab}e^a{}_i e^b{}_j.
\]

IDT supplies the positive relational lapse and temporal one-form,

\[
N_R=\frac{\mathfrak a_x}{\mathfrak a_r}>0,
\qquad
\Theta_R=N_Rc\,dt.
\]

RF-E8 assembles these into the Lorentzian coframe

\[
\boxed{E^0:=\Theta_R=N_Rdx^0,}
\]

\[
\boxed{E^a:=e^a{}_i(dx^i+b^i dx^0),}
\]

with `x^0=ct` and

\[
\boxed{g=\eta_{AB}E^A\otimes E^B,\qquad
\eta_{AB}=\operatorname{diag}(-1,1,1,1).}
\]

Hence

\[
\sqrt{-g}=N_R\sqrt h
\]

and the carrier is oriented by the coframe volume form

\[
\boxed{
\operatorname{vol}_4
=\frac1{4!}\epsilon_{ABCD}
E^A\wedge E^B\wedge E^C\wedge E^D.
}
\]

This is the parent carrier for the present action-selection theorem.

## 4. Declared minimal gravitational action class

RF-E21 considers bulk gravitational actions satisfying the following structural conditions on the admitted four-coframe:

1. local diffeomorphism covariance;
2. local Lorentz covariance of internal coframe indices;
3. orientation-preserving scalar action;
4. no additional independent gravitational field beyond the coframe and metric-compatible Lorentz connection;
5. polynomial exterior-form construction from `E^A` and curvature `R^{AB}`;
6. at most one curvature two-form in the dynamical bulk term;
7. the torsion-free GR branch after connection variation;
8. topological and boundary terms are tracked separately from bulk field equations.

These conditions define the theorem domain. Their deeper promotion from the primitive TIR×IDT layer remains an explicit upstream theorem program.

## 5. Degree-counting selection

The coframe is a one-form and curvature is a two-form,

\[
[E^A]_{\rm form}=1,
\qquad
[R^{AB}]_{\rm form}=2.
\]

A local four-dimensional bulk term linear in curvature must therefore contain exactly two coframes,

\[
1+1+2=4.
\]

The orientation-compatible Lorentz scalar is

\[
\boxed{
\mathcal L_R
=\epsilon_{ABCD}
E^A\wedge E^B\wedge R^{CD}.
}
\]

The second Lorentz-invariant curvature four-form,

\[
E^A\wedge E^B\wedge R_{AB},
\]

belongs to the torsional/Holst–Nieh–Yan channel. In the torsion-free Levi-Civita branch, the first Bianchi identity makes this channel bulk-null. Retaining it as an independent dynamical coordinate requires an additional torsional/Immirzi coupling and therefore belongs to a separate extension branch.

With no curvature, degree counting requires four coframes. The oriented Lorentz scalar is uniquely

\[
\boxed{
\mathcal L_\Lambda
=\epsilon_{ABCD}
E^A\wedge E^B\wedge E^C\wedge E^D.
}
\]

Thus, within the declared minimal branch, the bulk action basis is two-dimensional:

\[
\boxed{\{\mathcal L_R,\mathcal L_\Lambda\}.}
\]

Four-dimensional Euler/Gauss–Bonnet and Pontryagin densities remain topological channels and are separated from the local bulk Einstein equation.

## 6. Selected Cartan–Palatini action

Let `kappa_E>0` be the gravitational coupling coordinate owned by RF-E3. The selected action is

\[
\boxed{
S_g[E,\omega]
=\frac1{4\kappa_E}
\int\epsilon_{ABCD}E^A\wedge E^B\wedge R^{CD}
-\frac{\Lambda}{24\kappa_E}
\int\epsilon_{ABCD}E^A\wedge E^B\wedge E^C\wedge E^D.
}
\]

Using the oriented-coframe identities

\[
\boxed{
\epsilon_{ABCD}E^A\wedge E^B\wedge R^{CD}
=2R\,\operatorname{vol}_4,
}
\]

and

\[
\boxed{
\epsilon_{ABCD}E^A\wedge E^B\wedge E^C\wedge E^D
=24\,\operatorname{vol}_4,
}
\]

one obtains exactly

\[
\boxed{
S_g[g]
=\frac1{2\kappa_E}
\int d^4x\sqrt{-g}\,(R-2\Lambda).
}
\]

Therefore the metric Einstein–Hilbert form used by RF-E3 is the metric representation of the selected minimal Cartan action.

## 7. Connection variation and torsion gate

The curvature variation is

\[
\delta R^{AB}=D(\delta\omega^{AB}).
\]

After integration by parts and the standard boundary handling, connection stationarity gives the Cartan equation

\[
\boxed{
\epsilon_{ABCD}E^C\wedge T^D=0,
}
\]

with

\[
T^A=dE^A+\omega^A{}_B\wedge E^B.
\]

For an invertible coframe on the spinless/minimal GR branch this implies

\[
\boxed{T^A=0.}
\]

The connection is then the Levi-Civita spin connection of the assembled Lorentzian metric. This is the continuum torsion-free target anticipated by the TIR discrete solder/closure construction and the RFC spatial connection layer.

Spin-current/torsional matter belongs to a separately typed Einstein–Cartan extension branch.

## 8. Coframe/metric variation

With the torsion-free connection inserted, variation of the selected bulk action with the RF-E3 matter stress-energy convention gives

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\kappa_E T_{\mu\nu}.
}
\]

For `Lambda=0`,

\[
\boxed{G_{\mu\nu}=\kappa_E T_{\mu\nu}.}
\]

RF-E3 remains the owner of the coupling normalization

\[
\boxed{
\kappa_g^2=4\kappa_E=32\pi G
}
\]

in natural units and

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}
}
\]

in SI units.

RF-E21 therefore supplies the missing action-form selection, while RF-E3 supplies its physical normalization coordinate.

## 9. ADM closure handoff

The dependency chain is now

```text
TIR relational edge generators
 -> spatial solder/coframe target e^a
IDT activity ratio
 -> positive relational lapse N_R
TIR e^a + IDT N_R + typed shift b^i
 -> RF-E8 Lorentzian four-coframe/metric
 -> RF-E21 minimal Cartan action basis
 -> Palatini connection variation
 -> torsion-free Levi-Civita branch
 -> Einstein-Hilbert metric action
RF-E3 double-copy/Newton normalization
 -> kappa_E
 -> Einstein tensor equation
RF-E10/RF-E11
 -> ADM geometric/source projections
RF-E12
 -> Hamiltonian + momentum source constraints
RF-E13
 -> constraint propagation through Bianchi
```

The previous `Define S_EH` step is replaced by the explicit RF-E21 action-selection theorem inside its declared structural domain.

## 10. Dynamic Lambda boundary

For constant `Lambda`, the selected volume term gives the standard cosmological contribution.

For the RFC information-driven scalar coordinate `Lambda0(x)`, the metric-side insertion

\[
\frac1{2\kappa_E}\int\sqrt{-g}\,[R-2\Lambda_0(x)]\,d^4x
\]

is already recorded by RF-E3. An independently varied dynamic `Lambda0` requires its own kinetic/source/stability action and remains the dedicated Lambda-sector frontier.

## 11. Claim ledger

| Statement | Status |
|---|---|
| TIR rank-three solder/coframe continuum target | PARENT CANDIDATE/INTEGRATION SOURCE |
| IDT positive reparameterization-invariant lapse | PARENT EXACT ALGEBRA |
| RF-E8 four-dimensional Lorentzian coframe assembly | PARENT EXACT KINEMATICS |
| four-form degree counting | EXACT |
| minimal curvature basis on declared torsion-free branch | EXACT CONDITIONAL SELECTION |
| Cartan–Palatini ↔ metric EH coefficient conversion | EXACT ON STATED ORIENTATION CONVENTION |
| connection variation -> torsion-free Levi-Civita branch | EXACT FOR INVERTIBLE COFRAME/SPINLESS BRANCH |
| metric equation `G+Lambda g=kappa_E T` | EXACT VARIATION RESULT |
| `kappa_E` normalization | PARENT RF-E3 |
| ADM projection and propagation | PARENT RF-E12/RF-E13 |
| primitive derivation of all action-class assumptions | OPEN PROMOTION PROGRAM |
| dynamical `Lambda0` action | OPEN LAMBDA-SECTOR GATE |
| torsional/spin-current extension | SEPARATE EINSTEIN–CARTAN BRANCH |

## 12. Falsification and validation gates

RF-E21 fails if any of the following occurs inside the declared theorem domain:

1. the selected curvature term has form degree different from four;
2. the volume term has form degree different from four;
3. the Cartan coefficient fails to reduce to `1/(2 kappa_E)` in metric form;
4. the cosmological coefficient fails to reduce to `-Lambda/kappa_E` times the volume density;
5. connection variation on an invertible spinless branch retains nonzero torsion;
6. the resulting metric equation differs from the RF-E3 Einstein equation convention;
7. source locking no longer points to the frozen TIR/IDT/RFC parent commits.

Validation target:

`PASS_RF_E21_CARTAN_PALATINI_EINSTEIN_HILBERT_SELECTION`.
