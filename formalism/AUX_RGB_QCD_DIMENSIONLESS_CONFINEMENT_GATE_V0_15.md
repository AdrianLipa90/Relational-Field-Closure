# AUX RGB-Moire QCD dimensionless confinement gate v0.15

Status: `EXACT_CREUTZ_CANCELLATION / EXACT_PURE_YM_Z3_CENTER / FULL_QCD_CENTER_EXPLICITLY_BROKEN / STRONG_COUPLING_AREA_LAW_LEADING_ORDER / FINITE_MC_PILOT_INCONCLUSIVE`

Date: 2026-09-26

## 1. Purpose

The physical scale gate v0.14 remains open, but confinement diagnostics need not wait for a calibration of the lattice spacing.

This gate works only with dimensionless Wilson/holonomy observables.

No value in GeV, fm, or physical Lambda_QCD is used.

## 2. Creutz ratio removes arbitrary perimeter normalization

For rectangular Wilson-loop expectation values W(R,T), define

[
\boxed{
\chi(R,T)
=
-\ln
\frac{
W(R,T)W(R+1,T+1)
}{
W(R+1,T)W(R,T+1)
}.
}
]

If

[
W(R,T)
=
\exp[-\sigma a^2 RT-\mu(R+T)-c],
]

then exactly

[
\boxed{\chi(R,T)=\sigma a^2.}
]

Both the perimeter term and constant normalization cancel.

A perimeter-only control gives chi=0.

Thus Creutz ratios isolate a dimensionless area coordinate without assigning any physical value to a.

## 3. Pure Yang-Mills Z3 center gate

Let omega=exp(2 pi i/3). On a periodic pure SU(3) Wilson lattice, multiply every temporal link crossing one fixed time slice by omega.

Every plaquette crossing that slice contains one omega and one omega* factor, so

[
\boxed{S_W[U^\omega]=S_W[U].}
]

A fundamental Polyakov loop winds through the transformed slice once and therefore obeys

[
\boxed{P\mapsto\omega P.}
]

The executable gate verifies both identities on a seeded nontrivial SU(3) configuration.

## 4. Full-QCD center firewall

The pure-gauge center statement must not be promoted unchanged to full QCD with dynamical fundamental quarks.

The same center transformation changes a fundamental Wilson-Dirac determinant:

[
\det D_W[U^\omega]\neq\det D_W[U]
]

in the executable anti-periodic fermion witness.

Therefore:

[
\boxed{Z_3\ \text{is an exact pure-YM symmetry but is explicitly broken by fundamental dynamical quarks}.}
]

Consequently the Polyakov loop is an exact center order parameter only on the pure-gauge surface.

Likewise, with dynamical fundamental matter the asymptotic static string can break, so an unqualified infinite-area-law claim is not the correct full-QCD promotion target.

## 5. Strong-coupling leading-order area law

For the SU(3) Wilson action, the leading nonzero strong-coupling term for a fundamental Wilson loop is

[
\boxed{
\langle W(C)\rangle
=
\left(\frac{\beta_W}{18}\right)^{A(C)}
+\text{higher strong-coupling orders},
}
]

where A(C) is the minimal plaquette area in lattice units.

Therefore the leading dimensionless string-tension coordinate is

[
\boxed{
\sigma a^2
=
-\ln\left(\frac{\beta_W}{18}\right)
+\cdots.
}
]

For the current RFG4D/RFG4G candidate

[
\beta_W=2.84903771431338\ldots,
]

the leading coordinate is

[
\frac{\beta_W}{18}=0.15827987301741\ldots,
qquad
\sigma a^2|_{LO}=1.8433904647307773\ldots.
]

This is a strong-coupling expansion coordinate, not a precision prediction at this beta.

Classical references for the method include Drouffe and Zuber, Physics Reports 102 (1983), DOI 10.1016/0370-1573(83)90034-0.

## 6. Corrected 4D Metropolis pilot

A direct 4^4 SU(3) Wilson-action pilot was run at

[
\beta_W=2.84903771431338.
]

An initial implementation was rejected completely after an embedded SU(2) proposal was found not to be unitary because of a missing parenthesis. No number from that run is retained.

The corrected proposal satisfies

[
\|U^\dagger U-I\|<3.2\times10^{-16},
\qquad
|\det U-1|<4.5\times10^{-16}
]

in a 1000-proposal unit test.

Corrected seed 260926, 80 thermalization sweeps, 30 measured configurations:

[
W_{11}=0.23245,quad
W_{12}=0.06383,quad
W_{21}=0.05714,quad
W_{22}=0.00821,
]

and

[
\chi(1,1)=0.648,
]

with bootstrap estimate approximately

[
0.655\pm0.108.
]

An independent repeat with seed 260927 and longer thermalization produced

[
W_{22}=-0.00087\pm0.00122,
]

so the mean Creutz ratio was not defined.

Therefore the combined pilot verdict is

[
\boxed{\text{FINITE-STATISTICS CONFINEMENT PILOT: INCONCLUSIVE}.}
]

The first seed is positive evidence that the estimator works on the project action, but the second run proves that a simple single-level estimator does not resolve the 2x2 loop reliably at the present statistics.

## 7. Why the failure is informative

Large Wilson loops have exponentially worsening signal-to-noise in ordinary simulations.

Luescher and Weisz introduced a locality-based multilevel algorithm precisely to achieve exponential error reduction for Wilson/Polyakov observables in pure non-Abelian lattice gauge theory (JHEP 09 (2001) 010; arXiv:hep-lat/0108014).

This matches the project-side failure mode: W11 and 1x2 loops are stable while W22 is already noise limited.

## 8. Next admissible gate

For the pure-YM surface:

[
\boxed{
\text{RFG Wilson action}
\to
\text{multilevel sublattice averaging}
\to
W(R,T)
\to
\chi(R,T)
\to
\sigma a^2
}
]

with at least:

1. two independent seeds;
2. several R,T values;
3. stability under sublattice depth and update count;
4. finite-volume comparison;
5. perimeter-only and randomized-link controls;
6. no physical scale calibration.

A confinement promotion requires a plateau/consistent positive sigma*a^2 across increasing loop sizes with controlled statistical uncertainty.

For full QCD the target must be changed to include explicit center breaking and string breaking by dynamical fundamental matter.

## 9. Verdict

The dimensionless diagnostic architecture is closed.

Confinement itself is not yet promoted.

The current shortest missing edge is variance-reduced nonperturbative expectation-value estimation, not metric calibration.
