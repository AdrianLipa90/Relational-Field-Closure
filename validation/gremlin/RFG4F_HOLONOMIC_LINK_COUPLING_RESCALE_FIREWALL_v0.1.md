# RFG4F — Holonomic-Link Coupling Rescale Firewall

Status: `EXACT_GENERATOR_NORMALIZATION_MAP / EXACT_LINK_RESCALE_DEGENERACY / METATIME_CONTINUUM_ALPHA_BINDING_PRESENT / PHYSICAL_LINK_COUPLING_NORMALIZATION_OPEN`

RFG4F compares the actual Metatime holonomic `W_ij -> W_mu(x)` lineage with the NoParamSM continuum gluon convention and the RFG3 Wilson convention. Its purpose is to isolate the exact normalization coordinate left free by link holonomy.

## 1. Holonomic v4.1 link convention

The Metatime v4.1 local-connection script constructs links in the full Gell-Mann basis. Schematically,

\[
\boxed{
W_\mu(x)=\exp\!\left[i a\,q_\mu^a(x)\lambda^a\right].
}
\]

Its explicit constant-link witnesses include

\[
W_x=\exp(i a\alpha\lambda_1),
\qquad
W_y=\exp(i a\beta\lambda_2).
\]

The v4.1 curvature proxy, gauge covariance, Wilson trace and small-loop scaling are already validated in the upstream lineage.

## 2. Standard continuum/Wilson generator convention

NoParamSM and RFG3 use the fundamental `SU(3)` generators

\[
\boxed{
T^a=\frac{\lambda^a}{2},
\qquad
\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}.
}
\]

The standard local link is

\[
\boxed{
U_\mu(x)
=\exp\!\left[i g_0aA_\mu^a(x)T^a\right].
}
\]

Expressed in the full Gell-Mann basis,

\[
U_\mu(x)
=\exp\!\left[i a\frac{g_0A_\mu^a(x)}{2}\lambda^a\right].
\]

Therefore exact equality of the v4.1 and standard link bytes at the Lie-algebra coordinate level requires

\[
\boxed{
q_\mu^a
=\frac{g_0A_\mu^a}{2}.
}
\]

Equivalently,

\[
\boxed{
g_0A_\mu^a=2q_\mu^a.}
\]

This factor of two is fixed solely by the generator normalization.

## 3. Link-rescaling degeneracy theorem

For every positive `lambda`, define

\[
\boxed{
g_0' = \lambda g_0,
\qquad
A_\mu^{\prime a}=\frac{A_\mu^a}{\lambda}.}
\]

Then

\[
\frac{g_0'A_\mu^{\prime a}}2
=\frac{g_0A_\mu^a}2
=q_\mu^a,
\]

and therefore

\[
\boxed{
U_\mu'[g_0',A']=U_\mu[g_0,A].
}
\]

Thus the exact local link holonomy determines the product `g_0 A_mu^a` while retaining one continuous coupling/field-normalization coordinate.

The same statement holds for every closed Wilson loop built only from these links.

## 4. Metatime continuum `alpha_c` convention

The source files

```text
AdrianLipa90/Metatime/NoParamSM/gluons.py
AdrianLipa90/Metatime/NoParamSM/gluonsfull.py
```

explicitly define

\[
\boxed{
\alpha_c=\frac1{g^2},
\qquad
g=\alpha_c^{-1/2},
}
\]

and use the same generator normalization `T^a=lambda^a/2` in the continuum `SU(3)` algebra.

On the candidate same-field/same-coupling embedding

\[
\boxed{g_0=g=\alpha_c^{-1/2},}
\]

the physical continuum field corresponding to a v4.1 link coordinate is

\[
\boxed{
A_\mu^a
=\frac{2q_\mu^a}{g}
=2q_\mu^a\sqrt{\alpha_c}.
}
\]

This produces byte-equivalent local link exponents under the two generator conventions.

## 5. Non-identifiability coordinate

For a fixed holonomic coordinate `q_mu^a`, every positive candidate coupling `g_0` admits

\[
\boxed{
A_\mu^a(g_0)=\frac{2q_\mu^a}{g_0}
}
\]

and reproduces the same link.

Hence link/loop data alone leave the physical coupling normalization as an explicit free coordinate. A coupling value is selected only after one additional independently normalized physical structure is supplied.

Two admissible closures already exposed by the repository are:

1. **action normalization:** RFG4E derives the project plaquette coefficient `C_p` and tests
   \[
   C_p=2\alpha_c;
   \]
2. **matter-current / vertex normalization:** independently normalize the `g_0 A_mu^a J_a^mu` interaction on the same field convention.

Either route must freeze the field normalization before `beta_W` is promoted downstream.

## 6. Naive field-identification adversary

A direct assignment

\[
q_\mu^a=A_\mu^a
\]

combined with the exact generator map would force

\[
\boxed{g_0=2}
\]

on every nonzero component.

This provides a useful adversarial check: the holonomic link coordinate and the canonically normalized continuum gauge field cannot be silently identified component-by-component while simultaneously importing an unrelated coupling value.

## 7. Relation to `kappa`

The v4.1 script also carries the canonical information coordinate

\[
\kappa=\frac{\ln2}{24\pi}
\]

as an information-scale coordinate in a separately labelled action-density diagnostic. RFG4F keeps that information scaling distinct from the `alpha_c`/`g_0` Yang-Mills normalization path. The downstream coupling transfer uses only coordinates that pass their own normalization gates.

## 8. Downstream Wilson coupling

Once one independent normalization gate fixes

\[
g_0=\alpha_c^{-1/2},
\]

RFG3 immediately gives

\[
\boxed{
\beta_W=\frac6{g_0^2}=6\alpha_c.
}
\]

RFG4F therefore reduces the Wilson frontier to removal of one exact rescaling degeneracy rather than to reconstruction of the `SU(3)` structure itself.

## 9. Executable defects

For independently supplied `q`, `g_0`, and `A`, define

\[
\boxed{
\Delta_{link}
=\left|q-\frac{g_0A}{2}\right|.
}
\]

For a rescaled pair,

\[
\boxed{
\Delta_{rescale}
=\left|\frac{g_0A}{2}-\frac{g_0'A'}2\right|.
}
\]

A physical normalization gate must first fix either `A` or the action/current coefficient independently; only then can `g_0` be inferred.

## 10. Advancement

```text
v4.1 W_mu local SU(3) link                       upstream PASS
T^a=lambda^a/2 generator normalization           PASS EXACT
q_mu^a = g_0 A_mu^a / 2                          PASS EXACT
(g,A)->(lambda g,A/lambda) link invariance        PASS EXACT
NoParamSM alpha_c=1/g^2 source binding            SOURCE PROVENANCE PRESENT
same-field g_0=g transfer                         CONDITIONAL NORMALIZATION GATE
RFG4E action-coefficient route                    AVAILABLE
matter-current/vertex route                       OPEN ALTERNATIVE
physical beta_W                                   OPEN until degeneracy removed
```
