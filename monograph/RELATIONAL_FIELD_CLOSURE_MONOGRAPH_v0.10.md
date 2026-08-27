# Relational Field Closure
## Hexahedral Spacetime, Relational Lapse, Newton Source Operator and Source-Type Firewall

**Working monograph v0.10 — 27 August 2026**  
**Status:** `EXACT_LOCAL_METRIC_CONNECTION_LAPSE_KINEMATICS_AND_SOURCE_OPERATOR / SOURCE_TYPE_IDENTIFIABILITY_FIREWALL_PASS / SOURCE_OCCUPATION_AND_G_NORMALIZATION_OPEN`

## Abstract

RFC now carries a continuous derivation chain from projective/spinorial geometry and IDT clock dynamics to a local Lorentzian spacetime, a relational lapse, the Newton-facing force-law kinematics, and an independently obtained isotropic Laplace source operator. RF-N1B adds a source-type firewall: it separates the already-admitted relational density variable from a physical mass-density source, derives the unique dimensional form of a cell mass-density candidate once an independent occupation number and physical cell measure are supplied, and converts the Newton target into a universality condition rather than a fitted coupling.

The present frontier is therefore sharply typed. The operator side is locally closed:

\[
\Delta_h \Phi_R=c^2\mathcal S_R,
\qquad
\Phi_R=c^2\ln N_R.
\]

The source side requires an independently derived conserved source carrier/occupation map. Only after that map is admitted can RFC test the target normalization

\[
c^2\mathcal S_R\stackrel{?}{=}4\pi G\rho_m.
\]

`G` remains an open downstream normalization in the current dependency graph.

## 1. Derivation firewall

RFC treats Einstein, Maxwell and Newton equations as downstream validation oracles. The active Newton chain is

\[
\boxed{
\text{IDT clock ratio}
\rightarrow N_R
\rightarrow \Phi_R=c^2\ln N_R
\rightarrow \text{weak force-law kinematics}
}
\]

and independently

\[
\boxed{
\text{IDT Shannon--Onsager response}
+\text{TIR six-ray hexahedral symmetry}
\rightarrow \Delta_h.
}
\]

RF-N1B keeps the right-hand source map independent from this operator derivation.

## 2. Spatial carrier and physical cell scale

The regular hexahedral dual frame supplies the six signed directions

\[
\mathcal H^\star=\{\pm e_1,\pm e_2,\pm e_3\}
\]

with isotropic aggregate projective metric

\[
\boxed{h_H=\frac16 I_3.}
\]

IDT phase-clock calibration supplies

\[
\ell_\varphi=\frac{c}{|\omega|}=\frac{\hbar c}{E},
\]

hence the regular physical cell scale

\[
\boxed{
a_H=\frac{\ell_\varphi}{\sqrt6}
=\frac{c}{\sqrt6|\omega|}.}
\]

For the present local regular-cell audit define

\[
\boxed{V_H:=a_H^3.}
\]

The physical interpretation of this local cell volume as a source-support measure is a separate admission gate; RF-N1B uses it conditionally to expose the missing source variable.

## 3. Relational lapse and Newton-facing potential

IDT exports the positive clock ratio

\[
\boxed{N_R=\frac{d\tau_x}{d\tau_{\rm ref}}
=\frac{\phi_x}{\phi_{\rm ref}}>0.}
\]

After physical clock calibration the local static metric carrier is

\[
\boxed{
g_R=-N_R^2c^2dt^2+h_\perp.}
\]

The derived logarithmic lapse variable

\[
\boxed{u:=\ln N_R}
\]

defines

\[
\boxed{\Phi_R:=c^2u=c^2\ln N_R.}
\]

Near the reference-clock sector, slow-motion geodesic kinematics gives

\[
\boxed{a^i=-\partial^i\Phi_R+\cdots.}
\]

## 4. Independent Laplace operator gate

IDT detailed-balance Shannon--Onsager response has the graph form

\[
G^{(2)}_\pi=(\ln2)D^T\operatorname{diag}[c_{ab}\Lambda(r_a,r_b)]D.
\]

On the regular six-neighbour hexahedral cell graph,

\[
(L_Hf)(x)=\sum_{i=1}^{3}
\left[2f(x)-f(x+a_He_i)-f(x-a_He_i)\right].
\]

The physical continuum-sign operator is

\[
\boxed{\Delta_H^{(a)}=-\frac{L_H}{a_H^2}}
\]

with expansion

\[
\boxed{
\Delta_H^{(a)}f
=\Delta f+
\frac{a_H^2}{12}\sum_i\partial_i^4f+O(a_H^4).
}
\]

Signed-permutation symmetry independently removes first-order drift and off-diagonal second derivatives, enforces equal diagonal coefficients, and the constant-null condition removes the zeroth-order term. The leading local scalar second-order operator is therefore proportional to `Delta`; the normalized physical stencil fixes the principal coefficient to one.

Thus the active source equation is typed as

\[
\boxed{
\Delta_hu=\mathcal S_R,
\qquad
\Delta_h\Phi_R=c^2\mathcal S_R,
\qquad
[\mathcal S_R]=L^{-2}.
}
\]

## 5. Why relational density and mass density remain distinct

The upstream IDT kinetic variable `rho_R` enters the symmetric mobility

\[
\boxed{
M_{ab}=\frac{\sqrt{\rho_R(a)\rho_R(b)}}
{\tfrac12[\eta_R(a)+\eta_R(b)]}.
}
\]

At this gate its admitted role is therefore relational transition mobility. No independent upstream receipt yet supplies a map

\[
\rho_R\longrightarrow \rho_m
\]

with physical mass-density units and source conservation. RFC accordingly keeps the two types distinct.

The author/formalism may suggest a later relation between relational density and matter density, yet does not state such an identification as an established result at RF-N1B.

## 6. Energy scale is available, occupation is not yet fixed

The phase-clock gate already supplies

\[
\boxed{E=\hbar|\omega|.}
\]

An energy scale alone is insufficient to define a density. Introduce an independent dimensionless source occupation `n_E` for a regular local cell. Conditional on the physical cell measure `V_H=a_H^3`, define

\[
\boxed{
\rho_{\rm cell}
:=\frac{n_EE}{c^2V_H}.
}
\]

Substituting

\[
E=\hbar|\omega|,
\qquad
a_H=\frac{c}{\sqrt6|\omega|}
\]

gives the exact dimensional identity

\[
\boxed{
\rho_{\rm cell}
=6\sqrt6\,n_E
\frac{\hbar|\omega|^4}{c^5}.
}
\]

Indeed

\[
\left[\frac{\hbar\omega^4}{c^5}\right]
=M L^{-3}.
\]

This is a typed conditional cell-density candidate. Promotion to physical matter density requires an independently derived conserved occupation/current and an admitted physical support measure.

## 7. Information curvature remains a candidate source basis

The TIR×IDT information-curvature scalar has the required inverse-area type,

\[
\boxed{
\Xi_I=\frac{\mathcal J_\pi}{\mathcal A_{rel}},
\qquad [\Xi_I]=L^{-2}.
}
\]

For a constant-rate projective cell,

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{\omega}{c}\right)^2.
}
\]

Bounded GREMLIN retains only the candidate basis

\[
\boxed{\mathcal S_R=\beta_I\Xi_I+\cdots}
\]

with `beta_I` unfitted and unpromoted. Spatial `R^(3)` remains quarantined as a primary independent Newton source because it would recycle the geometry being solved; derivative self-terms remain higher-order candidates.

## 8. Newton target converted into a universality condition

Take only the conditional test pair

\[
\mathcal S_R=\beta_I\Xi_I,
\qquad
\rho_m\rightsquigarrow \rho_{\rm cell}.
\]

The Newton target

\[
c^2\mathcal S_R=4\pi G\rho_m
\]

then requires

\[
\beta_I\frac{\mathcal J_\pi}{a_{FS}}
\omega^2
=
24\pi\sqrt6\,G\,n_E
\frac{\hbar\omega^4}{c^5}.
\]

Solving algebraically for the target normalization gives

\[
\boxed{
G_{\rm target}
=
\frac{\beta_I\mathcal J_\pi}
{24\pi\sqrt6\,n_Ea_{FS}}
\frac{c^5}{\hbar\omega^2}.
}
\]

The factor

\[
\boxed{\frac{c^5}{\hbar\omega^2}}
\]

has exactly the dimensions of Newton's constant,

\[
[G]=L^3M^{-1}T^{-2}.
\]

Therefore any future derivation in this candidate channel must establish a source-independent invariant combination

\[
\boxed{
\mathcal U_G
:=
\frac{\beta_I\mathcal J_\pi}
{n_Ea_{FS}\omega^2}
}
\]

with the required universal value. A source-dependent `U_G` would falsify this candidate route to a universal `G`.

This converts a free normalization problem into an explicit cross-source universality test.

## 9. Constructive source-type non-identifiability theorem

The current premises admit multiple source assignments compatible with the already-derived left-hand operator and lapse kinematics. For example, different positive occupations `n_E` produce distinct candidate densities while leaving the operator construction unchanged. Likewise the mobility variable `rho_R` can be varied independently of a chosen physical occupation map unless an additional constitutive/conservation law ties them together.

Hence the present upstream set leaves at least one independent degree of freedom on the source side.

**RF-N1B theorem.** Given the currently admitted RFC/TIR/IDT interfaces, the physical mass-density source is underidentified until an independent conserved source occupation/current and physical measure are supplied.

This is a constructive identifiability boundary: two admissible source assignments can share the same operator and lapse sector while yielding different mass densities.

## 10. Required next source gate

The next admissible source gate must derive at least one object of the form

\[
\boxed{J_S^\mu}
\]

or a discrete conserved occupation/current whose continuum limit can define a source measure. The minimum requirements are:

1. an explicit conservation/continuity law;
2. a map to a dimensionless occupation or number density;
3. a physical measure/volume binding;
4. an energy-to-mass conversion already calibrated independently;
5. independence from the Newton target normalization;
6. a no-refit cross-source universality test.

Only then may RFC test whether

\[
\rho_m
\]

is obtained uniquely and whether `S_R` closes onto it.

## 11. Parallel Lambda0 and Einstein implications

The same source firewall matters for dynamic `Lambda0`. The information-curvature scalar may enter a scalar invariant basis for

\[
\Lambda_0=\Lambda_0[\Xi_I,\,F_{\mu\nu}F^{\mu\nu},\,\text{matter/source invariants},\ldots],
\]

but any matter/source contribution must pass the same typing and conservation requirements. The later Einstein-Bianchi gate must then account for exchange generated by a variable `Lambda0` rather than silently impose an incompatible separately conserved matter source.

The Maxwell branch remains parallel: the geometric identity `F=dA`, `dF=0` is structurally distinct from the sourced Maxwell action/current gate.

## 12. Current frontier

The Newton branch is now factorized into four gates:

\[
\boxed{
N_R
\rightarrow
\Phi_R=c^2\ln N_R
\rightarrow
-\nabla\Phi_R
}
\]

\[
\boxed{
\text{Onsager response}
+\text{hexahedral symmetry}
\rightarrow
\Delta_h
}
\]

\[
\boxed{
\text{conserved source carrier}
\rightarrow n_E\ \text{or continuum analogue}
\rightarrow \rho_m
}
\]

and finally

\[
\boxed{
\Delta_h\Phi_R
\stackrel{?}{=}
4\pi G\rho_m.
}
\]

The first two chains have local structural receipts. RF-N1B proves why the third chain is an independent requirement and supplies the dimensional candidate once its missing occupation variable is admitted. The fourth chain is therefore a genuine downstream normalization/universality audit rather than a premise.

## 13. Status table

| Gate | Status |
|---|---|
| RF-02H hexahedral rank-3 spatial metric | `LOCAL STRUCTURAL PASS` |
| RF-G0 Lorentzian signature | `EXACT CONDITIONAL PASS` |
| RF-02I coframe connection | `LOCAL EXACT CONNECTION PASS` |
| IDT 05C relational lapse ratio | `EXACT CLOCK-RATIO PASS` |
| RF-N0 lapse geodesic kinematics | `EXACT CONDITIONAL PASS` |
| RF-N1A hexahedral source operator | `LOCAL EXACT PASS` |
| RF-N1B relational-density/mass-density firewall | `SOURCE_TYPE_IDENTIFIABILITY_FIREWALL_PASS` |
| RF-N1B conditional cell-density identity | `EXACT DIMENSIONAL IDENTITY / OCCUPATION BINDING OPEN` |
| RF-N1B `G` universality condition | `TARGET CONSISTENCY CONDITION / OPEN` |
| RF-N1B conserved source occupation/current | `OPEN` |
| RF-N1C Newton normalization | `OPEN` |
| RF-M2 sourced Maxwell | `OPEN` |
| RF-L1 dynamic Lambda0 | `OPEN` |
| RF-E1 Einstein-Bianchi closure | `OPEN` |

## 14. Next theorem target

The immediate theorem target is:

\[
\boxed{
\text{upstream conserved relational source current}
\Longrightarrow
\text{unique local occupation measure}
\Longrightarrow
\rho_m
}
\]

with no use of `4 pi G rho_m` in the derivation. If that gate closes, RFC can perform its first genuine normalization test for `G` and determine whether the candidate information-curvature source channel survives universality.