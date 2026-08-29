# RF-F17 — State-Dependent Exchange Projector Theorem

Status: `PROJECTOR_EXCHANGE_THEOREM_EXACT / ETA1_NONTRIVIAL_STRESS_CONDITION_EXACT / CLOCK_GRADIENT_DUST_CANDIDATE / RFC_E19_CONGRUENCE_BINDING_OPEN`

RF-F17 is stacked on RF-F16. It characterizes the minimal additional structure required for an `eta=1` dynamic-`Lambda0` branch to retain the RF-F13 exchange derivative while producing a nonzero state-dependent stress beyond the pure metric counterterm.

Let

\[
\mathcal C[\Psi,g]
\]

be a dimensionless state scalar independent of `phi_L`, and let

\[
f(\mathcal C)
\]

be a differentiable projector profile. Use the interaction

\[
\boxed{
\mathcal L_{\rm int}
=
\eta\,\widehat U_L(\phi_L)\,f(\mathcal C).
}
\]

The physical projector surface is

\[
\boxed{
\mathcal C=1,\qquad f(1)=1.
}
\]

---

## 1. Exchange derivative theorem

Because

\[
\partial_{\phi_L}\mathcal C=0,
\]

one has

\[
\frac{\partial\mathcal L_{\rm int}}{\partial\phi_L}
=
\eta U_L' f(\mathcal C).
\]

On the projector surface,

\[
\boxed{
\frac{\partial\mathcal L_{\rm int}}{\partial\phi_L}
=
\eta U_L'.
}
\]

Thus the RF-F13 exchange allocation remains exact for every projector satisfying `f(1)=1`.

The total potential sector is

\[
\mathcal L_U
=
-\widehat U_L
+
\eta\widehat U_L f(\mathcal C).
\]

The scalar equation is

\[
\boxed{
\Box\phi_L
-
\left[1-\eta f(\mathcal C)\right]U_L'
=
0.
}
\]

On `C=1`,

\[
\boxed{
\Box\phi_L-(1-\eta)U_L'=0,
}
\]

so the RF-F16 scalar equation is preserved exactly.

---

## 2. Metric-variation theorem

For a scalar Lagrangian density without metric derivatives,

\[
T_{\mu\nu}
=
-2\frac{\partial\mathcal L}{\partial g^{\mu\nu}}
+
g_{\mu\nu}\mathcal L.
\]

Therefore the complete `U`-sector stress on `C=1` is

\[
\boxed{
T^U_{\mu\nu}
=
-(1-\eta)\widehat U_L g_{\mu\nu}
-
2\eta\widehat U_L f'(1)
\frac{\partial\mathcal C}{\partial g^{\mu\nu}}.
}
\]

For the all-generator branch,

\[
\boxed{\eta=1},
\]

this becomes

\[
\boxed{
T^U_{\mu\nu}
=
-2\widehat U_L f'(1)
\frac{\partial\mathcal C}{\partial g^{\mu\nu}}.
}
\]

Hence the exact nontriviality gate is

\[
\boxed{
f'(1)\,
\frac{\partial\mathcal C}{\partial g^{\mu\nu}}
\neq0
}
\]

on the physical solution surface.

The RF-F16 pure-counterterm representative corresponds to a metric-independent projector and therefore has zero residual `U`-sector tensor at `eta=1`.

---

## 3. Clock-gradient projector candidate

A natural candidate class is a normalized timelike clock one-form `t_mu`:

\[
\boxed{
\mathcal C_T
:=
-\frac{g^{\mu\nu}t_\mu t_\nu}{\mu_T^2}.
}
\]

On the unit-clock surface,

\[
\mathcal C_T=1.
\]

Define

\[
u^{(T)}_\mu:=\frac{t_\mu}{\mu_T},
\qquad
u^{(T)}_\mu u_{(T)}^\mu=-1.
\]

Then

\[
\boxed{
\frac{\partial\mathcal C_T}{\partial g^{\mu\nu}}
=
-u^{(T)}_\mu u^{(T)}_\nu.
}
\]

Therefore the `eta=1` stress is

\[
\boxed{
T^{U,T}_{\mu\nu}
=
2f'(1)\widehat U_L\,u^{(T)}_\mu u^{(T)}_\nu.
}
\]

This is exactly pressureless rank-one stress.

If the normalization condition is

\[
\boxed{f'(1)=\frac12},
\]

then

\[
\boxed{
T^{U,T}_{\mu\nu}
=
\widehat U_L\,u^{(T)}_\mu u^{(T)}_\nu.
}
\]

Thus the clock-projector class supplies an exact algebraic route from the RF-L2 vacuum potential coordinate to an RF-F7 dust-form generator tensor while retaining the exchange derivative.

---

## 4. Relation to the existing RFC material congruence

RF-E19 already supplies, on the future-timelike Noether-current sector,

\[
\nu^\mu=\frac{J^\mu}{\sqrt{-J^2}},
\qquad
\nu_\mu\nu^\mu=-1.
\]

RF-F17 therefore exposes the physical binding target

\[
\boxed{
u^\mu_T
\stackrel{?}{\longleftrightarrow}
\nu^\mu_J.
}
\]

The theorem requires only a normalized timelike clock one-form and a metric-sensitive projector. Physical promotion of the clock candidate requires a common lineage, orientation, measure and support receipt between the clock one-form and the RF-E19 material congruence.

---

## 5. Candidate registry

The following structures are candidate-only until their typing gates close:

```text
F17.CLOCK_GRADIENT:
  C_T = -g^{-1}(t,t)/mu_T^2
  surface: C_T=1
  metric derivative: -u_mu u_nu
  eta=1 residual tensor: 2 f'(1) Uhat u_mu u_nu
  status: CANDIDATE_ONLY

F17.NOETHER_NORM:
  normalized current-norm projector
  status: CANDIDATE_ONLY
  gate: independent norm/measure typing required

F17.HAMILTONIAN_PROJECTOR:
  degree-one Hamiltonian ratio surface
  status: GREMLIN_CANDIDATE_ONLY
  gate: phi-independence and off-shell metric-variation audit required
```

GREMLIN may search these and other relational-isomorphism candidates. Candidate generation has no promotion authority.

---

## 6. Promotion ledger

```text
L_int=eta Uhat f(C)                                        PASS EXACT DEFINITION
C independent of phi_L                                    REQUIRED TYPE GATE
C=1, f(1)=1 -> dL_int/dphi=eta U'                         PASS EXACT
scalar EOM on projector surface                           PASS EXACT
full U-sector metric stress theorem                       PASS EXACT
eta=1 residual stress=-2 U f'(1) dC/dg                   PASS EXACT
metric-sensitive projector -> nonzero eta=1 tensor        PASS EXACT CONDITION
clock-gradient dC/dg=-u_mu u_nu                           PASS EXACT CANDIDATE ALGEBRA
clock-gradient eta=1 tensor is pressureless rank-one      PASS EXACT CANDIDATE ALGEBRA
f'(1)=1/2 -> rho_dust=Uhat                                PASS EXACT NORMALIZATION CONDITION
clock one-form <-> RF-E19 material congruence              OPEN PHYSICAL BINDING
clock scale mu_T                                          OPEN PHYSICAL BINDING
projector profile f physical selection                    OPEN PHYSICAL BINDING
```

## 7. Validation authority

Reference implementation:

`src/rfc/state_dependent_exchange_projector.py`

Reference tests:

`tests/reference/test_rff17_state_dependent_exchange_projector.py`

Validation receipt:

`validation/RF_F17_STATE_DEPENDENT_EXCHANGE_PROJECTOR_V0_1.json`
