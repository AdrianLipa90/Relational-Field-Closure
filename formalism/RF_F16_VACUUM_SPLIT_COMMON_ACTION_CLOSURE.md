# RF-F16 — Vacuum-Split Renormalization / Dynamic-Lambda Common-Action Closure

Status: `CONSTANT_VACUUM_SPLIT_EXACT / SOURCE_MODIFIED_TRANSPORT_EXACT / ETA_ACTION_PARTITION_EXACT / RF_L2_ENDPOINT_EXACT / RF_F7_LEDGER_ENDPOINT_EXACT / MINIMAL_ETA1_DEGENERACY_FIREWALL / PHYSICAL_STATE_DEPENDENT_COUPLING_CONDITIONAL`

RF-F16 is stacked on RF-F15. It joins the RF-F15 constant vacuum integration component, the RF-L2 scalar-potential realization of `Lambda0`, and the RF-F13 `eta` exchange allocation on one generally covariant action ledger.

Use

\[
X:=\Phi_C+\kappa,\qquad P:=BX,
\]

and the RF-F15 microscopic variables

\[
K:=A^2\omega^2=K_0\omega^4,\qquad
x:=\frac{k^2}{\omega^2},\qquad
v:=\frac{V_G}{K},\qquad
D:=1+x+v.
\]

On the RF-N1B2K current/measure binding surface,

\[
\frac{P}{q_0}=\frac{D}{2}.
\]

---

## 1. Constant vacuum integration coordinate and reference renormalization

RF-F15 gives, on the fixed-`x` branch,

\[
V_G^{(15)}
=
\frac{1-x}{2}K+\rho_C,
\qquad
\boxed{\rho_C:=K_0C_\Lambda}.
\]

The constant component contributes

\[
\boxed{
T^{(C)}_{\mu\nu}=-\rho_C g_{\mu\nu}.
}
\]

RF-L2 supplies

\[
U_L(\phi_L)
=
U_0+\widehat U_L(\phi_L),
\qquad
U_0:=U_L(\phi_{L0}),
\]

with

\[
\widehat U_L(\phi_{L0})=0.
\]

Define the renormalized reference coordinate

\[
\boxed{
\Lambda_*
:=
\Lambda_{\rm ref}
+\kappa_E(\rho_C+U_0).
}
\]

Then the dynamical cosmological coordinate is

\[
\boxed{
\Lambda_0(x)
=
\Lambda_*+\kappa_E\widehat U_L(\phi_L(x)).
}
\]

Equivalently,

\[
\Lambda_0
=
\Lambda_{\rm ref}
+\kappa_E\left(\rho_C+U_L\right).
\]

The geometry is invariant under a constant vacuum repartition

\[
\rho_C\mapsto\rho_C+\delta,
\qquad
U_L\mapsto U_L-\delta.
\]

Thus the constant RF-F15 integration component, the RF-L2 potential zero point, and the reference cosmological coordinate form one exact constant-vacuum ledger.

---

## 2. Minimal common action with exchange allocation

Let `eta` label the RF-F13 exchange allocation,

\[
\boxed{0\le\eta\le1}.
\]

After absorbing `rho_C+U_0` into `Lambda_*`, use the minimal common action

\[
\boxed{
S
=
\int d^4x\sqrt{-g}
\left[
\frac{R-2\Lambda_*}{2\kappa_E}
-\frac12\nabla_\mu\phi_L\nabla^\mu\phi_L
-\widehat U_L(\phi_L)
+\mathcal L_G^{(0)}
+\eta\widehat U_L(\phi_L)
\right].
}
\]

Define

\[
\boxed{
\mathcal L_G
:=
\mathcal L_G^{(0)}
+\eta\widehat U_L.
}
\]

The total minimal potential coefficient is therefore

\[
\boxed{
-(1-\eta)\widehat U_L.
}
\]

Variation in `phi_L` gives

\[
\boxed{
\Box\phi_L-(1-\eta)U_L'(\phi_L)=0.
}
\]

The generator interaction satisfies

\[
\boxed{
\frac{\partial\mathcal L_G}{\partial\phi_L}
=
\eta U_L'(\phi_L),
}
\]

which is exactly the RF-F13 allocation condition.

---

## 3. Metric equation and exact Bianchi partition

The generator tensor contains the interaction counterstress

\[
T^G_{\mu\nu}
=
T^{G(0)}_{\mu\nu}
+\eta\widehat U_L g_{\mu\nu}.
\]

Keep the kinetic scalar tensor explicit:

\[
T^{kin}_{\mu\nu}
=
\nabla_\mu\phi_L\nabla_\nu\phi_L
-\frac12g_{\mu\nu}(\nabla\phi_L)^2.
\]

Writing the potential coordinate on the geometric side gives

\[
\boxed{
G_{\mu\nu}
+\Lambda_0g_{\mu\nu}
=
\kappa_E
\left(
T^G_{\mu\nu}
+
T^{kin}_{\mu\nu}
\right).
}
\]

On the generator equations,

\[
\boxed{
\nabla^\mu T^G_{\mu\nu}
=
\eta\,U_L'(\phi_L)\nabla_\nu\phi_L
=
\eta\,\nabla_\nu\widehat U_L.
}
\]

Using the scalar equation,

\[
\boxed{
\nabla^\mu T^{kin}_{\mu\nu}
=
(1-\eta)\,\nabla_\nu\widehat U_L.
}
\]

Therefore

\[
\boxed{
\nabla^\mu
\left(
T^G_{\mu\nu}
+
T^{kin}_{\mu\nu}
\right)
=
\nabla_\nu\widehat U_L
}
\]

and hence

\[
\boxed{
\kappa_E
\nabla^\mu
\left(
T^G_{\mu\nu}
+
T^{kin}_{\mu\nu}
\right)
=
\nabla_\nu\Lambda_0.
}
\]

This is the exact RF-L2/RF-F7 common Bianchi ledger.

---

## 4. Source-modified RF-F15 transport

Along the material flow, the generator allocation receives

\[
\boxed{
Q_G=-\eta\dot{\widehat U}_L.
}
\]

For the RF-F15 phase-cell branch,

\[
n\propto\omega^3,
\qquad
\rho_G=K D,
\qquad
\frac{P}{q_0}=\frac D2.
\]

The sourced perfect-fluid continuity equation is

\[
\dot\rho_G+(\rho_G+p_G)\theta
=
-\eta\dot{\widehat U}_L.
\]

Using

\[
\theta=-3\frac{d\ln|\omega|}{d\tau},
\]

the phase-cell EOS becomes

\[
\boxed{
w_{\rm cell}
=
\frac13
\left[
1+
\frac{d\ln D}{d\ln|\omega|}
+
\frac{\eta}{KD}
\frac{d\widehat U_L}{d\ln|\omega|}
\right].
}
\]

Equating this to the RF-F14 microscopic EOS

\[
w_{\rm micro}
=
\frac{1-x/3-v}{D}
\]

gives the exact source-modified transport equation

\[
\boxed{
\frac{dD}{d\ln|\omega|}
=
2(1-x-2v)
-
\frac{\eta}{K}
\frac{d\widehat U_L}{d\ln|\omega|}.
}
\]

For `eta=0`, RF-F15 is recovered exactly.

---

## 5. Fixed-`x` integration reconstructs the common-action interaction

Take

\[
x=\mathrm{constant}.
\]

Since `D=1+x+v`,

\[
\frac{dv}{d\ln|\omega|}
+4v
=
2(1-x)
-
\frac{\eta}{K}
\frac{d\widehat U_L}{d\ln|\omega|}.
\]

With

\[
K=K_0\omega^4,
\]

the exact solution is

\[
\boxed{
v
=
\frac{1-x}{2}
+
\frac{\rho_C}{K}
-
\eta\frac{\widehat U_L}{K}.
}
\]

Therefore

\[
\boxed{
V_G
=
\frac{1-x}{2}K
+\rho_C
-\eta\widehat U_L.
}
\]

Since the scalar matter action uses

\[
\mathcal L_G\supset -V_G,
\]

the transport solution reconstructs

\[
\boxed{
\mathcal L_G
\supset
+\eta\widehat U_L
}
\]

and consequently

\[
\boxed{
\partial_{\phi_L}\mathcal L_G
=
\eta U_L'.
}
\]

Thus the RF-F13 interaction sign and coefficient follow from the RF-F15 sourced transport closure.

---

## 6. Generator stress decomposition

The fixed-`x` generator density and pressure become

\[
\boxed{
\rho_G
=
\frac{3+x}{2}K
+\rho_C
-\eta\widehat U_L,
}
\]

\[
\boxed{
p_G
=
\frac{3+x}{6}K
-\rho_C
+\eta\widehat U_L.
}
\]

Hence

\[
\boxed{
\rho_G+p_G
=
\frac{2(3+x)}{3}K,
}
\]

independent of the constant vacuum split and of the `eta` counterterm.

The `eta` interaction therefore shifts only the metric-proportional part of the generator stress on this fixed-`x` solution.

---

## 7. Endpoint branches

### RF-L2 endpoint

For

\[
\boxed{\eta=0},
\]

the common action reduces to

\[
-\frac12(\nabla\phi_L)^2-\widehat U_L+\mathcal L_G^{(0)},
\]

with

\[
\boxed{
\Box\phi_L-U_L'=0,
}
\]

\[
\boxed{
\nabla^\mu T^G_{\mu\nu}=0,
}
\]

\[
\boxed{
\nabla^\mu T^{kin}_{\mu\nu}
=
\nabla_\nu\widehat U_L.
}
\]

This is the RF-L2 allocation.

### RF-F7 ledger endpoint

For

\[
\boxed{\eta=1},
\]

the minimal potential terms cancel in the total action,

\[
-\widehat U_L+\widehat U_L=0,
\]

and

\[
\boxed{
\Box\phi_L=0,
}
\]

\[
\boxed{
\nabla^\mu T^G_{\mu\nu}
=
\nabla_\nu\widehat U_L,
}
\]

\[
\boxed{
\nabla^\mu T^{kin}_{\mu\nu}=0.
}
\]

This realizes the RF-F7 all-generator exchange ledger. In the minimal pure-counterterm representative, the variable metric-proportional `Lambda0` contribution is compensated by the generator counterstress. A physically state-dependent `eta=1` realization therefore requires an independently validated state-dependent interaction surface beyond the pure `+\widehat U_L` counterterm.

---

## 8. Stability transfer

Linearize around a reference point with

\[
U_L'(\phi_{L0})=0.
\]

The common scalar equation gives

\[
\boxed{
(\Box-m_{\rm eff}^2)\delta\phi_L=0,
\qquad
m_{\rm eff}^2=(1-\eta)U_L''(\phi_{L0}).
}
\]

Thus RF-L2 stability transfers as

\[
\boxed{
(1-\eta)U_L''\ge0.
}
\]

For `0<=eta<1`, positive `U_L''` remains restoring. At `eta=1`, the potential contribution is marginal in the minimal representative.

---

## 9. Promotion ledger

```text
RF-F15 constant vacuum density rho_C=K0 C_Lambda           PASS EXACT
rho_C metric-proportional stress                            PASS EXACT
Lambda_* = Lambda_ref + kappa_E(rho_C+U_0)                 PASS EXACT
constant vacuum repartition invariance                      PASS EXACT
Lambda0 = Lambda_* + kappa_E Uhat                           PASS EXACT
minimal eta common action                                   PASS EXACT CONSTRUCTION
scalar EOM Box phi-(1-eta)U'                                PASS EXACT
generator divergence eta grad U                             PASS EXACT ON SHELL
kinetic divergence (1-eta) grad U                           PASS EXACT ON SHELL
total Bianchi transfer grad U                               PASS EXACT
source-modified RF-F15 transport                            PASS EXACT
fixed-x transport -> L_G,int=+eta Uhat                      PASS EXACT
eta=0 -> RF-L2 allocation                                   PASS EXACT
eta=1 -> RF-F7 all-generator ledger                         PASS EXACT
eta=1 minimal pure-counterterm degeneracy                   FIREWALL EXACT
m_eff^2=(1-eta)U''                                          PASS EXACT
physical RF-N1B2K current/measure binding                   OPEN PROMOTION INPUT
physical phi_L <-> RFC invariant lineage                    OPEN PROMOTION INPUT
state-dependent nontrivial eta=1 interaction receipt        OPEN PROMOTION INPUT
absolute kappa_E/G promotion                                OPEN PROMOTION INPUT
```

## 10. Validation authority

Reference implementation:

`src/rfc/vacuum_split_common_action.py`

Reference tests:

`tests/reference/test_rff16_vacuum_split_common_action.py`

Validation receipt:

`validation/RF_F16_VACUUM_SPLIT_COMMON_ACTION_V0_1.json`
