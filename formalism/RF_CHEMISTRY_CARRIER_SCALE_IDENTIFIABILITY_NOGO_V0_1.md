# RF Chemistry Carrier-Scale Identifiability No-Go v0.1

Status: EXACT_SOURCE_DENSITY_IDENTIFIABILITY_NOGO / INDEPENDENT_SCALE_RECEIPT_REQUIRED / CHEMISTRY_PROMOTION_BLOCKED

## 1. Scope

RF-S13 gives the exact source-density factorization

\[
\rho_E
=
\frac{B\,\omega\,\mathcal N}{V_R}
(\phi+\kappa),
\qquad
V_R=AR.
\]

This note asks only an identifiability question:

> If \(\rho_E\), \(\omega\), and \(\phi\) are known, can the source-density equation by itself determine \(B\), \(\mathcal N\), and \(V_R\) separately?

The answer is no.

This is not a claim that these quantities can never be measured. It is a theorem that **RF-S13 source density alone does not identify them separately**.

## 2. Two-parameter rescaling symmetry

For any positive dimensionless scales \(a,b>0\), define

\[
B' = aB,
\qquad
\mathcal N' = b\mathcal N,
\qquad
V_R' = ab\,V_R.
\]

Then

\[
\frac{B'\mathcal N'}{V_R'}
=
\frac{(aB)(b\mathcal N)}{abV_R}
=
\frac{B\mathcal N}{V_R}.
\]

Therefore

\[
\boxed{
\rho_E(B',\mathcal N',V_R')
=
\rho_E(B,\mathcal N,V_R).
}
\]

The observable source density is constant on a two-parameter orbit.

Hence the map

\[
(B,\mathcal N,V_R)
\longmapsto
\rho_E
\]

is non-injective.

## 3. What changes along the same source-density orbit

The RF-S13 factors are

\[
n_R=\frac{\mathcal N}{V_R},
\qquad
\epsilon_\Psi=B\omega(\phi+\kappa),
\qquad
\rho_E=n_R\epsilon_\Psi.
\]

Under the rescaling,

\[
n_R'
=
\frac{b\mathcal N}{abV_R}
=
\frac{n_R}{a},
\]

while

\[
\epsilon_\Psi'
=
a\epsilon_\Psi.
\]

Thus

\[
\boxed{
n_R'\epsilon_\Psi'
=
n_R\epsilon_\Psi
=
\rho_E.
}
\]

Source density alone cannot distinguish a higher carrier energy with a lower occupation density from a lower carrier energy with a higher occupation density.

## 4. Jacobian rank statement

At fixed \(\omega\) and \(\phi\), write logarithmic variables

\[
x=(\ln B,\ln\mathcal N,\ln V_R).
\]

Then

\[
\ln|\rho_E|
=
x_B+x_N-x_V+\text{constant}.
\]

The logarithmic sensitivity row is

\[
\boxed{
J_\rho=(1,1,-1).
}
\]

Its rank is one.

The nullspace is two-dimensional:

\[
\boxed{
\delta x_B+\delta x_N-\delta x_V=0.
}
\]

For example,

\[
(1,0,1),
\qquad
(0,1,1)
\]

are independent null directions.

This is the differential form of the same exact rescaling degeneracy.

## 5. What is sufficient to break the degeneracy

The no-go is removed only by independent information not reducible to the same product.

Examples include a source-owned receipt for at least enough independent coordinates such as:

- carrier energy \(\epsilon_\Psi\), which with known \(\omega,\phi\) fixes \(B\);
- occupation density \(n_R\);
- occupation \(\mathcal N\) plus cell volume \(V_R\);
- an independently sourced action quantum \(q_A\) plus an independently admitted RF-E5 carrier-observable branch;
- another observable with a linearly independent sensitivity vector.

A numerical choice of \(B(\phi+\kappa)=\hbar/2\) or \(=\hbar\) does not resolve the physical branch unless the corresponding carrier observable has independent source authority. RF-S13 itself marks that selection as OPEN INPUT.

## 6. Minimal identifiability ladder

Use logarithmic parameter coordinates

\[
x=(\ln B,\ln\mathcal N,\ln V_R).
\]

Relevant independently measured quantities have sensitivity rows

\[
J_\rho=(1,1,-1),
\]

\[
J_\epsilon=(1,0,0),
\]

\[
J_n=(0,1,-1),
\]

\[
J_{\mathcal N}=(0,1,0),
\qquad
J_{V_R}=(0,0,1).
\]

Because

\[
\boxed{
J_\rho=J_\epsilon+J_n,
}
\]

the three quantities \(\rho_E,\epsilon_\Psi,n_R\) are not three independent scale constraints. Their matrix has rank two.

This yields the exact minimal ladder:

### Identify B only

A physical per-carrier energy receipt gives

\[
\epsilon_\Psi=B\omega(\phi+\kappa)
\]

and therefore identifies \(B\) when \(\omega,\phi\) are independently known.

Alternatively, source density plus occupation density gives

\[
\boxed{
B
=
\frac{\rho_E}
{n_R\,\omega(\phi+\kappa)}
}
\]

when the denominator is nonzero.

Thus either

\[
\{\epsilon_\Psi\}
\]

or

\[
\{\rho_E,n_R\}
\]

breaks the \(B\)-direction degeneracy.

### Identify all of B, N, V_R

The set

\[
\{\rho_E,\epsilon_\Psi,n_R\}
\]

still has rank two because \(\rho_E=n_R\epsilon_\Psi\).

To obtain full rank three, one needs an absolute occupation or volume coordinate in addition to an energy/density scale. Examples are

\[
\{\rho_E,\epsilon_\Psi,\mathcal N\},
\qquad
\{\rho_E,\epsilon_\Psi,V_R\},
\]

\[
\{\rho_E,n_R,\mathcal N\},
\qquad
\{\rho_E,n_R,V_R\}.
\]

Each corresponding sensitivity matrix has rank three.

Hence the source-owned open inputs have a precise role:

- a carrier-energy or occupation-density receipt can identify \(B\);
- an absolute occupation or cell-volume receipt is additionally required to separate \(\mathcal N\) from \(V_R\).

This is the minimal rank requirement, not a heuristic data wish-list.

## 7. Chemistry consequence

A chemical residual cannot be used to solve for \(B\) and then be reused as evidence for an RFC-induced chemical interaction.

That procedure would be circular:

\[
\text{target residual}
\to
B_{\rm fitted}
\to
V_I
\to
\text{same target residual}.
\]

Therefore the chemistry admission gate must require an independently sourced normalization before the target observable is opened.

## 8. Exact scope of the no-go

Proved here:

- non-injectivity of the RF-S13 source-density map in \(B,\mathcal N,V_R\);
- exact two-parameter positive rescaling symmetry;
- two-dimensional logarithmic Jacobian nullspace;
- source density alone cannot determine the three factors separately.

Not proved:

- that \(B\), \(\mathcal N\), or \(V_R\) are physically nonexistent;
- that no future independent measurement can identify them;
- that a particular RF-E5 branch is physically selected;
- any nonzero new chemistry effect.

The theorem therefore strengthens the existing source-owned OPEN INPUT status rather than replacing it.
