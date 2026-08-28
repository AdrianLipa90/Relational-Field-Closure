# RF-N1B2M — Gauge-Covariant Phase Pullback and Noether Generator

Status: `GAUGE_COVARIANT_PULLBACK_EXACT_PASS_CONDITIONAL / COMMON_U1_BUNDLE_ADMISSION_OPEN / RFC_CURRENT_PROMOTION_OPEN`

RF-N1B2M is the RFC-side consumer of IDT 01AC. It fixes the sign and gauge-covariant structure of the field↔rotor phase bridge before any RFC carrier promotion.

## 1. Common U(1) convention

The admitted Berry connection is

\[
\mathcal A_B=i\langle u|du\rangle.
\]

For

\[
|u\rangle\mapsto e^{i\lambda}|u\rangle,
\]

direct substitution gives

\[
\boxed{\mathcal A_B' = \mathcal A_B-d\lambda.}
\]

The same convention is used by the total Aharonov–Bohm–Berry–Euler phase connection

\[
\mathcal A^{ABE}=\mathcal A_{AB}+\mathcal A_B+\mathcal A_E.
\]

For

\[
\psi=Ae^{i\vartheta},
\qquad
\vartheta' = \vartheta+\lambda,
\]

the invariant phase one-form is

\[
\boxed{\mathscr D\vartheta=d\vartheta+\mathcal A^{ABE}.}
\]

Thus the connection sign used by the RFC bridge is fixed by the admitted bundle convention.

## 2. Covariant field current

Use

\[
\mathcal D_\mu\psi
=(\partial_\mu+i\mathcal A^{ABE}_\mu)\psi.
\]

Then

\[
(\mathcal D_\mu\psi)^*\mathcal D^\mu\psi
=(\partial_\mu A)(\partial^\mu A)
+A^2\mathscr D_\mu\vartheta\mathscr D^\mu\vartheta
\]

and the phase current is

\[
\boxed{
J_\vartheta^\mu
=2A^2\mathscr D^\mu\vartheta.}
\]

## 3. Pullback to the rotor

Let \(q(\tau)\) be the relational trajectory and admit the common local fiber-coordinate reduction

\[
\chi(\tau)=\vartheta(q(\tau))+\chi_0.
\]

Then

\[
\boxed{
q^*(\mathscr D\vartheta)
=D_\tau\chi\,d\tau,}
\]

with

\[
D_\tau\chi
=\dot\chi+\mathcal A^{ABE}_a\dot q^a.
\]

The common phase-rate gate is therefore a gauge-covariant pullback identity.

## 4. Collective action reduction

For one common collective rate

\[
r:=D_\tau\chi,
\]

define

\[
C_A:=\int_\Sigma A^2dV_h,
\qquad
I_A:=2C_A.
\]

The field phase sector reduces to

\[
\boxed{
L_{phase}^{field}
=\frac{I_A}{2}r^2.}
\]

The independent rotor sector has

\[
L_{phase}^{rotor}
=\frac{I_\phi}{2}r^2.
\]

On the common reduction gate,

\[
\boxed{I_\phi=I_A.}
\]

This is the RF-N1B2L coefficient theorem recovered through the gauge-covariant pullback.

## 5. Equality of U(1) generators

For a slice normal aligned with the collective phase evolution,

\[
n_\mu\mathscr D^\mu\vartheta=r.
\]

The field Noether charge is

\[
Q_\vartheta
=\int_\Sigma n_\mu J_\vartheta^\mu dV_h
=I_A r.
\]

The rotor kinetic generator is

\[
P_\Phi:=J-J_I=I_\phi r.
\]

Therefore

\[
\boxed{Q_\vartheta=P_\Phi}
\]

on the exact common reduction.

After Euler/Berry closure,

\[
\boxed{Q_\vartheta^{EB}=P_\Phi^{EB}=J-J_I^{EB}.}
\]

The field and rotor moment maps for the admitted common `U(1)` action therefore coincide.

## 6. RFC normalization consequence

With

\[
H_\Phi^{EB}
=\frac{(P_\Phi^{EB})^2}{2I_\phi},
\]

the finite Noether energy-per-carrier coordinate is

\[
\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{Q_\vartheta^{EB}}
=\frac12D_\tau\chi.
\]

After the separately measured RF-N1B2K current/measure promotion,

\[
Q_\Sigma=Q_\vartheta=P_\Phi^{EB}
\]

and the RFC downstream normalization candidate is

\[
\boxed{\epsilon_Q=\frac12D_\tau\chi.}
\]

## 7. Executable admission coordinates

The RFC↔PNCS gate should keep separate coordinates for

\[
\Delta_{bundle},
\Delta_{phase},
\Delta_{conn},
\Delta_{rate},
\Delta_{normal},
\Delta_Q.
\]

The numerical coordinates include

\[
\Delta_{rate}
=\frac{|r_{field}-r_{rotor}|}{|r_{rotor}|},
\qquad
\Delta_Q
=\frac{|Q_\vartheta-P_\Phi|}{|P_\Phi|},
\]

plus exact ID checks for bundle, local patch, connection, slice normal, measure and ordered support.

The common generator theorem is admitted on the zero-defect surface

\[
\boxed{
\Delta_{bundle}=\Delta_{phase}=\Delta_{conn}
=\Delta_{rate}=\Delta_{normal}=\Delta_Q=0.}
\]

## 8. PNCS target

Proposed contract:

`PNCS_PNV_GAUGE_COVARIANT_PHASE_PULLBACK_V0_1`

Proposed semantic loop:

`SOURCE.PHASE.NOETHER.GAUGE_COVARIANT_PULLBACK.ROUNDTRIP`

Physical `J_Q^\mu <-> J_\vartheta^\mu` promotion remains the downstream measured RFC gate.
