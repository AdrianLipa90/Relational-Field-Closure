# Relational Field Closure
## Scalar Matter Composition and Action-Derived Dynamic Lambda Closure

**Working monograph v0.13 — 28 August 2026**

**Status:** `RF_E6_LORENTZIAN_ACTION_PASS / RF_E7_SINGLE_SCALAR_TOTAL_MATTER_PASS / RF_L2_DYNAMIC_LAMBDA_ACTION_PASS / RFC_INVARIANT_LAMBDA_POTENTIAL_OPEN / PHYSICAL_G_UNIVERSALITY_OPEN`

## 1. Relativistic source spine

The active RFC relativistic chain is

\[
\boxed{
\mathfrak a_{AB}
\to A
\to F=dA
\to J_{RFC}
\xrightarrow{\Pi_Q}
J_{EM}
\to T^{EM}+T^{scalar}
\to G_{\mu\nu}+\Lambda_0g_{\mu\nu}.
}
\]

RF-G0 fixes the canonical signature `(-,+,+,+)`. RF-E6 aligns the charged matter action to that signature and fixes the microscopic Maxwell source sign. RF-E7 closes the full one-complex-scalar matter tensor. RF-L2 supplies an independent action realization for a dynamic `Lambda0` sector.

## 2. Exact one-scalar matter composition

For

\[
\psi=Ae^{i\vartheta},
\qquad
q_\mu=\partial_\mu\vartheta+\frac q\hbar A_\mu^{EM},
\]

RF-E7 gives

\[
D_\mu\psi=e^{i\vartheta}(\partial_\mu A+iAq_\mu)
\]

and the exact polar kinetic identity

\[
\boxed{
(D_\mu\psi)^*D^\mu\psi
=(\partial A)^2+A^2q^2.
}
\]

The scalar stress tensor decomposes with no independent sector coefficients:

\[
\boxed{
T_{\mu\nu}^{scalar}
=T_{\mu\nu}^{amp}
+T_{\mu\nu}^{phase}
+T_{\mu\nu}^{pot}.
}
\]

The three pieces are

\[
T_{\mu\nu}^{amp}
=2\partial_\mu A\partial_\nu A-g_{\mu\nu}(\partial A)^2,
\]

\[
T_{\mu\nu}^{phase}
=2A^2q_\mu q_\nu-g_{\mu\nu}A^2q^2,
\]

\[
T_{\mu\nu}^{pot}=-g_{\mu\nu}V.
\]

The synchronized AB gauge transformation leaves `q_mu` invariant, so the decomposition is gauge covariant.

For the admitted single-scalar electromagnetic system,

\[
\boxed{
T_{\mu\nu}^{base}
=T_{\mu\nu}^{EM}+T_{\mu\nu}^{scalar}.
}
\]

On the coupled equations,

\[
\boxed{\nabla^\mu T_{\mu\nu}^{base}=0.}
\]

## 3. RF-E4/RF-E5 limits

For homogeneous phase flow with `K=A^2r_n^2`,

\[
\boxed{
\varepsilon=K+V,
\qquad
p=K-V,
\qquad
\varepsilon+3p=4K-2V.
}
\]

For the homogeneous quadratic on-shell scalar,

\[
\boxed{
V=K,
\qquad
p=0,
\qquad
\varepsilon=2K.
}
\]

The kinetic carrier energy remains `omega/2`, while the total on-shell energy per carrier is `omega`.

A spatial amplitude gradient is retained as anisotropic stress:

\[
\partial_{\hat a}A=(0,g,0,0)
\quad\Rightarrow\quad
\boxed{
T_{\hat a\hat b}^{amp}
=\operatorname{diag}(g^2,g^2,-g^2,-g^2).
}
\]

## 4. Action-derived dynamic Lambda0

RF-L2 introduces a canonical real scalar `phi_L` through

\[
\boxed{
S
=\int d^4x\sqrt{-g}
\left[
\frac{R-2\Lambda_{ref}}{2\kappa_E}
-\frac12(\nabla\phi_L)^2
-U_L(\phi_L)
+\mathcal L_{base}
\right].
}
\]

Its stress tensor splits as

\[
\boxed{
T^L_{\mu\nu}=T^{kin}_{\mu\nu}-U_Lg_{\mu\nu},
}
\]

with

\[
T^{kin}_{\mu\nu}
=\nabla_\mu\phi_L\nabla_\nu\phi_L
-\frac12g_{\mu\nu}(\nabla\phi_L)^2.
\]

Moving the potential contribution to the geometric side defines

\[
\boxed{
\Lambda_0(x)
=\Lambda_{ref}+\kappa_EU_L(\phi_L(x)).
}
\]

and yields

\[
\boxed{
G_{\mu\nu}+\Lambda_0g_{\mu\nu}
=\kappa_E
\left(T^{base}_{\mu\nu}+T^{kin}_{\mu\nu}\right).
}
\]

## 5. Bianchi transfer from the scalar equation

The scalar equation is

\[
\boxed{\Box\phi_L-U_L'(\phi_L)=0.}
\]

On shell,

\[
\nabla^\mu T^{kin}_{\mu\nu}=\nabla_\nu U_L.
\]

With the conserved base sector,

\[
\boxed{
\kappa_E\nabla^\mu
\left(T^{base}_{\mu\nu}+T^{kin}_{\mu\nu}\right)
=\nabla_\nu\Lambda_0.
}
\]

This reproduces the RF-E0 dynamic transfer directly from an action.

## 6. Stationary vacuum and dynamic stress

At

\[
\nabla_\mu\phi_L=0,
\qquad
U_L'(\phi_{L0})=0,
\]

one has

\[
T^{kin}_{\mu\nu}=0
\]

and

\[
\boxed{
\Lambda_0
=\Lambda_{ref}+\kappa_EU_L(\phi_{L0})
=\mathrm{constant}.
}
\]

For homogeneous dynamics,

\[
K_L=\frac12\dot\phi_L^2,
\]

\[
\boxed{
\varepsilon_L=K_L+U_L,
\qquad
p_L=K_L-U_L,
\qquad
\varepsilon_L+p_L=\dot\phi_L^2.
}
\]

A spatial gradient produces anisotropic kinetic stress and remains explicitly on the source side.

## 7. Local stability gate

Around a stationary point,

\[
\phi_L=\phi_{L0}+\delta\phi,
\]

with `U_L'(phi_L0)=0`, linearization gives

\[
\boxed{
(\Box-m_L^2)\delta\phi=0,
\qquad
m_L^2=U_L''(\phi_{L0}).
}
\]

The local non-tachyonic criterion is

\[
\boxed{U_L''(\phi_{L0})\ge0.}
\]

Strict positivity gives a locally restoring stationary point; zero curvature is marginal and requires higher-order analysis.

## 8. Validation chain

- RF-E6 PR #16: final hosted gate **470/470 PASS**.
- RF-E7 PR #17: final hosted gate **479/479 PASS**.
- RF-L2 PR #18: tested commit `38c9589608abe77bdcf05d46e997731ef5d6e430`, run `33208242527`, job `98974734417`, **489/489 PASS**.

Receipt:

`validation/RFL2_DYNAMIC_LAMBDA0_ACTION_STABILITY_V0_1.json`

Cross-reference authority:

`CROSS_REFERENCE_LOCK.json` v0.38.

## 9. Current frontier

The next Lambda-sector problem is now sharply typed:

\[
\boxed{
U_L(\phi_L)
\longleftrightarrow
U_L(\mathcal I_{RFC})
}
\]

where `I_RFC` denotes independently admitted scalar invariants with correct dimensions and provenance. The resulting potential must then pass parameter-free calibration and nonlinear/global stability tests.

In parallel, the physical gravity-coupling line still requires cross-system `G` universality and the RFG35 projected-cut Ward gate. Multispecies/additional matter sectors remain additive only after their own action/variation provenance is supplied.
