# RF-L1A — Hermitian Oriented Exchange Gate

Status: `RF_L1_SOURCE_HOLONOMY_BOUND / IDT_01M_OPERATOR_INTERFACE_BOUND / TARGET_ATTRIBUTION_OPEN`

Pinned upstreams and implementation witness:

- RF-L1 branch `feat/rfl1-relational-lambda-oriented-holonomy-v0.1`: current stacked upstream
- IDT 01M branch `feat/hermitian-oriented-exchange-interface-v0.1`: `09e9abe24ecaf362cb46e8da40aff915593da68f`
- GREMLIN branch `feat/gremlin-hermitian-oriented-exchange-v1.4`: `1cfeb2df52f3b98318bf207c6a12cd3e6a913f24`
- GREMLIN CI run `33125674008`: `209 passed`

## 1. Purpose

RF-L1A binds the RF-L1 oriented relational coupling

\[
\mathcal J_R=E_Re^{i\tau_R}
\]

to the Hermitian operator interface exported by IDT 01M.

The closure path is

\[
\boxed{
\Lambda_R
\rightarrow E_R
\rightarrow \tau_R
\rightarrow \mathcal J_R
\rightarrow H_{\rm ex}=H_{\rm ex}^{\dagger}
\rightarrow U_{\rm ex}(t).
}
\]

The RFC scalar-source commitment and IDT connection commitment remain attached to the operator receipt.

## 2. Operator binding

For an admitted two-state target subspace, define

\[
\boxed{
H_{\rm ex}
=\mathcal J_R|01\rangle\langle10|
+\mathcal J_R^*|10\rangle\langle01|.
}
\]

With

\[
\mathcal J_R
=E_R\cos\tau_R+iE_R\sin\tau_R,
\]

the Pauli decomposition is

\[
\boxed{
H_{\rm ex}
=\frac{E_R\cos\tau_R}{2}(X\otimes X+Y\otimes Y)
+\frac{E_R\sin\tau_R}{2}(X\otimes Y-Y\otimes X).
}
\]

Thus the RF-L1 source-energy magnitude and the IDT signed holonomy quadrature both enter the Hermitian operator.

## 3. Hermiticity and spectrum

The conjugate off-diagonal structure gives

\[
\boxed{H_{\rm ex}=H_{\rm ex}^{\dagger}.}
\]

In the single-excitation sector,

\[
\boxed{
\lambda_{\pm}=\pm|\mathcal J_R|=\pm|E_R|.
}
\]

The spectral-radius receipt therefore closes directly to the RF-L1 source-energy magnitude.

## 4. Unitary exchange

Define

\[
\phi_R=\frac{|E_R|\Delta t}{\hbar}.
\]

The single-excitation amplitudes evolve as

\[
\boxed{
\begin{aligned}
a'_{01}
&=\cos\phi_R\,a_{01}
-i\sin\phi_R e^{i\arg\mathcal J_R}a_{10},\\
a'_{10}
&=\cos\phi_R\,a_{10}
-i\sin\phi_R e^{-i\arg\mathcal J_R}a_{01}.
\end{aligned}
}
\]

The reference implementation receipts norm closure and excitation-number conservation.

## 5. Relational-source lineage

Every RF-L1A operator receipt must carry:

```text
RFC_Lambda_R_commitment
RFC_source_energy_commitment
IDT_temporal_connection_commitment
IDT_cycle_holonomy
RF_L1_oriented_coupling_commitment
IDT_01M_operator_interface_pin
operator_matrix_commitment
```

This preserves one provenance chain from scalar source through geometry/holonomy into the unitary operator.

## 6. Orientation-sensitive test

For

\[
\tau_R\mapsto-\tau_R,
\]

RF-L1A requires

\[
\operatorname{Re}\mathcal J_R\mapsto\operatorname{Re}\mathcal J_R,
\qquad
\operatorname{Im}\mathcal J_R\mapsto-\operatorname{Im}\mathcal J_R.
\]

The reference exchange model preserves population-transfer probabilities and changes the transfer phase. For positive source energy,

\[
\boxed{
\Delta\varphi_{\rm transfer}=2\tau_R\pmod{2\pi}.
}
\]

The orientation-reversal pair is therefore a required falsification/control test for any physical adapter.

## 7. Joint-state diagnostic

For the declared two-qubit reference model, initial `|10>` at

\[
\Delta t_{1/4}=\frac{\pi\hbar}{4|E_R|}
\]

produces a state with pure-state concurrence

\[
\boxed{C=1}
\]

inside the reference exchange dynamics. This supplies an operator-level witness for the model and remains attached to the target-attribution gate.

## 8. Neutrino adapter gate

The neutrino target requires a separately receipted map between the physical flavor/mass state space and the operator subspace used above. The adapter must carry the standard vacuum Hamiltonian and matter contribution where applicable, then expose the RF-L1A term as a separately identifiable phase contribution.

The target comparison should therefore bind

\[
H_{\rm test}
=H_{\rm vac}+H_{\rm matter}+H_{\rm RF},
\]

where `H_RF` is generated from the admitted `Lambda_R -> E_R -> tau_R -> J_R` chain.

## 9. Promotion gates

RF-L1A advances through independent receipts for:

1. physical target-state mapping;
2. multi-level Hermitian extension for a three-flavor neutrino system;
3. compatibility with standard vacuum and matter evolution;
4. phase-residual prediction derived from the holonomy input;
5. orientation-reversal control;
6. uncertainty propagation from `Lambda_R`, geometry and connection inputs;
7. comparison with oscillation data;
8. joint-state witness when entanglement attribution is tested.

The author/formalism may suggest that the relational-Lambda source and internal geometric rotation generate an interaction phase through a single Hermitian closure, yet does not state the physical neutrino realization as an established result before these gates are receipted.
