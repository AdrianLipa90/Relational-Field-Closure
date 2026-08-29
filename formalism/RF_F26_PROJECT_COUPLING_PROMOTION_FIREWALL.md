# RF-F26 — Project Coupling Promotion Firewall

Status: `REFERENCE_IMPLEMENTED_AWAITING_CI / BCJ_REFERENCE_RECEIPT_ADMISSION / GREMLIN_AUTHORITY_REJECTED / WILSON_GAMMA_CARRIER_PROVENANCE_EXPLICIT`

RF-F26 follows RF-F25. Its role is to separate already validated project color-kinematics algebra from the remaining physical normalization inputs entering the reduced-gravity and Einstein coupling.

The gate does not choose a value of the gravitational coupling. It freezes the gauge/double-copy inputs first and only then computes the resulting coupling coordinate.

## 1. BCJ evidence surface

RFG29 has a root-level validation receipt for an explicit five-point representation with

- 15 cubic graphs,
- six DDM masters,
- rank-two propagator matrix,
- nine independent Jacobi relations,
- color-dressed reconstruction,
- current residue factorization.

RFG30 independently supplies a root-level validation receipt for explicit fifteen-graph double-copy / KLT equivalence, generalized-gauge invariance, Ward checks and copy exchange.

RF-F26 consumes such reference receipts as evidence coordinates. A `GREMLIN_CANDIDATE` label is not accepted as promotion authority.

The executable BCJ defect is

\[
\Delta_{BCJ}=\max\{\Delta_J,\Delta_{rec},\Delta_{KLT},\Delta_{Ward},\Delta_{struct}\}.
\]

For the admitted five-point reference surface,

\[
N_{graph}=15,\qquad \operatorname{rank}J=9.
\]

A graph-count or Jacobi-rank mismatch sets the structural defect nonzero.

## 2. Wilson normalization

The standard Wilson coordinate is retained as an independently frozen project input:

\[
\boxed{g_{YM}^2=\frac{6}{\beta_W}}.
\]

RF-F26 audits

\[
\Delta_W
=\frac{2|g_{YM}^2-6/\beta_W|}
{|g_{YM}^2|+|6/\beta_W|}.
\]

The RFG3 candidate document is not itself promotion authority. A physical or project-action determination of `beta_W` must carry independent provenance.

## 3. Double-copy normalization

`Gamma_DC` is retained as a positive independently sourced normalization coordinate. The gravity output may not be used to select it.

The same rule is imposed on BCJ numerator selection, `beta_W`, and `M_star`.

If any of these coordinates is selected using the gravitational target, the promotion-independence defect is nonzero.

The provenance IDs for BCJ, Wilson, `Gamma_DC`, and the carrier scale must also differ from the gravity-output receipt ID.

## 4. Carrier-scale type firewall

RF-N1C4 defines

\[
\boxed{\zeta_M=\frac{M_\star}{\epsilon_Q}}.
\]

RF-F26 keeps three explicit branches:

```text
KINETIC_CARRIER       zeta_M = 1
TOTAL_ONSHELL_REST    zeta_M = 2
INDEPENDENT_DERIVED   zeta_M independently frozen
```

For the first two branches the declared type is audited against the supplied `M_star` and `epsilon_Q` rather than assigned by construction.

The factor-four discriminator is retained exactly. For fixed `Gamma_DC` and `g_YM`, changing from `zeta_M=1` to `zeta_M=2` doubles the reduced gravity scale and therefore gives

\[
\boxed{\kappa_E^{rest}=\frac14\kappa_E^{kin}}.
\]

## 5. Coupling coordinate after input freezing

Define

\[
\boxed{\bar M_G=\frac{M_\star}{\Gamma_{DC}g_{YM}^2}}.
\]

In the natural-unit convention of RF-N1C2/RF-E3,

\[
\boxed{\kappa_E=\frac{1}{\bar M_G^2}}.
\]

This value is an output of the frozen project coordinates. It is not an input used to tune them.

## 6. Exact promotion firewall

A reference receipt passes only when all of the following close within the declared numerical floor:

```text
BCJ graph/Jacobi structure
BCJ Jacobi defect
project reconstruction defect
double-copy/KLT defect
Ward defect
Wilson normalization defect
carrier-type defect
gravity-target selection independence
provenance-collision firewall
```

`Gamma_DC` remains visible in the receipt as an independently sourced normalization coordinate.

## 7. Consequence for the Einstein frontier

RF-F25 already supplies the cross-system reduced-gravity universality test. RF-F26 localizes the remaining coupling promotion problem:

```text
RFG29/RFG30 reference BCJ evidence      -> executable project evidence
independent beta_W / g_YM normalization -> Wilson gate
independent Gamma_DC                    -> double-copy normalization gate
independent M_star physical type        -> RF-N1C4 type gate
all frozen first                        -> Mbar_G -> kappa_E
cross-system RF-F25                     -> universality test
```

The next physical step is therefore to provide realized, independently sourced normalization receipts for the coordinates entering this firewall, rather than adding another Einstein-field identity.
