# RF-GSC3H — SP3 Physical Event-Time Rank Collapse v0.24

Status: CANDIDATE_ONLY / EXACT_EVENT_TIME_SUBSTITUTION_RANK_COLLAPSE / CLOCK_CORRECTION_FEATURE_NEQ_EVENT_TIME_REINFORCED / PHYSICAL_S3_IDENTITY_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.13–v0.15 obtain a nondegenerate affine four-simplex and a smooth \(S^3\)-like carrier from five four-component midpoint records

\[
y_s
=
\left(
\mathbf X_s,
c\,\delta t_{{\rm clock},s}
\right).
\]

The fourth component is the SP3 clock-correction feature converted to length units.

Earlier validation already rejects direct identification of that raw clock-correction feature with the physical event-trace time.

This note tests what happens if the fourth component is replaced by the actual common physical event time of the midpoint epoch.

## 2. Common physical midpoint epoch

The frozen source uses two common epochs for all five satellites:

\[
t_1=\text{2015-01-21T00:01:00Z},
\]

\[
t_2=\text{2015-01-21T00:03:00Z}.
\]

Therefore every satellite has the same physical midpoint epoch

\[
\boxed{
t_\star
=
\frac{t_1+t_2}{2}
=
\text{2015-01-21T00:02:00Z}.
}
\]

If the fourth coordinate is the actual event time, the five midpoint events are

\[
\boxed{
\widetilde y_s
=
(\mathbf X_s,c\,t_\star).
}
\]

All five therefore lie in the affine hyperplane

\[
x^0=c\,t_\star.
\]

## 3. Exact affine-rank consequence

Choose one midpoint as affine base point.

For every other midpoint,

\[
\widetilde y_s-\widetilde y_{s_0}
=
(\mathbf X_s-\mathbf X_{s_0},0).
\]

Thus the fourth component of every affine-difference vector is exactly zero.

The \(4\times4\) affine-difference determinant therefore satisfies

\[
\boxed{
\det D_4=0.
}
\]

Hence

\[
\boxed{
\operatorname{affrank}
\{\widetilde y_s\}
\le3.
}
\]

For the frozen source the spatial midpoint differences have rank three, so in fact

\[
\boxed{
\operatorname{affrank}
\{\widetilde y_s\}
=3.
}
\]

The five common-time physical midpoint events therefore do not define a nondegenerate affine four-simplex.

## 4. Contrast with the clock-correction feature lift

The existing v0.13 source lift uses

\[
y_s
=
\left(
\mathbf X_s,
c\,\delta t_{{\rm clock},s}
\right).
\]

Those five source vectors have affine rank four.

Therefore the rank-four closure depends on the satellite-dependent clock-correction feature.

Schematically,

\[
\boxed{
(\mathbf X,\text{common physical event time})
\Rightarrow
\text{rank }3,
}
\]

while

\[
\boxed{
(\mathbf X,\text{SP3 clock-correction feature})
\Rightarrow
\text{rank }4.
}
\]

## 5. Physical interpretation firewall

This result does not invalidate the four-component data construction.

It establishes that the fourth direction responsible for the nondegenerate four-simplex is not supplied merely by the common event epoch.

Therefore the resulting smooth \(S^3\)-like carrier cannot be promoted to a physical spatial manifold by saying that its fourth source coordinate is simply physical time.

That route is exactly ruled out.

## 6. Relation to the Hermitian causal-time result

The causal \(3+1\) theorem uses the physical elapsed scale

\[
\ell=c\,\Delta t
\]

in the Hermitian pair difference.

That temporal coordinate is source-owned and physically interpreted.

The v0.15 smooth-carrier construction instead uses the midpoint clock-correction feature

\[
c\,\delta t_{\rm clock}.
\]

These are different quantities and must remain separated.

Thus:

\[
\boxed{
\text{causal physical time}
\ne
\text{v0.15 carrier feature axis}
}
\]

unless an independent physical binding theorem is supplied.

## 7. Production consequence

The physical product-domain gate from v0.22 cannot be closed by relabelling the v0.15 fourth feature axis as event time.

A production spatial-carrier binding must instead supply an independent map from the physical spatial realization to \(\mathcal E_Q\), with full-domain coverage and provenance.

## 8. Main no-go statement

For the frozen five-source two-epoch SP3 realization,

\[
\boxed{
\text{replacing the clock-correction feature by the actual common event time collapses the midpoint affine rank from }4\text{ to }3.
}
\]

Therefore the v0.15 rank-four simplex and \(S^3\)-like carrier are feature-derived rather than direct consequences of the shared physical event epoch.

## 9. Evidence boundary

Exact:

- common source epochs;
- common midpoint event epoch;
- zero fourth component in all common-time affine differences;
- rank-four determinant equals zero;
- spatial affine rank equals three.

Previously validated parent:

- clock-correction-feature lift has affine rank four;
- raw SP3 clock correction is not physical event-trace time.

Still open:

- nonlinear physical spatial binding to \(\mathcal E_Q\);
- full-domain physical product realization;
- physical interpretation of the clock-correction feature inside the spatial carrier.
