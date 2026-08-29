# RF-F15 — Microscopic Scalar ↔ Phase-Cell Transport Closure

Status: `CURRENT_CELL_AMPLITUDE_SCALING_EXACT / EOS_TRANSPORT_ODE_EXACT / RADIATION_FIXED_POINT_EXACT / RADIATION_VACUUM_DECOMPOSITION_EXACT / DUST_TRAJECTORY_EXACT / PHYSICAL_CURRENT_BINDING_CONDITIONAL`

RF-F15 is stacked on RF-F14. It closes the mathematical transport condition left open between the microscopic RF-E7 scalar stress tensor and the RF-F8/RF-F12 phase-cell perfect-fluid scaling, conditional on the RF-N1B2K local current/measure identity.

Use the positive-orientation branch

\[
\omega>0
\]

and define

\[
X:=\Phi_C+\kappa,
\qquad
P:=BX,
\]

\[
x:=\frac{k^2}{\omega^2},
\qquad
v:=\frac{V}{A^2\omega^2},
\qquad
D:=1+x+v.
\]

RF-F14 gives

\[
\boxed{
\rho_{micro}=A^2\omega^2D
}
\]

and

\[
\boxed{
 p_{micro}=A^2\omega^2
 \left(1-\frac x3-v\right).
}
\]

---

## 1. Current binding fixes the amplitude scaling

RF-F3 gives the phase-cell volume

\[
V_R=a_{FS}\frac{c^3}{\omega^3}.
\]

For fixed occupation `N` in one comoving phase cell,

\[
\boxed{
 n=\frac{\mathcal N}{V_R}
 =\frac{\mathcal N\omega^3}{a_{FS}c^3}.
}
\]

RF-S16 writes the action-charge current as

\[
\boxed{j_Q=q_0n.}
\]

The Euler/Noether scalar phase current is

\[
\boxed{j_\vartheta=2A^2\omega.}
\]

On the zero-defect RF-N1B2K local-current surface,

\[
j_Q=j_\vartheta,
\]

so exactly

\[
2A^2\omega
=\frac{q_0\mathcal N\omega^3}{a_{FS}c^3}.
\]

Hence

\[
\boxed{
A^2
=\frac{q_0\mathcal N}{2a_{FS}c^3}\omega^2.
}
\]

Therefore the temporal phase-kinetic density

\[
K:=A^2\omega^2
\]

obeys

\[
\boxed{K=K_0\omega^4},
\qquad
\boxed{
K_0:=\frac{q_0\mathcal N}{2a_{FS}c^3}.
}
\]

This amplitude law follows from current binding plus phase-cell geometry; it is not an independent ansatz.

---

## 2. Exact total-energy/current binding

The current is

\[
j_\vartheta=2A^2\omega.
\]

Therefore

\[
\frac{\rho_{micro}}{j_\vartheta}
=\frac\omega2D.
\]

RF-F13/S16 gives

\[
\epsilon_Q=\frac{P\omega}{q_0}.
\]

Binding the F13 generator to the complete scalar energy/current ratio gives

\[
\boxed{
\frac{P}{q_0}=\frac D2.
}
\]

Thus all microscopic composition dependence enters the generator prefactor through the single scalar

\[
\boxed{D=1+x+v.}
\]

---

## 3. Microscopic ↔ phase-cell compatibility equation

RF-F14 gives

\[
 w_{micro}
=\frac{1-x/3-v}{D}.
\]

RF-F8 gives

\[
 w_{cell}
=\frac13
\left(
1+rac{d\ln|P|}{d\ln\omega}
\right).
\]

With constant positive `q0` and `P/q0=D/2`,

\[
\frac{d\ln|P|}{d\ln\omega}
=\frac{d\ln D}{d\ln\omega}.
\]

Requiring one common separately conserved perfect-fluid stress ledger,

\[
w_{cell}=w_{micro},
\]

gives

\[
\frac{d\ln D}{d\ln\omega}
=3\frac{1-x/3-v}{D}-1.
\]

Multiplying by `D` yields the exact transport equation

\[
\boxed{
\frac{dD}{d\ln\omega}
=2(1-x-2v).
}
\]

Since `D=1+x+v`, equivalently

\[
\boxed{
\frac{dx}{d\ln\omega}
+
\frac{dv}{d\ln\omega}
=2(1-x-2v).
}
\]

This is the RF-F15 microscopic composition transport closure.

---

## 4. Constant-composition fixed point: radiation

For

\[
\frac{dx}{d\ln\omega}=0,
\qquad
\frac{dv}{d\ln\omega}=0,
\]

RF-F15 reduces to

\[
\boxed{x+2v=1.}
\]

This is exactly the RF-F14 radiation surface. Therefore every constant microscopic composition compatible with the separately conserved phase-cell branch is radiation-like:

\[
\boxed{w=\frac13}.
\]

For nonnegative potential and `0<=x<=1`,

\[
\boxed{v=\frac{1-x}{2}}
\]

and

\[
D
=1+x+\frac{1-x}{2}
=\frac{3+x}{2}.
\]

Hence

\[
\boxed{
\frac{P}{q_0}=\frac{3+x}{4}.
}
\]

The two RF-F14 endpoint realizations are recovered:

\[
x=0
\Rightarrow
v=\frac12,
\quad
\frac{P}{q_0}=\frac34,
\]

\[
x=1
\Rightarrow
v=0,
\quad
\frac{P}{q_0}=1.
\]

---

## 5. Fixed spatial ratio: exact radiation + vacuum solution

Take

\[
\boxed{x=\text{constant}.}
\]

Then RF-F15 becomes

\[
\frac{dv}{d\ln\omega}
+4v
=2(1-x).
\]

Its exact solution is

\[
\boxed{
v(\omega)
=\frac{1-x}{2}
+\frac{C_\Lambda}{\omega^4},
}
\]

where `C_Lambda` is an integration constant with fourth-power rate type.

Because

\[
K=K_0\omega^4,
\]

the potential is

\[
V
=Kv
=
\frac{1-x}{2}K_0\omega^4
+K_0C_\Lambda.
\]

Define

\[
\boxed{
\rho_\Lambda:=K_0C_\Lambda
}
\]

and

\[
\boxed{
\rho_r
:=\frac{3+x}{2}K_0\omega^4.
}
\]

Then the full microscopic stress becomes exactly

\[
\boxed{
\rho_{micro}=\rho_r+\rho_\Lambda
}
\]

and

\[
\boxed{
 p_{micro}=\frac13\rho_r-\rho_\Lambda.
}
\]

Thus the integration constant of the microscopic/phase-cell transport equation is a constant vacuum-density contribution, while the dynamical term is radiation-like.

Using RF-F12,

\[
\omega\propto a^{-1},
\]

so

\[
\boxed{ho_r\propto a^{-4}},
\qquad
\boxed{ho_\Lambda=\mathrm{constant}}.
\]

The `C_Lambda=0` fixed point is pure radiation.

---

## 6. Exact dust transport trajectory

Impose the microscopic pressureless surface

\[
\boxed{p_{micro}=0}.
\]

From RF-F14,

\[
1-\frac x3-v=0,
\]

so

\[
\boxed{v=1-\frac x3.}
\]

Then

\[
D
=1+x+v
=2+\frac{2x}{3}
=\frac{2(x+3)}{3}.
\]

The RF-F15 transport equation reduces to

\[
\boxed{
\frac{dx}{d\ln\omega}=-(x+3).
}
\]

Integrating gives

\[
\boxed{
x+3=\frac{C_d}{\omega}}
\]

with positive rate constant `C_d`. Hence

\[
\boxed{
x=\frac{C_d}{\omega}-3},
\]

\[
\boxed{
v=2-\frac{C_d}{3\omega}},
\]

and

\[
\boxed{
D=\frac{2C_d}{3\omega}.
}
\]

Therefore the generator prefactor is

\[
\boxed{
\frac{P}{q_0}
=\frac{C_d}{3\omega}
}
\]

and the energy per action charge becomes

\[
\boxed{
\epsilon_Q
=\frac{P\omega}{q_0}
=\frac{C_d}{3}
=\mathrm{constant}.
}
\]

This reproduces the RF-F11 constant carrier-energy property of dust.

Since

\[
K=K_0\omega^4
\]

and

\[
D\propto\omega^{-1},
\]

the dust density is

\[
\boxed{
\rho_d
=KD
=\frac{2K_0C_d}{3}\omega^3.
}
\]

With RF-F12,

\[
\boxed{ho_d\propto a^{-3}}.
\]

For the nonnegative microscopic coordinates `x>=0`, `v>=0`, the local dust chart satisfies

\[
oxed{3\omega\le C_d\le6\omega}.
\]

The transport solution may be continued through other admitted matter coordinates when this chart boundary is reached.

---

## 7. Vacuum placement

RF-F14 gives

\[
\rho_{phase}+p_{phase}>0
\]

for every nonzero phase carrier. The exact metric-proportional vacuum surface is therefore the zero-current potential boundary. RF-F15 additionally shows that a constant vacuum density arises as the integration constant `rho_Lambda=K0 C_Lambda` in the fixed-spatial-ratio transport family.

This yields two compatible representations of the vacuum coordinate:

\[
\boxed{
\text{zero-current potential surface}
}
\]

and

\[
\boxed{
\text{constant integration component in the coupled transport solution}.
}
\]

Their physical identification remains controlled by the RF-L2/RF-F13 `Lambda0` binding.

---

## 8. Unified transport picture

The microscopic/phase-cell bridge now has the exact structure

\[
\boxed{
J^\mu\text{ binding}
\rightarrow
A^2\propto\omega^2
\rightarrow
K\propto\omega^4
\rightarrow
D=1+x+v
\rightarrow
P/q_0=D/2
}
\]

followed by

\[
\boxed{
\frac{dD}{d\ln\omega}=2(1-x-2v).
}
\]

Its principal exact sectors are

\[
\boxed{
\text{radiation fixed point: }x+2v=1,\quad\rho\propto\omega^4
}
\]

\[
\boxed{
\text{fixed-}x\text{ family: }ho=\rho_r+\rho_\Lambda
}
\]

\[
\boxed{
\text{dust trajectory: }p=0,\quad P\propto\omega^{-1},\quad\rho\propto\omega^3.
}
\]

With `a omega=const`, these become the standard `a^-4`, constant-vacuum, and `a^-3` density laws from one common microscopic transport equation.

---

## 9. Advancement

```text
phase-cell n=N omega^3/(a_FS c^3)                         PASS PARENT
current binding j_Q=q0 n = j_theta                        CONDITIONAL RF-N1B2K
A^2=q0 N omega^2/(2 a_FS c^3)                            PASS EXACT ON BINDING
K=K0 omega^4                                               PASS EXACT
P/q0=(1+x+v)/2 total-scalar binding                        PASS EXACT
microscopic/phase-cell dD/dlnomega=2(1-x-2v)              PASS EXACT
constant-composition radiation fixed point x+2v=1          PASS EXACT
radiation P/q0=(3+x)/4                                     PASS EXACT
fixed-x v=(1-x)/2+C_Lambda/omega^4                        PASS EXACT
rho=rho_r+rho_Lambda                                       PASS EXACT
p=rho_r/3-rho_Lambda                                       PASS EXACT
dust v=1-x/3                                               PASS EXACT
dust x+3=C_d/omega                                         PASS EXACT
dust P/q0=C_d/(3 omega)                                    PASS EXACT
dust epsilon_Q=C_d/3 constant                              PASS EXACT
dust rho proportional omega^3                              PASS EXACT
RF-F12 -> radiation a^-4 / dust a^-3 / vacuum constant    PASS EXACT PARENT COMPOSITION
physical zero-defect local current/measure receipt          OPEN RF-N1B2K INPUT
physical rho_Lambda <-> RF-L2 Lambda0 attribution           OPEN BINDING
multispecies transport composition                          OPEN INPUT
absolute kappa_E/G promotion                                OPEN PROJECT FRONTIER
```

## 10. Validation authority

Reference implementation:

`src/rfc/microscopic_phase_cell_transport.py`

Reference tests:

`tests/reference/test_rff15_microscopic_phase_cell_transport.py`

Validation receipt:

`validation/RF_F15_MICROSCOPIC_PHASE_CELL_TRANSPORT_V0_1.json`

Stack parent:

`RF-F14 branch head a46315fa118da4343dd4d0310b2b6c69df6769e1`.
