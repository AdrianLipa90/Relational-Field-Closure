# RF-L2 — Dynamic Lambda0 Action Realizability / Stability Gate

Status: `EXACT_ACTION_SPLIT / EXACT_DYNAMIC_TRANSFER / STATIONARY_VACUUM_LIMIT_PASS / HOMOGENEOUS_STABILITY_CRITERION_EXACT / RFC_INVARIANT_POTENTIAL_BINDING_OPEN`

RF-L2 consumes RF-L1, RF-E0 and the RF-E6/RF-E7 matter-action closure. It gives an independent generally covariant action realization of the dynamic `Lambda0` transfer law and separates the metric-proportional vacuum contribution from the kinetic stress of the field that carries the dynamics.

## 1. Independent scalar action

Introduce a real scalar closure coordinate `phi_L` with action

\[
\boxed{
S
=\int d^4x\sqrt{-g}
\left[
\frac{R-2\Lambda_{ref}}{2\kappa_E}
-\frac12\nabla_\mu\phi_L\nabla^\mu\phi_L
-U_L(\phi_L)
+\mathcal L_{base}
\right].
}
\]

Here `Lambda_ref` is a constant reference vacuum coordinate and `L_base` contains the already admitted Maxwell/scalar matter sectors from RF-E6/RF-E7.

The scalar equation is

\[
\boxed{
\Box\phi_L-U_L'(\phi_L)=0.
}
\]

## 2. Scalar stress tensor

Metric variation gives

\[
\boxed{
T^{L}_{\mu\nu}
=\nabla_\mu\phi_L\nabla_\nu\phi_L
-g_{\mu\nu}
\left[
\frac12(\nabla\phi_L)^2+U_L
\right].
}
\]

Split it into

\[
\boxed{
T^{kin}_{\mu\nu}
=\nabla_\mu\phi_L\nabla_\nu\phi_L
-\frac12g_{\mu\nu}(\nabla\phi_L)^2
}
\]

and

\[
\boxed{T^{pot}_{\mu\nu}=-U_Lg_{\mu\nu}.}
\]

The full scalar tensor is exactly

\[
\boxed{T^L_{\mu\nu}=T^{kin}_{\mu\nu}+T^{pot}_{\mu\nu}.}
\]

## 3. Action-derived dynamic Lambda coordinate

The Einstein equation from the action is

\[
G_{\mu\nu}+\Lambda_{ref}g_{\mu\nu}
=\kappa_E
\left(
T^{base}_{\mu\nu}+T^{kin}_{\mu\nu}-U_Lg_{\mu\nu}
\right).
\]

Move the potential contribution to the geometric side and define

\[
\boxed{
\Lambda_0(x)
:=\Lambda_{ref}+\kappa_EU_L(\phi_L(x)).
}
\]

Then

\[
\boxed{
G_{\mu\nu}+\Lambda_0(x)g_{\mu\nu}
=\kappa_E
\left(T^{base}_{\mu\nu}+T^{kin}_{\mu\nu}\right).
}
\]

This is the RF-L1 target form with an explicit action origin for the varying metric-proportional term and an explicit kinetic ledger for the dynamical carrier.

## 4. Exact Bianchi transfer

For a canonical scalar,

\[
\nabla^\mu T^{kin}_{\mu\nu}
=(\Box\phi_L)\nabla_\nu\phi_L.
\]

Using the field equation,

\[
\Box\phi_L=U_L'(\phi_L),
\]

one obtains

\[
\boxed{
\nabla^\mu T^{kin}_{\mu\nu}
=\nabla_\nu U_L.
}
\]

Therefore, when the base sector is separately conserved,

\[
\boxed{
\kappa_E\nabla^\mu
\left(T^{base}_{\mu\nu}+T^{kin}_{\mu\nu}\right)
=\nabla_\nu\Lambda_0,
}
\]

which is precisely the RF-E0 dynamic-`Lambda0` transfer identity.

Equivalently, if

\[
T^{\Lambda}_{\mu\nu}
=-\frac{\Lambda_0}{\kappa_E}g_{\mu\nu},
\]

then

\[
\boxed{
\nabla^\mu
\left(
T^{base}_{\mu\nu}
+T^{kin}_{\mu\nu}
+T^{\Lambda}_{\mu\nu}
\right)=0.
}
\]

## 5. Stationary vacuum surface

At a stationary point

\[
\boxed{
\nabla_\mu\phi_L=0,
\qquad
U_L'(\phi_{L0})=0,
}
\]

one has

\[
T^{kin}_{\mu\nu}=0
\]

and

\[
\boxed{
\Lambda_0
=\Lambda_{ref}+\kappa_EU_L(\phi_{L0})
=\mathrm{constant}.
}
\]

The scalar stress becomes exactly metric-proportional:

\[
\boxed{
T^L_{\mu\nu}
=-U_L(\phi_{L0})g_{\mu\nu}.
}
\]

This recovers the constant cosmological-term sector of RF-L1/RF-E0.

## 6. Homogeneous dynamic equation of state

For a spatially homogeneous scalar in a local orthonormal frame,

\[
\phi_L=\phi_L(t),
\]

let

\[
K_L:=\frac12\dot\phi_L^2.
\]

Then

\[
\boxed{
\varepsilon_L=K_L+U_L,
\qquad
p_L=K_L-U_L,
}
\]

so

\[
\boxed{
\varepsilon_L+p_L=\dot\phi_L^2.
}
\]

The exact metric-proportional vacuum equation of state is reached on the zero-kinetic surface `dot(phi_L)=0`. Away from that surface the kinetic tensor remains an explicit part of the Einstein source.

## 7. Spatial-gradient stress

A spatial gradient also carries non-vacuum stress. For

\[
\nabla_{\hat a}\phi_L=(0,g,0,0)
\]

in an orthonormal frame, the kinetic tensor is

\[
\boxed{
T^{kin}_{\hat a\hat b}
=\frac12\operatorname{diag}(g^2,g^2,-g^2,-g^2).
}
\]

Thus the action keeps gradient anisotropy explicitly typed rather than absorbing it into the metric-proportional potential coordinate.

## 8. Local stability at the stationary surface

Let

\[
\phi_L=\phi_{L0}+\delta\phi,
\qquad
U_L'(\phi_{L0})=0.
\]

Linearization gives

\[
\boxed{
\left(\Box-m_L^2\right)\delta\phi=0,
\qquad
m_L^2:=U_L''(\phi_{L0}).
}
\]

For the local canonical scalar sector,

\[
\boxed{m_L^2\ge0}
\]

is the non-tachyonic small-perturbation stability condition. A strictly positive curvature gives a locally restoring stationary point; `m_L^2=0` is marginal and requires higher-order analysis.

## 9. RFC invariant reconstruction interface

RF-L1 requires the dynamic closure coordinate to be reconstructed from admitted RFC scalar invariants. RF-L2 moves that requirement to the potential map

\[
\boxed{
U_L(\phi_L)
\longleftrightarrow
U_L\bigl(\mathcal I_{RFC}\bigr),
}
\]

where admissible scalar inputs may include independently typed information/time invariants, matter invariants and electromagnetic scalars after dimensional and provenance audits.

The physical dimensional requirement is

\[
\boxed{[\Lambda_0]=L^{-2}.}
\]

Therefore

\[
\boxed{[\kappa_EU_L]=L^{-2}}
\]

in the selected unit convention.

The explicit RFC-invariant potential and its parameter-free physical calibration remain the next promotion coordinates for this line.

## 10. Executable reference gates

RF-L2 tests verify:

1. exact `T_L=T_kin-Ug` decomposition;
2. stationary scalar gives pure metric-proportional vacuum stress;
3. `Lambda0=Lambda_ref+kappa_E U` mapping;
4. homogeneous `epsilon=K+U`, `p=K-U` and `epsilon+p=dot(phi)^2`;
5. exact Bianchi transfer from the on-shell scalar equation;
6. total scalar energy conservation for homogeneous motion;
7. spatial-gradient anisotropic kinetic stress;
8. stationary-point stability classification from `U''`;
9. constant `Lambda_ref` leaves the transfer derivative unchanged;
10. finite/nonzero coupling and finite-state fail-closed handling.

## 11. Advancement

```text
RF-L1 dynamic Lambda0 target                         ADMITTED
independent generally covariant scalar action        PASS EXACT CONSTRUCTION
Lambda0 = Lambda_ref + kappa_E U_L                   PASS EXACT DEFINITION FROM ACTION SPLIT
kinetic stress ledger                                PASS EXACT
RF-E0 Bianchi transfer from scalar EOM               PASS EXACT ON SHELL
stationary constant-Lambda vacuum limit              PASS EXACT
homogeneous dynamic equation of state                PASS EXACT
spatial-gradient anisotropic stress                  PASS EXACT
local non-tachyonic stability U''>=0                 PASS EXACT LINEAR CRITERION
RFC-invariant potential reconstruction               OPEN
parameter-free physical calibration                  OPEN
```
