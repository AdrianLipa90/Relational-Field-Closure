# RF-S19 — Conserved Four-Current → Relativistic Dust Tensor Closure

Status: `EXACT_TIMELIKE_CURRENT_TENSOR_MAP / VELOCITY_ELIMINATED / CARRIER_NORMALIZATION_COVARIANT`

RF-S19 is stacked on exact-green RF-S18. RF-S18 lifts the relational-generator rest energy density into a relativistic dust tensor once a local velocity is supplied. RF-S19 removes that independent velocity input whenever the full conserved future-timelike four-current is available.

## 1. Future-timelike current

Let

\[
J_Q^\mu=(J^0,\mathbf J)
\]

be an admitted conserved current in a local orthonormal frame with signature `(-,+,+,+)`, satisfying

\[
J^0>0,
\qquad
J_\mu J^\mu<0.
\]

Define the proper carrier density

\[
\boxed{
q:=\sqrt{-J_\mu J^\mu}
=\sqrt{(J^0)^2-|\mathbf J|^2}>0.
}
\]

Then

\[
\boxed{
u^\mu:=\frac{J_Q^\mu}{q}}
\]

satisfies

\[
\boxed{u_\mu u^\mu=-1.}
\]

The Eulerian velocity and Lorentz factor are therefore not additional inputs:

\[
\boxed{
\beta^i=\frac{J^i}{J^0},
\qquad
\gamma=\frac{J^0}{q}.
}
\]

## 2. Energy-per-charge source

RF-S16 gives

\[
\rho_G=\epsilon_Qj_Q
\]

for the scalar carrier-density representation. Covariantly, let \(\epsilon_Q\ge0\) be the energy per conserved carrier charge. The comoving/rest-frame energy density carried by the current is

\[
\boxed{
\rho_0=\epsilon_Q q.
}
\]

The dust tensor is therefore

\[
\boxed{
T^{\mu\nu}
=\rho_0u^\mu u^\nu
=\epsilon_Q\frac{J_Q^\mu J_Q^\nu}{q}.
}
\]

Equivalently in covariant components,

\[
\boxed{
T_{\mu\nu}
=\epsilon_Q\frac{J_{Q\mu}J_{Q\nu}}{q}.
}
\]

Thus one future-timelike conserved four-current plus its energy-per-charge coordinate determines the complete pressureless stress-energy tensor.

## 3. Exact RF-E11 projections

In the RF-E11 adapted orthonormal frame,

\[
\boxed{
\rho_n
=\epsilon_Q\frac{(J^0)^2}{q},
}
\]

\[
\boxed{
j_i^{ADM}
=\epsilon_Q\frac{J^0J^i}{q},
}
\]

and

\[
\boxed{
S_{ij}
=\epsilon_Q\frac{J^iJ^j}{q}.
}
\]

Using \(J^0=q\gamma\) and \(J^i=q\gamma\beta^i\), these reduce exactly to RF-S18:

\[
\rho_n=\rho_0\gamma^2,
\qquad
j_i^{ADM}=\rho_0\gamma^2\beta_i,
\qquad
S_{ij}=\rho_0\gamma^2\beta_i\beta_j.
\]

## 4. Tensor invariants

The RF-S18 dust identities follow directly:

\[
\boxed{
-\rho_n+S=-\rho_0,
}
\]

\[
\boxed{
|\mathbf j^{ADM}|^2=\rho_nS.
}
\]

The local rest density is reconstructed from either representation:

\[
\boxed{
\rho_0=\epsilon_Qq=\rho_n-S.
}
\]

## 5. Carrier-normalization covariance

RF-S17 establishes the positive carrier-unit transformation

\[
J_Q^\mu\mapsto\lambda J_Q^\mu,
\qquad
\epsilon_Q\mapsto\frac{\epsilon_Q}{\lambda},
\qquad \lambda>0.
\]

Then

\[
q\mapsto\lambda q,
\]

while

\[
\boxed{
u^\mu\mapsto u^\mu}
\]

and

\[
\boxed{
T_{\mu\nu}
\mapsto
\frac{\epsilon_Q}{\lambda}
\frac{(\lambda J_\mu)(\lambda J_\nu)}{\lambda q}
=T_{\mu\nu}.
}
\]

Therefore the entire relativistic stress-energy tensor, not only its scalar energy density, is invariant under the arbitrary positive carrier-charge normalization.

## 6. Relational generator insertion

RF-S16 supplies

\[
\boxed{
\epsilon_Q
=\frac{B\omega}{q_0}(\phi+\kappa)
}
\]

when the current is expressed in carrier units \(q_0\). RF-S17 shows that the simultaneous current normalization removes the dependence of the physical tensor on that convention.

Thus the chain becomes

\[
\boxed{
(B,\omega,\phi,\kappa)
+J_Q^\mu
\longrightarrow
\epsilon_Q,q,u^\mu
\longrightarrow
T_{\mu\nu}
\longrightarrow
(\rho_n,j_i,S_{ij}).
}
\]

No separately supplied three-velocity is needed on this branch.

## 7. RF-E12/RF-E13 consequence

Because RF-E12 and RF-E13 already consume \(\rho_n,j_i,S_{ij}\), the full conserved four-current directly supplies the matter side of the ADM system:

\[
{}^{(3)}R+K^2-K_{ij}K^{ij}
=2\kappa_E\epsilon_Q\frac{(J^0)^2}{q},
\]

\[
D_jK^j{}_i-D_iK
=\kappa_E\epsilon_Q\frac{J^0J^i}{q},
\]

with the spatial evolution source obtained from

\[
S_{ij}=\epsilon_Q\frac{J^iJ^j}{q}.
\]

This closes the kinematic transport coordinate of RF-S18 whenever a full timelike conserved current is admitted.

## 8. Advancement

```text
future timelike J_Q^mu -> proper density q                 PASS EXACT
u^mu=J^mu/q, u^2=-1                                     PASS EXACT
beta^i=J^i/J^0                                          PASS EXACT
gamma=J^0/q                                              PASS EXACT
rho_0=epsilon_Q q                                        PASS EXACT
T_mn=epsilon_Q J_m J_n/q                                 PASS EXACT
RF-E11 ADM projections                                   PASS EXACT
RF-S18 tensor identities                                 PASS EXACT
full T_mn invariant under carrier-unit rescaling          PASS EXACT
separate local velocity input                            ELIMINATED ON FOUR-CURRENT BRANCH
physical four-current receipt                            OPEN INPUT
physical energy-per-charge realization                   OPEN INPUT
absolute project-side kappa_E/G promotion                OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/fourcurrent_dust_tensor_closure.py`.
Reference tests: `tests/reference/test_rfs19_fourcurrent_dust_tensor_closure.py`.
Validation receipt: `validation/RF_S19_FOURCURRENT_DUST_TENSOR_CLOSURE_V0_1.json`.

Stack parent: RF-S18 exact-green head `179eff3c31fbec7cb90e6d95b46e93ba394f83ff`, RFC reference suite #284 SUCCESS.
