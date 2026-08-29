# RF-S13 — Relational Generator Source-Density Binding

Status: `EXACT_GENERATOR_FACTORIZATION / EXACT_NEWTON_EINSTEIN_SOURCE_CROSSWALK / CARRIER_ACTION_NORMALIZATION_TYPED`

RF-S13 is stacked on exact-green RF-S12. It inserts the canonical relational generator

\[
\boxed{
\mathcal G(t)
=
\frac{B(t)\,\omega(t)\,\mathcal N(t)}{A(t)R(t)}
\bigl(\phi(t)+\kappa\bigr),
\qquad
\kappa=\frac{\ln 2}{24\pi}
}
\]

into the already-derived RFC source ledger.

The symbol \(\mathcal N\) is used here for carrier occupation so it cannot be confused with the ADM lapse \(N_R\).

## 1. Dimensional source realization

RF-N1B2 reduced the source problem to

\[
\text{carrier occupation/density}
\to
\text{energy per carrier}
\to
\rho_{\rm source}
\to
\mathcal S_R.
\]

RF-S13 factorizes the generator exactly as

\[
\boxed{
\mathcal G
=
\left(\frac{\mathcal N}{AR}\right)
\left[B\omega(\phi+\kappa)\right].
}
\]

On the source-density dimensional branch take

\[
[A]=L^2,
\qquad
[R]=L,
\qquad
[\mathcal N]=1,
\qquad
[\omega]=T^{-1},
\qquad
[\phi]=[\kappa]=1.
\]

Then \(AR\) is the relational cell volume

\[
\boxed{V_R:=AR}
\]

and

\[
\boxed{n_R:=\frac{\mathcal N}{V_R}}
\]

is the occupation density.

For \(\mathcal G\) to carry energy-density units, the required dimensional role of \(B\) is action:

\[
\boxed{[B]=ET.}
\]

Define the per-carrier energy

\[
\boxed{
\epsilon_\Psi
:=B\omega(\phi+\kappa).
}
\]

Therefore

\[
\boxed{
\rho_E
:=n_R\epsilon_\Psi
=
\frac{B\omega\mathcal N}{AR}(\phi+\kappa)
=\mathcal G.
}
\]

The original generator is thus exactly the energy density on this typed source branch.

The equivalent mass density is

\[
\boxed{
\rho_m=\frac{\rho_E}{c^2}.
}
\]

## 2. Exact Newton source crosswalk

RFC already derives the lapse-source operator

\[
\Delta_h\Phi_R=c^2\mathcal S_R
\]

and RF-N1C records the weak-field target normalization

\[
c^2\mathcal S_R=4\pi G\rho_m.
\]

Substituting \(\rho_m=\rho_E/c^2\) gives

\[
\boxed{
\mathcal S_R
=
\frac{4\pi G}{c^4}\rho_E.
}
\]

Using the independently recorded Einstein normalization

\[
\boxed{\kappa_E=\frac{8\pi G}{c^4}}
\]

gives the exact identity

\[
\boxed{
\mathcal S_R
=
\frac{\kappa_E}{2}\rho_E
=
\frac{\kappa_E}{2}
\frac{B\omega\mathcal N}{AR}(\phi+\kappa).
}
\]

Thus the same relational generator occupies the matter-source slot of the Newton and Einstein ledgers with one coefficient crosswalk.

## 3. ADM source insertion

RF-E11/RF-E12 use the normal-frame matter energy density \(\rho_n=T_{nn}\). On the admitted source branch

\[
\boxed{\rho_n=\rho_E=\mathcal G.}
\]

The dynamic-Lambda Hamiltonian constraint therefore becomes

\[
\boxed{
{}^{(3)}R+K^2-K_{ij}K^{ij}-2\Lambda_0
=
2\kappa_E
\frac{B\omega\mathcal N}{AR}(\phi+\kappa).
}
\]

This is an insertion into the already-derived ADM equation; the geometry and Bianchi propagation spine remain unchanged.

## 4. Exact match to the RFC phase-carrier energy

RF-N1B2N derives on the positive common-generator branch, in natural units,

\[
\boxed{
\epsilon_Q=\frac12\omega_Q.
}
\]

Restoring an independently admitted action scale \(q_A\), this is

\[
\boxed{
\epsilon_Q=\frac{q_A}{2}\omega_Q.
}
\]

RF-S13 gives on the common-rate branch \(\omega=\omega_Q\)

\[
\epsilon_\Psi=B\omega_Q(\phi+\kappa).
\]

Hence the two per-carrier energies coincide exactly when

\[
\boxed{
B(\phi+\kappa)=\frac{q_A}{2}.
}
\]

Equivalently,

\[
\boxed{
B_\star=\frac{q_A}{2(\phi+\kappa)}.
}
\]

This removes one free normalization product from the source ledger once \(q_A\) and \(\phi\) have independent provenance.

## 5. RF-04 / RF-E5 factor-two crosswalk

RF-04 records the standard transferred-energy relation

\[
E=\hbar\omega.
\]

RF-E5 independently distinguishes two homogeneous on-shell scalar carrier observables:

\[
\epsilon_{kin}=\frac{\hbar\omega}{2},
\qquad
\epsilon_{tot}=\hbar\omega.
\]

The relational generator preserves that firewall as two exact normalization surfaces:

\[
\boxed{
B(\phi+\kappa)=\frac{\hbar}{2}
\quad\Longleftrightarrow\quad
\epsilon_\Psi=\epsilon_{kin},
}
\]

and

\[
\boxed{
B(\phi+\kappa)=\hbar
\quad\Longleftrightarrow\quad
\epsilon_\Psi=\epsilon_{tot}.
}
\]

Therefore the generator supplies a direct observable-normalization coordinate for the RF-E5 carrier-energy factor-two gate.

## 6. Occupation/current crosswalk

RF-N1B2 uses the conserved density \(j_Q\) and extensive carrier \(Q_\Sigma\). RF-S13 supplies the discrete occupation density

\[
\boxed{n_R=\frac{\mathcal N}{AR}.}
\]

On a one-unit carrier-charge realization,

\[
\boxed{j_Q=n_R,}
\]

and the RF-N1B2 continuous source map becomes

\[
\rho_E=\epsilon_Qj_Q
=\frac{B\omega\mathcal N}{AR}(\phi+\kappa).
\]

For a general carrier quantum \(q_0\), the typed relation is

\[
\boxed{j_Q=q_0n_R,}
\]

with the corresponding per-charge energy \(\epsilon_Q=\epsilon_\Psi/q_0\). The product \(\epsilon_Qj_Q\) remains exactly \(\rho_E\).

Thus the physical source density is invariant under the bookkeeping choice of carrier quantum:

\[
\boxed{
\epsilon_Qj_Q=n_R\epsilon_\Psi=\rho_E.
}
\]

## 7. Scaling identities

The source density obeys exact homogeneity:

\[
\rho_E\propto B,
\qquad
\rho_E\propto\omega,
\qquad
\rho_E\propto\mathcal N,
\qquad
\rho_E\propto(\phi+\kappa),
\]

and

\[
\boxed{
\rho_E\propto A^{-1}R^{-1}.
}
\]

This makes the generator immediately compatible with the already-separated RFC ledgers for phase rate, occupation, projective area and radial scale.

## 8. Promotion ledger

```text
canonical kappa = ln(2)/(24 pi)                         PASS EXACT
user generator algebraic factorization                 PASS EXACT
AR -> relational volume on typed source branch         PASS DEFINITION
N/(AR) -> occupation density                           PASS EXACT
B action-units -> per-carrier energy role              PASS DIMENSIONAL
rho_E = generator                                      PASS EXACT
rho_m = rho_E/c^2                                      PASS EXACT
S_R = (kappa_E/2) rho_E                                PASS EXACT CROSSWALK
Newton <-> Einstein weak-field normalization           PASS EXACT PARENT
RFC half-rate normalization product                    PASS EXACT CONDITIONAL
RF-E5 kinetic/total factor-two surfaces                PASS EXACT PARENT
physical B-action realization                          OPEN INPUT
physical occupation/current receipt                    OPEN INPUT
physical AR cell-volume receipt                        OPEN INPUT
RF-E5 physical carrier-observable selection            OPEN INPUT
absolute project-side kappa_E / G promotion            OPEN INPUT
```

## 9. Validation authority

Reference implementation: `src/rfc/relational_generator_source_density.py`.
Reference tests: `tests/reference/test_rfs13_relational_generator_source_density.py`.
Validation receipt: `validation/RF_S13_RELATIONAL_GENERATOR_SOURCE_DENSITY_V0_1.json`.

Stack parent: RF-S12 exact-green head `7cd1ade094db2379c9d76b75819007451a84628e`, RFC reference suite #278 SUCCESS.
