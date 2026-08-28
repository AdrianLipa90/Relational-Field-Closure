# RF-N1B2 — Conserved Source-Carrier Factorization Gate

Status: `CONSERVED_CONTINUOUS_CARRIER_PASS / DISCRETE_QUANTUM_OPEN / MATTER_BINDING_OPEN`

RF-N1B proved that the existing lapse/operator sector does not identify a unique physical matter density. The missing interface was localized to

\[
\text{conserved source carrier}
\to \text{occupation/density}
\to \text{physical source map}.
\]

This gate asks only the first question: does the admitted TIR/time-field stack already contain a genuinely conserved carrier from which a normalized occupation profile can be constructed without inserting Newton's source law?

The answer is **yes for a continuous carrier**, while the conversion to discrete carrier count and ordinary matter density remains open.

## 1. Existing conserved temporal carrier

The pinned `fluid_time.pdf` source defines a time-density scalar and current

\[
\rho_\tau(x),
\qquad
J_\tau^\mu=\rho_\tau u^\mu,
\]

with

\[
\boxed{\nabla_\mu J_\tau^\mu=0.}
\]

Its continuity equation is

\[
u^\mu\nabla_\mu\rho_\tau+\rho_\tau\nabla_\mu u^\mu=0.
\]

Thus the current is already a local conserved continuous carrier in the upstream time-field formalism. This statement does **not** identify `rho_tau` with ordinary matter density.

The same source later introduces a thermodynamic variable `n_tau` as a possible chronon-number density through

\[
d\rho_\tau=T_\tau ds_\tau+\mu_\tau dn_\tau,
\]

but the source itself presents that number-density interpretation as optional/undeveloped. RF-N1B2 therefore does not use `n_tau` as an admitted source count.

## 2. Independent TIR / Noether carrier support

The TIR phase-Hamiltonian sector has a cyclic coordinate `chi` with conjugate phase momentum

\[
J=I_\phi D_t\chi+J_0,
\]

so absence of explicit `chi` dependence gives

\[
\boxed{\dot J=0.}
\]

Independently, the Euler–Noether–Berry scalar-field formalism supplies the global-U(1) current

\[
J_\varphi^\mu
=i\left(\psi\partial^\mu\psi^*-\psi^*\partial^\mu\psi\right),
\qquad
\partial_\mu J_\varphi^\mu=0,
\]

and with

\[
\psi=Ae^{i\vartheta}
\]

its exact polar reduction is

\[
\boxed{J_\varphi^\mu=2A^2\partial^\mu\vartheta.}
\]

These structures confirm that conservation is not unique to one representation. However,

\[
(\vartheta,J_\varphi^\mu)
\stackrel{?}{\longleftrightarrow}
(\chi,J)
\stackrel{?}{\longleftrightarrow}
(\rho_\tau,J_\tau^\mu)
\]

is a **cross-binding candidate**, not an admitted identity.

## 3. Conserved-carrier factorization theorem

Let `J_Q^mu` be any admitted conserved current on a spacetime region,

\[
\nabla_\mu J_Q^\mu=0,
\]

and let `Sigma_t` be a spatial slice with future normal `n_mu` and physical measure `dV_h` supplied by the RF-02H/RF-02I geometry. Define the slice density

\[
j_Q:=J_Q^\mu n_\mu
\]

and the extensive carrier

\[
\boxed{
Q_\Sigma(t)=\int_{\Sigma_t}j_Q\,dV_h.
}
\]

By the divergence theorem, for two slices bounding a spacetime slab,

\[
Q_\Sigma(t_2)-Q_\Sigma(t_1)
=-\int_{\partial\mathcal V_{\rm side}}J_Q^\mu s_\mu\,dS.
\]

Hence under vanishing side-boundary flux, periodic boundary conditions, or sufficient decay,

\[
\boxed{\frac{dQ_\Sigma}{dt}=0.}
\]

This is the extensive conserved quantity required by the RF-N1B source-carrier criterion.

### Positive-source sector

On a sector where

\[
j_Q(x)\ge0,
\qquad Q_\Sigma>0,
\]

define

\[
\boxed{
p_Q(x)=\frac{j_Q(x)}{Q_\Sigma}.
}
\]

Then

\[
\boxed{
\int_{\Sigma_t}p_Q\,dV_h=1.
}
\]

For a cell partition `Sigma = union_a C_a`, define

\[
Q_a=\int_{C_a}j_Q\,dV_h,
\qquad
p_a^{(Q)}=\frac{Q_a}{Q_\Sigma}.
\]

Therefore

\[
\boxed{\sum_a p_a^{(Q)}=1.}
\]

The source carrier naturally factorizes into

\[
\boxed{
Q_a=Q_\Sigma\,p_a^{(Q)}.
}
\]

This separates **how much source exists** from **how that source is distributed**.

## 4. Exact relation to the IDT ensemble variable

IDT 01D already uses a strictly positive normalized ensemble distribution `p_a` and stationary reference `pi_a`, with Shannon–Onsager descent

\[
\dot p=-G_{\rm Sh}(p)\nabla I_\pi(p).
\]

The mathematical type of IDT `p_a` therefore matches the normalized carrier profile `p_a^(Q)`: both are dimensionless normalized distributions.

But normalization erases extensive source scale. For every `lambda>0`,

\[
Q_a\mapsto \lambda Q_a,
\qquad
Q_\Sigma\mapsto\lambda Q_\Sigma
\]

leaves

\[
\boxed{p_a^{(Q)}\mapsto p_a^{(Q)}}
\]

unchanged.

Consequently,

\[
\boxed{
\text{IDT }p_a\ \text{alone does not determine total source amount}.
}
\]

The candidate identification

\[
p_a\stackrel{?}{=}p_a^{(Q)}
\]

requires an explicit TIR/IDT/current cross-binding gate.

## 5. When a discrete occupation exists

A dimensionless discrete occupation can be obtained only after an independently derived carrier quantum `q_0` is available. Define

\[
N_Q:=\frac{Q_\Sigma}{q_0},
\qquad
n_{Q,a}:=\frac{Q_a}{q_0}.
\]

Then exactly

\[
\boxed{
n_{Q,a}=N_Qp_a^{(Q)},
\qquad
\sum_a n_{Q,a}=N_Q.
}
\]

This is the precise structure that the earlier RF-N1B symbol `n_E` was standing in for.

However, the currently admitted current equations do not determine `q_0`. In particular, classical U(1) current conservation fixes conservation of charge but does not by itself fix the physical normalization or a one-carrier quantum.

Therefore

\[
\boxed{
q_0\ \text{OPEN}
\quad\Rightarrow\quad
n_E\ \text{not yet uniquely identified}.
}
\]

## 6. Continuous energy/rest-mass map

A discrete particle count is not necessary if an energy-per-carrier-charge conversion is independently known. Let

\[
\epsilon_Q
\]

have units of energy per carrier charge. Then the continuous energy-density candidate is

\[
\varepsilon_Q(x)=\epsilon_Q j_Q(x),
\]

and the equivalent mass-density candidate is

\[
\boxed{
\rho_Q(x)=\frac{\epsilon_Q}{c^2}j_Q(x).
}
\]

If a later quantization gate derives both `q_0` and a per-quantum energy `E_Q`, then

\[
\epsilon_Q=\frac{E_Q}{q_0}
\]

and

\[
\rho_Q(x)
=\frac{E_Q}{q_0c^2}j_Q(x).
\]

For a cell,

\[
\rho_{Q,a}
=\frac{E_Q}{c^2V_a}\frac{Q_a}{q_0}
=\frac{E_Q n_{Q,a}}{c^2V_a}.
\]

Thus the RF-N1B phase-cell expression is recovered exactly if a later bridge independently establishes

\[
E_Q=\hbar|\omega|,
\qquad
n_{Q,a}=n_{E,a},
\qquad
V_a=V_H.
\]

RF-N1B2 does not assume those equalities.

## 7. Two constructive non-identifiability results

### 7.1 Distribution does not fix amount

Choose a normalized profile `p_a` and two positive totals `Q_1 != Q_2`. Then

\[
Q_a^{(1)}=Q_1p_a,
\qquad
Q_a^{(2)}=Q_2p_a
\]

have the same normalized distribution but different extensive source amount.

Therefore

\[
\boxed{
p_a\not\Rightarrow Q_\Sigma.}
\]

### 7.2 Conservation does not fix energy per carrier

For the same conserved `j_Q`, choose two positive conversions

\[
\epsilon_Q^{(1)}\neq\epsilon_Q^{(2)}.
\]

Both preserve current conservation but produce different candidate mass densities

\[
\rho_Q^{(k)}=\frac{\epsilon_Q^{(k)}}{c^2}j_Q.
\]

Therefore

\[
\boxed{
\nabla_\mu J_Q^\mu=0
\not\Rightarrow
\text{unique }\rho_m.
}
\]

This locates the remaining debt in **source normalization/binding**, not in conservation itself.

## 8. GREMLIN relational-isomorphism audit

Bounded GREMLIN may compare the following structures:

```text
TIR cyclic chi        -> conserved finite J
ENB global U(1)       -> conserved local J_phi^mu
fluid_time rho_tau    -> conserved local J_tau^mu
IDT master equation   -> normalized distribution p_a
```

The shared invariant is

```text
conserved extensive carrier + normalized distributional shape
```

The following mappings remain candidate-only:

```text
J_phi^mu <-> J_tau^mu
J <-> integral(J_phi^0 dV)
p_IDT <-> normalized carrier density
q0 <-> a fundamental carrier quantum
E=hbar|omega| <-> energy per carrier quantum
rho_Q <-> ordinary matter density
```

No GREMLIN result may promote any of these mappings without a separate derivation and validation receipt.

## 9. Advancement

RF-N1B2 changes the source frontier from

```text
conserved source carrier OPEN
```

to

```text
continuous conserved carrier        PASS
extensive total Q from continuity   PASS (boundary-conditioned)
normalized carrier profile          PASS on positive-source sector
IDT p <-> carrier profile           OPEN
carrier quantum q0                  OPEN
E-per-carrier binding               OPEN
continuous carrier <-> rho_m        OPEN
S_R coupling / universal G          OPEN
```

The dependency chain is now

\[
\boxed{
J_Q^\mu,\ \nabla_\mu J_Q^\mu=0
\to
Q_\Sigma,\ p_Q
\to
\{q_0\ \text{or}\ \epsilon_Q\}
\to
\rho_{\rm source}
\to
\mathcal S_R
\to
G.
}
\]

Thus RF-N1C remains a **coupling/universality audit**. It should start only after a separate gate fixes the carrier-to-energy/matter normalization or provides an independently measurable source-density observable.