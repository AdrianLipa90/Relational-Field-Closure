# RFG4E — `alpha_c` ↔ Wilson Action-Coefficient Gate

Status: `EXACT_ACTION_COEFFICIENT_EQUIVALENCE / ARCHIVE_PARAMETER_PROVENANCE_PRESENT / PROJECT_PLAQUETTE_COEFFICIENT_OPEN / YM_PROMOTION_GATED`

RFG4E consumes RFG3 and the RFG4 genealogy. It replaces the informal candidate statement

\[
\alpha_c\stackrel{?}{=}\frac1{g_0^2}
\]

with an exact action-coefficient condition that can be audited directly on the project holonomy action.

## 1. Project plaquette defect

RFG3 uses the `SU(3)` project defect

\[
\boxed{
D_p:=3-\operatorname{ReTr}U_p.
}
\]

Suppose the independently derived project plaquette action has coefficient `C_p` in

\[
\boxed{
S_{proj}=C_p\sum_pD_p.
}
\]

`C_p` is the coordinate to be recovered from the actual project action or continuum reduction.

## 2. Standard Wilson normalization

For `SU(3)`,

\[
S_W
=\beta_W\sum_p
\left(1-\frac13\operatorname{ReTr}U_p\right).
\]

Since

\[
D_p
=3\left(1-\frac13\operatorname{ReTr}U_p\right),
\]

one has exactly

\[
\boxed{
S_W=\frac{\beta_W}{3}\sum_pD_p.
}
\]

Matching `S_proj=S_W` on the same plaquette support therefore gives

\[
\boxed{
C_p=\frac{\beta_W}{3}.
}
\]

Thus

\[
\boxed{
\beta_W=3C_p.
}
\]

Using the Wilson relation

\[
\beta_W=\frac6{g_0^2},
\]

we also obtain

\[
\boxed{
g_0^2=\frac2{C_p},
\qquad
\frac1{g_0^2}=\frac{C_p}{2}.
}
\]

## 3. Exact `alpha_c` equivalence condition

The candidate Yang–Mills binding

\[
\alpha_c=\frac1{g_0^2}
\]

is therefore equivalent to

\[
\boxed{
C_p=2\alpha_c.
}
\]

Consequently,

\[
C_p=2\alpha_c
\quad\Longrightarrow\quad
\boxed{
\beta_W=6\alpha_c,
\qquad
g_0^2=\alpha_c^{-1}.
}
\]

The converse also follows from `C_p=beta_W/3` and `beta_W=6/g_0^2`. Hence on the admitted Wilson plaquette convention,

\[
\boxed{
\alpha_c=1/g_0^2
\quad\Longleftrightarrow\quad
C_p=2\alpha_c.
}
\]

This is the RFG4E action-coefficient theorem.

## 4. Archive provenance audit

The recovered CIEL archive carries `alpha_c=0.474812` as an explicit scalar constant/alias and RFG4 carries its historical spectral-extraction genealogy. RFG4C supplies the clean-room spectral identifiability theorem for `alpha_c` once its effective-unit and peak-label inputs are frozen.

RFG4E therefore separates two independently auditable coordinates:

```text
alpha_c              <- spectral / analytic genealogy
C_p                   <- project SU(3) plaquette action
```

The physical Wilson promotion occurs when their independently obtained values satisfy

\[
\boxed{\Delta_{\alpha W}=|C_p-2\alpha_c|=0}
\]

within the declared action-normalization tolerance.

## 5. Canonical information-normalization candidate

RFG4D gives the canonical candidate

\[
\alpha_c^{C}
=\ln\varphi-\kappa\ln2
=0.474839619052230\ldots
\]

with

\[
\kappa=\frac{\ln2}{24\pi}.
\]

If the independently reconstructed project action yields

\[
C_p=2\alpha_c^{C},
\]

then the corresponding Wilson coordinate is fixed to

\[
\boxed{
\beta_W^{C}
=6\alpha_c^{C}
=2.84903771431338\ldots
}
\]

by the action theorem rather than by direct assignment.

The archived coordinate is retained as a separate sensitivity surface until the action coefficient is measured or derived.

## 6. Downstream RF-N1C2 consequence

RF-N1C2 uses

\[
\bar M_G
=\frac{\beta_WM_\star}{6\Gamma_{DC}}.
\]

On a passed RFG4E surface `beta_W=6 alpha_c`,

\[
\boxed{
\bar M_G
=\frac{\alpha_cM_\star}{\Gamma_{DC}}.
}
\]

On the local carrier-scale candidate `M_star=omega_Q/2`,

\[
\boxed{
\bar M_G^{local}
=\frac{\alpha_c\omega_Q}{2\Gamma_{DC}}.
}
\]

Thus the Wilson-coordinate debt in RF-N1C2 can be replaced by one direct action-coefficient defect `Delta_alphaW`.

## 7. Executable defects

Define

\[
\boxed{
\Delta_{Wilson}
=\left|C_p-\frac{\beta_W}{3}\right|,
}
\]

\[
\boxed{
\Delta_g
=\left|g_0^2-\frac2{C_p}\right|,
}
\]

and

\[
\boxed{
\Delta_{\alpha W}
=|C_p-2\alpha_c|.
}
\]

All three vanish on the proposed action-normalized `alpha_c`↔Yang–Mills surface.

## 8. Promotion path

1. reconstruct the project `SU(3)` plaquette action from the holonomic link sector;
2. freeze the exact defect convention `D_p=3-ReTr U_p`;
3. read or derive its coefficient `C_p` before comparison with `alpha_c`;
4. verify the Wilson continuum normalization;
5. evaluate `Delta_alphaW` against the independently frozen `alpha_c` coordinate;
6. only after a zero-defect result transfer `beta_W=6 alpha_c` into RF-N1C/RF-N1C2.

The author/repository/formalism/code may suggest the canonical information coordinate supplies the Yang–Mills bare coupling, yet does not state that physical binding as an established result until the project action coefficient is independently frozen and passes this gate.

## 9. Advancement

```text
project defect D_p                                inherited PASS
S_W=(beta_W/3) sum D_p                            PASS EXACT
project C_p -> beta_W=3 C_p                       PASS EXACT
project C_p -> g_0^2=2/C_p                        PASS EXACT
alpha_c=1/g_0^2 <-> C_p=2 alpha_c                PASS EXACT EQUIVALENCE
canonical alpha_c candidate                       inherited RFG4D
project plaquette action coefficient C_p          OPEN PHYSICAL/DERIVATION GATE
physical beta_W promotion                         OPEN pending C_p
```
