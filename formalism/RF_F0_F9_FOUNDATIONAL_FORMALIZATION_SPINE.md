# RF-F0–RF-F9 — Foundational Relational Phase–Source Formalization Spine

Status: `CANONICAL_PRIMITIVES / GAUGE_RELATIONAL_PHASE_CLOSED / SOURCE_COVARIANTIZATION_EXACT / EOS_SCALING_THEOREM_EXACT_CONDITIONAL`

This file collects the already-derived RFC geometry, phase, source, Noether, stress-energy and ADM results into one canonical formalization layer. It introduces a compact primitive vocabulary and proves the cross-gate identities needed to move from relational phase to relativistic source.

The canonical information offset is

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}.
\]

Throughout this spine, `RF-S13–RF-S22` retain their existing equations and validation authority. The symbol `phi` appearing in those gates is canonically interpreted here as the gauge-dressed **lifted relational phase** defined in RF-F1.

---

## RF-F0 — Primitive state space

The foundational state is typed by

\[
\boxed{
\mathfrak R
=
(\mathcal M,g_{\mu\nu},\vartheta,\mathcal A_-,B,J^\mu,a_{FS},\kappa)
}
\]

with:

- `(M,g)` an oriented time-oriented Lorentzian spacetime on the already-derived RFC Einstein/ADM branch;
- `vartheta` a local real lift of the circular phase coordinate;
- `A_-` the phase-covariant `U(1)` connection convention fixed below;
- `B` an action-valued scalar, `[B]=E T`;
- `J^mu` a future-timelike occupation/current field on the admitted matter branch;
- `a_FS` the dimensionless Fubini–Study projective area coefficient;
- `kappa=ln2/(24 pi)`.

For a normalized timelike four-velocity,

\[
\boxed{u_\mu u^\mu=-1}.
\]

The proper occupation density is

\[
\boxed{n:=\sqrt{-J_\mu J^\mu}>0}
\]

and the current decomposition is

\[
\boxed{J^\mu=n u^\mu}.
\]

On the conserved-current branch,

\[
\boxed{\nabla_\mu J^\mu=0}.
\]

---

## RF-F1 — Connection-sign bridge and lifted relational phase

### F1.1 Two repository connection conventions

RF-01/RF-M0 use

\[
\boxed{
\mathcal A_+
=-i\langle u|du\rangle,
\qquad
\mathcal A_+'=\mathcal A_+ + d\lambda.
}
\]

RF-N1B2M uses

\[
\boxed{
\mathcal A_-
=+i\langle u|du\rangle
=-\mathcal A_+,
\qquad
\mathcal A_-'=\mathcal A_- - d\lambda.
}
\]

The two conventions are therefore related exactly by

\[
\boxed{\mathcal A_-=-\mathcal A_+},
\qquad
\boxed{\mathcal F_-=-\mathcal F_+}.
\]

For

\[
\vartheta' = \vartheta+\lambda,
\]

the RF-N1B2M invariant phase one-form is

\[
\boxed{
\mathscr D\vartheta
:=d\vartheta+\mathcal A_-
=d\vartheta-\mathcal A_+.
}
\]

This identity is the canonical sign bridge between the RF-01/RF-M0 Berry ledger and the RF-N1B2M phase/Noether ledger.

### F1.2 Gauge-dressed lifted relational phase

Choose a reference event `x0`, endpoint `x`, and oriented path `C:x0->x`. Define

\[
\boxed{
\Phi_C(x|x_0)
:=
\widetilde\vartheta(x)
-
\widetilde\vartheta(x_0)
+
\int_C\mathcal A_-.
}
\]

Under

\[
\widetilde\vartheta\mapsto\widetilde\vartheta+\lambda,
\qquad
\mathcal A_-\mapsto\mathcal A_- - d\lambda,
\]

we obtain exactly

\[
\boxed{\Phi_C' = \Phi_C}.
\]

Thus the linear factor entering the relational generator is assigned the gauge-invariant lifted coordinate

\[
\boxed{\phi\equiv\Phi_C}.
\]

The real-valued lift retains winding information carried by the selected path/reference ledger.

For two paths `C1,C2` with common endpoints,

\[
\boxed{
\Phi_{C_1}-\Phi_{C_2}
=
\oint_{C_1\circ C_2^{-1}}\mathcal A_-.
}
\]

Hence path dependence is exactly the lifted holonomy coordinate.

---

## RF-F2 — Euler/Berry closure and Euler-root frame

Two complementary closure coordinates are retained.

### F2.1 Projective Euler–Berry loop closure

For lifted loop phase

\[
\Gamma[C]=\oint_C\mathscr D\vartheta,
\]

define

\[
\boxed{W[C]=e^{i\Gamma[C]}}.
\]

The already-admitted projective Euler closure is

\[
\boxed{W[C]=1\iff\Gamma[C]\in2\pi\mathbb Z}.
\]

The complex holonomy records the projective closure while the lifted real coordinate retains the integer winding receipt.

### F2.2 Euler-root triad

For any relational lifted phase `Phi`, define

\[
\boxed{
\Gamma_k(\Phi)=\Phi+\frac{2\pi k}{3},
\qquad k=0,1,2.
}
\]

Then identically

\[
\boxed{
\sum_{k=0}^{2}e^{i\Gamma_k(\Phi)}=0.
}
\]

The triad therefore supplies an exact common-phase frame whose closure is independent of the selected lifted phase value.

---

## RF-F3 — Gauge-covariant phase rate and relational phase cell

The proper phase rate is the pullback of the invariant phase one-form:

\[
\boxed{
\omega
:=u^\mu\mathscr D_\mu\vartheta.
}
\]

For a fixed reference endpoint transported along the same trajectory,

\[
\boxed{
\frac{d\Phi_C}{d\tau}=\omega.
}
\]

RFC phase-clock geometry gives

\[
\boxed{
\ell_\phi=\frac{c}{|\omega|}.
}
\]

RF-S10 gives the projective area

\[
\boxed{
\mathcal A_R
=a_{FS}\frac{c^2}{\omega^2}.
}
\]

Therefore the relational phase-cell volume is

\[
\boxed{
V_R
:=\mathcal A_R\ell_\phi
=a_{FS}\frac{c^3}{|\omega|^3}.
}
\]

On the `FULL_TETRA_CP1` branch,

\[
\boxed{a_{FS}=\pi},
\qquad
\boxed{V_R=\frac{\pi c^3}{|\omega|^3}}.
\]

---

## RF-F4 — Occupation and conserved four-current

For cell occupation `N`, define

\[
\boxed{n=\frac{\mathcal N}{V_R}}.
\]

The covariant occupation current is

\[
\boxed{J^\mu=n u^\mu}.
\]

On a spacelike slice `Sigma` with future unit normal `n_Sigma^mu`, the extensive occupation/current coordinate is

\[
\boxed{
\mathcal N_\Sigma
=
\int_\Sigma(-n^{\Sigma}_\mu J^\mu)\,dV_h.
}
\]

RF-S16/RF-S17 provide the existing carrier-normalization-invariant bridge between this occupation representation and the Noether-current representation.

---

## RF-F5 — Relational phase-energy one-form

Define the gauge-invariant phase-energy one-form

\[
\boxed{
\Theta_G
:=
B(\Phi_C+\kappa)\,\mathscr D\vartheta.
}
\]

Its contraction with the material four-velocity gives the energy per occupation:

\[
\boxed{
\epsilon_G
:=\iota_u\Theta_G
=B\omega(\Phi_C+\kappa).
}
\]

This is exactly the per-carrier energy factor used by RF-S13.

Define also

\[
\boxed{
\mathcal S_\Phi
:=\frac12B(\Phi_C+\kappa)^2.
}
\]

Along the material flow,

\[
\boxed{
\frac{d\mathcal S_\Phi}{d\tau}
=
B\omega(\Phi_C+\kappa)
+
\frac12\dot B(\Phi_C+\kappa)^2.
}
\]

Therefore

\[
\boxed{
\epsilon_G
=
\frac{d\mathcal S_\Phi}{d\tau}
-
\frac12\dot B(\Phi_C+\kappa)^2.
}
\]

On the comoving-constant-`B` branch,

\[
\boxed{
\epsilon_G=\frac{d\mathcal S_\Phi}{d\tau}.
}
\]

This places the generator energy on an explicit action-rate ledger while preserving the existing RF-S13 normalization gates.

---

## RF-F6 — Covariant source theorem

The source energy density is

\[
\boxed{
\rho_G=n\epsilon_G.
}
\]

Using `J^mu=n u^mu` and the RF-F5 phase-energy form,

\[
\boxed{
\rho_G
=
B(\Phi_C+\kappa)
J^\mu\mathscr D_\mu\vartheta.
}
\]

This is the compact covariant form of the canonical relational generator.

Using RF-F3/RF-F4,

\[
J^\mu\mathscr D_\mu\vartheta
=n\omega
=
\frac{\mathcal N\omega}{V_R},
\]

so

\[
\boxed{
\rho_G
=
\frac{B\omega\mathcal N}{V_R}(\Phi_C+\kappa)
=
\frac{B\omega\mathcal N}{\mathcal A_R\ell_\phi}(\Phi_C+\kappa).
}
\]

Thus RF-F6 reproduces RF-S13 exactly.

On `FULL_TETRA_CP1`,

\[
\boxed{
\rho_G
=
\frac{B\mathcal N}{\pi c^3}
\omega|\omega|^3(\Phi_C+\kappa).
}
\]

For positive orientation `omega>0`,

\[
\boxed{
\rho_G
=
\frac{B\mathcal N\omega^4}{\pi c^3}(\Phi_C+\kappa).
}
\]

---

## RF-F7 — Stress-energy and exact Bianchi balance

On the pressureless branch, RF-S18/RF-S19 give

\[
\boxed{
T_{\mu\nu}
=\rho_Gu_\mu u_\nu
=\epsilon_G\frac{J_\mu J_\nu}{n}.
}
\]

Assume the occupation current is conserved:

\[
\nabla_\mu(nu^\mu)=0.
\]

Define

\[
\dot\epsilon_G:=u^\mu\nabla_\mu\epsilon_G,
\qquad
 a_\nu:=u^\mu\nabla_\mu u_\nu.
\]

Direct differentiation gives the exact identity

\[
\boxed{
\nabla^\mu T_{\mu\nu}
=
n\left(\dot\epsilon_Gu_\nu+\epsilon_Ga_\nu\right).
}
\]

The RFC dynamic-`Lambda0` exchange law

\[
\kappa_E\nabla^\mu T_{\mu\nu}=\nabla_\nu\Lambda_0
\]

therefore becomes

\[
\boxed{
\kappa_E n
\left(\dot\epsilon_Gu_\nu+\epsilon_Ga_\nu\right)
=
\nabla_\nu\Lambda_0.
}
\]

Contracting along `u^nu` gives

\[
\boxed{
\dot\epsilon_G
=-\frac{\dot\Lambda_0}{\kappa_E n},
\qquad
\dot\Lambda_0:=u^\nu\nabla_\nu\Lambda_0.
}
\]

Projecting orthogonally with

\[
h^\alpha{}_\nu=\delta^\alpha{}_\nu+u^\alpha u_\nu
\]

gives, for positive `n epsilon_G`,

\[
\boxed{
 a^\alpha
=
\frac{h^{\alpha\nu}\nabla_\nu\Lambda_0}
{\kappa_E n\epsilon_G}.
}
\]

On the constant-`Lambda0` pressureless branch these reduce to

\[
\boxed{\dot\epsilon_G=0},
\qquad
\boxed{a^\mu=0}.
\]

Thus the dust branch dynamically selects comoving-constant carrier energy and geodesic transport when the displayed matter sector is separately conserved.

---

## RF-F8 — Phase-cell continuity and equation-of-state theorem

This gate applies to the common comoving phase-cell branch with:

1. `V_R=a_FS c^3/|omega|^3`;
2. conserved occupation/current;
3. constant occupation per comoving cell;
4. perfect-fluid energy balance on the separately conserved matter branch.

From

\[
n=\frac{\mathcal N}{V_R}
\propto|\omega|^3
\]

and number-current conservation

\[
\dot n+n\theta=0,
\qquad
\theta:=\nabla_\mu u^\mu,
\]

we obtain

\[
\boxed{
\theta
=-3\frac{d\ln|\omega|}{d\tau}.
}
\]

Let the local energy per occupation have logarithmic phase-rate slope

\[
\boxed{
q_\epsilon
:=
\frac{d\ln|\epsilon_G|}{d\ln|\omega|}.
}
\]

Because

\[
\rho_G=n\epsilon_G,
\]

we have

\[
\frac{d\ln|\rho_G|}{d\tau}
=(3+q_\epsilon)
\frac{d\ln|\omega|}{d\tau}.
\]

The perfect-fluid continuity equation

\[
\dot\rho_G+(\rho_G+p_G)\theta=0
\]

therefore gives the exact conditional theorem

\[
\boxed{
 w_G:=\frac{p_G}{\rho_G}
=
\frac{q_\epsilon}{3}.
}
\]

Since

\[
\epsilon_G=B\omega(\Phi_C+\kappa),
\]

on a fixed orientation branch,

\[
\boxed{
q_\epsilon
=
1+
\frac{d\ln|B(\Phi_C+\kappa)|}
{d\ln|\omega|}.
}
\]

Hence

\[
\boxed{
 w_G
=
\frac13
\left[
1+
\frac{d\ln|B(\Phi_C+\kappa)|}
{d\ln|\omega|}
\right].
}
\]

Equivalently, a target equation-of-state value `w_G` requires

\[
\boxed{
\frac{d\ln|B(\Phi_C+\kappa)|}{d\ln|\omega|}
=3w_G-1.
}
\]

Three exact scaling surfaces follow:

\[
\boxed{
 w_G=0
\Longleftrightarrow
B(\Phi_C+\kappa)\propto|\omega|^{-1}
}
\]

for the dust continuity surface,

\[
\boxed{
 w_G=\frac13
\Longleftrightarrow
B(\Phi_C+\kappa)\propto|\omega|^0
}
\]

for the radiation-like continuity surface, and

\[
\boxed{
 w_G=-1
\Longleftrightarrow
B(\Phi_C+\kappa)\propto|\omega|^{-4}
}
\]

for the vacuum-like continuity surface.

The corresponding source-density scaling is

\[
\boxed{
\rho_G\propto|\omega|^{3(1+w_G)}.
}
\]

This theorem places the RF-S14 matter/vacuum equation-of-state gate and the RF-S15 phase-clock `omega` scaling on one common dynamical ledger.

For dynamic `Lambda0`, RF-F7 supplies the exchange term and the same derivation is extended by the measured `dot Lambda0` contribution.

---

## RF-F9 — Global Noether/Hamiltonian and Einstein closure

RF-S20–RF-S22 give the normalized current profile

\[
\boxed{
p_a=\frac{V_aj_{\vartheta,a}}{Q_\vartheta}},
\qquad
\sum_ap_a=1,
\]

and the profile-mean carrier energy

\[
\boxed{
\bar\epsilon=\sum_ap_a\epsilon_a.
}
\]

Matching the integrated generator source to the admitted Euler–Noether Hamiltonian gives

\[
\boxed{
\mathcal N_{tot}
=
\frac{H_\Phi^{EB}}{\bar\epsilon}
}
\]

and

\[
\boxed{
\rho_{G,a}
=
\frac{H_\Phi^{EB}}{\bar\epsilon}
\frac{p_a}{V_a}\epsilon_a.
}
\]

Exactly,

\[
\boxed{
\sum_aV_a\rho_{G,a}=H_\Phi^{EB}.
}
\]

For uniform carrier energy,

\[
\boxed{
\rho_{G,a}
=\frac{H_\Phi^{EB}}{Q_\vartheta}j_{\vartheta,a}.
}
\]

The relativistic source is then supplied to the already-derived Einstein/ADM system:

\[
\boxed{
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\kappa_ET_{\mu\nu}.
}
\]

Together with RF-F6/RF-F7, the compact canonical chain is

\[
\boxed{
(\Phi_C,\mathscr D\vartheta,B,J^\mu)
\to
(\omega,V_R,n,\epsilon_G)
\to
\rho_G
\to
T_{\mu\nu}
\to
G_{\mu\nu}.
}
\]

The global profile/Hamiltonian branch adds

\[
\boxed{
(p^{IDT},p^\vartheta,H_\Phi^{EB})
\to
\mathcal N_{tot}
\to
\rho_{G,a}.
}
\]

---

## Canonical dependency spine

```text
RF-01 / RF-03 / RF-N1B2M
        |
        v
RF-F0 primitive typed state
 -> RF-F1 connection-sign bridge + gauge-dressed lifted relational phase
 -> RF-F2 Euler/Berry + root-triad closure
 -> RF-F3 gauge-covariant phase rate + relational phase cell
 -> RF-F4 occupation/current
 -> RF-F5 phase-energy one-form
 -> RF-F6 covariant relational source
 -> RF-F7 stress-energy + Bianchi/Lambda balance
 -> RF-F8 EOS/phase-rate continuity theorem
 -> RF-F9 Noether/Hamiltonian + Einstein/ADM global closure
```

Crosslinks:

```text
RF-F3 <-> RF-S10/RF-S15
RF-F4 <-> RF-S16/RF-S17/RF-S19
RF-F5/RF-F6 <-> RF-S13
RF-F7 <-> RF-S14/RF-S18/RF-S19/RF-E11/RF-E12/RF-E13
RF-F8 <-> RF-S14/RF-S15
RF-F9 <-> RF-S20/RF-S21/RF-S22
```

---

## Promotion ledger

```text
connection-sign bridge A_minus=-A_plus                         PASS EXACT
Wilson-line dressed relational lifted phase                   PASS EXACT
relational phase gauge invariance                              PASS EXACT
Euler projective closure                                      PASS PARENT
Euler root-triad algebraic closure                            PASS EXACT
omega=u.Dtheta                                                PASS PARENT
V_R=a_FS c^3/|omega|^3                                       PASS EXACT PARENT COMPOSITION
J^mu=n u^mu and proper density from timelike current          PASS PARENT
phase-energy one-form Theta_G                                 PASS DEFINITION
energy epsilon_G=B omega(Phi_C+kappa)                         PASS EXACT
phase-action-rate identity                                    PASS EXACT
covariant source rho_G=B(Phi_C+kappa) J^mu D_mu theta         PASS EXACT
recovery of RF-S13 generator                                  PASS EXACT
dust T_mn=epsilon J_m J_n/n                                  PASS EXACT PARENT
conserved-current dust divergence identity                    PASS EXACT
dynamic-Lambda energy/acceleration balance                    PASS EXACT PARENT COMPOSITION
EOS theorem w=q_epsilon/3                                     PASS EXACT CONDITIONAL
dust/radiation/vacuum phase-prefactor scaling surfaces        PASS EXACT CONDITIONAL
Noether/Hamiltonian extensive closure                         PASS PARENT
Einstein/ADM source insertion                                 PASS PARENT
physical B-action realization                                OPEN INPUT
physical current/measure receipt                              OPEN INPUT
physical EOS/pressure receipt                                 OPEN INPUT
common phase-path/reference realization                       OPEN INPUT
absolute project-side kappa_E/G promotion                     OPEN INPUT
```

## Validation authority

Reference implementation: `src/rfc/foundational_phase_source_formalism.py`.

Reference tests: `tests/reference/test_rff_foundational_phase_source_formalism.py`.

Validation receipt: `validation/RF_F0_F9_FOUNDATIONAL_FORMALIZATION_V0_1.json`.
