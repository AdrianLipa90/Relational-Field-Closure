# GREMLIN bounded audit — RF-N1B physical source bridge

Status: `CANDIDATE_GENERATION_ONLY / NO_CANON_PROMOTION`

GREMLIN is restricted to proposing and rejecting source-bridge candidates after RF-N1A has derived the lapse operator. It does not assign matter semantics or determine `G`.

Required final Newton-source structure:

\[
\Delta_h\Phi_R=c^2\mathcal S_R,
\qquad
\mathcal S_R\stackrel{?}{\longrightarrow}\frac{4\pi G}{c^2}\rho_m.
\]

## Candidate audit

| candidate bridge | dimensional result | structural issue | disposition |
|---|---|---|---|
| `rho_R -> rho_m` | unspecified by IDT 00C | `rho_R` is introduced as a relational kinetic/mobility scalar; no mass-density type or conserved matter current is supplied | `REJECT_DIRECT_IDENTITY` |
| `Xi_I -> S_R` | exact `L^-2 -> L^-2` | type-compatible but no matter semantics or coupling normalization | `RETAIN_SOURCE_BASIS_CANDIDATE` |
| `E=hbar|omega| -> rho_m` | energy, not density | no volume or occupation/source-count map | `REJECT_DIRECT_IDENTITY` |
| `E/(c^2 V_H)` | mass density if `V_H` is admitted | requires physical cell-volume binding and assumes one source quantum per cell | `QUARANTINE_ONE_PER_CELL_ANSATZ` |
| `n_E E/(c^2 V_H)` | mass density | correct type; `n_E` source occupation/current remains independent | `RETAIN_BRIDGE_TEMPLATE` |
| historical TIR sector mass ansatz | mass | active claim hierarchy classifies it B/C by sector, not a universal established source law; no local density/current map | `DO_NOT_PROMOTE_TO_NEWTON_SOURCE` |
| Maxwell stress-energy | energy density after sourced Maxwell normalization | downstream of RF-M2 | `DEFER_PARALLEL_BRANCH` |
| dynamic `Lambda0` / `Xi_I` vacuum sector | inverse-area curvature | homogeneous/vacuum and matter roles must not be conflated | `DEFER_CROSS_COUPLING` |

## Strongest retained template

GREMLIN retains only the typed template

\[
\boxed{
\rho_{src}
=\frac{n_EE}{c^2V_H}
}
\]

subject to independent derivations of:

1. `V_H` as the physical measure of the source cell rather than only a metric scale;
2. `n_E` as a conserved occupation/source weight;
3. the assignment of `E` to that source carrier;
4. the map from `rho_src` into `S_R`.

For the conditional regular-cell choices

\[
V_H=a_H^3,
\quad a_H=\frac{c}{\sqrt6|\omega|},
\quad E=\hbar|\omega|,
\]

the template reduces algebraically to

\[
\rho_{src}
=6\sqrt6\,n_E\frac{\hbar|\omega|^4}{c^5}.
\]

This is not promoted because `n_E` and the physical measure assignment remain open.

## Universality diagnostic

If a separate derivation also gave

\[
\mathcal S_R=\beta_I\Xi_I,
\]

then matching the Newton target would require

\[
G
=\frac{\beta_I\mathcal J_\pi}{24\pi\sqrt6\,n_Ea_{FS}}
\frac{c^5}{\hbar\omega^2}.
\]

GREMLIN marks this as `UNIVERSALITY_TEST_CANDIDATE`, not a formula for `G`.

A universal coupling requires the complete source-dependent prefactor multiplying `c^5/(hbar omega^2)` to compensate any allowed variation of the local phase rate and source state. This is a falsifiable constraint on future source bridges.

## Audit result

The current shortest safe path is:

```text
conserved source carrier
 -> occupation/current n_E
 -> physical measure V_H
 -> energy assignment E
 -> rho_src
 -> source map S_R[rho_src]
 -> universality test
 -> Newton target
```

Direct `rho_R=rho_m`, direct `E=rho_m`, and direct `Xi_I=rho_m` identifications are rejected at this gate.