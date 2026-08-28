# RFG5 — Horizon / Double-Copy Newton-Coupling Cross-Check

Status: `CHYBA / CANDIDATE_ONLY / TWO_ROUTE_CONSISTENCY_GATE / CIRCULARITY_FIREWALL_ACTIVE`

RFG5 compares two separately typed routes to the Newton coupling without using a numerical CODATA target as the selection rule.

Route A is the RFG2/RFG3 color–kinematics / double-copy candidate. Route B is the Schwarzschild horizon consistency relation combined with the RF-E1 Hawking/Euler surface-gravity gate.

## 1. Route A — double-copy candidate

For a self-copy gauge sector,

\[
\boxed{
G_{DC}
=\frac{\Gamma_{DC}^2g_{YM}^4}{8\pi M_\star^2}.
}
\]

With the RFG3 Wilson coordinate

\[
g_{YM}^2=\frac6{\beta_W},
\]

this becomes

\[
\boxed{
G_{DC}
=\frac{9\Gamma_{DC}^2}
{2\pi\beta_W^2M_\star^2}.
}
\]

With the independent source-carrier scale candidate

\[
M_\star\stackrel{?}{=}\epsilon_N=\frac12D_\tau\chi,
\]

one obtains

\[
\boxed{
G_{DC}
=\frac{18\Gamma_{DC}^2}
{\pi\beta_W^2(D_\tau\chi)^2}.
}
\]

All three coordinates `beta_W`, `Gamma_DC` and `D_tau chi` remain independently gated.

## 2. Route B — Schwarzschild horizon consistency coordinate

For the standard Schwarzschild family, the physical surface gravity is

\[
\boxed{
\kappa_H=\frac{c^4}{4GM_H}.
}
\]

Therefore an independently supplied Schwarzschild mass `M_H` and surface gravity `kappa_H` define the consistency coordinate

\[
\boxed{
G_H:=\frac{c^4}{4M_H\kappa_H}.
}
\]

RF-E1 independently relates the same surface gravity to the Euclidean/Hawking temperature,

\[
T_H=\frac{\hbar\kappa_H}{2\pi c k_B}.
\]

Hence the equivalent thermal form is

\[
\boxed{
G_H
=\frac{\hbar c^3}{8\pi k_BM_HT_H}.
}
\]

## 3. Circularity firewall

`G_H` is a Schwarzschild-family consistency estimator. The Schwarzschild relation contains the Einstein/Newton coupling in the metric-source solution. RFG5 therefore uses Route B only as an independent cross-check after the horizon mass/geometry has been admitted through a source route that is logically separate from the double-copy construction.

A claim of first-principles Newton-coupling derivation must be carried by Route A or another non-circular normalization theorem. Route B can then falsify or corroborate that value.

## 4. G-free cross-route invariant

Set

\[
G_{DC}=G_H
\]

in natural units `hbar=c=k_B=1`. Then

\[
\frac{\Gamma_{DC}^2g_{YM}^4}{8\pi M_\star^2}
=\frac{1}{4M_H\kappa_H}.
\]

The Newton constant cancels and the two routes predict the dimensionless consistency identity

\[
\boxed{
\Gamma_{DC}^2g_{YM}^4M_H\kappa_H
=2\pi M_\star^2.
}
\]

If

\[
M_\star=\frac12D_\tau\chi,
\]

then

\[
\boxed{
\Gamma_{DC}^2g_{YM}^4M_H\kappa_H
=\frac\pi2(D_\tau\chi)^2.
}
\]

Using `g_YM^2=6/beta_W`, this becomes

\[
\boxed{
72\Gamma_{DC}^2M_H\kappa_H
=\pi\beta_W^2(D_\tau\chi)^2.
}
\]

This is the preferred RFG5 cross-check because it tests the relational isomorphism before inserting a numerical value of `G`.

## 5. Hawking-temperature form of the invariant

In natural units RF-E1 gives

\[
\kappa_H=2\pi T_H.
\]

Therefore

\[
72\Gamma_{DC}^2M_H(2\pi T_H)
=\pi\beta_W^2(D_\tau\chi)^2,
\]

or

\[
\boxed{
144\Gamma_{DC}^2M_HT_H
=\beta_W^2(D_\tau\chi)^2.
}
\]

Thus the same candidate can be tested using a thermal horizon observable rather than an explicit `G` target.

## 6. Independent defects

Define

\[
\Delta_{cross}
=
\frac{
|72\Gamma_{DC}^2M_H\kappa_H
-\pi\beta_W^2(D_\tau\chi)^2|
}{
\pi\beta_W^2(D_\tau\chi)^2
},
\]

and equivalently

\[
\Delta_{thermal}
=
\frac{
|144\Gamma_{DC}^2M_HT_H
-\beta_W^2(D_\tau\chi)^2|
}{
\beta_W^2(D_\tau\chi)^2
}.
\]

If all inputs are independently frozen, a valid two-route bridge requires

\[
\boxed{\Delta_{cross}=\Delta_{thermal}=0}
\]

within the declared numerical/observational tolerance.

## 7. Promotion requirements

Before RFG5 can move beyond GREMLIN candidate status, all of the following must be independent:

1. project Yang–Mills normalization and `beta_W`;
2. color–kinematics matched-Jacobi representation;
3. double-copy normalization `Gamma_DC`;
4. source-carrier scale `M_star` and its proposed binding to `epsilon_N`;
5. horizon mass `M_H`;
6. horizon surface gravity or Hawking temperature;
7. an explicit provenance graph showing that Route B inputs were not generated using Route A's candidate `G`.

## 8. GREMLIN verdict

`CHYBA / CANDIDATE_ONLY`.

The useful result is a `G`-free relational invariant:

\[
\boxed{
72\Gamma_{DC}^2M_H\kappa_H
=\pi\beta_W^2(D_\tau\chi)^2
}
\]

or, using the Euclidean/Hawking relation,

\[
\boxed{
144\Gamma_{DC}^2M_HT_H
=\beta_W^2(D_\tau\chi)^2.
}
\]

This converts the proposed gluon↔gravity / AB↔Hawking cosmic isomorphism into a falsifiable cross-route constraint before a numerical Newton constant is promoted.
