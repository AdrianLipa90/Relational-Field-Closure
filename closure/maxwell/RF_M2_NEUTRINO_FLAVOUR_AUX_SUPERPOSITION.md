# RF-M2 — Neutrino-Flavour AUX Superposition and Charge-Preserving Source Gate

Status: `EXACT_AUX_FLAVOUR_ALGEBRA / EXACT_NEUTRINO_EM_NULL_CONTROL / CHARGED_FLAVOUR_SOURCE_GATE_CONDITIONAL / PMNS_BINDING_OPEN`

RF-M2 rewrites the three-channel AUX phase frame in neutrino-flavour coordinates and connects it to the Aharonov–Bohm/Maxwell source architecture.

The physical flavour labels are

\[
\boxed{\nu_e,\;\nu_\mu,\;\nu_\tau},
\]

while RGB is retained only as an implementation alias for the three AUX channels.

## 1. Three bipolar neutrino-flavour channels

Each flavour carries one bipolar phase coordinate

\[
s_e,s_\mu,s_\tau\in\{+1,-1\}.
\]

Thus

\[
\boxed{
\mathcal H_{\nu,\mathrm{AUX}}
=\mathbb C^2_{\nu_e}\otimes\mathbb C^2_{\nu_\mu}\otimes\mathbb C^2_{\nu_\tau},
\qquad
\dim\mathcal H_{\nu,\mathrm{AUX}}=8.
}
\]

The eight basis sectors are

\[
|s_e,s_\mu,s_\tau\rangle,
\qquad
(s_e,s_\mu,s_\tau)\in\{\pm1\}^3,
\]

and the general AUX state is

\[
\boxed{
|\Psi_\nu\rangle
=\sum_s c_s|s_e,s_\mu,s_\tau\rangle,
\qquad
\sum_s|c_s|^2=1.
}
\]

The `3 x (1,-1)` structure therefore supplies eight bipolar basis sectors; superposition is carried by the complex amplitudes `c_s`.

## 2. Root-of-unity flavour phase frame

Let

\[
\omega=e^{2\pi i/3},
\qquad
1+\omega+\omega^2=0.
\]

Assign

\[
\phi_e=0,
\qquad
\phi_\mu=\frac{2\pi}{3},
\qquad
\phi_\tau=\frac{4\pi}{3}.
\]

The bipolar flavour-phase vector is

\[
\boxed{
\Xi_\nu(s)
=\begin{pmatrix}
s_e\\
\omega s_\mu\\
\omega^2s_\tau
\end{pmatrix}
}
\]

with coherent projection

\[
\boxed{
Z_\nu(s)=s_e+\omega s_\mu+\omega^2s_\tau.
}
\]

Exactly,

\[
Z_\nu(+,+,+)=Z_\nu(-,-,-)=0,
\]

while the remaining six bipolar sectors obey

\[
\boxed{|Z_\nu|=2.}
\]

Hence the root-of-unity projection gives the exact AUX decomposition

\[
\boxed{8=2_{Z_\nu=0}+6_{|Z_\nu|=2}.}
\]

This decomposition is an algebraic phase classification. Physical mass, generation and measured oscillation assignments remain separate bindings.

## 3. Flavour oscillation operator

Let

\[
a_\nu=(a_e,a_\mu,a_\tau)^T
\]

be the one-particle flavour-amplitude vector. A general flavour rotation is

\[
\boxed{a_\nu'=U_fa_\nu},
\qquad
U_f\in U(3).
\]

Therefore

\[
\boxed{a_\nu'^\dagger a_\nu'=a_\nu^\dagger a_\nu.}
\]

The physical PMNS matrix is a downstream candidate realization of `U_f`; RF-M2 does not import numerical PMNS angles into the theorem.

## 4. Charge-preservation theorem

Let `Q` denote the electric-charge operator on the same flavour space. The electromagnetic current bilinear has the form

\[
J_{\rm EM}^\mu=\bar\Psi\gamma^\mu Q\Psi.
\]

Under the flavour rotation

\[
\Psi_f=U_f\Psi_m,
\]

the charge operator in the rotated basis is

\[
Q'=U_f^\dagger Q U_f.
\]

Therefore flavour oscillation preserves the electromagnetic source current exactly when

\[
\boxed{U_f^\dagger Q U_f=Q.}
\]

For a finite matrix representation this is equivalent to

\[
\boxed{[Q,U_f]=0}
\]

when the same basis/domain is used.

Thus flavour amplitudes may oscillate while the Maxwell source seen by the AB connection remains invariant, provided the mixing acts inside a charge-degenerate subspace.

## 5. Neutrino electromagnetic null-control sector

For the neutrino flavour triplet,

\[
\boxed{Q_\nu=0_{3\times3}.}
\]

Hence every flavour rotation satisfies

\[
\boxed{U_f^\dagger Q_\nu U_f=Q_\nu=0.}
\]

and therefore

\[
\boxed{J_{\rm EM}^\mu[\nu]=0}
\]

at the ordinary electric-charge projection gate.

This is a useful null control for RF-M1: a state may carry nontrivial flavour-phase holonomy and oscillatory redistribution while producing no direct electromagnetic source current.

## 6. Relation to Aharonov–Bohm normalization

RF-M1 fixes the electromagnetic connection by

\[
\mathfrak a_{AB}=\frac q\hbar A.
\]

RF-M2 separates the phase carrier from the electric source projection:

\[
\boxed{
\text{flavour phase state}
\xrightarrow{\;Q\;}
\text{electric source sector}
\xrightarrow{\;q/\hbar\;}
\text{AB coupling}.
}
\]

For the neutrino block the first projection vanishes. For a charged flavour-degenerate block, nontrivial flavour rotation may survive while the projected electric current remains invariant.

The later RFC conserved-carrier promotion should therefore compare the RFC current to a charge-projected, flavour-invariant source current rather than to an untyped individual flavour component.

## 7. Executable defects

An executable gate should keep separate

\[
\Delta_U=\|U_f^\dagger U_f-I\|,
\]

\[
\Delta_Q=\|U_f^\dagger Q U_f-Q\|,
\]

\[
\Delta_{norm}=\left|\|a_\nu'\|^2-\|a_\nu\|^2\right|,
\]

and the root-of-unity defects

\[
\Delta_{+++}=|1+\omega+\omega^2|,
\qquad
\Delta_{---}=|-1-\omega-\omega^2|.
\]

Promotion of a measured physical flavour sector requires an independently supplied physical mixing matrix, charge operator, current measurement and state-space binding.
