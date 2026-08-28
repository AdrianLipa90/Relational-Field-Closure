# RFG27 — Five-Point Project Normalization Firewall

Status: `BG_STANDARD_COLOR_ORDER_PASS / RFG15_TO_BG_ETA_A_2_PASS / PROJECT_KLT_CORE_FACTOR_4_PASS / CONSERVED_GRAVITY_SOFT_5_TO_4_PASS / ZETA5_MINUS_I_OVER_4_PASS / OLD_PLUS_I_BG_PHASE_FAIL_MINUS1`

RFG27 closes the normalization coordinate left open by RFG24–RFG26. It compares the direct Berends–Giele basis to the RFG15/RFG20 four-point project basis and then uses a momentum-conserving positive-helicity graviton soft family to transport the already admitted four-point Einstein normalization to five points.

## 1. Berends–Giele color-order normalization

On independent complex MHV points, the RFG25 recursion satisfies

\[
\boxed{A_4^{BG}=A_4^{PT}},\qquad
\boxed{A_5^{BG}=A_5^{PT}},
\]

where `PT` denotes the raw stripped Parke–Taylor rational function used by the higher-point reference layer.

RFG20 established for the RFG15 project partial amplitude

\[
A_{1234}^{project}=-2iA_{1234}^{PT(i)},
\]

with `A_PT(i)=i A_PT(raw)`. Therefore

\[
\boxed{A_4^{project}=2A_4^{BG}}.
\]

Define the color-order basis map

\[
\boxed{\eta_A:=2},\qquad
\boxed{A_n^{project}:=\eta_A A_n^{BG}}
\]

for the higher-point project handoff. This is a basis-normalization map anchored directly to the admitted RFG15/RFG20 four-point surface.

## 2. KLT bilinear map

Because KLT is bilinear in the two Yang–Mills copies,

\[
\boxed{\mathcal C_5^{project}=\eta_A^2\mathcal C_5^{BG}=4\mathcal C_5^{BG}}.
\]

The Ward, BCJ, copy-exchange and quartic-contact results of RFG25/RFG26 are unchanged by this constant basis map.

## 3. Conserved five-to-four gravity soft gate

RFG27 uses the same momentum-conserving soft construction as the higher-point reference spine. For a positive-helicity soft leg 5,

\[
\lambda_5,\widetilde\lambda_5\mapsto\sqrt\varepsilon(\lambda_5,\widetilde\lambda_5),
\]

with two hard anti-holomorphic spinors re-solved at each `epsilon` so total momentum remains conserved.

The stripped gravity soft factor is

\[
\boxed{S_5^+=\sum_{a=1}^{4}\frac{[5a]}{\langle5a\rangle}\frac{\langle xa\rangle\langle ya\rangle}{\langle x5\rangle\langle y5\rangle}}.
\]

The executable witness verifies

\[
\boxed{\frac{\mathcal C_5^{project}}{S_5^+\mathcal C_4^{project}}\to1}.
\]

## 4. Five-point coefficient

Let

\[
P_4=\left(\frac{\kappa_g}{2}\right)^2=\kappa_E,
\qquad
P_5=\left(\frac{\kappa_g}{2}\right)^3=\frac1{\bar M_G^3}.
\]

RFG20 fixed

\[
\mathcal M_4^{project}=-\frac{i}{4}P_4\mathcal C_4^{project}.
\]

The conserved soft gate requires

\[
\mathcal M_5^{project}\to\left(\frac{\kappa_g}{2}\right)S_5^+\mathcal M_4^{project}.
\]

Since the project cores themselves factorize with unit coefficient, the five-point normalization coordinate is

\[
\boxed{\zeta_5=-\frac{i}{4}}.
\]

Hence

\[
\boxed{\mathcal M_5^{project}=-\frac{i}{4}\left(\frac{\kappa_g}{2}\right)^3\mathcal C_5^{project}}
\]

or, equivalently in the BG basis,

\[
\boxed{\mathcal M_5^{project}=-i\left(\frac{\kappa_g}{2}\right)^3\mathcal C_5^{BG}}.
\]

Using `Mbar_G=2/kappa_g`,

\[
\boxed{\mathcal M_5^{project}=-\frac{i}{4\bar M_G^3}\mathcal C_5^{project}}.
\]

## 5. Old-prefactor firewall

The earlier five-point expression

\[
+iP_5\mathcal C_5^{BG}
\]

has the conserved-soft ratio

\[
\boxed{\frac{M_5^{old}}{(\kappa_g/2)S_5^+M_4^{project}}\to-1}.
\]

The defect is a phase flip on the common four-to-five-point normalization surface.

## 6. Executable validation

Fresh local result:

```text
6 passed, 0 failed
```

The six tests verify: `BG4/PT4=1`, `RFG15_partial/BG4=2`, `BG5/PT5=1`, the quadratic KLT map `4`, conserved gravity-core soft factorization, and the coefficient/phase firewall above.

## 7. Advancement

```text
RFG23 five-point BCJ / soft reference              PASS
RFG24 five-point KLT kernel / scale coordinate      PASS
RFG25 direct BG Yang-Mills recursion                PASS
RFG27 color-order project map eta_A=2               PASS
RFG26 BG x BG KLT core                              PASS
RFG27 project KLT core = 4 BG core                  PASS
RFG27 zeta_5=-i/4                                   PASS
old +i P5 C5_BG                                     FAIL PHASE -1
five-point multi-particle pole residue audit         NEXT RFG28
explicit 15-cubic-graph project numerator set        OPEN
```
