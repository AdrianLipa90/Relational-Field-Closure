# RFG26 — Project Five-Point KLT Gravity Gate

Status: `DIRECT_BGxBG_KLT_CORE_PASS / LEFT_RIGHT_GRAVITY_WARD_PASS / COPY_EXCHANGE_PASS / QUARTIC_PROPAGATION_PASS / PROJECT_CORE_MAP_FACTOR_4_PASS_RFG27 / ZETA5_MINUS_I_OVER_4_PASS_RFG27`

RFG26 consumes the direct RFG25 Berends–Giele amplitudes and the RFG24 KLT kernel. Its byte-preserved executable test admits the raw/BG-basis KLT core

\[
\boxed{\mathcal C_5^{BG}=\mathbf A_L^{BG\,T}S_5\mathbf A_R^{BG}},
\]

including independent two-term reconstruction, all five left/right Ward replacements, copy exchange and the quartic-contact propagation firewall.

RFG27 maps the RFG25 BG basis to the RFG15 project color-order basis by `eta_A=2`. Therefore

\[
\boxed{\mathcal C_5^{project}=4\mathcal C_5^{BG}}.
\]

With

\[
P_5=\left(\frac{\kappa_g}{2}\right)^3=\frac1{\bar M_G^3},
\]

RFG27's conserved gravity soft gate fixes

\[
\boxed{\mathcal M_5^{project}=-\frac{i}{4}P_5\mathcal C_5^{project}=-iP_5\mathcal C_5^{BG}}.
\]

Thus the same project-core coefficient `-i/4` appearing at four points is transported to five points once the color-order basis map is included.

Recorded RFG26 core result remains

```text
6 passed, 0 failed
```

and the overall normalization is now closed by RFG27.
