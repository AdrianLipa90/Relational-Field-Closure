# RF-F13 — Variational Integrability and Common-Action Gate

Status: `SYMPLECTIC_CANONICAL_PAIR_EXACT / DEGREE_ONE_HAMILTONIAN_SOURCE_BINDING_EXACT / RF_F11_HAMILTONIAN_IDENTITY_EXACT / CONSTANT_B_BRANCH_EXACT / LAMBDA_PARTITION_EXACT / COVARIANT_DUST_ACTION_TEMPLATE_CONDITIONAL / PHYSICAL_NOETHER_HAMILTONIAN_BINDING_OPEN`

RF-F13 is stacked on the canonical RF-F0–RF-F12 spine, RF-S16–RF-S22 source/current normalization gates, RF-E3/RF-E13 Einstein–Bianchi action ledger, and RF-L2 dynamic-`Lambda0` scalar action.

Define

\[
X:=\Phi_C+\kappa,
\qquad
\kappa=\frac{\ln 2}{24\pi},
\qquad
\omega:=u^\mu\mathscr D_\mu\vartheta,
\qquad
\epsilon_G=B\omega X.
\]

RF-F5 supplies the phase-energy one-form

\[
\Theta_G=BX\,\mathscr D\vartheta.
\]

On the local relational-lift branch `dX=mathscr D vartheta`, RF-F13 identifies the canonical phase-space pair

\[
\boxed{q=X,\qquad P:=BX}
\]

so that

\[
\boxed{\Theta_G=P\,dX.}
\]

The canonical reconstruction is

\[
\boxed{B=\frac{P}{X}}
\]

on the nondegenerate surface `X != 0`.

---

## 1. Symplectic roundtrip to RF-F10

Since

\[
dP=X\,dB+B\,dX,
\]

we obtain

\[
\boxed{dP\wedge dX=X\,dB\wedge dX.}
\]

Restoring the admitted phase connection with `d(mathscr D vartheta)=mathcal F_-` gives

\[
\boxed{
\mathcal K_G
=d\Theta_G
=X\,dB\wedge\mathscr D\vartheta
+BX\,\mathcal F_-.
}
\]

This is the RF-F10 phase-energy curvature exactly. The variable `B` is therefore represented on this branch through the canonical momentum coordinate `P=BX`.

---

## 2. Material phase-space action

For one occupied material element, take the first-order action

\[
\boxed{
S_G^{(1)}
=\int d\tau\left[P\dot X-H_G(X,P,\phi_L)\right].
}
\]

Hamilton variation gives

\[
\boxed{\dot X=\partial_P H_G,}
\qquad
\boxed{\dot P=-\partial_XH_G.}
\]

Using the RF-F3/RF-F5 pullback identity

\[
\dot X=\omega,
\]

the first Hamilton equation requires

\[
\boxed{\omega=\partial_P H_G.}
\]

The relational generator energy satisfies

\[
\epsilon_G=P\omega.
\]

Therefore exact Hamiltonian/source identification is equivalent to the Euler homogeneity condition

\[
\boxed{
H_G=P\,\partial_P H_G.
}
\]

For differentiable one-dimensional `P` dependence on one fixed-sign branch, this is the degree-one family

\[
\boxed{
H_G=P\,h(X,\phi_L),
}
\]

with

\[
\boxed{
\omega=h(X,\phi_L),
\qquad
H_G=P\omega=BX\omega=\epsilon_G.
}
\]

Thus the RF-F5 energy per occupation is the on-shell Hamiltonian of the material phase-space block.

---

## 3. Covariant material-density lift and dust tensor

Let

\[
J^\mu=nu^\mu,
\qquad
n=\sqrt{-J_\mu J^\mu}>0
\]

be the admitted future-timelike occupation/current field. The material phase-space block lifts to

\[
\boxed{
S_G
=\int d^4x\sqrt{-g}
\left[
P J^\mu\nabla_\mu X
-nH_G(X,P,\phi_L)
\right].
}
\]

The `P` variation gives

\[
J^\mu\nabla_\mu X=n\partial_PH_G,
\]

hence

\[
\boxed{\dot X=\partial_PH_G=\omega.}
\]

The `X` variation gives

\[
\boxed{
\nabla_\mu(PJ^\mu)+n\partial_XH_G=0.
}
\]

On the admitted conserved-current branch

\[
\nabla_\mu J^\mu=0,
\]

this reduces to

\[
\boxed{\dot P=-\partial_XH_G.}
\]

For the degree-one Hamiltonian surface `H_G=P omega`, the material Lagrangian density satisfies

\[
P J^\mu\nabla_\mu X-nH_G
=n(P\omega-H_G)=0
\]

on shell. Holding the independent contravariant current fixed under metric variation,

\[
\frac{\partial n}{\partial g^{\mu\nu}}
=\frac n2u_\mu u_\nu.
\]

Therefore the on-shell metric variation of the material block gives

\[
\boxed{
T^G_{\mu\nu}
=nH_Gu_\mu u_\nu
=\rho_Gu_\mu u_\nu,
}
\]

with

\[
\boxed{\rho_G=nH_G=n\epsilon_G.}
\]

This roundtrips RF-F6/RF-F7 and RF-S18/RF-S19 on the degree-one Hamiltonian surface. The current origin and its physical `J_Q^mu <-> J_vartheta^mu` promotion remain controlled by the existing RF-N1B2M/RF-N1B2K current gates.

---

## 4. RF-F11 as an exact Hamiltonian identity

Take

\[
H_G=P\,h(X,\phi_L),
\qquad
P=BX.
\]

Hamilton's equations give

\[
\dot X=h,
\qquad
\dot P=-P\,h_X.
\]

Hence

\[
\boxed{
\dot B
=-\frac{B}{X}\left(h+Xh_X\right)
}
\]

and

\[
\boxed{
\dot\omega
=h_Xh+h_{\phi_L}\dot\phi_L.
}
\]

Substitution into the RF-F11 left-hand side gives exactly

\[
\begin{aligned}
X(\dot B\,\omega+B\dot\omega)+B\omega^2
&=BX\,h_{\phi_L}\dot\phi_L\\
&=P\,h_{\phi_L}\dot\phi_L\\
&=\boxed{\partial_{\phi_L}H_G\,\dot\phi_L}.
\end{aligned}
\]

Therefore the full phase-energy transport law is the explicit coupling-rate identity of the degree-one Hamiltonian family.

---

## 5. Dynamic-Lambda partition theorem

RF-L2 supplies

\[
\boxed{
\Lambda_0=\Lambda_{ref}+\kappa_EU_L(\phi_L).
}
\]

Introduce a dimensionless transfer-allocation coordinate

\[
\boxed{0\le\eta\le1}
\]

through

\[
\boxed{
 n\,\partial_{\phi_L}H_G
=-\eta\,U_L'(\phi_L).
}
\]

The generator energy transport becomes

\[
\boxed{
\dot H_G
=-\eta\frac{\dot\Lambda_0}{\kappa_E n}.
}
\]

The scalar equation from the combined scalar-plus-material action is

\[
\boxed{
\Box\phi_L-U_L'-n\partial_{\phi_L}H_G=0,
}
\]

hence on the `eta` surface

\[
\boxed{
\Box\phi_L=(1-\eta)U_L'.
}
\]

The on-shell stress-transfer split is then

\[
\boxed{
\nabla^\mu T^G_{\mu\nu}
=\eta U_L'\nabla_\nu\phi_L,
}
\]

\[
\boxed{
\nabla^\mu T^{kin}_{\mu\nu}
=(1-\eta)U_L'\nabla_\nu\phi_L.
}
\]

Adding the two sectors gives identically

\[
\boxed{
\kappa_E\nabla^\mu
\left(T^G_{\mu\nu}+T^{kin}_{\mu\nu}\right)
=\nabla_\nu\Lambda_0.
}
\]

The endpoint allocations are:

\[
\boxed{\eta=0: \text{RF-L2 kinetic-carrier allocation}},
\]

\[
\boxed{\eta=1: \text{RF-F7 relational-generator allocation}}.
\]

For `eta=1`, RF-F11 follows exactly:

\[
\boxed{
X(\dot B\,\omega+B\dot\omega)+B\omega^2
=-\frac{\dot\Lambda_0}{\kappa_E n}.
}
\]

Thus RF-L2 and RF-F7 are two exact allocation surfaces of one coupled action ledger.

---

## 6. Constant-B / constant-Lambda theorem

For the constant-`Lambda0` branch, take `h_phi_L=0`. Requiring

\[
\dot B=0
\]

in the Hamiltonian expression above gives

\[
\boxed{h+Xh_X=0.}
\]

Therefore

\[
\boxed{h(X)=\frac C X}
\]

and hence

\[
\boxed{\omega=\frac C X,}
\qquad
\boxed{\omega X=C.}
\]

The Hamiltonian is

\[
\boxed{H_G=P\omega=BC=\mathrm{constant}}
\]

and

\[
\boxed{\dot\omega=-\frac{\omega^2}{X}.}
\]

This is exactly the RF-F11 constant-`B`, constant-`Lambda0` dust solution.

---

## 7. First-order variational integrability audit for B

Consider the general first-order local form that is affine in `Bdot`,

\[
L=A(B,X,\dot X)\dot B+C(B,X,\dot X).
\]

Its Euler-Lagrange expression for `B` is

\[
E_B
=\partial_BL-\frac{d}{d\tau}\partial_{\dot B}L.
\]

The coefficient multiplying the self-rate `Bdot` cancels identically in `E_B`. RF-F11 carries the generic self-rate coefficient

\[
\boxed{X\omega}
\]

multiplying `Bdot`. RF-F13 therefore assigns the canonical dynamical coordinate as

\[
\boxed{P=BX}
\]

and assigns RF-F11 to the Hamiltonian/Bianchi transport identity derived above. This is the executable variational-integrability firewall used by the reference tests.

---

## 8. Noether/Hamiltonian normalization bridge

RF-S16 gives

\[
\epsilon_Q
=\frac{B\omega X}{q_0}.
\]

RF-S22 supplies the finite Noether/Hamiltonian coordinate

\[
\epsilon_Q=\frac{H_\Phi^{EB}}{Q_\vartheta}.
\]

The RF-F13 physical binding target is therefore

\[
\boxed{
\frac{H_\Phi^{EB}}{Q_\vartheta}
=\frac{H_G}{q_0}
=\frac{B\omega X}{q_0}.
}
\]

Under the RF-S17 positive carrier rescaling

\[
q_0\mapsto\lambda q_0,
\qquad
Q_\vartheta\mapsto\lambda Q_\vartheta,
\]

both sides scale by `1/lambda`, while the physical source density and dust tensor remain invariant. The zero-defect physical current/Hamiltonian receipt remains the promotion gate for this equality.

---

## 9. Common-action architecture

The RF-F13 coupled action template is

\[
\boxed{
S_{common}
=
\int d^4x\sqrt{-g}
\left[
\frac{R-2\Lambda_{ref}}{2\kappa_E}
-\frac12\nabla_\mu\phi_L\nabla^\mu\phi_L
-U_L(\phi_L)
+P J^\mu\nabla_\mu X
-nH_G(X,P,\phi_L)
+\mathcal L_{current/rest}
\right].
}
\]

`L_current/rest` denotes the already gated current-origin and additional admitted matter sectors. On the zero-defect current-binding surface, the displayed common action gives:

\[
\delta_P S\rightarrow\dot X=\omega,
\]

\[
\delta_X S\rightarrow\dot P=-\partial_XH_G,
\]

\[
\delta_g S\rightarrow T^G_{\mu\nu}=\rho_Gu_\mu u_\nu
\]

on the degree-one Hamiltonian surface,

\[
\delta_{\phi_L}S\rightarrow\text{dynamic-}\Lambda_0\text{ partition ledger},
\]

and diffeomorphism/Bianchi closure gives the total exchange identity.

The `delta_vartheta S -> J^mu` origin remains inherited from the RF-N1B2M/RF-E6 Noether sector and is promoted into this common action after the existing local current/measure binding receipt is zero-defect.

---

## 10. Advancement

```text
P=B(Phi_C+kappa) canonical momentum                    PASS EXACT
Theta_G=P dX local canonical one-form                  PASS EXACT
RF-F10 curvature roundtrip                             PASS EXACT
Hamilton equations from first-order material action    PASS EXACT
H_G=P*dH/dP source-energy condition                    PASS EXACT
H_G=P h(X,phi_L) degree-one family                     PASS EXACT
H_G=epsilon_G=B X omega                                PASS EXACT ON HOMOGENEITY SURFACE
covariant material-density lift                        PASS EXACT CONSTRUCTION
on-shell dust tensor T_mn=n H_G u_m u_n                PASS EXACT UNDER STATED METRIC TYPING
RF-F11 lhs = partial_phi H_G * phi_dot                 PASS EXACT
eta-partition total Bianchi exchange                   PASS EXACT
eta=0 RF-L2 allocation                                 PASS EXACT ENDPOINT
eta=1 RF-F7 allocation                                 PASS EXACT ENDPOINT
constant-B constant-Lambda omega X=C                   PASS EXACT
constant-B H_G=B C invariant                           PASS EXACT
first-order direct-B integrability audit               PASS EXACT
carrier-rescaling covariance of H/Q binding            PASS EXACT
physical J_Q^mu <-> J_vartheta^mu receipt              OPEN RF-N1B2K
physical H_Phi^EB/Q_vartheta <-> H_G/q0 receipt        OPEN RF-S22 INPUT
full current/rest sector composition                   OPEN COMPOSITION INPUT
absolute kappa_E/G promotion                           OPEN PROJECT FRONTIER
```

## 11. Validation authority

Reference implementation:

`src/rfc/variational_common_action.py`

Reference tests:

`tests/reference/test_rff13_variational_common_action.py`

Validation receipt:

`validation/RF_F13_VARIATIONAL_COMMON_ACTION_V0_1.json`

Stack parent:

`58655c7fe9d25d09c13545965e951f171316e6b2`.
