# RFG4 — alpha_c Gauge-Coupling Genealogy Firewall

Status: `CHYBA / CANDIDATE_ONLY / ARCHIVE_CONSTANT_ROOT_FOUND / DERIVATION_ROOT_OPEN / YM_PROMOTION_BLOCKED`

RFG4 audits the archived Metatime/CIEL value

\[
\alpha_c=0.474812
\]

before it can enter RFG3 as a physical Yang–Mills normalization.

## 1. Archived dependency

The archived gluon implementation declares

\[
\boxed{\alpha_c=0.474812}
\]

as an information-field kinetic coefficient and then defines

\[
\boxed{g_{archive}=\frac{1}{\sqrt{\alpha_c}}}
\]

and

\[
\boxed{\alpha_s^{archive}=\frac{g_{archive}^2}{4\pi}.}
\]

Thus the archived value `g≈1.4512` is downstream of `alpha_c`; its physical derivation status is exactly the derivation status of `alpha_c`.

## 2. Provenance result

The current Library provenance search finds repeated declarations of `0.474812` under names such as `ALPHA_C`, `CONSCIOUSNESS_QUANTUM` and `LIPA_CONSTANT`. The located sources instantiate the number as a constant. The current search did not locate an upstream equation whose independently supplied inputs evaluate to `0.474812`.

Therefore the promotion state is

\[
\boxed{
\texttt{ARCHIVE_CONSTANT_ROOT_FOUND}
\;\wedge\;
\texttt{DERIVATION_ROOT_OPEN}.
}
\]

The archived downstream identities are executable, while physical Yang–Mills promotion remains blocked.

## 3. Relation to the Wilson coordinate

RFG3 uses

\[
\beta_W=\frac6{g_0^2}.
\]

If the archive relation `g_0^2=1/alpha_c` is admitted provisionally, then

\[
\boxed{\beta_W^{archive}=6\alpha_c.}
\]

For the archived constant,

\[
\beta_W^{archive}=2.848872.
\]

This value is an archive-derived coordinate only. Its status cannot exceed the genealogy status of `alpha_c`.

## 4. Candidate-generation grammar

GREMLIN may search for a source formula for `alpha_c` only inside a frozen low-complexity grammar built from independently admitted project primitives. A candidate expression `C` must be generated before any physical `g`, `alpha_s`, Wilson `beta_W` or Newton `G` comparison is used for selection.

Allowed primitive classes for the first pass are:

- canonical information constant `kappa=ln(2)/(24pi)`;
- exact algebraic constants already independently defined by the project;
- admitted integer geometric coordinates such as `L3,L4,L5`;
- exact Euler/Berry winding coordinates;
- independently derived Kähler/phase invariants with provenance.

Allowed first-pass operations are limited to

\[
+,-,\times,/,\log,\exp,\sqrt{\phantom{x}}
\]

with expression depth bounded before execution.

## 5. Numerical gate

For a proposed candidate `C`, define

\[
\boxed{
\Delta_{\alpha_c}
=\frac{|C-0.474812|}{0.474812}.
}
\]

A numerical match alone is insufficient for promotion. The candidate must additionally have an upstream derivation that selects its expression independently of the archived target.

The archive value has six decimal digits. A reconstruction claiming exact archive identity must therefore satisfy an absolute tolerance compatible with that stated precision and preserve the same value under independent re-execution.

## 6. Downstream firewall

Until the genealogy closes, the following quantities retain candidate/archive-input status:

\[
g_{archive}=\alpha_c^{-1/2},
\]

\[
\beta_W^{archive}=6\alpha_c,
\]

and any RFG2/RFG3 candidate

\[
G_{cand}(g_{archive})
\quad\text{or}\quad
G_{cand}(\beta_W^{archive}).
\]

They may be used for sensitivity analysis but not as zero-parameter derivations of the physical Yang–Mills or Newton coupling.

## 7. Falsification / promotion contract

Promotion requires all of:

1. one explicit upstream equation for `alpha_c`;
2. independently typed inputs to that equation;
3. a frozen expression chosen without using a downstream QCD or gravity target;
4. reproduction of the archived value within declared precision;
5. a separate Yang–Mills/Wilson normalization check;
6. running-coupling validation performed only after the bare-coordinate derivation is frozen.

## 8. GREMLIN verdict

`CHYBA / CANDIDATE_ONLY`.

The audit improves the dependency graph by replacing the apparent chain

```text
archive gluon solver -> derived g
```

with the explicit chain

```text
alpha_c archive constant
 -> g = alpha_c^(-1/2)
 -> beta_W = 6 alpha_c
 -> Yang–Mills candidate
```

and marks the genealogy of `alpha_c` as the current root gate.
