# RF-F14 — Noether Energy / Phase-Cell EOS Sector Compatibility Firewall

Status: `ACTION_CHARGE_DIMENSION_CLOSED / MICROSCOPIC_PHASE_EOS_EXACT / RADIATION_SURFACE_EXACT / NULL_ISOTROPIC_RADIATION_PASS / NORMAL_PHASE_HALF_RATE_TYPED / PHASE_CELL_COMPATIBILITY_EXACT / VACUUM_ZERO_CURRENT_BOUNDARY_EXACT`

RF-F14 is stacked on RF-F13 and cross-checks four already-derived ledgers that use the same phase variables for different physical roles:

- RF-N1B2I/J/L/M/O: Euler/Noether action charge and the collective phase-energy ratio;
- RF-S16/RF-S17: carrier-normalized generator energy;
- RF-E4/RF-E6/RF-E7: microscopic scalar stress-energy and pressure;
- RF-F8/RF-F12: phase-cell continuity and effective perfect-fluid scaling.

The purpose is to type the common surfaces before promoting one energy/current ratio into a total-matter equation of state.

Let

\[
X:=\Phi_C+\kappa,
\qquad
P:=BX,
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

RF-F13 gives

\[
H_G=P\omega
\]

on the degree-one Hamiltonian surface.

---

## 1. Action-charge dimensional bridge

RF-N1B2I fixes the Euler-closed intention charge as

\[
J_I^{EB}=\hbar\theta_I^{EB},
\]

so the Noether/rotor carrier has action type. Consequently

\[
\epsilon_N^{EB}:=\frac{H_\Phi^{EB}}{Q_\vartheta}
\]

has units of inverse time.

RF-S16 writes the source in an arbitrary positive carrier unit `q0`,

\[
j_Q=q_0 n,
\qquad
\epsilon_Q=\frac{B\omega X}{q_0}=\frac{P\omega}{q_0}.
\]

On the physical RF-N1B2K binding to the Noether action-charge current, `q0` therefore inherits action type. Then

\[
\boxed{[P]=[q_0]=\text{action}},
\qquad
\boxed{[\epsilon_Q]=T^{-1}},
\]

and the comparison

\[
\boxed{
\frac{P\omega}{q_0}
\stackrel{bind}{=}
\frac{H_\Phi^{EB}}{Q_\vartheta}
}
\]

is dimensionally closed.

---

## 2. Normal collective phase-energy surface

RF-N1B2M/O and RF-E4 use the pure normal collective phase mode

\[
q_{\hat a}=(\omega,0,0,0),
\qquad
K:=A^2\omega^2.
\]

For the phase-kinetic piece `V=0`,

\[
\boxed{j_\vartheta=2A^2\omega},
\qquad
\boxed{\rho_{phase}=K},
\qquad
\boxed{p_{phase}=K}.
\]

Hence

\[
\boxed{w_{micro}=1}
\]

and

\[
\boxed{
\frac{\rho_{phase}}{j_\vartheta}
=\frac\omega2.
}
\]

On the zero-defect RF-N1B2K binding,

\[
\epsilon_Q=\epsilon_N=\frac\omega2.
\]

Combining with RF-F13/S16,

\[
\frac{P\omega}{q_0}=\frac\omega2
\]

for nonzero positive `omega`, so

\[
\boxed{
\frac{P}{q_0}=\frac12.
}
\]

This is the exact normal-phase Noether normalization surface.

---

## 3. General microscopic phase EOS

In a local orthonormal frame take

\[
q_{\hat a}=(\omega,\mathbf k),
\qquad
k:=|\mathbf k|.
\]

For the canonical scalar action, after isotropic directional averaging of the spatial phase direction, RF-E7 gives

\[
\boxed{
\rho_{micro}
=A^2(\omega^2+k^2)+V,
}
\]

\[
\boxed{
p_{micro}
=A^2\left(\omega^2-\frac{k^2}{3}\right)-V.
}
\]

Define

\[
\boxed{x:=\frac{k^2}{\omega^2}},
\qquad
\boxed{v:=\frac{V}{A^2\omega^2}}.
\]

Then

\[
\boxed{
 w_{micro}
=\frac{1-x/3-v}{1+x+v}.
}
\]

The normal Noether carrier density is

\[
\boxed{j_\vartheta=2A^2\omega}
\]

on the positive orientation branch, so the complete scalar energy/action-charge rate is

\[
\boxed{
\epsilon_{scalar}
:=\frac{\rho_{micro}}{j_\vartheta}
=\frac\omega2(1+x+v).
}
\]

Therefore a total-scalar F13 generator binding requires

\[
\boxed{
\frac{P}{q_0}
=\frac12(1+x+v).
}
\]

This is separately typed from the phase-kinetic-only value `P/q0=1/2`.

---

## 4. Exact radiation surface

Set

\[
w_{micro}=\frac13.
\]

Direct substitution gives

\[
3\left(1-\frac x3-v\right)=1+x+v,
\]

hence exactly

\[
\boxed{x+2v=1.}
\]

This is the RF-F14 microscopic radiation surface.

Two exact realizations are immediate.

### 4.1 Isotropic null phase ensemble

For

\[
k=\omega,
\qquad
V=0,
\]

we have

\[
\boxed{x=1,\qquad v=0},
\]

so

\[
\boxed{w_{micro}=\frac13}.
\]

The stress tensor of each mode is null-directed; isotropic directional averaging gives the radiation pressure. Its energy/action-charge rate is

\[
\boxed{
\epsilon_{null}=\omega
}
\]

and therefore

\[
\boxed{
\frac{P}{q_0}=1.
}
\]

### 4.2 Homogeneous normal radiation completion

For

\[
k=0,
\qquad
V=\frac12K,
\qquad
K=A^2\omega^2,
\]

we have

\[
\boxed{x=0,\qquad v=\frac12}
\]

and again

\[
\boxed{w_{micro}=\frac13}.
\]

The complete scalar energy/action-charge rate is now

\[
\boxed{
\epsilon_{scalar}=\frac34\omega
}
\]

so the total-scalar F13 normalization is

\[
\boxed{
\frac{P}{q_0}=\frac34.
}
\]

Thus the same radiation EOS can be realized by distinct microscopic stress compositions carrying distinct energy/current normalization ratios.

---

## 5. Phase-cell continuity compatibility

RF-F8 gives, for the separately conserved comoving phase-cell perfect-fluid branch,

\[
\boxed{
 w_{cell}
=\frac13\left(1+rac{d\ln|P|}{d\ln|\omega|}\right).
}
\]

Equivalently a microscopic target `w` requires

\[
\boxed{
\frac{d\ln|P|}{d\ln|\omega|}=3w-1.
}
\]

Therefore:

\[
\boxed{w=1\Rightarrow d\ln|P|/d\ln|\omega|=2},
\]

\[
\boxed{w=\frac13\Rightarrow d\ln|P|/d\ln|\omega|=0},
\]

\[
\boxed{w=0\Rightarrow d\ln|P|/d\ln|\omega|=-1},
\]

\[
\boxed{w=-1\Rightarrow d\ln|P|/d\ln|\omega|=-4}.
\]

A fixed carrier unit `q0` plus a fixed microscopic ratio `P/q0` gives a constant `P` surface. On the RF-F8 separately conserved phase-cell branch this selects

\[
\boxed{w_{cell}=\frac13}.
\]

Consequently the isotropic-null radiation branch and the homogeneous `V=K/2` radiation completion are directly compatible with constant-prefactor phase-cell scaling. The pure normal phase-kinetic `P/q0=1/2` surface carries microscopic `w=1`; its separately conserved phase-cell realization requires the distinct scaling `P\propto|\omega|^2`.

This is the sector-typing firewall between the local Noether reduction and the cosmological phase-cell continuity assumptions.

---

## 6. Dust surface

RF-E5/RF-E7 give the homogeneous on-shell massive scalar surface

\[
k=0,
\qquad
V=K.
\]

Then

\[
\boxed{w_{micro}=0},
\qquad
\boxed{\rho_{dust}=2K},
\]

and

\[
\boxed{
\frac{\rho_{dust}}{j_\vartheta}=\omega.
}
\]

Thus the local total-scalar normalization is

\[
\boxed{
\frac{P}{q_0}=1.
}
\]

The RF-F8 comoving phase-cell dust branch independently requires

\[
\boxed{P\propto|\omega|^{-1}}.
\]

RF-F14 therefore keeps the local on-shell massive realization and the varying-`omega` phase-cell transport realization as separately typed dust coordinates until a common transport receipt relates their scale evolution.

---

## 7. Vacuum boundary theorem

For the general microscopic phase sector,

\[
\rho_{micro}+p_{micro}
=2A^2\omega^2+\frac23A^2k^2.
\]

Therefore

\[
\boxed{
\rho_{micro}+p_{micro}>0
}
\]

for every nonzero positive-orientation phase carrier.

The exact metric-proportional scalar vacuum surface is reached on the zero-phase-current boundary

\[
\boxed{\omega=0,\qquad k=0},
\]

where the remaining potential contribution satisfies

\[
T_{\mu\nu}^{pot}=-Vg_{\mu\nu}.
\]

This aligns the vacuum-like EOS with the RF-L2/RF-F13 potential/`Lambda0` ledger while preserving the current-carrying phase sectors for matter/radiation transport.

---

## 8. Branch matrix

| branch | microscopic condition | `w_micro` | energy/action-charge rate | `P/q0` on total binding | RF-F8 required `d ln P/d ln|omega|` |
|---|---|---:|---:|---:|---:|
| normal phase kinetic | `k=0, V=0` | `1` | `omega/2` | `1/2` | `2` |
| isotropic null phase | `k=omega, V=0` | `1/3` | `omega` | `1` | `0` |
| homogeneous radiation completion | `k=0, V=K/2` | `1/3` | `3 omega/4` | `3/4` | `0` |
| homogeneous dust | `k=0, V=K` | `0` | `omega` | `1` | `-1` |
| potential vacuum boundary | `omega=k=0` | `-1` | current ratio degenerates | routed through potential | `-4` on RF-F8 effective branch |

The table is a type map: equal EOS values can arise from different microscopic compositions and therefore need not share the same energy/current normalization.

---

## 9. Advancement

```text
Noether charge has action type via J_I=hbar theta_I             PASS PARENT
q0 inherits action type on RF-N1B2K Noether-current binding     PASS EXACT CONDITIONAL
P/q0=1/2 normal phase-kinetic Noether surface                   PASS EXACT CONDITIONAL
microscopic rho=A2(omega^2+k^2)+V                               PASS EXACT
microscopic p=A2(omega^2-k^2/3)-V                               PASS EXACT ISOTROPIC AVERAGE
w_micro=(1-x/3-v)/(1+x+v)                                      PASS EXACT
radiation iff x+2v=1                                           PASS EXACT
isotropic-null radiation x=1,v=0                               PASS EXACT
homogeneous radiation completion x=0,v=1/2                     PASS EXACT
null radiation P/q0=1 on total-energy binding                  PASS EXACT
homogeneous radiation P/q0=3/4 on total-energy binding         PASS EXACT
RF-E5 homogeneous dust P/q0=1 on total-energy binding          PASS EXACT
RF-F8 required prefactor slope = 3w-1                           PASS PARENT
constant-P phase-cell effective EOS w=1/3                      PASS EXACT
nonzero phase carrier gives rho+p>0                             PASS EXACT
zero-current potential vacuum surface                           PASS EXACT BOUNDARY
physical RF-N1B2K local current/measure promotion               OPEN INPUT
common microscopic <-> phase-cell transport receipt             OPEN INPUT
multispecies/additional matter composition                      OPEN INPUT
absolute kappa_E/G promotion                                    OPEN PROJECT FRONTIER
```

## 10. Validation authority

Reference implementation:

`src/rfc/noether_eos_compatibility.py`

Reference tests:

`tests/reference/test_rff14_noether_eos_compatibility.py`

Validation receipt:

`validation/RF_F14_NOETHER_EOS_COMPATIBILITY_V0_1.json`

Stack parent:

`RF-F13 branch head a14da535354f30ad8b0b672713863a9734970328`.
