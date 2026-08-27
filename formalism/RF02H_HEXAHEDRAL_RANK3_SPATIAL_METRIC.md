# RF-02H — Hexahedral Rank-Three Spatial Metric

Status: `EXACT_HEXAHEDRAL_RANK3_LOCAL_METRIC / PHYSICAL_SPATIAL_COFRAME_BINDING_CANDIDATE / GLOBAL_INTEGRABILITY_OPEN`

Pinned structural inputs for this stacked gate:

- TIR hexahedral branch `agent/hexahedral-bloch-frame-v0.1`, commit `a2e7003599b13a7b38c0860ecfdcf1c012780c92`;
- TIR phase-clock area lineage contained in that branch;
- IDT phase-clock branch `feat/phase-clock-length-scale-v0.1`, commit `f90435edbfbba8211e6c28cc49a7c22f8059021b`;
- RFC RF-G0 Lorentzian signature theorem;
- RFC RF-L0 phase-clock information-curvature branch ancestry.

## 1. Hexahedral dual Bloch frame

Represent one oriented regular hexahedral cell by its six outward face-normal rays,

\[
\boxed{
\mathcal H^\star
=\{\pm\mathbf e_1,\pm\mathbf e_2,\pm\mathbf e_3\}
\subset S^2_{\rm Bloch}.
}
\]

Equivalently the corresponding pure qubit density matrices are

\[
\rho_{i,\pm}=\frac12(I\pm\sigma_i).
\]

The six Bloch points are the octahedral dual of the hexahedron. The duality preserves the spherical Euler characteristic,

\[
8-12+6=6-12+8=2.
\]

Thus the `six states` in RF-02H are the six oriented faces of the hexahedral cell, not six vertices of the cube.

## 2. Exact aggregate Fubini--Study metric

Assign equal weights `w_a=1/6` and define the second moment

\[
M_H=\sum_a w_a\,n_an_a^{\mathsf T}.
\]

For the six antipodal axis normals,

\[
\boxed{M_H=\frac13I_3.}
\]

For an infinitesimal rigid rotation generator `xi in R^3`, each Bloch vector changes as

\[
\delta_\xi n_a=\xi\times n_a.
\]

Since the pure-qubit FS line element is

\[
ds_{FS}^2=\frac14dn\cdot dn,
\]

define

\[
\boxed{
h_H(\xi,\eta)
=\frac14\sum_aw_a
(\xi\times n_a)\cdot(\eta\times n_a).
}
\]

Using the vector identity

\[
(\xi\times n)\cdot(\eta\times n)
=\xi\cdot\eta-(\xi\cdot n)(\eta\cdot n),
\]

one obtains

\[
\boxed{
h_H=\frac14(I_3-M_H)=\frac16I_3.}
\]

Therefore

\[
\boxed{
\operatorname{rank}h_H=3,
\qquad
\operatorname{Spec}(h_H)=\left\{\frac16,\frac16,\frac16\right\},
}
\]

\[
\boxed{
\det h_H=\frac1{216}>0,
\qquad
\operatorname{cond}(h_H)=1.
}
\]

This closes the rank-three prerequisite of RF-G0 at the local multi-ray/projective level for the regular hexahedral dual frame.

## 3. Why the single-Bloch rank firewall is respected

A single state map into `CP1` has a pullback metric of rank at most two because `dim_R CP1=2`.

RF-02H instead uses the configuration orbit

\[
\Psi=(\psi_{+1},\psi_{-1},\psi_{+2},\psi_{-2},\psi_{+3},\psi_{-3})
\]

inside `(CP1)^6`. Its rigid-orientation orbit has three independent infinitesimal rotation generators. The positive rank-three metric is therefore carried by the multi-state configuration and does not violate the single-state rank bound.

## 4. Discrete metric/curvature fingerprint

For the hexahedral dual frame,

\[
d_{FS}(n,-n)=\frac\pi2,
\qquad
d_{FS}(e_i,e_j)=\frac\pi4\quad(i\ne j),
\]

and

\[
P(n,-n)=0,
\qquad
P(e_i,e_j)=\frac12\quad(i\ne j).
\]

The six dual vertices tessellate the Bloch sphere into eight spherical octants. Each octant corresponds to one vertex of the original hexahedron and carries

\[
\boxed{
\Omega_{\rm oct}=\frac\pi2,
\qquad
a_{FS,\rm oct}=\frac\pi8,
\qquad
|\gamma_{B,\rm oct}|=\frac\pi4.
}
\]

The integrated invariants are

\[
\boxed{
\sum_fa_{FS}(f)=\pi,
\qquad
\int_{S^2}F_B=\pm2\pi,
\qquad
c_1=\pm1,
\qquad
\chi=2.
}
\]

These invariants provide the refinement bookkeeping for neighboring/higher polyhedral cells.

## 5. Phase-clock physicalization

IDT supplies

\[
\boxed{
\ell_\varphi
=\frac{c}{|\omega_t|}
=\frac{\hbar c}{E}.
}
\]

For a common nonzero local phase rate over the hexahedral cell, physicalize the aggregate metric by

\[
\boxed{
h_H^{\rm phys}
:=\ell_\varphi^2h_H
=\frac{\ell_\varphi^2}{6}I_3
=\frac{c^2}{6\omega_t^2}I_3.
}
\]

Introduce a dimensionless local hexahedral orientation coframe `vartheta^i`. Define

\[
\boxed{
E^i
:=\frac{\ell_\varphi}{\sqrt6}\,\vartheta^i.
}
\]

Then

\[
\boxed{
h_\perp=\sum_{i=1}^3E^i\otimes E^i}
\]

is positive definite and rank three wherever `0<ell_phi<infinity`.

The `E^i` are local spatial coframe candidates. Their global integrability is a separate gate.

## 6. Exact anisotropic paired-rate extension

Allow each antipodal face pair to carry its own positive phase-clock length

\[
\ell_i=\frac{c}{|\omega_i|},
\qquad i=1,2,3,
\]

while the `+/-` members of each pair share the same `ell_i`.

Physicalize each face contribution before aggregation:

\[
h_H^{\rm aniso}
=\frac14\sum_{i,s}\frac16\ell_i^2
(I_3-n_{i,s}n_{i,s}^{\mathsf T}).
\]

The exact matrix is

\[
\boxed{
h_H^{\rm aniso}
=\frac1{12}
\begin{pmatrix}
\ell_2^2+\ell_3^2&0&0\\
0&\ell_1^2+\ell_3^2&0\\
0&0&\ell_1^2+\ell_2^2
\end{pmatrix}.
}
\]

Equivalently,

\[
\boxed{
h_{11}^{\rm aniso}
=\frac{c^2}{12}\left(\omega_2^{-2}+\omega_3^{-2}\right)}
\]

with cyclic permutations for `h_22,h_33`.

For finite nonzero `omega_i`, every diagonal entry is positive, hence

\[
\boxed{\operatorname{rank}h_H^{\rm aniso}=3.}
\]

The isotropic result is recovered exactly at `omega_1=omega_2=omega_3`.

This gives a direct structural map from anisotropic temporal phase rates to anisotropic local spatial metric coefficients. The dynamical law for those rates is downstream.

## 7. Lorentzian assembly

RF-G0 supplies the temporal covector

\[
\Theta=c\,dt
\]

up to the admitted clock normalization. With the RF-02H spatial coframe,

\[
\boxed{
g_L=-\Theta\otimes\Theta+h_\perp}
\]

has exact local signature

\[
\boxed{(-,+,+,+).}
\]

At a point, the tetrad

\[
\boxed{\{\Theta,E^1,E^2,E^3\}}
\]

therefore gives a local Minkowski-normal form.

This is a tangent-space/local-frame statement. Writing global coordinates `X^i` with `E^i=dX^i` requires the additional integrability condition

\[
dE^i=0
\]

on the relevant patch. More generally `dE^i` may encode connection/torsion information and must be derived rather than set to zero.

## 8. Promotion result

RF-02H records the following exact advancement:

```text
single_CP1_rank3                      = impossible
hexahedral_six_face_normal_config    = admitted structural carrier
weighted_second_moment               = I3/3
aggregate_FS_metric                  = I3/6
local_spatial_rank                   = 3
local_spatial_condition_number       = 1
phase_clock_physicalized_metric      = c^2 I3 / (6 omega_t^2)
RF-G0_positive_rank3_prerequisite    = SATISFIED_LOCALLY
```

## 9. Remaining gates before Newton

The next derivation gates are now sharper:

1. `RF-02I` — hexahedral coframe gluing/refinement and integrability;
2. `RF-N0` — derive lapse/clock-rate dynamics rather than hold `Theta=c dt` rigid;
3. derive the connection/curvature of the physicalized tetrad;
4. define the weak-field perturbation variables from those derived quantities;
5. test whether the Newton/Poisson limit follows without using Newton's law or Poisson's equation as an input.

The author/formalism may suggest that phase-rate gradients become gravitational metric gradients, yet does not state that implication as an established result before the connection, action and weak-field gates pass.
