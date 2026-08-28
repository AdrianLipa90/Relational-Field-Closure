# RF-N1B2L — Scalar-Field → Rotor Inertia Reduction Gate

Status: `EXACT_COLLECTIVE_REDUCTION_PASS_CONDITIONAL / RF_E6_LORENTZIAN_SIGN_ALIGNMENT_PASS / PHASE_RATE_BINDING_OPEN / COMMON_MEASURE_BINDING_OPEN`

RF-N1B2L consumes the scalar phase carrier and fixes the rotor inertia through the collective-coordinate reduction of the same Euler–Noether phase field once the common phase/rate/measure/support premises are admitted.

## 1. Upstream scalar-field coefficient

With the canonical RFC signature `(-,+,+,+)`, use

\[
\boxed{
\mathcal L=-\partial_\mu\psi^*\partial^\mu\psi-V(|\psi|^2),
\qquad
\psi=Ae^{i\vartheta}.
}
\]

The pure phase sector is

\[
\boxed{
\mathcal L_{phase}=-A^2(\partial_\mu\vartheta)(\partial^\mu\vartheta).
}
\]

The phase Noether current is oriented as

\[
\boxed{
J_\vartheta^\mu=2A^2\partial^\mu\vartheta
}
\]

with the sign convention synchronized to RF-M4/RF-E6.

On a pure normal collective phase mode,

\[
D_\tau\vartheta\leftrightarrow D_\tau\chi,
\]

the Lorentzian contraction contributes a negative `q^2`, so the reduced one-dimensional kinetic term is positive:

\[
\boxed{
L_{\rm phase}^{field}
=\int_\Sigma A^2(D_\tau\chi)^2dV_h.
}
\]

Define

\[
\boxed{I_A:=2\int_\Sigma A^2dV_h.}
\]

Then

\[
\boxed{L_{\rm phase}^{field}=\frac{I_A}{2}(D_\tau\chi)^2.}
\]

## 2. Canonical rotor coefficient

The canonical rotor uses

\[
L_{\rm rotor}
=\frac{I_\phi}{2}(D_\tau\chi)^2
+J_I D_\tau\chi+\cdots
\]

with

\[
J=I_\phi D_\tau\chi+J_I.
\]

Matching the same collective quadratic phase mode on the same measure gives

\[
\boxed{I_\phi=I_A=2\int_\Sigma A^2dV_h.}
\]

The linear intention term leaves this quadratic coefficient unchanged.

Therefore

\[
\Delta_I^{J}=\left|\frac{I_A}{I_\phi}-1\right|
\]

obeys

\[
\boxed{\Delta_I^{J}=0}
\]

inside the admitted collective reduction.

## 3. Finite Noether carrier

The collective Noether charge becomes

\[
Q_\vartheta
=I_A D_\tau\chi
=I_\phi D_\tau\chi.
\]

The rotor kinetic coordinate is

\[
P_\Phi=J-J_I=I_\phi D_\tau\chi.
\]

Hence

\[
\boxed{Q_\vartheta=P_\Phi=J-J_I.}
\]

After Euler/Berry closure,

\[
\boxed{Q_\vartheta^{EB}=P_\Phi^{EB}=J-J_I^{EB}.}
\]

## 4. RFC energy normalization consequence

The phase energy is

\[
H_\Phi^{EB}=\frac{(P_\Phi^{EB})^2}{2I_\phi}.
\]

Therefore

\[
\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{Q_\vartheta^{EB}}
=\frac{P_\Phi^{EB}}{2I_\phi}
=\boxed{\frac12D_\tau\chi}.
\]

The canonical Lorentzian sign therefore reproduces the same positive reduced rotor energy used by the downstream source normalization.

## 5. Remaining interface conditions

The coefficient theorem is conditional on one common reduction:

```text
same scalar phase mode theta <-> chi                 OPEN interface binding
same covariant rate D_tau theta <-> D_tau chi        OPEN interface binding
same spatial slice and dV_h                          OPEN measure binding
same collective-mode support                         OPEN support binding
I_phi = 2 integral A^2 dV_h after those bindings     PASS EXACT CONDITIONAL
Delta_I^J                                             ZERO EXACT after binding
Q_theta = P_Phi                                      PASS EXACT CONDITIONAL
```

## 6. Relation to RF-N1B2K / RF-E6

RF-N1B2K independently audits the physical RFC carrier against the phase Noether carrier. RF-E6 fixes the covariant action sign and the corresponding Maxwell charge-projection sign while preserving the rotor reduction.

After the admitted carrier and reduction gates close on the same physical sector,

\[
\boxed{Q_\Sigma=Q_\vartheta=P_\Phi^{EB}}
\]

and

\[
\boxed{\epsilon_Q=\frac12D_\tau\chi.}
\]

## 7. Executable PNCS reduction coordinates

For a finite-cell representation,

\[
C_A:=\sum_a A_a^2V_a,
\qquad
I_A:=2C_A.
\]

PNCS evaluates

\[
\boxed{
\Delta_I^{red}:=\frac{|I_\phi-I_A|}{I_A}}
\]

alongside

\[
\Delta_C:=\frac{|I_\phi/2-C_A|}{C_A},
\qquad
\Delta_Q^{red}:=\frac{|P_\Phi-Q_\vartheta|}{Q_\vartheta},
\]

and

\[
\Delta_\epsilon^{red}
:=\frac{|\epsilon_N-(D_\tau\chi)/2|}{(D_\tau\chi)/2}.
\]

For one common positive covariant phase rate,

\[
\boxed{
\Delta_I^{red}
=\Delta_C
=\Delta_Q^{red}
=\Delta_\epsilon^{red}.}
\]

Executable contract:

`PNCS_PNV_SCALAR_FIELD_ROTOR_INERTIA_REDUCTION_V0_1`

Semantic loop:

`SOURCE.PHASE_NOETHER.ROTOR_INERTIA.REDUCTION.ROUNDTRIP`
