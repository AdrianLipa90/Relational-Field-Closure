# RF-E8 — ADM Kinematic Assembly Firewall

Status: `EXACT_BLOCK_METRIC_ASSEMBLY_CANDIDATE / EINSTEIN_DYNAMICS_GATE`

## 1. Source carriers

The current four-repository integration supplies two promoted kinematic inputs:

1. TIR local spatial relation geometry provides a positive three-metric `h_ij` on an admitted local spatial carrier;
2. IDT 05C provides a positive relational lapse `N_R>0` and a calibrated temporal one-form.

Introduce the length-valued temporal coordinate

\[
\boxed{x^0:=ct}
\]

and write the IDT temporal coframe component as

\[
\boxed{\vartheta^0=N_R\,dx^0.}
\]

Let `e^a_i` be a local spatial coframe satisfying

\[
\boxed{h_{ij}=\delta_{ab}e^a_i e^b_j.}
\]

A spatial shift coordinate `b^i` is kept as an independently typed gluing/coordinate carrier at this gate. Its proposed source from TIR affine-gluing transport is downstream and separately gated.

## 2. ADM coframe assembly

Define

\[
\boxed{
\vartheta^a=e^a_i\left(dx^i+b^i dx^0\right).
}
\]

With local Minkowski coframe metric

\[
\eta_{AB}=\operatorname{diag}(-1,1,1,1),
\]

the line element is

\[
\boxed{
 ds^2
=-(\vartheta^0)^2+\delta_{ab}\vartheta^a\vartheta^b.
}
\]

Therefore

\[
\boxed{
 ds^2
=-N_R^2(dx^0)^2
+h_{ij}(dx^i+b^i dx^0)(dx^j+b^j dx^0).
}
\]

This is the ADM block form written with `x^0=ct` and dimensionless shift `b^i`.

## 3. Metric components

Define

\[
b_i:=h_{ij}b^j,
\qquad
b^2:=h_{ij}b^i b^j.
\]

Then

\[
\boxed{
g_{00}=-N_R^2+b^2,
\qquad
g_{0i}=b_i,
\qquad
g_{ij}=h_{ij}.
}
\]

In block form,

\[
\boxed{
 g_{\mu\nu}
=
\begin{pmatrix}
-N_R^2+b^2 & b_j\\
b_i & h_{ij}
\end{pmatrix}.
}
\]

## 4. Exact inverse

Let `h^{ij}` be the inverse spatial metric. The inverse four-metric is

\[
\boxed{
 g^{00}=-\frac1{N_R^2},
\qquad
g^{0i}=\frac{b^i}{N_R^2},
\qquad
g^{ij}=h^{ij}-\frac{b^i b^j}{N_R^2}.
}
\]

Direct block multiplication gives

\[
\boxed{g_{\mu\alpha}g^{\alpha\nu}=\delta_\mu{}^\nu.}
\]

No field equation is used in this identity.

## 5. Determinant and volume element

The Schur complement of the spatial block is

\[
(-N_R^2+b^2)-b_i h^{ij}b_j=-N_R^2.
\]

Hence

\[
\boxed{\det g=-N_R^2\det h.}
\]

For `N_R>0` and positive `h`,

\[
\boxed{\sqrt{-g}=N_R\sqrt{h}.}
\]

This factorization is exact.

## 6. Lorentzian signature

Because `h_ij` is positive definite and `N_R>0`, the coframe representation

\[
 g=-(\vartheta^0)^2+\sum_{a=1}^3(\vartheta^a)^2
\]

has signature

\[
\boxed{(-,+,+,+).}
\]

The shift does not alter the signature because it appears through an invertible coframe change.

## 7. Unit normal and spatial projector

Choose the future-oriented unit normal covector

\[
\boxed{n_\mu=(-N_R,0,0,0).}
\]

Using the inverse metric,

\[
\boxed{
n^\mu=\left(\frac1{N_R},-\frac{b^i}{N_R}\right),
}
\]

and

\[
\boxed{n_\mu n^\mu=-1.}
\]

The induced spatial projector is

\[
\boxed{\gamma_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu.}
\]

Its spatial block is exactly

\[
\boxed{\gamma_{ij}=h_{ij}.}
\]

## 8. Source-typing firewall

The present assembly assigns distinct roles:

```text
TIR spatial carrier        -> h_ij / e^a_i
IDT relational lapse       -> N_R
RFC kinematic assembly     -> g_mn, g^mn, sqrt(-g), n^mu
shift carrier b^i          -> typed independent input at RF-E8
```

The active GREMLIN/TIR `SE(3)` gluing candidate suggests a future source map from affine local-frame transport to the shift carrier. RF-E8 records that as a candidate dependency rather than importing it as an established source.

## 9. Einstein-dynamics firewall

RF-E8 closes only the kinematic block assembly. The next dynamical targets are separately typed:

\[
\boxed{
K_{ij}
\to
\mathcal H_{ADM}
\to
\mathcal M_i
\to
\text{constraint propagation}
\to
G_{\mu\nu}=\kappa_E T_{\mu\nu}.
}
\]

where

- `K_ij` is the extrinsic-curvature source/definition gate with dimensional convention fixed explicitly;
- `H_ADM` is the Hamiltonian constraint;
- `M_i` is the momentum constraint.

These equations are not premises of the present metric assembly.

## 10. GREMLIN dependency refinement

The integrated cross-repository graph is refined to

```text
TIR local R3 metric/coframe h_ij
 + IDT positive lapse N_R
 + typed shift b^i
 -> RF-E8 ADM block metric
 -> inverse + determinant + unit normal            [EXACT KINEMATIC GATE]
 -> K_ij                                           [NEXT]
 -> Hamiltonian / momentum constraints             [OPEN]
 -> constraint propagation                         [OPEN]
 -> Einstein closure                               [OPEN]
```

Candidate future shift source:

```text
TIR SE(3) affine gluing
 -> local-frame displacement rate
 -> b^i                                            [GREMLIN CANDIDATE]
```

## 11. Claim ledger

| Statement | Status |
|---|---|
| ADM coframe expansion | EXACT ALGEBRA |
| metric components | EXACT ALGEBRA |
| inverse metric | EXACT BLOCK-MATRIX IDENTITY |
| `det g=-N_R^2 det h` | EXACT |
| `sqrt(-g)=N_R sqrt(h)` | EXACT |
| signature `(-,+,+,+)` for `N_R>0`, `h>0` | EXACT |
| unit normal formulas | EXACT |
| spatial projector recovers `h_ij` | EXACT |
| TIR `h_ij` + IDT `N_R` cross-repository source typing | INTEGRATION CONTRACT |
| TIR `SE(3)` gluing -> shift `b^i` | GREMLIN CANDIDATE |
| ADM constraints from TIR/IDT/RFC | OPEN DYNAMICAL GATE |
| Einstein field-equation closure | OPEN DYNAMICAL GATE |

## 12. Validation target

Deterministic validation must verify for multiple positive spatial metrics, lapses and shifts:

1. `g g^{-1}=I`;
2. determinant factorization;
3. unit-normal normalization;
4. projector spatial block;
5. zero-shift reduction;
6. rejection of nonpositive lapse or non-positive-definite spatial metric.

Verdict target:

`PASS_RF_E8_ADM_KINEMATIC_ASSEMBLY`.
