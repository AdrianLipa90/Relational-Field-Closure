# Relational Field Closure
## Hexahedral Spacetime, Relational Lapse, Newton Source Operator and Conserved Carrier Factorization

**Working monograph v0.11 — 27 August 2026**  
**Status:** `LOCAL_GEOMETRY_LAPSE_AND_NEWTON_OPERATOR_PASS / SOURCE_TYPE_FIREWALL_PASS / CONSERVED_CONTINUOUS_CARRIER_PASS / SOURCE_NORMALIZATION_AND_G_OPEN`

## Abstract

Relational Field Closure (RFC) now contains a continuous derivation chain from the TIR/IDT relational phase-clock sector to a local rank-three spatial metric, a Lorentzian lapse carrier, Newton-facing geodesic kinematics, and an independently derived isotropic Laplace principal source operator. RF-N1B separated relational mobility, phase energy, inverse-area information curvature and physical matter density into distinct source types. RF-N1B2 advances the right-hand side by identifying an already-existing conserved continuous carrier and factorizing it into an extensive conserved total and a normalized spatial distribution.

The current operator side is

\[
\boxed{
\Delta_h\Phi_R=c^2\mathcal S_R,
\qquad
\Phi_R=c^2\ln N_R.
}
\]

The current source-carrier side is

\[
\boxed{
\nabla_\mu J_Q^\mu=0
\longrightarrow
Q_\Sigma
\longrightarrow
p_Q,
}
\]

with the normalization/binding frontier

\[
\boxed{
\{q_0\ \text{or}\ \epsilon_Q\}
\longrightarrow
\rho_{\rm source}
\longrightarrow
\mathcal S_R
\longrightarrow
G.
}
\]

`RF-N1C` remains reserved for the downstream coupling/universality audit.

## 1. Derivation firewall

RFC keeps the Newton validation target downstream. The two independently derived left-hand chains are

\[
\boxed{
\text{IDT clock ratio}
\rightarrow N_R
\rightarrow \Phi_R=c^2\ln N_R
\rightarrow -\nabla\Phi_R
}
\]

and

\[
\boxed{
\text{IDT Shannon--Onsager response}
+\text{TIR six-ray hexahedral symmetry}
\rightarrow \Delta_h.
}
\]

Their combination defines the typed source equation

\[
\boxed{
\Delta_h\ln N_R=\mathcal S_R,
\qquad
\Delta_h\Phi_R=c^2\mathcal S_R,
\qquad
[\mathcal S_R]=L^{-2}.
}
\]

The source functional and physical normalization are downstream gates.

## 2. Hexahedral physical geometry

The regular six-direction dual frame

\[
\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\}
\]

produces the isotropic local metric

\[
\boxed{h_H=\frac16 I_3.}
\]

The IDT phase-clock calibration supplies

\[
\ell_\varphi=\frac{c}{|\omega|}
=\frac{\hbar c}{E},
\qquad
E=\hbar|\omega|,
\]

and hence the regular coframe scale

\[
\boxed{
a_H=\frac{c}{\sqrt6|\omega|}.}
\]

The physical spatial metric supplies

\[
\boxed{dV_h=\sqrt{\det h}\,d^3X.}
\]

For the regular-cell audit the candidate cell support remains

\[
V_H=a_H^3
\]

with cell-to-source-support binding tracked separately.

## 3. Relational lapse and Newton-facing force law

IDT exports the positive relational clock ratio

\[
\boxed{
N_R=\frac{d\tau_x}{d\tau_{\rm ref}}
=\frac{\phi_x}{\phi_{\rm ref}}>0.
}
\]

The local static metric carrier is

\[
\boxed{
g_R=-N_R^2c^2dt^2+h_\perp.}
\]

With

\[
u=\ln N_R,
\qquad
\Phi_R=c^2u,
\]

the slow-motion weak sector gives

\[
\boxed{a^i=-\partial^i\Phi_R+\cdots.}
\]

This establishes the Newton-facing potential form independently of the source normalization.

## 4. Shannon--Onsager plus hexahedral symmetry gives the Laplace operator

IDT detailed-balance response has graph form

\[
G^{(2)}_\pi
=(\ln2)D^T\operatorname{diag}[c_{ab}\Lambda(r_a,r_b)]D.
\]

On the regular six-neighbour hexahedral graph,

\[
(L_Hf)(x)
=\sum_{i=1}^3
\left[2f(x)-f(x+a_He_i)-f(x-a_He_i)\right].
\]

The physical continuum-sign operator

\[
\boxed{\Delta_H^{(a)}=-\frac{L_H}{a_H^2}}
\]

has expansion

\[
\boxed{
\Delta_H^{(a)}f
=\Delta f+
\frac{a_H^2}{12}\sum_i\partial_i^4f
+O(a_H^4).
}
\]

Signed-permutation symmetry removes first-order drift and off-diagonal principal terms, equalizes the three diagonal second-order coefficients, and the constant-null condition removes the zeroth-order scalar term. The normalized regular stencil therefore fixes the leading principal operator to `Delta`.

## 5. RF-N1B source-type firewall

The IDT variable

\[
M_{ab}
=\frac{\sqrt{\rho_R(a)\rho_R(b)}}
{\tfrac12[\eta_R(a)+\eta_R(b)]}
\]

enters the relational kinetic/mobility sector. Its current admitted type is therefore distinct from the physical mass-density source type.

The phase-energy scale

\[
\boxed{E=\hbar|\omega|}
\]

supplies energy, while the temporal information-curvature scalar

\[
\boxed{
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{rel}},
\qquad
[\Xi_I]=L^{-2}
}
\]

supplies a source-basis-compatible inverse-area scalar.

The author/formalism may suggest later bindings among these source sectors, yet does not state such bindings as established results at RF-N1B/RF-N1B2.

## 6. Conditional phase-cell density from RF-N1B

For an independently supplied dimensionless cell occupation `n_E`, the regular-cell candidate is

\[
\rho_{\rm cell}
=\frac{n_EE}{c^2V_H}.
\]

With

\[
V_H=a_H^3,
\qquad
E=\hbar|\omega|,
\qquad
a_H=\frac{c}{\sqrt6|\omega|},
\]

one obtains

\[
\boxed{
\rho_{\rm cell}
=6\sqrt6\,n_E
\frac{\hbar|\omega|^4}{c^5}.
}
\]

This identity remains the correct discrete limit once the occupation is derived from a conserved carrier rather than inserted as an independent free variable.

## 7. RF-N1B2: an admitted continuous conserved carrier exists

The pinned `fluid_time.pdf` source defines

\[
\boxed{
J_\tau^\mu=\rho_\tau u^\mu,
\qquad
\nabla_\mu J_\tau^\mu=0.
}
\]

Its local continuity form is

\[
\boxed{
u^\mu\nabla_\mu\rho_\tau
+\rho_\tau\nabla_\mu u^\mu=0.}
\]

This closes the existence part of the continuous-carrier requirement. The source-type binding

\[
\rho_\tau\stackrel{?}{\longleftrightarrow}\rho_m
\]

remains `OPEN`.

There is independent structural support in the phase sector. A cyclic relational phase coordinate gives

\[
J=I_\phi D_t\chi+J_0,
\qquad
\boxed{\dot J=0,}
\]

while the Euler--Noether--Berry scalar field gives

\[
J_\varphi^\mu
=i(\psi\partial^\mu\psi^*-\psi^*\partial^\mu\psi),
\qquad
\partial_\mu J_\varphi^\mu=0.
\]

For

\[
\psi=Ae^{i\vartheta},
\]

the exact polar current is

\[
\boxed{J_\varphi^\mu=2A^2\partial^\mu\vartheta.}
\]

The cross-binding among the relational phase charge, local U(1) current and time-fluid current is tracked as a separate candidate gate.

## 8. Conserved-carrier factorization theorem

Let an admitted current satisfy

\[
\nabla_\mu J_Q^\mu=0.
\]

On a spatial slice `Sigma_t`, define

\[
j_Q=J_Q^\mu n_\mu
\]

and

\[
\boxed{
Q_\Sigma(t)=\int_{\Sigma_t}j_Q\,dV_h.
}
\]

For a spacetime slab bounded by two slices, the divergence theorem gives

\[
Q_\Sigma(t_2)-Q_\Sigma(t_1)
=-\int_{\partial\mathcal V_{\rm side}}
J_Q^\mu s_\mu\,dS.
\]

Hence zero side flux, periodic boundary conditions, or sufficient decay gives

\[
\boxed{\frac{dQ_\Sigma}{dt}=0.}
\]

On a positive-source sector,

\[
j_Q\ge0,
\qquad Q_\Sigma>0,
\]

define

\[
\boxed{p_Q(x)=\frac{j_Q(x)}{Q_\Sigma}.}
\]

Then

\[
\boxed{\int_{\Sigma_t}p_Q\,dV_h=1.}
\]

For a cell partition,

\[
Q_a=\int_{C_a}j_Q\,dV_h,
\qquad
p_a^{(Q)}=\frac{Q_a}{Q_\Sigma},
\]

and therefore

\[
\boxed{
Q_a=Q_\Sigma p_a^{(Q)},
\qquad
\sum_a p_a^{(Q)}=1.
}
\]

This is the key structural advance of v0.11: source amount and source shape are now separate variables derived from one conserved carrier.

## 9. Relation to the IDT normalized ensemble

IDT uses a positive normalized distribution `p_a` in the Shannon--Onsager master equation

\[
\dot p=-G_{\rm Sh}(p)\nabla I_\pi(p).
\]

Its mathematical type matches the normalized carrier profile `p_a^(Q)`. This gives the candidate bridge

\[
\boxed{p_a^{\rm IDT}\stackrel{?}{=}p_a^{(Q)}}.
\]

The bridge status is `OPEN` pending common state-space and transport compatibility.

A normalization theorem already constrains any such bridge. Under

\[
Q_a\mapsto\lambda Q_a,
\qquad
Q_\Sigma\mapsto\lambda Q_\Sigma,
\]

the profile remains

\[
p_a^{(Q)}\mapsto p_a^{(Q)}.
\]

Thus the normalized shape and extensive amount are independently identifiable data.

## 10. Discrete occupation and continuous energy conversion

If a future gate derives a carrier quantum `q_0`, then

\[
N_Q=\frac{Q_\Sigma}{q_0},
\qquad
n_{Q,a}=\frac{Q_a}{q_0},
\]

so

\[
\boxed{
n_{Q,a}=N_Qp_a^{(Q)},
\qquad
\sum_a n_{Q,a}=N_Q.
}
\]

This is the precise discrete structure previously represented by `n_E`.

A continuous theory may instead derive an energy-per-carrier-charge conversion `epsilon_Q`. Then

\[
\boxed{
\varepsilon_Q=\epsilon_Qj_Q,
\qquad
\rho_Q=\frac{\epsilon_Q}{c^2}j_Q.
}
\]

If a quantized sector later establishes

\[
\epsilon_Q=\frac{E_Q}{q_0},
\]

then

\[
\rho_Q(x)=\frac{E_Q}{q_0c^2}j_Q(x).
\]

For a cell this becomes

\[
\rho_{Q,a}
=\frac{E_Q}{c^2V_a}\frac{Q_a}{q_0}.
\]

The earlier RF-N1B cell formula follows when the independent bindings

\[
E_Q=\hbar|\omega|,
\qquad
Q_a/q_0=n_{E,a},
\qquad
V_a=V_H
\]

are admitted.

The normalization frontier is now explicit:

```text
q0                         OPEN
energy per carrier charge  OPEN
IDT p <-> carrier p_Q      OPEN
carrier density <-> rho_m  OPEN
```

## 11. Information-curvature candidate and universality target

Bounded GREMLIN retains the source-basis candidate

\[
\boxed{\mathcal S_R=\beta_I\Xi_I+\cdots}
\]

with coefficient promotion reserved for a separate derivation gate.

For a constant-rate projective cell,

\[
\Xi_I
=\frac{\mathcal J_\pi}{a_{FS}}
\left(\frac{\omega}{c}\right)^2.
\]

Combining this only as a target consistency test with the RF-N1B phase-cell candidate gives

\[
\boxed{
G_{\rm target}
=\frac{\beta_I\mathcal J_\pi}
{24\pi\sqrt6\,n_Ea_{FS}}
\frac{c^5}{\hbar\omega^2}.
}
\]

Therefore a viable downstream route must generate the required source-independent behavior of

\[
\boxed{
\mathcal U_G=
\frac{\beta_I\mathcal J_\pi}
{n_Ea_{FS}\omega^2}.
}
\]

RF-N1C will test this only after source normalization is independently fixed.

## 12. GREMLIN carrier isomorphism

The bounded relational-isomorphism audit finds the common abstract structure

```text
TIR cyclic chi       -> conserved total phase charge
ENB global U(1)      -> conserved local phase current
fluid_time rho_tau   -> conserved local temporal current
IDT normalized p     -> distributional shape
```

with invariant

```text
conserved extensive carrier + normalized distributional shape
```

The following candidate maps remain explicitly gated:

\[
J\stackrel{?}{=}Q_\Sigma,
\qquad
J_\varphi^\mu\stackrel{?}{=}J_\tau^\mu,
\qquad
p_{\rm IDT}\stackrel{?}{=}p_Q.
\]

Candidate generation has no authority to fix `q_0`, `epsilon_Q`, matter semantics, `beta_I`, or `G`.

## 13. Current frontier

The Newton chain is now

\[
\boxed{
N_R
\to
\Phi_R=c^2\ln N_R
\to
-\nabla\Phi_R
}
\]

and

\[
\boxed{
\text{Onsager}
+\text{hexahedral symmetry}
\to
\Delta_h
}
\]

and independently

\[
\boxed{
J_Q^\mu
\to
Q_\Sigma,p_Q
\to
\{q_0\text{ or }\epsilon_Q\}
\to
\rho_{\rm source}.
}
\]

The remaining normalization chain is

\[
\boxed{
\rho_{\rm source}
\to
\mathcal S_R
\to
G.
}
\]

## 14. Status table

| Gate | Status |
|---|---|
| RF-02H hexahedral rank-3 spatial metric | `LOCAL STRUCTURAL PASS` |
| RF-G0 Lorentzian signature | `EXACT CONDITIONAL PASS` |
| RF-02I coframe connection | `LOCAL EXACT CONNECTION PASS` |
| IDT 05C relational lapse ratio | `EXACT CLOCK-RATIO PASS` |
| RF-N0 lapse geodesic kinematics | `EXACT CONDITIONAL PASS` |
| RF-N1A hexahedral source operator | `LOCAL EXACT PASS` |
| RF-N1B source-type firewall | `EXACT TYPE-SEPARATION PASS` |
| RF-N1B conditional phase-cell density | `EXACT ALGEBRA / OCCUPATION BINDING OPEN` |
| RF-N1B2 continuous conserved carrier | `PASS` |
| RF-N1B2 extensive carrier `Q_Sigma` | `PASS / BOUNDARY-CONDITIONED` |
| RF-N1B2 normalized carrier profile | `PASS / POSITIVE-SOURCE SECTOR` |
| IDT `p` to carrier-profile cross-binding | `OPEN` |
| carrier quantum `q0` | `OPEN` |
| energy-per-carrier `epsilon_Q` | `OPEN` |
| carrier-to-matter/source binding | `OPEN` |
| RF-N1C coupling / universality / `G` | `OPEN` |
| RF-M2 sourced Maxwell | `OPEN` |
| RF-L1 dynamic Lambda0 | `OPEN` |
| RF-E1 Einstein-Bianchi closure | `OPEN` |

## 15. Immediate theorem target

The next theorem target is now narrower than in v0.10:

\[
\boxed{
\text{derive }q_0\text{ or }\epsilon_Q
\quad\text{from the admitted phase/time Hamiltonian}
}
\]

followed by the cross-binding

\[
\boxed{
\rho_{\rm carrier}
\stackrel{?}{\longrightarrow}
\rho_{\rm physical\ source}.
}
\]

A successful gate would eliminate the last free normalization between the now-conserved carrier and the Newton-source density, opening RF-N1C as a genuine no-refit universality test for `G`.
