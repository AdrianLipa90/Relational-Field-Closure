# RFG33 — Explicit Loop Internal Pure-Spin-2 Projector Gate

Status: `EXPLICIT_CUT_STATE_PROJECTOR_PASS / HERMITIAN_IDEMPOTENT_RANK2_PASS / RFG32_MIXED_SUBTRACTION_EXACT / COPY_EXCHANGE_PASS / ALL_CUTS_LOOP_PROMOTION_OPEN`

RFG33 consumes the RFG32 loop internal-state spectrum firewall. RFG32 established that the raw `YM x YM` two-particle cut contains both matched helicity-two states and crossed helicity-zero tensor-product states. This gate introduces an explicit projector on the internal tensor-product state space and validates its action on the same exact massless cut family.

## 1. One-line tensor-product helicity space

For one internal massless line use the ordered tensor-product helicity basis

\[
\mathcal H_{\rm DC}=\{|++\rangle,|+-\rangle,|-+\rangle,|--\rangle\}.
\]

The pure spin-two subspace is

\[
\mathcal H_2=\operatorname{span}\{|++\rangle,|--\rangle\}.
\]

Define

\[
\boxed{P_2=|++\rangle\langle++|+|--\rangle\langle--|}
\]

or in the frozen basis

\[
\boxed{P_2=\operatorname{diag}(1,0,0,1)}.
\]

Its complement is

\[
\boxed{Q_0=I-P_2=\operatorname{diag}(0,1,1,0)}.
\]

The executable gate verifies

\[
P_2^\dagger=P_2,\qquad P_2^2=P_2,\qquad \operatorname{rank}P_2=2,
\]

\[
Q_0^2=Q_0,\qquad P_2Q_0=0,\qquad P_2+Q_0=I.
\]

## 2. Two-particle RFG32 cut

For one Yang–Mills copy the allowed internal assignments are

\[
A=(+,-),\qquad B=(-,+).
\]

The independent two-copy cut basis is therefore

\[
\{|AA\rangle,|AB\rangle,|BA\rangle,|BB\rangle\}.
\]

On this basis the induced pure-spin-two cut projector is

\[
\boxed{P_{\rm cut}=\operatorname{diag}(1,0,0,1)}.
\]

Thus `AA` and `BB` are retained while the crossed `AB` and `BA` sectors are removed.

## 3. Exact cut decomposition

Let `x_A` and `x_B` be the two nonzero one-copy cut products of RFG32. The raw state vector is

\[
\mathbf v=(x_A^2,x_Ax_B,x_Bx_A,x_B^2)^T.
\]

RFG33 verifies directly that

\[
\boxed{\mathcal C_{\rm proj}=\mathbf 1^TP_{\rm cut}\mathbf v=x_A^2+x_B^2}
\]

and

\[
\boxed{\mathcal C_{\rm removed}=\mathbf 1^T(I-P_{\rm cut})\mathbf v=2x_Ax_B}.
\]

Therefore

\[
\boxed{\mathcal C_{\rm raw}=\mathcal C_{\rm proj}+\mathcal C_{\rm removed}}
\]

with

\[
\boxed{\mathcal C_{\rm removed}=\mathcal C_{\rm mixed}^{\rm RFG32}}.
\]

The projector therefore implements exactly the state separation diagnosed by RFG32; no numerical cancellation or gravity target is used to define it.

## 4. Copy-exchange symmetry

Let `X` exchange the two Yang–Mills copies, mapping `AB <-> BA` and leaving `AA,BB` fixed. The gate verifies

\[
\boxed{XP_{\rm cut}X=P_{\rm cut}}.
\]

Hence the projected cut is invariant under copy exchange.

## 5. Executable validation

Fresh live-surface local result:

```text
6 passed, 0 failed
```

The tests verify: Hermiticity/idempotence/rank, orthogonal complement completeness, matched-state selection, exact projected cut on generic RFG32 kinematics, exact removal of the mixed sector, and copy-exchange invariance.

## 6. Advancement

```text
RFG31 selected tree internal pure-spin2 factorization       PASS
RFG32 raw loop mixed internal sector                         PASS FIREWALL
RFG33 explicit cut-state pure-spin2 projector                PASS
RFG33 exact mixed-sector subtraction                         PASS
projected-cut Ward / crossing / channel-complete audit       NEXT RFG34
loop-integrand realization with projector                    OPEN
integrated loop amplitude                                    OPEN
```

RFG33 is a cut-level state projector gate. Promotion of a loop quantity requires independent validation that the same projector prescription is consistent across the relevant unitarity cuts and with the project normalization/factorization spine.
