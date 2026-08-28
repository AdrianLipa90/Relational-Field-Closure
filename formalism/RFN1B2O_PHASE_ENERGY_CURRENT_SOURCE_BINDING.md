# RF-N1B2O — Gauge-Covariant Phase-Energy / Noether-Carrier Source Binding

Status: `EXACT_LOCAL_PHASE_ENERGY_CURRENT_FACTORIZATION / COLLECTIVE_ROTOR_MATCH_PASS / RF_E6_LORENTZIAN_ALIGNMENT_PASS / PHASE_KINETIC_MATTER_SOURCE_PASS_CONDITIONAL / TOTAL_MATTER_SUM_GATE_OPEN`

RF-N1B2O consumes RF-N1B2L, RF-N1B2M and RF-N1B2N. It closes the carrier-to-energy-density map on the admitted gauge-covariant phase-kinetic matter sector.

## 1. Common gauge-covariant phase sector

RF-N1B2M supplies

\[
\mathscr D\vartheta=d\vartheta+\mathcal A^{ABE}.
\]

RF-N1B2N supplies

\[
\boxed{
r_n:=c\,e_{\hat0}\lrcorner\mathscr D\vartheta
=D_{\hat\tau}\chi
=\frac{D_t\chi}{N_R}.
}
\]

For

\[
\psi=Ae^{i\vartheta},
\]

define the local normal Noether carrier density

\[
\boxed{j_\vartheta:=2A^2r_n>0.}
\]

## 2. Local phase-energy density

The local phase-kinetic Hamiltonian density is

\[
\boxed{\mathcal E_\vartheta:=A^2r_n^2.}
\]

Therefore

\[
\boxed{
\mathcal E_\vartheta
=\epsilon_Nj_\vartheta,
\qquad
\epsilon_N=\frac12r_n
=\frac12D_{\hat\tau}\chi.
}
\]

RF-E6 shows that this positive normal-flow reduction follows from the canonical `(-,+,+,+)` scalar action

\[
\mathcal L=-D_\mu\psi^*D^\mu\psi-V.
\]

## 3. Phase-sector mass density

\[
\boxed{
\rho_\vartheta
=\frac{\mathcal E_\vartheta}{c^2}
=\frac{\epsilon_N}{c^2}j_\vartheta
=\frac{D_t\chi}{2N_Rc^2}j_\vartheta.
}
\]

## 4. Collective rotor consistency

For a common collective rate,

\[
Q_\vartheta
=2r_n\int_\Sigma A^2dV_h.
\]

With

\[
I_A=2\int_\Sigma A^2dV_h,
\]

one has

\[
\boxed{Q_\vartheta=I_Ar_n.}
\]

The integrated phase energy is

\[
H_\vartheta
=\frac12I_Ar_n^2,
\]

so

\[
\boxed{
\frac{H_\vartheta}{Q_\vartheta}
=\frac12r_n
=\epsilon_N.
}
\]

## 5. RFC source-carrier specialization

On this phase-field sector,

\[
\boxed{J_{RFC,\vartheta}^\mu:=J_\vartheta^\mu.}
\]

The source map is

\[
\boxed{
J_\vartheta^\mu
\longrightarrow j_\vartheta
\longrightarrow \mathcal E_\vartheta=\epsilon_Nj_\vartheta
\longrightarrow \rho_\vartheta=\mathcal E_\vartheta/c^2.
}
\]

## 6. Electric charge as a separate projection

RF-M4/RF-E6 supply

\[
\boxed{J_{EM}^\mu=\frac1\hbar\mathcal J_Q^\mu.}
\]

For one charge eigenvalue,

\[
\boxed{J_{EM}^\mu=\frac q\hbar J_\vartheta^\mu.}
\]

On the RF-N1B2K zero-defect RFC carrier surface,

\[
\boxed{J_{EM}^\mu=\frac q\hbar J_{RFC,\vartheta}^\mu.}
\]

The matter/gravity source uses the unweighted carrier and its energy, while Maxwell uses the charge-projected image. The neutral `Q=0` sector therefore carries matter stress-energy with an exact Maxwell-null current.

## 7. Total-matter composition gate

The phase-kinetic contribution is one explicit matter sector. The total stress tensor is assembled from separately derived contributions,

\[
\boxed{
T_{\mu\nu}^{matter}
=T_{\mu\nu}^{phase}
+T_{\mu\nu}^{amp/grad}
+T_{\mu\nu}^{pot/rest}
+\cdots.
}
\]

RF-E4 and RF-E6 now provide the explicit phase/charged-matter stress tensors. The remaining Einstein source gate is the complete admitted sector composition.

## 8. RF-N1C specialization

Define

\[
\omega_Q:=r_n=D_{\hat\tau}\chi.
\]

Then

\[
\boxed{
\rho_\vartheta
=\frac{\omega_Q}{2c^2}j_\vartheta.
}
\]

The Newton coupling coordinate is

\[
\boxed{
G_N^{(\vartheta)}
=\frac{c^4\mathcal S_R}{2\pi\omega_Qj_\vartheta}.
}
\]

In natural units, the independently gated double-copy comparison yields

\[
\boxed{
\beta_W^2\mathcal S_R\omega_Q
=36\Gamma_{DC}^2j_\vartheta.
}
\]

## 9. Executable defects

Reference tests audit

\[
\Delta_E=|\mathcal E_\vartheta-\epsilon_Nj_\vartheta|,
\]

\[
\Delta_\rho
=\left|\rho_\vartheta-\frac{\epsilon_Nj_\vartheta}{c^2}\right|,
\]

and

\[
\Delta_{coll}
=\left|\frac{H_\vartheta}{Q_\vartheta}-\frac12r_n\right|.
\]

## 10. Advancement

```text
local gauge-covariant phase rate                    PASS
local Noether carrier j_theta=2 A^2 r_n             PASS CONDITIONAL
local phase energy E_theta=A^2 r_n^2                PASS CONDITIONAL
E_theta=(r_n/2) j_theta                              PASS EXACT
rho_theta=epsilon_N j_theta/c^2                      PASS EXACT CONDITIONAL
collective H_theta/Q_theta=r_n/2                     PASS EXACT
canonical Lorentzian action alignment                PASS via RF-E6
charge-projected Maxwell branch                      PASS TYPED via RF-M4/RF-E6
explicit phase/charged-matter stress tensor          PASS via RF-E4/RF-E6
total matter stress-energy composition               NEXT
```
