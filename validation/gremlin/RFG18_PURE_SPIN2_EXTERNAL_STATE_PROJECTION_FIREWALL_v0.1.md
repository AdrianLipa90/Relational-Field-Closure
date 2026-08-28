# RFG18 — Pure Spin-2 External-State Projection Firewall

Status: `EXACT_TRANSVERSE_STATE_DECOMPOSITION / PURE_SPIN2_EXTERNAL_PROJECTOR_PASS / PROJECT_DOUBLE_COPY_SPECTRUM_TYPED / EINSTEIN_EXTERNAL_STATE_GATE_PASS`

RFG18 consumes the project four-point double-copy construction of RFG16 and the G-free coupling holonomy of RFG17. Its purpose is to type the external state space before the project amplitude is identified with the Einstein spin-2 branch.

## 1. Physical transverse tensor product

For one massless momentum, each Yang–Mills copy contributes a two-dimensional physical transverse polarization space. Let

\[
M_{ab}=\varepsilon_a\widetilde\varepsilon_b,
\qquad a,b=1,2.
\]

Define

\[
S=\frac12(M+M^T),
\qquad
B=\frac12(M-M^T),
\]

\[
\phi=\frac12\operatorname{tr}(S)I_\perp,
\qquad
h^{(2)}=S-\phi.
\]

Then exactly

\[
\boxed{M=h^{(2)}+B+\phi}
\]

with pairwise orthogonal sectors under the transverse Frobenius inner product. The dimensions are

\[
\boxed{2\otimes2=2_{\rm sym,traceless}\oplus1_{\rm antisym}\oplus1_{\rm trace}.}
\]

The Einstein external-state branch is the symmetric traceless sector

\[
\boxed{h^{(2)}\in \mathrm{Sym}^2_0(T_\perp).}
\]

The complementary antisymmetric and trace sectors remain explicitly typed as separate double-copy states.

## 2. Canonical transverse basis

For an orthonormal transverse pair `(e_x,e_y)`, define

\[
h_+=\frac{e_x\otimes e_x-e_y\otimes e_y}{\sqrt2},
\]

\[
h_\times=\frac{e_x\otimes e_y+e_y\otimes e_x}{\sqrt2},
\]

\[
B_\perp=\frac{e_x\otimes e_y-e_y\otimes e_x}{\sqrt2},
\]

\[
\phi_\perp=\frac{e_x\otimes e_x+e_y\otimes e_y}{\sqrt2}.
\]

These four tensors form an orthonormal basis of the physical `2 x 2` tensor-product space. `h_+` and `h_x` span the two spin-2 polarizations.

A factorized self-copy state illustrates why this projection is required:

\[
\boxed{
e_x\otimes e_x
=\frac{h_++\phi_\perp}{\sqrt2}.
}
\]

Thus a generic factorized product contains typed components from more than one transverse sector. The Einstein branch is selected by the symmetric-traceless projector rather than by factorization alone.

## 3. Four-dimensional lift

For each external momentum `k`, RFG18 uses the same transverse basis already admitted by the RFG16 kinematics. The lifted spin-2 tensors obey

\[
k^\mu h^{(2)}_{\mu\nu}=0,
\qquad
h^{(2)}_{\mu\nu}k^\nu=0,
\]

\[
h^{(2)}_{\mu\nu}=h^{(2)}_{\nu\mu},
\qquad
\eta^{\mu\nu}h^{(2)}_{\mu\nu}=0.
\]

These are checked directly for both `h_+` and `h_x` over a deterministic set of scattering angles.

## 4. Projected project amplitude

RFG16 supplies a double-copy core that is multilinear in the polarization vectors of each copy. Therefore a projected tensor state is evaluated by linear superposition of the corresponding factorized double-copy terms.

For example,

\[
\mathcal M_4[h_+,\ldots]
=\frac1{\sqrt2}
\left(
\mathcal M_4[e_x\otimes e_x,\ldots]
-
\mathcal M_4[e_y\otimes e_y,\ldots]
\right)
\]

on each projected external leg, with the product expansion applied independently to all legs.

## 5. Linearized diffeomorphism Ward gate

A pure-gauge symmetric tensor deformation has the form

\[
\delta h_{\mu\nu}
=k_\mu\xi_\nu+\xi_\mu k_\nu.
\]

Each term contains one Yang–Mills copy whose polarization is replaced by its momentum. RFG16 already verifies the Ward identity independently in either copy. Consequently the projected amplitude obeys

\[
\boxed{
\mathcal M_4[\delta h, h_2,h_3,h_4]=0
}
\]

for every external leg on the admitted four-point kinematic surface.

## 6. Executable validation

The reference test checks:

1. exact reconstruction of 1000 random transverse `2 x 2` tensors into spin-2, antisymmetric and trace sectors;
2. pairwise orthogonality of all three sectors;
3. orthonormality of the `(h_+, h_x, B, phi)` basis;
4. idempotence of the spin-2 projection and annihilation of the complementary basis sectors;
5. transverse, symmetric and traceless four-dimensional lift of the spin-2 states;
6. the projected four-point linearized-diffeomorphism Ward gate using the actual RFG16 numerator construction.

Local result:

```text
6 passed, 0 failed
```

## 7. Advancement

```text
RFG16 project double copy                         PASS
RFG17 G-free coupling holonomy                    PASS EXACT ALGEBRAIC
2x2 transverse tensor decomposition               PASS EXACT
spin-2 symmetric-traceless projector              PASS EXACT
external h_+, h_x transversality/trace            PASS REFERENCE
projected four-point diffeomorphism Ward gate     PASS REFERENCE
Einstein external-state branch                    ADMITTED AT FOUR POINTS
higher-point spin-2 projection                    OPEN
internal-state / loop spectrum audit              OPEN
```

The project double-copy state space is therefore explicitly typed before promotion of the spin-2 Einstein branch. The four-point Einstein external-state gate is the symmetric-traceless projected sector with the same `kappa_E` normalization established by RFG16/RFG17.