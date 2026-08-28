# RFG21 — Project Gravity Pole Factorization Gate

Status: `MASSLESS_T_CHANNEL_POLE_REFERENCE_PASS / QUARTIC_RESIDUE_DECOUPLING_PASS / CUBIC_DOUBLE_COPY_RESIDUE_FACTORIZATION_PASS / FOUR_POINT_SCOPE`

RFG21 consumes the RFG14/RFG15 project Yang–Mills construction and the RFG16 project double-copy amplitude. Its purpose is to verify that a physical massless channel pole is controlled by the cubic double-copy residue, while the distributed quartic contact contribution vanishes from the pole residue.

## 1. Project numerator near the pole

RFG15 defines

\[
\boxed{n_t=X_t+tK_t,}
\]

where `X_t` is the product of the two actual project cubic currents in the `t` channel and `K_t` is the finite quartic-contact coefficient assigned to that channel.

Therefore

\[
\boxed{n_t\xrightarrow[t\to0]{}X_t.}
\]

The executable gate follows the forward-scattering sequence where

\[
t=(p_1+p_3)^2\sim-\theta^2
\]

while the other channel denominators remain finite.

## 2. Gravity residue

The RFG16 gravity core is

\[
\mathcal C_{DC}
=\frac{n_s\widetilde n_s}{s}
+\frac{n_t\widetilde n_t}{t}
+\frac{n_u\widetilde n_u}{u}.
\]

Multiplying by `t` and taking the forward massless pole gives

\[
\boxed{
\lim_{t\to0}t\,\mathcal C_{DC}
=X_t\widetilde X_t.
}
\]

Hence the project gravity amplitude satisfies

\[
\boxed{
\operatorname*{Res}_{t=0}\mathcal M_4^{project}
=i\kappa_E X_t\widetilde X_t.
}
\]

The `s`- and `u`-channel contributions vanish after multiplication by `t` on the tested pole sequence.

## 3. Cubic-current factorization

For each Yang–Mills copy write the cubic exchange numerator as

\[
X_t=J_L\cdot J_R,
\qquad
\widetilde X_t=\widetilde J_L\cdot\widetilde J_R.
\]

Define rank-two double-copy currents

\[
\mathcal J_L^{\mu\nu}=J_L^\mu\widetilde J_L^\nu,
\qquad
\mathcal J_R^{\alpha\beta}=J_R^\alpha\widetilde J_R^\beta.
\]

Then exactly

\[
\boxed{
X_t\widetilde X_t
=
\mathcal J_L^{\mu\nu}\eta_{\mu\alpha}\eta_{\nu\beta}\mathcal J_R^{\alpha\beta}.
}
\]

Thus the pole residue factorizes into a left and a right three-point double-copy current joined by the massless rank-two propagator contraction.

## 4. Contact-term firewall

The distributed contact contribution obeys

\[
n_t-X_t=tK_t.
\]

For finite `K_t`, this difference vanishes linearly with `t`. The executable reference verifies the expected `O(theta^2)` decay independently in both project copies.

The pole residue is therefore insensitive to finite quartic-contact redistribution while the full off-pole amplitude continues to require the RFG13/RFG14 contact term for gauge invariance and matched Jacobi closure.

## 5. Executable validation

The reference test checks:

1. forward `t`-channel denominator scales as `theta^2` while `s` and `u` remain finite;
2. `n_t-X_t=t K_t` and the contact correction vanishes with the pole coordinate in both copies;
3. `t * C_DC -> X_t Xtilde_t` with the observed quadratic angular convergence;
4. non-`t` channels vanish after multiplication by `t`;
5. `X_t Xtilde_t` equals the rank-two left/right cubic-current contraction exactly;
6. a very small-pole witness confirms finite contact redistribution leaves the limiting residue unchanged.

Local result:

```text
6 passed, 0 failed
```

## 6. Advancement

```text
RFG14 full gauge-invariant project A4                PASS
RFG15 matched-Jacobi cubicization                    PASS
RFG16 project double copy                            PASS
massless t-channel pole                              PASS REFERENCE
quartic contact removal from residue                 PASS
cubic double-copy current factorization              PASS
kappa_E residue prefactor                            INHERITS RFG16/RFG17
higher-point multi-particle factorization            OPEN
loop/internal-state spectrum                         OPEN
```

RFG21 establishes four-point tree pole factorization on the same project numerator surface used by the Einstein-coupling bridge.