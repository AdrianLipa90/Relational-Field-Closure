# RF-GSC3H — 3+1 Two-Epoch Dissociation/Association Constructor v0.13

Status: \`CANDIDATE_ONLY / EXACT_LINEAR_TWO_EPOCH_CHANGE_OF_COORDINATES / EXTERNAL_ARCHIVE_MODEL_LEVEL_BINDING / PHYSICAL_PRODUCTION_CLAIM_FALSE / CANON_ALLOWED_FALSE\`

Date: 2026-09-19

## 1. Purpose

This candidate isolates an exact constructor already implicit in the archived SP3 observational E2E.

For each observed entity \(s\) and epoch \(a\in\{1,2\}\), the source record is a literal \(3+1\) tuple

\[
y_s^{(a)}
=
(\mathbf x_s^{(a)},c_s^{(a)})
\in
\mathbb R^3\oplus\mathbb R,
\]

where \(\mathbf x=(x,y,z)\) is the spatial position and \(c\) is the source clock coordinate.

The mnemonic label "dissociate 3+1, associate by /2" is treated here only as a compact name for an exact linear transformation. It is not used as physical evidence by itself.

## 2. Exact two-epoch transform

For \(\Delta t\neq0\), define

\[
\boxed{
\bar y_s=\frac{y_s^{(1)}+y_s^{(2)}}{2}
}
\]

and

\[
\boxed{
\dot y_s=\frac{y_s^{(2)}-y_s^{(1)}}{\Delta t}.
}
\]

Componentwise,

\[
\bar y_s=(\bar{\mathbf x}_s,\bar c_s),
\qquad
\dot y_s=(\boldsymbol\beta_s,\dot c_s).
\]

The inverse is exact:

\[
\boxed{
y_s^{(1)}=\bar y_s-\frac{\Delta t}{2}\dot y_s,
\qquad
y_s^{(2)}=\bar y_s+\frac{\Delta t}{2}\dot y_s.
}
\]

Hence no information is lost by the change of coordinates.

For one scalar component the transform matrix is

\[
M=
\begin{pmatrix}
1/2 & 1/2\\
-1/\Delta t & 1/\Delta t
\end{pmatrix},
\qquad
\det M=\frac1{\Delta t}.
\]

For all four \(3+1\) components independently,

\[
\boxed{
\det M_{3+1}=\left(\frac1{\Delta t}\right)^4\neq0.
}
\]

Thus the two-epoch \(3+1\) source and the midpoint+tangent representation are exactly equivalent whenever \(\Delta t\neq0\).

## 3. Existing SP3 realization

The current archived candidate source is

\`RT218283.SP3@8013\`

at epochs

\`2015-01-21T00:01:00Z\`

and

\`2015-01-21T00:03:00Z\`

with \(\Delta t=120\,\mathrm{s}\).

The existing implementation

\`experiments/toe_solver_candidate_v0_1/igs_sp3_observational_e2e_v0_11.py\`

already uses the same source records to derive three surfaces:

1. clock/lapse packet from the clock-coordinate difference;
2. spatial carrier from the observed node set and two-epoch midpoint geometry;
3. inter-leaf matching packet from the spatial difference divided by \(\Delta t\).

Explicitly,

\[
\boldsymbol\beta_s
=
\frac{\mathbf x_s^{(2)}-\mathbf x_s^{(1)}}{\Delta t},
\]

while the field-fit position uses

\[
\bar{\mathbf x}_s
=
\frac{\mathbf x_s^{(1)}+\mathbf x_s^{(2)}}{2}.
\]

The clock branch similarly uses

\[
\dot c_s
=
\frac{c_s^{(2)}-c_s^{(1)}}{\Delta t}
\]

with the SP3 clock-unit conversion retained by the existing clock packet.

## 4. Same-parent association

The current E2E computes one realization identifier from the complete frozen source record:

\[
R
=
\texttt{physical:igs-sp3:sha256:}
\;H(\text{source records}).
\]

The clock, spatial and matching packet constructors all consume that same parent record and carry the same identifier.

Therefore the exact source-level statement is

\[
\boxed{
S
\xrightarrow{\pi_{\rm clock},\pi_{\rm space},\pi_{\rm match}}
(C,P,M),
\qquad
R(C)=R(P)=R(M)=H(S),
}
\]

where \(S\) denotes the frozen two-epoch source.

This is stronger than manually assigning the same identifier after independent construction: all three packet surfaces are deterministic projections of one source parent.

## 4A. Data-defined affine 4-simplex

The five satellite midpoint records are five points in the same \(3+1\) affine carrier:

\[
\bar y_{\mathrm{G01}},\ldots,\bar y_{\mathrm{G05}}\in\mathbb R^4.
\]

Using \(\bar y_{\mathrm{G01}}\) as affine origin, form the \(4\times4\) difference matrix

\[
D=
\big[
\bar y_{\mathrm{G02}}-\bar y_{\mathrm{G01}},
\ldots,
\bar y_{\mathrm{G05}}-\bar y_{\mathrm{G01}}
\big].
\]

For the frozen SP3 decimals the determinant is exactly

\[
\boxed{
\det D=
-\frac{
13977020116417867310346922964392497592033
}{
1600000000000000000000000
}
\neq0.
}
\]

Hence the five observed midpoint events are affinely independent and determine a unique nondegenerate affine 4-simplex.

The boundary of a 4-simplex has exactly five tetrahedral facets, obtained by omitting one of its five vertices. The existing \`spatial_packet()\` constructs exactly those five four-vertex subsets.

Therefore, at the candidate level,

\[
\boxed{
\text{five observed }(3+1)\text{ midpoint events}
\Longrightarrow
\text{data-defined affine 4-simplex}
\Longrightarrow
\partial\Delta^4
}
\]

with no additional tetrahedral-incidence choice.

This rejects the earlier assumption that the particular boundary-of-a-4-simplex incidence in the SP3 candidate was arbitrary. It does **not** by itself prove that this finite simplicial boundary is the global physical spatial manifold.

Affine independence is unchanged by any nonzero rescaling of the clock coordinate, so the rank statement does not depend on a particular positive clock-unit conversion.

## 5. Relation to the TIR 3+1 half-lift

TIR separately contains the exact local carrier decomposition

\[
\operatorname{Herm}(2)
=
\mathbb R I\oplus\operatorname{Herm}_0(2),
\qquad
\dim_{\mathbb R}=1+3,
\]

and the normalized-state lift

\[
\rho
=
\frac12(I+\mathbf r\cdot\boldsymbol\sigma),
\qquad
X=\ell\rho.
\]

Hence

\[
x^0=\frac{\ell}{2},
\qquad
x^i=\frac{\ell}{2}r_i.
\]

The present SP3 constructor and the TIR Hermitian half-lift therefore contain an exact shared algebraic motif: a \(3+1\) carrier together with a factor \(1/2\).

No theorem in this candidate identifies the SP3 coordinate tuple with the TIR Hermitian event carrier. That remains a separate cross-repository physical binding.

## 6. Relation to Collatz

TIR Stage 48 independently freezes the ordinary Collatz branch alphabet

\[
O:n\mapsto3n+1,
\qquad
E:n\mapsto n/2.
\]

This is another exact occurrence of the mnemonic sequence \(3n+1\) and halving.

The present candidate does **not** identify the two-epoch linear transform with Collatz dynamics. The Collatz correspondence is recorded only as an independent structural rhyme until an explicit intertwiner is derived.

## 7. Evidence boundary

The source is an external observational archive. The new v0.13 audit sharpens the old v0.12 typing:

- the clock quantities are archive-derived;
- the five midpoint \(3+1\) events determine the affine 4-simplex exactly;
- its five tetrahedral boundary facets are therefore data-determined rather than freely chosen;
- the matching tangent field is archive-derived while the overlap binding remains a model surface;
- the fitted metric and numerical Bianchi checks remain model-derived.

Therefore:

\`\`\`text
external source archive                         PRESENT
3+1 tuple per epoch                             EXACT SOURCE FORMAT
two-epoch midpoint/tangent transform            EXACT / INVERTIBLE
five midpoint events affine rank                4 / EXACT
4-simplex boundary incidence                    DATA-DETERMINED
same-parent packet projection                   EXECUTABLE
clock/spatial/matching common realization hash  EXECUTABLE
global physical spatial-manifold binding        OPEN
full physical 3+1 production capture            OPEN
physical production claim                       FALSE
canon allowed                                   FALSE
\`\`\`

The mnemonic may guide the constructor. It cannot by itself promote the finite archive-derived construction into a global physical-production claim.
