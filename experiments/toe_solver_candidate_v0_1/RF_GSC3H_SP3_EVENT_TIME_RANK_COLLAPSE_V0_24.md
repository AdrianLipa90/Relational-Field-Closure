# RF-GSC3H — SP3 Physical Event-Time Rank Collapse v0.24

Status: CANDIDATE_ONLY / EXACT_EVENT_TIME_SUBSTITUTION_RANK_COLLAPSE / RELATIONAL_MIDPOINT_NEQ_TRAJECTORY_MIDEVENT / CLOCK_CORRECTION_FEATURE_NEQ_EVENT_TIME_REINFORCED / PHYSICAL_S3_IDENTITY_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.13–v0.15 obtain a nondegenerate affine four-simplex and a smooth \(S^3\)-like carrier from five four-component **relational midpoint** records

\[
y_s
=
\left(
\frac{\mathbf X_s^{(1)}+\mathbf X_s^{(2)}}2,
c\,\frac{\delta t_{{\rm clock},s}^{(1)}+\delta t_{{\rm clock},s}^{(2)}}2
\right).
\]

The fourth component is an SP3 clock-correction feature converted to length units.

The source file also contains an actual record at the physical midpoint epoch 00:02. Therefore the relational midpoint can be compared directly with the physical mid-epoch trajectory event.

## 2. Relational midpoint is not the physical mid-epoch event

The frozen source epochs are

\[
t_1=\text{2015-01-21T00:01:00Z},
\qquad
t_2=\text{2015-01-21T00:03:00Z},
\]

with actual source records also present at

\[
\boxed{
t_\star=\text{2015-01-21T00:02:00Z}.
}
\]

Define the relational spatial midpoint

\[
\mathbf M_s
=
\frac{\mathbf X_s^{(1)}+\mathbf X_s^{(2)}}2
\]

and the actual physical mid-epoch position

\[
\mathbf P_s^\star
=
\mathbf X_s(t_\star).
\]

For all five frozen satellites,

\[
\boxed{
\mathbf M_s\ne\mathbf P_s^\star.
}
\]

The discrepancy is of order \(0.7\)–\(0.85\) km for this 120-second chord.

Therefore

\[
\boxed{
M=\frac{A+B}{2}
}
\]

must be interpreted as the affine/relational centre of the endpoint pair, not automatically as a third physical event lying on the actual trajectory at the midpoint time.

This distinction is fully compatible with the causal-pair theorem.

## 3. Actual common-time physical events

The five actual source records at \(t_\star\) are

\[
\widehat y_s
=
(\mathbf P_s^\star,c\,t_\star).
\]

All five share the same physical event time.

Hence for any affine base point \(s_0\),

\[
\widehat y_s-\widehat y_{s_0}
=
(\mathbf P_s^\star-\mathbf P_{s_0}^\star,0).
\]

The fourth component of every affine-difference vector is exactly zero.

Therefore the four-dimensional affine determinant satisfies

\[
\boxed{
\det D_4=0.
}
\]

Thus

\[
\boxed{
\operatorname{affrank}
\{\widehat y_s\}
\le3.
}
\]

The actual 00:02 spatial positions have affine rank three, so

\[
\boxed{
\operatorname{affrank}
\{\widehat y_s\}
=3.
}
\]

## 4. Contrast with the feature-derived v0.13 lift

The v0.13/v0.15 carrier does not use the common event time as its fourth coordinate.

It uses the satellite-dependent clock-correction feature.

For the same five source identities, that feature lift has nonzero four-dimensional affine determinant and therefore affine rank four.

Hence

\[
\boxed{
(\mathbf P^\star,\text{common physical event time})
\Rightarrow
\text{rank }3,
}
\]

while

\[
\boxed{
(\mathbf M,\text{SP3 clock-correction feature})
\Rightarrow
\text{rank }4.
}
\]

## 5. Consequence for the /2 interpretation

The factor \(1/2\) remains exact and unique for endpoint centring:

\[
M=\frac{A+B}{2},
\qquad
H=\frac{B-A}{2}.
\]

But the pair centre \(M\) is an affine relation variable.

For a curved physical trajectory,

\[
\boxed{
M
\ne
\gamma\!\left(\frac{t_1+t_2}{2}\right)
}
\]

in general.

The SP3 source gives a direct finite witness of this distinction.

Therefore the earlier causal theorem should be read as a theorem about the **binary relation representation**, not as a claim that the affine midpoint is itself an observed midpoint event.

## 6. Physical interpretation firewall

The fourth direction responsible for the v0.15 rank-four closure is not supplied by common physical event time.

Earlier validation also rejects direct identification of raw SP3 clock correction with the physical event-trace scale.

Therefore the v0.15 fourth feature axis cannot be promoted to physical time by relabelling.

Likewise, the \(S^3\)-like carrier cannot be promoted to the physical spatial manifold merely because it contains the five feature-derived relation centres.

## 7. Production consequence

The physical product-domain gate from v0.22 still requires an independent full-domain binding

\[
\Phi_\Sigma:
|\Sigma_{\rm prod}|\to\mathcal E_Q.
\]

Neither of the following is sufficient:

1. the five relational midpoint anchors alone;
2. replacing the feature axis by physical event time.

## 8. Main result

For the frozen SP3 source:

\[
\boxed{
\text{actual same-time physical records have affine rank }3,
}
\]

whereas

\[
\boxed{
\text{the relation-centre plus clock-correction feature lift has affine rank }4.
}
\]

Additionally,

\[
\boxed{
\text{relational midpoint}
\ne
\text{actual mid-epoch trajectory event}
}
\]

for all five source satellites.

## 9. Evidence boundary

Exact/source-derived:

- actual 00:02 records from the same immutable SP3 revision;
- common physical midpoint epoch;
- zero event-time difference across the five same-epoch records;
- rank-four determinant exactly zero for the physical same-time lift;
- spatial affine rank exactly three;
- nonzero separation between relational chord midpoint and actual mid-epoch position.

Previously validated parent:

- clock-correction-feature relation-centre lift has affine rank four;
- raw SP3 clock correction is not physical event-trace time.

Still open:

- nonlinear physical spatial binding to \(\mathcal E_Q\);
- full-domain physical product realization;
- physical interpretation, if any, of the clock-correction feature inside the candidate carrier.
