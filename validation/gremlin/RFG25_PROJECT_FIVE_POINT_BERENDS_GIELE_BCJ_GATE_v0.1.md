# RFG25 — Project Five-Point Berends–Giele / BCJ Gate

Status: `DIRECT_VERTEX_BG_ASSEMBLY_PASS / FIVE_LEG_WARD_PASS / FUNDAMENTAL_BCJ_PASS / QUARTIC_FIREWALL_PASS / BG_STANDARD_COLOR_ORDER_PASS_RFG27 / PROJECT_MAP_ETA_A_2_PASS_RFG27`

RFG25 evaluates five-point color-ordered amplitudes directly from the RFG8/RFG13 cubic/quartic interaction layer with

\[
P^2J_P^\mu=\sqrt2\sum_{XY=P}[J_X,J_Y]^\mu+\sum_{XYZ=P}\{J_X,J_Y,J_Z\}^\mu.
\]

Its Ward, BCJ, reflection/decoupling and quartic-contact tests remain byte-preserved PASS results.

RFG27 identifies the normalization of this Berends–Giele color-order basis:

\[
\boxed{A_4^{BG}=A_4^{PT(raw)}},\qquad
\boxed{A_5^{BG}=A_5^{PT(raw)}}.
\]

Comparison with the admitted RFG15/RFG20 four-point project partial gives

\[
\boxed{A_4^{project}=2A_4^{BG}}.
\]

The canonical project handoff is therefore

\[
\boxed{\eta_A=2},\qquad
\boxed{A_5^{project}=2A_5^{BG}}.
\]

This basis map preserves all homogeneous Ward/BCJ identities and carries the RFG15 project color-order convention into the five-point layer.

Recorded RFG25 result remains

```text
6 passed, 0 failed
```

and RFG27 independently passes `6/6` normalization/soft-transport tests.
