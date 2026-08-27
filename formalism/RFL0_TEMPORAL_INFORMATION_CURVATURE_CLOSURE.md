# RF-L0 — Temporal Information Curvature Closure

Status: `EXACT_TIR_IDT_PHASE_CLOCK_INTERFACE / LAMBDA0_COUPLING_CANDIDATE / ACTION_LEVEL_METRIC_VARIATION_OPEN`

Pinned upstreams for this gate:

- TIR branch `agent/phase-clock-area-scale-v0.2`: `b69ba6055c0535c666e12dbba069ffb87238eee6`
- IDT branch `feat/phase-clock-length-scale-v0.1`: `f90435edbfbba8211e6c28cc49a7c22f8059021b`
- Secret of a Half `main`: `206e49e306b246c4b0f4d182b0d32d5511739408`

## 1. Exact imported phase-clock scale

IDT supplies the calibrated angular phase rate

\[
\omega_t
=\frac{d\varphi}{dt}
=\frac{d\varphi/d\tau_{\rm int}}{dt/d\tau_{\rm int}},
\qquad |\omega_t|>0,
\]

and the exact local length carrier

\[
\boxed{
\ell_\varphi
=\frac{c}{|\omega_t|}
=\frac{\hbar c}{E}.
}
\]

TIR supplies the dimensionless Fubini--Study area form `da_FS` and Berry relation

\[
\boxed{
\mathcal F_B=\pm2\,da_{FS}.
}
\]

The phase-clock physicalized area candidate is

\[
\boxed{
 d\mathcal A_{\rm rel}
=\ell_\varphi^2 da_{FS}
=\frac{c^2}{\omega_t^2}da_{FS}.
}
\]

For a constant-rate cell `P`,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\frac{c^2}{\omega_P^2}a_{FS}^{(P)}.
}
\]

Thus the earlier free scale `ell_R` is replaced, under this binding, by

\[
\boxed{
\ell_R(x)\equiv\ell_\varphi(x)=\frac{c}{|\omega_t(x)|}.
}
\]

## 2. Temporal information curvature with explicit phase-rate dependence

Let

\[
\mathcal J_\pi=(\ln2)\mathcal I_\pi
=24\pi\kappa\,\mathcal I_\pi.
\]

Define

\[
\boxed{
\Xi_I
:=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}}.
}
\]

For a constant-rate cell,

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{\omega_P}{c}\right)^2
}
\]

and equivalently

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{E_P}{\hbar c}\right)^2.
}
\]

Using the canonical TIR normalization,

\[
\boxed{
\Xi_I^{(P)}
=\frac{24\pi\kappa}{a_{FS}^{(P)}}
\mathcal I_\pi
\left(\frac{\omega_P}{c}\right)^2.
}
\]

For the full CP1/Bloch sphere, `a_FS = pi`, hence

\[
\boxed{
\Xi_I^{(S^2)}
=24\kappa\,\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2.
}
\]

This has the required type

\[
\boxed{[\Xi_I]=L^{-2}}.
\]

## 3. Exact temporal rate

In the constant-dimensionless-area sector,

\[
\Xi_I
=\frac{\mathcal J_\pi}{a_{FS}}
\frac{\omega_t^2}{c^2}.
\]

Therefore

\[
\boxed{
\frac{d\Xi_I}{d\tau_{\rm int}}
=
\frac{\omega_t^2}{c^2a_{FS}}
\frac{d\mathcal J_\pi}{d\tau_{\rm int}}
+
\frac{2\mathcal J_\pi\omega_t}{c^2a_{FS}}
\frac{d\omega_t}{d\tau_{\rm int}}.
}
\]

Equivalently, wherever `J_pi` and `omega_t` are nonzero,

\[
\boxed{
\frac{1}{\Xi_I}
\frac{d\Xi_I}{d\tau_{\rm int}}
=
\frac{1}{\mathcal J_\pi}
\frac{d\mathcal J_\pi}{d\tau_{\rm int}}
+2\frac{1}{\omega_t}
\frac{d\omega_t}{d\tau_{\rm int}}.
}
\]

The curvature-typed scalar therefore carries both information flow and phase-clock-rate flow.

## 4. Information contribution to the dynamic Lambda sector

Introduce a dimensionless coupling `alpha_I` and define

\[
\boxed{
\Lambda_I:=\alpha_I\Xi_I.
}
\]

Then

\[
\boxed{[\Lambda_I]=L^{-2}.}
\]

For a constant-rate cell,

\[
\boxed{
\Lambda_I^{(P)}
=\alpha_I
\frac{24\pi\kappa}{a_{FS}^{(P)}}
\mathcal I_\pi
\left(\frac{\omega_P}{c}\right)^2.
}
\]

For the full CP1/Bloch sphere,

\[
\boxed{
\Lambda_I^{(S^2)}
=24\alpha_I\kappa\,\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2
}
\]

or, using `E = hbar |omega|`,

\[
\boxed{
\Lambda_I^{(S^2)}
=24\alpha_I\kappa\,\mathcal I_\pi
\left(\frac{E}{\hbar c}\right)^2.
}
\]

The general scalar-basis candidate remains

\[
\boxed{
\Lambda_0
=\Lambda_{\rm vac}
+\Lambda_I
+\sum_r\alpha_r\mathcal S_r,
}
\]

where every admitted scalar `S_r` has type `L^-2` after its own normalization.

The exact sensitivity is

\[
\boxed{
\frac{\partial\Lambda_0}{\partial\Xi_I}=\alpha_I.
}
\]

For the minimal information sector,

\[
\boxed{
\frac{d\Lambda_0}{d\tau_{\rm int}}
=\alpha_I\frac{d\Xi_I}{d\tau_{\rm int}}.
}
\]

## 5. Bianchi bookkeeping

For the phenomenological field-equation convention

\[
G_{\mu\nu}+\Lambda_0 g_{\mu\nu}
=\frac{8\pi G}{c^4}T^{\rm visible}_{\mu\nu},
\]

the contracted Bianchi identity gives

\[
\boxed{
\nabla_\mu T_{\rm visible}^{\mu\nu}
=\frac{c^4}{8\pi G}\nabla^\nu\Lambda_0.
}
\]

The information-phase channel contributes

\[
\boxed{
\nabla^\nu\Lambda_0
=\alpha_I\nabla^\nu\Xi_I
+\sum_r\alpha_r\nabla^\nu\mathcal S_r.
}
\]

In a constant-`a_FS` patch,

\[
\nabla^\nu\Xi_I
=\frac{1}{c^2a_{FS}}
\left(
\omega^2\nabla^\nu\mathcal J_\pi
+2\mathcal J_\pi\omega\nabla^\nu\omega
\right).
\]

Thus both information gradients and phase-rate gradients enter the dynamic scalar bookkeeping.

## 6. Action-level metric-variation firewall

Consider

\[
S_{\Lambda}
=-\frac{c^3}{8\pi G}
\int d^4x\,\sqrt{-g}\,\Lambda_0.
\]

When `Lambda0` is independent of `g^{mu nu}` during metric variation, its contribution is the familiar `Lambda0 g_{mu nu}` term.

When `Lambda0` contains metric-dependent invariants, the variation also carries the metric sensitivity of those invariants. For purely algebraic metric dependence,

\[
\boxed{
G_{\mu\nu}
+\Lambda_0 g_{\mu\nu}
-2\frac{\partial\Lambda_0}{\partial g^{\mu\nu}}
=\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

For derivative-dependent functionals, the partial derivative is replaced by the corresponding functional Euler--Lagrange variation.

The present phase-clock area binding therefore creates a concrete next question: whether `omega_t`, `a_FS` or their physicalized area carrier depend functionally on the emergent spacetime metric.

## 7. Projective/spinorial scale relation

IDT supplies

\[
L_{2\pi}=2\pi\ell_\varphi,
\qquad
L_{4\pi}=4\pi\ell_\varphi,
\]

so

\[
\boxed{
\frac{L_{2\pi}}{L_{4\pi}}=\frac12.
}
\]

This keeps the projective/Berry and spinorial closure scales separately typed while preserving their exact half relation.

## 8. Temporal coupling criterion

RFC records the typed criterion

```text
TEMPORAL_INFORMATION_LAMBDA_COUPLING
  requires:
    alpha_I != 0
    Xi_I admitted from pinned TIR + IDT
    phase-clock area binding admitted on the patch
  exact sensitivity:
    d Lambda0 / d Xi_I = alpha_I
  constant-cell form:
    Xi_I = (J_pi/a_FS) (omega/c)^2
```

For the minimal information sector, temporal phase-rate variation and information variation jointly determine the temporal variation of `Lambda_I`.

The author/formalism may suggest a stronger global inseparability of time and `Lambda0`, yet does not state that stronger claim as an established result until the remaining scalar sectors, zero-rate patches, refinement convergence and action-level closure are fixed.

## 9. Promotion gates

RF-L0 advances when the following are separately receipted:

1. TIR phase-clock physicalized area/refinement contract;
2. IDT calibrated phase-rate and `Xi_I` evolution;
3. phase-rate-zero patch treatment;
4. nonuniform polyhedral refinement convergence;
5. `alpha_I` determination or falsifiable bound;
6. action-level metric dependence of the physicalized area;
7. Bianchi/stress-energy partition;
8. Newton and Einstein limit tests.