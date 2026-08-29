# RF-E15 — Information Legendre / Hamiltonian Audit

Status: `EXACT_CONVEX_DUALITY_PASS / ADM_SHIFT_CONJUGATE_BINDING_PASS / PHYSICAL_ENERGY_SELECTION_OPEN`

RF-E14 produces the dimensionless directional relative-information potential

\[
\boxed{\Phi(x)=x-1-\ln x,\qquad x>0}
\]

on the two ADM reciprocal directional factors

\[
 x_\to=\frac1{1-b},
 \qquad
 x_\leftarrow=\frac1{1+b},
 \qquad |b|<1.
\]

RF-E15 performs the canonical convex/Legendre audit before any physical energy interpretation is promoted.

## 1. Convex gradient coordinate

The exact derivatives are

\[
\boxed{\Phi'(x)=1-\frac1x,}
\]

\[
\boxed{\Phi''(x)=\frac1{x^2}>0.}
\]

Define the conjugate scalar

\[
\boxed{p:=\Phi'(x).}
\]

Then

\[
\boxed{x=\frac1{1-p},\qquad p<1.}
\]

On the RF-E14 directional ADM factors,

\[
\boxed{p_\to=b,}
\qquad
\boxed{p_\leftarrow=-b.}
\]

Thus the dimensionless ADM shift ratio is exactly the orientation-sensitive conjugate coordinate of the relative-information traversal factor.

## 2. Exact Legendre dual

The convex conjugate is

\[
\Phi^*(p)
:=\sup_{x>0}\{px-\Phi(x)\}.
\]

At the stationary point `x=1/(1-p)`, one obtains

\[
\boxed{\Phi^*(p)=-\ln(1-p),\qquad p<1.}
\]

Write

\[
\boxed{\Psi(p):=-\ln(1-p).}
\]

The exact Fenchel equality is

\[
\boxed{\Phi(x)+\Psi(p)=px}
\]

when `p=Phi'(x)`.

## 3. Directional pair

For the co-oriented branch,

\[
 p=b,
 \qquad
 x=\frac1{1-b},
\]

so

\[
\boxed{\Psi_\to(b)=-\ln(1-b)}
\]

and

\[
\boxed{
\mathcal I_\to(b)
=\frac{b}{1-b}-\Psi_\to(b)
=\frac{b}{1-b}+\ln(1-b).
}
\]

For the counter-oriented branch,

\[
 p=-b,
 \qquad
 x=\frac1{1+b},
\]

so

\[
\boxed{\Psi_\leftarrow(b)=-\ln(1+b)}
\]

and

\[
\boxed{
\mathcal I_\leftarrow(b)
=-\frac{b}{1+b}-\Psi_\leftarrow(b)
=-\frac{b}{1+b}+\ln(1+b).
}
\]

The logarithmic/rational expressions are therefore the primal relative-information values in an exact primal-dual decomposition.

## 4. Rapidity relation

With

\[
\eta=\operatorname{artanh}b,
\qquad
\gamma=(1-b^2)^{-1/2},
\]

RF-E14 gives

\[
 x_\to=\gamma e^\eta,
 \qquad
 x_\leftarrow=\gamma e^{-\eta}.
\]

The dual pair satisfies

\[
\boxed{
\Psi_\to=\eta+\ln\gamma,
\qquad
\Psi_\leftarrow=-\eta+\ln\gamma.
}
\]

Hence

\[
\boxed{
\frac{\Psi_\to+\Psi_\leftarrow}{2}=\ln\gamma,
}
\]

\[
\boxed{
\frac{\Psi_\to-\Psi_\leftarrow}{2}=\eta.
}
\]

The even dual coordinate is the logarithmic Lorentz factor and the odd dual coordinate is rapidity itself.

## 5. Canonical-action selection gate

RF-E15 now exposes two mathematically distinct but exactly dual scalar objects:

```text
primal information cost     : Phi(x)=x-1-ln x
conjugate coordinate         : p=1-1/x
Legendre-dual generator      : Psi(p)=-ln(1-p)
Fenchel relation             : Phi+Psi=p x
ADM directional realization : p=+b / -b
```

A physical action must specify which variable is a generalized coordinate, which is a generalized rate, and which quantity is the canonical Hamiltonian/Noether charge. That source-variable binding selects the physical role of `Phi`, `Psi`, or a composed energy functional.

The existing RFC phase-energy/Noether sector supplies a separate canonical energy carrier through RF-N1B2O. RF-E15 therefore assigns the next gate to an explicit pullback between the ADM directional information pair and an admitted RFC matter/Noether action variable.

## 6. Physical energy candidates and firewall

Introduce a positive energy scale `E_*`. The two immediately available scaled objects are

\[
E_\Phi=E_*\Phi(x),
\qquad
E_\Psi=E_*\Psi(p).
\]

RF-E14 shows that choosing `E_*=mc^2` and `b=v/c` makes `E_Phi` reproduce the two external logarithmic/rational expressions and the Newtonian quadratic coefficient.

RF-E15 records the exact canonical dual `E_Psi` as an independent action-level comparison target. Physical promotion therefore requires a source-pinned derivation from the RFC matter action/Noether charge rather than a naming convention.

## 7. New falsification handles

The gate provides three separable tests:

1. `shift conjugacy`: whether the physical shift/relative-motion realization obeys `p=+-b`;
2. `action pullback`: whether the admitted matter action selects `Phi`, `Psi`, or another exact composition as its conserved energy coordinate;
3. `scale binding`: whether the selected dimensionless generator receives `E_*=mc^2` from upstream mass/rest-energy structure.

A failure of any one gate localizes the physical-energy claim without affecting the RF-E14 exact kinematic-information identity.

## 8. Validation authority

Reference implementation: `src/rfc/information_legendre_hamiltonian.py`.
Reference tests: `tests/reference/test_rfe15_information_legendre_hamiltonian.py`.
Validation receipt: `validation/RF_E15_INFORMATION_LEGENDRE_HAMILTONIAN_V0_1.json`.

Next gate: RF-E16 — source-pin the primal/dual information coordinates into the existing RF-N1B2O phase-energy / Noether action sector and report PASS/FAIL for physical energy promotion.
