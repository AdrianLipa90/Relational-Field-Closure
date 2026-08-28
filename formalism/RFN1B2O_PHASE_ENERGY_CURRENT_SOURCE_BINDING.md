# RF-N1B2O — Gauge-Covariant Phase-Energy / Noether-Carrier Source Binding

Status: `EXACT_LOCAL_PHASE_ENERGY_CURRENT_FACTORIZATION / COLLECTIVE_ROTOR_MATCH_PASS / PHASE_KINETIC_MATTER_SOURCE_PASS_CONDITIONAL / TOTAL_MATTER_SUM_GATE_OPEN`

RF-N1B2O consumes RF-N1B2L, RF-N1B2M and RF-N1B2N. It closes the carrier-to-energy-density map on the admitted gauge-covariant phase-kinetic matter sector without introducing an electric-charge weighting and without fitting a Newton source coefficient.

## 1. Common gauge-covariant phase sector

RF-N1B2M supplies the gauge-invariant phase one-form

\[
\mathscr D\vartheta=d\vartheta+\mathcal A^{ABE}.
\]

RF-N1B2N supplies the normal proper-time phase rate

\[
\boxed{
r_n:=c\,e_{\hat0}\lrcorner\mathscr D\vartheta
=D_{\hat\tau}\chi
=\frac{D_t\chi}{N_R}
}
\]

on the admitted zero-shift calibrated-lapse sector.

For the complex scalar field

\[
\psi=Ae^{i\vartheta},
\]

RF-N1B2L carries the phase kinetic term and Noether current. On the positive normal-flow sector define

\[
\boxed{
j_\vartheta:=2A^2r_n>0.}
\]

This is the local normal Noether-carrier density associated with the same phase mode used by the collective rotor reduction.

## 2. Local phase-energy density

The local Hamiltonian density of the pure normal phase-rate term is

\[
\boxed{
\mathcal E_\vartheta:=A^2r_n^2.}
\]

Using the Noether density above,

\[
\mathcal E_\vartheta
=A^2r_n^2
=\frac{r_n}{2}(2A^2r_n).
\]

Therefore

\[
\boxed{
\mathcal E_\vartheta
=\epsilon_\vartheta j_\vartheta,
\qquad
\epsilon_\vartheta:=\frac12r_n.
}
\]

RF-N1B2N gives exactly the same energy-per-action-charge coordinate,

\[
\boxed{
\epsilon_N
=\frac12D_{\hat\tau}\chi
=\frac12r_n.
}
\]

Hence the local source factorization is

\[
\boxed{
\mathcal E_\vartheta(x)
=\epsilon_N(x)j_\vartheta(x).
}
\]

This identity is local and therefore remains valid for spatially varying `A(x)` and `r_n(x)` wherever the admitted positive phase sector is regular.

## 3. Phase-sector mass density

The equivalent inertial/gravitating mass-density coordinate of this energy sector is

\[
\boxed{
\rho_\vartheta(x)
:=\frac{\mathcal E_\vartheta(x)}{c^2}
=\frac{\epsilon_N(x)}{c^2}j_\vartheta(x).
}
\]

Using the lapse form from RF-N1B2N,

\[
\boxed{
\rho_\vartheta
=\frac{D_t\chi}{2N_Rc^2}\,j_\vartheta.
}
\]

Thus the RF-N1B source factorization receives a physically typed matter-density realization on the phase-kinetic scalar sector directly from the admitted field and clock dynamics.

## 4. Collective rotor consistency

For a common collective rate `r_n` on a slice,

\[
Q_\vartheta
=\int_\Sigma j_\vartheta dV_h
=2r_n\int_\Sigma A^2dV_h.
\]

RF-N1B2L defines

\[
I_A=2\int_\Sigma A^2dV_h,
\]

so

\[
\boxed{Q_\vartheta=I_Ar_n.}
\]

The integrated phase energy is

\[
H_\vartheta
=\int_\Sigma\mathcal E_\vartheta dV_h
=r_n^2\int_\Sigma A^2dV_h
=\frac12I_Ar_n^2.
\]

Therefore

\[
\boxed{
\frac{H_\vartheta}{Q_\vartheta}
=\frac12r_n
=\epsilon_N.
}
\]

This reproduces the RF-N1B2L/RF-N1B2N collective rotor ratio from the local field densities.

## 5. RFC source-carrier specialization

RF-N1B2 allows any admitted conserved local carrier to seed the normalized source factorization. On this phase-field sector choose the admitted Noether carrier itself:

\[
\boxed{
J_{RFC,\vartheta}^\mu:=J_\vartheta^\mu.
}
\]

Its normal density is `j_theta`, and the source map is now derived within the same matter action:

\[
\boxed{
J_\vartheta^\mu
\longrightarrow
j_\vartheta
\longrightarrow
\mathcal E_\vartheta=\epsilon_Nj_\vartheta
\longrightarrow
\rho_\vartheta=\mathcal E_\vartheta/c^2.
}
\]

This is a sector specialization of the generic RF-N1B2 carrier interface, so it removes the free current-normalization coordinate for this admitted phase-kinetic source sector.

## 6. Electric charge remains a separate projection

RF-M4 supplies the independently typed electromagnetic source projection

\[
J_{EM}^\mu=-\frac1\hbar\mathcal J_Q^\mu,
\]

and for one electric-charge eigenvalue

\[
J_{EM}^\mu=-\frac q\hbar J_\vartheta^\mu.
\]

RF-N1B2O uses `J_theta` before this electric-charge projection. The gravitational phase-energy source therefore retains the common Noether carrier for both charged and electrically neutral phase sectors; the Maxwell source remains the charge-projected branch.

## 7. Total-matter composition gate

The phase-kinetic source is one explicitly derived contribution to the matter energy budget. The total matter stress-energy promotion is represented as a sum of separately admitted sectors,

\[
T_{\mu\nu}^{matter}
=T_{\mu\nu}^{phase}
+T_{\mu\nu}^{amp}
+T_{\mu\nu}^{grad}
+T_{\mu\nu}^{pot/rest}
+\cdots.
\]

Each additional term carries its own action/variation and source provenance. RF-N1B2O promotes only the phase-kinetic carrier-energy factorization and leaves the total-matter sum as the downstream Einstein-source gate.

## 8. RF-N1C specialization

Define

\[
\omega_Q:=r_n=D_{\hat\tau}\chi.
\]

Then on the RF-N1B2O phase-source sector

\[
\boxed{
\rho_\vartheta
=\frac{\omega_Q}{2c^2}j_\vartheta.
}
\]

The Newton coupling coordinate becomes

\[
\boxed{
G_N^{(\vartheta)}
=\frac{c^4\mathcal S_R}{2\pi\omega_Qj_\vartheta}.
}
\]

In natural units, equating to the independently gated double-copy route yields

\[
\boxed{
\beta_W^2\mathcal S_R\omega_Q
=36\Gamma_{DC}^2j_\vartheta.
}
\]

Thus RF-N1C now has a source-current realization that is derived from the same scalar phase sector rather than supplied as an arbitrary generic carrier.

## 9. Executable defects

Reference tests audit

\[
\Delta_E
=|\mathcal E_\vartheta-\epsilon_Nj_\vartheta|,
\]

\[
\Delta_\rho
=\left|\rho_\vartheta-\frac{\epsilon_Nj_\vartheta}{c^2}\right|,
\]

and on a common-rate finite-cell slice

\[
\Delta_{coll}
=\left|\frac{H_\vartheta}{Q_\vartheta}-\frac12r_n\right|.
\]

The positive-source gate requires finite `A`, `r_n>0`, `N_R>0`, and the admitted common gauge/normal-flow conventions.

## 10. Advancement

```text
local gauge-covariant phase rate r_n             PASS via RF-N1B2N
local Noether carrier j_theta=2 A^2 r_n          PASS conditional on admitted phase field
local phase energy E_theta=A^2 r_n^2             PASS conditional on admitted phase Hamiltonian sector
E_theta=(r_n/2) j_theta                           PASS EXACT
rho_theta=epsilon_N j_theta/c^2                   PASS EXACT CONDITIONAL
collective H_theta/Q_theta=r_n/2                  PASS EXACT
phase-sector RFC carrier specialization           PASS CONDITIONAL
charge-projected Maxwell branch                   SEPARATELY TYPED via RF-M4
total matter stress-energy composition            OPEN downstream gate
RF-N1C phase-source specialization                AVAILABLE
```
