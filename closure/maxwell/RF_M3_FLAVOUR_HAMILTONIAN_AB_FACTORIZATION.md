# RF-M3 — Flavour Hamiltonian Charge Conservation and Aharonov–Bohm Factorization

Status: `EXACT_CHARGE_COMMUTATOR_THEOREM / EXACT_EQUAL_CHARGE_AB_FACTORIZATION / NEUTRINO_AB_NULL_EXACT / PHYSICAL_FLAVOUR_HAMILTONIAN_BINDING_OPEN`

RF-M3 follows RF-M2 and upgrades the static charge-preserving flavour gate into a continuous dynamical theorem.

## 1. Flavour evolution

Let the three-component flavour amplitude obey

\[
\boxed{
i\,\frac{d}{d\tau}a_f=H_fa_f,
\qquad
H_f=H_f^\dagger.
}
\]

The resulting finite evolution `U_f` is unitary. RF-M3 keeps the numerical physical realization of `H_f` separate from the theorem.

## 2. Charge commutator theorem

Let `Q` be the Hermitian electric-charge operator on the same flavour space and define

\[
\langle Q\rangle=a_f^\dagger Qa_f.
\]

Using the flavour equation of motion,

\[
\dot a_f=-iH_fa_f,
\qquad
\dot a_f^\dagger=i a_f^\dagger H_f,
\]

one obtains exactly

\[
\boxed{
\frac{d}{d\tau}\langle Q\rangle
=i\,a_f^\dagger[H_f,Q]a_f.
}
\]

Therefore the continuous electromagnetic charge-preservation gate is

\[
\boxed{[H_f,Q]=0.}
\]

On that surface,

\[
\boxed{\frac{d}{d\tau}\langle Q\rangle=0,}
\]

and finite evolution satisfies

\[
\boxed{U_f^\dagger Q U_f=Q.}
\]

## 3. Equal-charge flavour blocks

For a charge-degenerate multiplet

\[
\boxed{Q=qI,}
\]

one has

\[
[H_f,Q]=0
\]

for every Hermitian `H_f`. Thus internal flavour redistribution cannot change the electric charge of the block.

## 4. Central Aharonov–Bohm factor

RF-M1 fixes the AB connection by

\[
\mathfrak a_{AB}=\frac q\hbar A.
\]

On an equal-charge flavour block the corresponding matrix-valued connection is

\[
\boxed{
\mathfrak A_{AB}=\frac q\hbar A\,I.
}
\]

Hence

\[
\boxed{[\mathfrak A_{AB},H_f]=0.}
\]

The path transport factor is

\[
\boxed{
W_{AB}[C]
=\exp\!\left(i\frac q\hbar\int_CA\right)I,
}
\]

and therefore the electromagnetic and flavour transports factorize:

\[
\boxed{
U_{\rm total}[C]
=W_{AB}[C]U_f[C]
=U_f[C]W_{AB}[C].
}
\]

The AB factor is thus flavour-blind inside a charge-degenerate block.

## 5. Neutrino null-control block

For the neutrino flavour triplet

\[
\boxed{Q_\nu=0_{3\times3},}
\]

one has

\[
[H_f,Q_\nu]=0
\]

for arbitrary Hermitian `H_f`, while

\[
\boxed{\mathfrak A_{AB}^{(\nu)}=0,}
\qquad
\boxed{W_{AB}^{(\nu)}[C]=I_3.}
\]

Thus nontrivial neutrino flavour evolution may coexist with an exactly trivial ordinary electromagnetic AB factor.

## 6. Charge-superselection form of the flavour space

For a general decomposition

\[
\mathcal H_f=\bigoplus_q\mathcal H_q,
\qquad
Q=\bigoplus_q qI_{\mathcal H_q},
\]

the commutator gate

\[
[H_f,Q]=0
\]

forces `H_f` to preserve each electric-charge eigenspace. Therefore flavour mixing may occur within one charge-degenerate block, while a Hamiltonian that couples different electric-charge eigenspaces fails the Maxwell-source compatibility gate.

Correspondingly,

\[
U_f=\bigoplus_qU_q,
\]

and each charge block carries a central AB factor

\[
W_{AB}^{(q)}[C]
=\exp\!\left(i\frac q\hbar\int_CA\right)I_{\mathcal H_q}.
\]

## 7. Relation to RF-M2 AUX flavours

RF-M2 provides the discrete neutrino-flavour AUX basis

\[
|s_e,s_\mu,s_\tau\rangle,
\qquad
s_\alpha\in\{\pm1\},
\]

with eight bipolar sectors and the exact root-of-unity `2+6` projection classification.

RF-M3 operates on the continuous three-component flavour-amplitude layer. The discrete eight-dimensional AUX superposition register and continuous `U(3)` evolution are maintained as distinct representations. Their physical PMNS lift remains a separately testable binding.

## 8. Maxwell source implication

The Maxwell source is the charge-projected flavour current. RF-M3 therefore replaces a per-flavour source identification by a dynamical invariant:

\[
\boxed{
[H_f,Q]=0
\Longrightarrow
\text{flavour evolution preserves the electromagnetic source charge.}
}
\]

For equal-charge blocks, the same statement is encoded geometrically by the central AB factor. For the neutrino block, the electromagnetic source projection remains identically zero.

## 9. Executable defects

The reference gate should keep independent

\[
\Delta_H=\|H_f-H_f^\dagger\|,
\]

\[
\Delta_{HQ}=\|[H_f,Q]\|,
\]

\[
\Delta_{Qdot}=\left|\frac{d}{d\tau}\langle Q\rangle\right|,
\]

\[
\Delta_U=\|U_f^\dagger U_f-I\|,
\]

and for charge-degenerate blocks

\[
\Delta_{ABcomm}=\|W_{AB}U_f-U_fW_{AB}\|.
\]

An adversarial cross-charge mixing Hamiltonian must generate nonzero `Delta_HQ` and fail the source-preservation gate.
