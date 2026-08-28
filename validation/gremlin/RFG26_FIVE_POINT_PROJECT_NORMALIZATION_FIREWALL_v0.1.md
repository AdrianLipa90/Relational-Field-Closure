# RFG26 — Five-Point Project Normalization Firewall

Status: `FOUR_POINT_BG_TO_RFG15_BRIDGE_PASS / FIVE_POINT_TREE_SCALING_PASS / KLT_CORE_FACTOR8_PASS / KAPPA_OVER4_CUBED_TRANSFER_PASS / PHYSICAL_PRODUCT_INVARIANT`

RFG26 closes the higher-point per-vertex normalization frontier opened by RFG20 and encountered by RFG24/RFG25.

## 1. Four-point normalization witness

Using the same complex on-shell MHV states as the RFG20 firewall, compare the RFG15 project partial amplitude with the Berends–Giele recursion initially used by RFG24. For the initial stripped-current coefficients

\[
V_3^{BG}:V_4^{BG}=\sqrt2:1,
\]

the executable witness gives

\[
\boxed{A_4^{BG,base}=\frac12 A_4^{RFG15}}.
\]

Applying one common interaction normalization factor

\[
c=\sqrt2
\]

gives

\[
V_3^{BG}\mapsto cV_3^{BG}=2,
\qquad
V_4^{BG}\mapsto c^2V_4^{BG}=2,
\]

and then

\[
\boxed{A_4^{BG,project}=A_4^{RFG15}}.
\]

The gauge-coupling coordinate remains fixed; this aligns stripped-current normalization with the already admitted project amplitude convention.

## 2. Tree-level scaling

A tree-level `n`-point Yang–Mills amplitude carries interaction degree `n-2`, so

\[
A_n^{BG,project}=c^{n-2}A_n^{BG,base}.
\]

The executable witness verifies explicitly

\[
\boxed{A_4^{project}=2A_4^{base}},
\qquad
\boxed{A_5^{project}=2\sqrt2\,A_5^{base}}.
\]

## 3. Five-point KLT scaling

Because the KLT gravity core is bilinear,

\[
\mathcal C_5=A_L^T S_5 A_R,
\]

RFG26 obtains and verifies

\[
\boxed{\mathcal C_5^{project}=8\,\mathcal C_5^{base}}.
\]

## 4. Gravity coupling transfer

RFG20 fixed the project-normalized gauge-to-gravity replacement

\[
\boxed{g\to\kappa_g/4}.
\]

At five points,

\[
\boxed{\left(\frac{\kappa_g}{4}\right)^3=\frac18\left(\frac{\kappa_g}{2}\right)^3}.
\]

Therefore

\[
\boxed{i\left(\frac{\kappa_g}{4}\right)^3\mathcal C_5^{project}=i\left(\frac{\kappa_g}{2}\right)^3\mathcal C_5^{base}}.
\]

The physical five-point product is invariant under the normalization transfer.

## 5. Reduced-scale form

With

\[
\bar M_G=\frac2{\kappa_g},
\qquad
\kappa_E=\frac1{\bar M_G^2},
\]

the project-core coefficient is

\[
\boxed{\left(\frac{\kappa_g}{4}\right)^3=\frac1{8\bar M_G^3}=\frac{\kappa_E}{8\bar M_G}}.
\]

## 6. Executable validation

The independent RFG26 test verifies:

1. old BG four-point amplitude = exactly one half of RFG15;
2. corrected `2:2` BG four-point amplitude = RFG15;
3. tree rescaling = `2` at four points and `2 sqrt(2)` at five points;
4. two-copy five-point KLT core rescaling = exactly `8`;
5. `(kappa_g/4)^3` compensates the factor `8`;
6. reduced-scale identity `1/(8 Mbar_G^3)=kappa_E/(8 Mbar_G)`.

Local result:

```text
6 passed, 0 failed
```

Joint corrected replay:

```text
RFG24 + RFG25 + RFG26
18 passed, 0 failed
```

## 7. Advancement

```text
RFG20 four-point project normalization               PASS
RFG24 direct project five-point BG normalization     CORRECTED PASS
RFG25 direct project five-point KLT normalization    CORRECTED PASS
physical five-point KLT product                      INVARIANT
five-point multi-particle pole residue audit         NEXT
explicit 15-cubic-graph numerator representation     OPEN
internal-state / loop spectrum                       OPEN
```
