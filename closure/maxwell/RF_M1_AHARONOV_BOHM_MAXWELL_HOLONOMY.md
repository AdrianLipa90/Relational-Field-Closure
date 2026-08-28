# RF-M1 — Aharonov–Bohm Holonomy to Maxwell Curvature

Status: `EXACT_AB_NORMALIZATION / EXACT_LOCAL_HOMOGENEOUS_MAXWELL / SOURCED_ACTION_CONDITIONAL / VACUUM_COUPLING_OPEN`

## 1. Purpose

RF-M0 identified the formal similarity between an Abelian phase connection and the homogeneous Maxwell sector, but left a dimensional scaling `alpha_A` open. RF-M1 replaces that scaling candidate by the physical Aharonov–Bohm connection already present in the admitted phase-Hamiltonian source.

The source-level electromagnetic phase connection is

\[
\boxed{
\mathfrak a_{AB}:=\frac{q}{\hbar}A,
\qquad
A=A_\mu dx^\mu,
}
\]

with closed-loop phase

\[
\boxed{
\phi_{AB}[C]=\oint_C\mathfrak a_{AB}
=\frac{q}{\hbar}\oint_C A
\quad (\mathrm{mod}\ 2\pi).
}
\]

For `q != 0`, the physical four-potential normalization is therefore fixed by

\[
\boxed{A=\frac{\hbar}{q}\mathfrak a_{AB}.}
\]

No independent field-rescaling parameter is required at this gate.

## 2. Curvature reconstruction from infinitesimal AB holonomy

Define the dimensionless AB curvature

\[
\boxed{\mathfrak f_{AB}:=d\mathfrak a_{AB}.}
\]

Because `q/hbar` is constant for a fixed probe species,

\[
\mathfrak f_{AB}
=\frac{q}{\hbar}dA.
\]

Define the electromagnetic field-strength two-form

\[
\boxed{F:=dA.}
\]

Then exactly

\[
\boxed{
F=\frac{\hbar}{q}\mathfrak f_{AB}.
}
\]

For a smooth gauge patch and a contractible loop `C=partial Sigma`, Stokes gives

\[
\boxed{
\phi_{AB}[\partial\Sigma]
=\frac{q}{\hbar}\int_\Sigma F.
}
\]

Thus infinitesimal AB Wilson-loop data recover the local electromagnetic curvature. Finite noncontractible AB holonomy may remain nontrivial even when `F=0` along the particle path; this is retained as global bundle information rather than collapsed into a local field value.

## 3. Gauge convention synchronized with IDT 01AC

IDT 01AC uses the local `U(1)` convention

\[
\vartheta' = \vartheta+\lambda,
\qquad
\mathcal A' = \mathcal A-d\lambda,
\qquad
\mathcal D_\mu=\partial_\mu+i\mathcal A_\mu.
\]

RF-M1 therefore fixes the electromagnetic gauge parameterization to the same sign convention. Let

\[
\boxed{
A' = A-d\Lambda,
\qquad
\lambda:=\frac{q}{\hbar}\Lambda.
}
\]

Then

\[
\boxed{
\mathfrak a_{AB}'
=\mathfrak a_{AB}-d\lambda,
}
\]

and a charged phase section transforms as

\[
\boxed{
\psi'=e^{i\lambda}\psi,
\qquad
\vartheta'=\vartheta+\lambda.
}
\]

Consequently

\[
\boxed{
\mathcal D_\mu\psi
=(\partial_\mu+i\mathfrak a_{AB,\mu})\psi
}
\]

transforms covariantly and the phase one-form

\[
\boxed{
d\vartheta+\mathfrak a_{AB}}
\]

is invariant. This is the same convention already used by the total ABE connection in IDT 01AC.

The alternative parameterization `A -> A+dLambda` is physically equivalent after `Lambda -> -Lambda`, but it is not used inside the RFC↔IDT interface because mixing the two parameterizations obscures the current sign.

Since

\[
F'=dA'=dA-d^2\Lambda=F,
\]

and for a closed contractible loop

\[
\oint_C A'=\oint_C A-\oint_Cd\Lambda=\oint_C A,
\]

the local curvature and closed-loop AB phase are gauge invariant. Large gauge transformations may change a phase representative by an integer multiple of `2pi`; the Wilson factor remains the appropriate global observable.

## 4. Homogeneous Maxwell theorem

Since

\[
F=dA,
\]

nilpotency of the exterior derivative gives

\[
\boxed{dF=d^2A=0.}
\]

In components,

\[
\boxed{\nabla_{[\alpha}F_{\beta\gamma]}=0}
\]

for a torsion-free connection. Under the standard 3+1 electromagnetic decomposition this is equivalent locally to

\[
\boxed{\nabla\cdot\mathbf B=0,}
\]

\[
\boxed{\partial_t\mathbf B+\nabla\times\mathbf E=0.}
\]

Therefore the homogeneous Maxwell sector follows exactly from the admitted AB four-potential connection plus ordinary differential geometry.

This theorem is local on regular gauge patches. Singular defects or nontrivial bundle topology require patchwise potentials while retaining a globally defined curvature where the bundle connection is regular.

## 5. Wilson-loop / plaquette form

The Abelian Wilson factor is

\[
\boxed{
W[C]=\exp\!\left(i\frac{q}{\hbar}\oint_C A\right).
}
\]

For an infinitesimal oriented plaquette with area bivector `Sigma^{mu nu}`,

\[
\boxed{
W[C]
=\exp\!\left[
 i\frac{q}{2\hbar}F_{\mu\nu}\Sigma^{\mu\nu}
 +O(|\Sigma|^{3/2})
\right].
}
\]

This is the natural executable holonomy observable for a later PNCS loop: local curvature is audited by closed-path phase rather than by a gauge-dependent potential value.

## 6. Sourced Maxwell gate

AB holonomy determines the connection normalization and homogeneous curvature identity. A sourced field equation requires a dynamical action.

Admit a local parity-even, gauge-invariant, lowest-derivative Abelian field action coupled to a conserved current,

\[
\boxed{
S_{EM}[A,J]
=\int d^4x\sqrt{-g}
\left[
-\frac{1}{4\mu_*}F_{\mu\nu}F^{\mu\nu}
-J^\mu A_\mu
\right].
}
\]

Here `mu_* > 0` is kept explicit as the vacuum field normalization/coupling coordinate.

Variation with respect to `A_nu` gives

\[
\boxed{
\nabla_\mu F^{\mu\nu}=\mu_*J^\nu.
}
\]

Gauge invariance of the current coupling requires

\[
\boxed{\nabla_\mu J^\mu=0.}
\]

Equivalently, current conservation follows as the compatibility condition of the sourced equation with antisymmetry of `F` on the admitted torsion-free metric connection.

The structural equation is therefore fixed once this action class is admitted. The numerical identification of `mu_*` with a chosen electromagnetic unit convention remains an empirical normalization gate.

## 7. Electromagnetic stress-energy bridge to Einstein closure

Varying the same field action with respect to the metric gives

\[
\boxed{
T^{EM}_{\mu\nu}
=\frac{1}{\mu_*}
\left(
F_{\mu\alpha}F_\nu{}^\alpha
-\frac14 g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}
\right).
}
\]

In four dimensions its vacuum trace vanishes:

\[
\boxed{T^{EM\,\mu}{}_{\mu}=0.}
\]

On the sourced Maxwell equation, the field stress-energy exchange is

\[
\nabla^\mu T^{EM}_{\mu\nu}
=-F_{\nu\lambda}J^\lambda,
\]

so field plus charged matter can form a conserved total stress-energy tensor after the corresponding matter exchange term is admitted.

This supplies a concrete Maxwell-side input to the later Einstein–Bianchi gate.

## 8. Relation to RF-M0 and IDT 01AC

RF-M0 used a generic Abelian/Berry curvature candidate and therefore required

\[
A^{EM}=\alpha_A\mathcal A.
\]

RF-M1 instead uses the physically typed AB component of the combined phase connection:

\[
\boxed{
\mathfrak a_{AB}=\frac{q}{\hbar}A.
}
\]

The synchronized gauge convention is

\[
\boxed{
\vartheta' = \vartheta+\lambda,
\qquad
\mathfrak a_{AB}'=\mathfrak a_{AB}-d\lambda,
\qquad
\mathcal D=d+i\mathfrak a_{AB}.
}
\]

Therefore the potential normalization is inherited from the AB phase coupling itself and the electromagnetic component can enter the same gauge-covariant phase-current interface used by IDT 01AC. Berry and Euler connections remain separately typed contributions to the total ABE phase connection.

## 9. Promotion contract

Exact at RF-M1:

- AB connection normalization `a_AB=(q/hbar)A` for nonzero admitted probe charge;
- curvature recovery `F=(hbar/q)d a_AB`;
- local Stokes relation between AB loop phase and flux;
- synchronized IDT/RFC gauge convention `A -> A-dLambda`, `theta -> theta+(q/hbar)Lambda`;
- gauge invariance of `F` and closed-loop AB phase;
- homogeneous Maxwell identity `dF=0`;
- local 3+1 homogeneous equations after the standard field decomposition.

Conditional on the admitted lowest-derivative Maxwell action:

- sourced equation `nabla_mu F^{mu nu}=mu_* J^nu`;
- current conservation;
- electromagnetic stress-energy tensor and its exchange law.

Open downstream coordinates:

- exact variation-level binding between the IDT 01AC phase current and electromagnetic source current;
- empirical/vacuum normalization `mu_*` in the chosen unit system;
- physical binding of the RFC conserved carrier to the common phase/electric current;
- charged-matter action completing total stress-energy conservation;
- Einstein coupling normalization and RF-N1C Newton-limit value of `G`;
- global bundle/singularity sectors beyond regular local patches.
