# Einstein closure

Current exact-head closure surface: RF-E21 stacked branch.

## Canonical dependency chain

```text
TIR rank-three positive spatial carrier
 + IDT positive relational lapse / temporal carrier
 -> RF-G0 Lorentzian 3+1 metric
 -> RF-02I torsion-free metric connection / curvature
 -> RF-E3 Einstein-Hilbert normalization
 -> RF-E6/RF-E7 matter action and stress-energy
 -> RF-E8 ADM kinematics
 -> RF-E9 extrinsic curvature
 -> RF-E10 Gauss-Codazzi Einstein projections
 -> RF-E11 matter projections
 -> RF-E12 Einstein equation + ADM source constraints
 -> RF-E13 ADM evolution + Bianchi constraint propagation
 -> RF-E17 clock-information scalar action
 -> RF-E20 tetra-clock mass-scale closure
 -> RF-E21 gravitational action-selection gate
```

## Current gate ledger

1. canonical Lorentzian signature `(-,+,+,+)` — **PASS at RF-G0/RF-02H**;
2. torsion-free metric connection and curvature — **PASS at RF-02I**;
3. contracted Bianchi identity — **EXACT**;
4. AB-normalized electromagnetic curvature — **PASS at RF-M1**;
5. charge-projected Maxwell current — **PASS at RF-M4/RF-N1B2P with RF-E6 sign alignment**;
6. canonical energy-positive charged scalar/multiplet action — **PASS at RF-E6**;
7. charged-matter stress tensor and EM/matter exchange — **PASS at RF-E0/RF-E6**;
8. exact amplitude/phase/potential scalar decomposition — **CLOSED at RF-E7**;
9. Newton ↔ Einstein normalization `kappa_E=8piG/c^4` — **EXACT TRANSFER at RF-N1C/RF-E3**;
10. double-copy ↔ Einstein normalization `kappa_E=kappa_g^2/4` — **EXACT**;
11. ADM kinematics/extrinsic curvature — **PASS at RF-E8/RF-E9**;
12. Gauss-Codazzi Einstein projections — **EXACT at RF-E10**;
13. matter ADM projections — **PASS at RF-E11**;
14. action-projected Hamiltonian/momentum constraints — **PASS at RF-E12**;
15. ADM evolution and Bianchi constraint propagation — **PASS at RF-E13**;
16. clock-information scalar action/potential — **PASS at RF-E17**;
17. tetra-clock mass-scale bridge — **PASS at RF-E20**;
18. TIR×IDT 4D gravitational action selection — **PASS CONDITIONAL at RF-E21**;
19. reduced-gravity universality coordinate and promotion firewall — **PRESENT at RF-F25/RF-F26**;
20. dynamic-`Lambda` independent action/stability — **EXTENSION FRONTIER**;
21. additional independently admitted matter species — **MATTER-COMPOSITION FRONTIER**.

## RF-E21 action-selection closure

RF-E21 receives the source-bound 3+1 carrier

\[
\operatorname{rank}h_\perp=3,
\qquad
N_R=\frac{\mathfrak a_x}{\mathfrak a_r}>0,
\]

and RF-G0 assembles

\[
\boxed{g=-\Theta\otimes\Theta+h_\perp},
\qquad
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

The conditional Lovelock admissibility tuple is

\[
\mathfrak A_{E21}
=
(D=4,\;
\text{Lorentzian metric},\;
\text{diffeomorphism covariance},\;
\text{local metric bulk dynamics},\;
\text{second-order metric equations}).
\]

On the complete admitted tuple, the four-dimensional local bulk basis is

\[
\boxed{\mathcal B_{\rm grav}^{(4)}=\{1,R\}},
\]

up to topological and boundary densities, yielding

\[
S_g
=
A\int d^4x\,\sqrt{-g}(R-2\Lambda)
+
S_{\rm top}
+
S_{\rm boundary}.
\]

RF-E3 fixes

\[
A=\frac{c^4}{16\pi G}
=\frac{1}{2\kappa_E},
\qquad
\kappa_E=\frac{8\pi G}{c^4}.
\]

RF-E12 then gives

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}
}.
\]

RF-E13 carries the corresponding ADM evolution and homogeneous Bianchi
constraint-propagation system.

## Covariance and amplitude support

RF-E21 v0.2 binds the following project support surfaces:

```text
RF-F13  covariant common-action architecture
RFG18   linearized diffeomorphism Ward firewall
RFG20   four-point Einstein MHV normalization
RFG27   five-point normalization firewall
RFG29   five-point BCJ/Jacobi root validation
RFG30   five-point pre-KLT closure
```

These surfaces support the finite-order/covariant gravity line.  The nonlinear
all-orders promotion is assigned to its dedicated frontier coordinate.

## Reduced-gravity universality

RF-F25 defines the zero-fit project coordinate

\[
\bar M_{G,i}
=
-\frac1{\beta_W}
\ln\!\left[
\frac{|\omega_{t,i}|^2}
{16\pi\Gamma_{DC}M_\star^3}
\right].
\]

RF-F26 owns the physical-coupling promotion firewall.  Its realized admission
requires frozen prerequisite normalization surfaces plus multiple independent,
nondegenerate source pairs sharing one \(\bar M_G\) within the declared
tolerance.

## Three-coordinate project-native frontier

The broad Einstein-closure problem is now localized to:

```text
NONLINEAR_ALL_ORDERS_GRAVITATIONAL_COVARIANCE_PROMOTION
NATIVE_LOCAL_SECOND_ORDER_METRIC_GRAVITY_SELECTION
REALIZED_INDEPENDENT_REDUCED_GRAVITY_UNIVERSALITY_ADMISSION
```

For constant \(\Lambda\), the current chain has **conditional standard-GR
closure**.  Promotion to **project-native first-principles GR closure** is owned
by the three coordinates above.

Dynamic-\(\Lambda\) dynamics and additional matter species continue as parallel
extension/composition programmes.

## Validation

RF-E21 theorem:

`closure/einstein/RF_E21_TIR_IDT_EINSTEIN_ACTION_SELECTION_GATE.md`

Implementation:

`src/rfc/einstein_action_selection.py`

Focused reference tests:

`tests/reference/test_rfe21_einstein_action_selection.py`

Receipts:

```text
validation/RF_E21_TIR_IDT_EINSTEIN_ACTION_SELECTION_V0_1.json
validation/RF_E21_TIR_IDT_EINSTEIN_ACTION_SELECTION_V0_2.json
```

The v0.1 exact-head reference suite passed on
`a761ed254e4535535a8ef6095deeaa6de47e75a0`, GitHub Actions run #377.
