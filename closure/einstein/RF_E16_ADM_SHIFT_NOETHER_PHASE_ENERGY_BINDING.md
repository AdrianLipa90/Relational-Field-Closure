# RF-E16 — ADM Shift / Noether Phase-Energy Binding

Status: `EXACT_NONZERO_SHIFT_NORMAL_PHASE_RATE / DIRECTIONAL_RATE_CARRIER_ALIGNMENT_PASS / ENERGY_FUNCTIONAL_SELECTION_OPEN`

RF-E16 source-pins the RF-E14/RF-E15 ADM directional rate carrier into the already admitted RFC phase-energy / Noether sector of RF-N1B2O.

The purpose is to distinguish three exact functions of one common directional rate carrier before physical kinetic-energy promotion.

## 1. Full ADM unit normal

RF-E8 supplies

\[
 ds^2=-N^2(dx^0)^2+h_{ij}(dx^i+b^i dx^0)(dx^j+b^j dx^0),
\qquad x^0=ct.
\]

The future unit normal is

\[
\boxed{
n^\mu=\frac1N(1,-b^i).
}
\]

For the gauge-covariant phase one-form `D vartheta`, RF-N1B2O defines the local normal phase rate

\[
\boxed{
r_n:=c\,n^\mu\mathscr D_\mu\vartheta.
}
\]

Since `c D_0 vartheta = D_t vartheta`, one obtains exactly

\[
\boxed{
r_n
=\frac1N\left(
\mathscr D_t\vartheta
-c\,b^i\mathscr D_i\vartheta
\right).
}
\]

The zero-shift IDT 01AD formula is recovered at `b^i=0`.

## 2. Directional null/phase specialization

Choose a local orthonormal 1+1 event,

\[
N=1,
\qquad
h_{11}=1,
\]

and a locally monochromatic null phase carrier with orientation label `s=+1` or `s=-1` satisfying

\[
\boxed{
c\,\mathscr D_x\vartheta=s\,\omega,}
\qquad
\boxed{\mathscr D_t\vartheta=\omega>0.}
\]

Then

\[
\boxed{
r_n^{(s)}=\omega(1-sb).}
\]

Relative to the zero-shift normal rate `r_0=omega`,

\[
\boxed{
R_s:=\frac{r_n^{(s)}}{r_0}=1-sb.
}
\]

This is exactly the RF-E14 directional null-rate carrier. Its reciprocal is

\[
\boxed{x_s=R_s^{-1}=\frac1{1-sb}.}
\]

Thus the ADM null-characteristic derivation and the gauge-covariant normal phase-rate derivation meet on the same directional rate ratio.

## 3. Existing RF-N1B2O phase-energy coordinates

RF-N1B2O gives

\[
\boxed{j_\vartheta=2A^2r_n,}
\]

\[
\boxed{\mathcal E_\vartheta=A^2r_n^2,}
\]

and

\[
\boxed{\epsilon_N=\frac{\mathcal E_\vartheta}{j_\vartheta}=\frac12r_n.}
\]

For the directional specialization,

\[
\boxed{
\frac{\epsilon_N^{(s)}}{\epsilon_0}=R_s=1-sb,
}
\]

and

\[
\boxed{
\frac{\mathcal E_\vartheta^{(s)}}{\mathcal E_{\vartheta,0}}
=R_s^2=(1-sb)^2.
}
\]

The existing canonical phase-sector energy therefore provides linear and quadratic functions of the same directional rate carrier.

## 4. RF-E14 relative-information coordinate on the same carrier

RF-E14/IDT 05D assigns the dimensionless relative-information cost to the reciprocal factor,

\[
\boxed{
\mathcal I_s
=\Phi(x_s)
=x_s-1-\ln x_s.
}
\]

Since `x_s=1/(1-sb)`,

\[
\boxed{
\mathcal I_s
=\ln(1-sb)+\frac{sb}{1-sb}.
}
\]

Hence one common source-bound directional rate ratio generates three exact coordinates:

```text
rate ratio               R_s = 1 - s b
phase energy/carrier      epsilon_s/epsilon_0 = R_s
phase energy density      Ephase_s/Ephase_0 = R_s^2
information cost          I_s = Phi(1/R_s)
```

RF-E16 promotes this dictionary as the exact bridge result.

## 5. Legendre coordinate

RF-E15 supplies

\[
p_s=s b,
\qquad
x_s=\frac1{1-p_s},
\]

and

\[
\boxed{\Psi(p_s)=-\ln(1-p_s).}
\]

Thus the same rate carrier also has the exact primal-dual representation

\[
\boxed{
\Phi(x_s)+\Psi(p_s)=p_sx_s.
}
\]

The ADM shift coordinate, phase-rate ratio, relative-information cost and rapidity/log-gamma dual coordinates are now linked by exact algebra on one local directional sector.

## 6. Energy-scale candidate from the existing carrier sector

RF-N1B2O provides the zero-shift phase energy-per-carrier scale

\[
\boxed{\epsilon_0=\frac12\omega.}
\]

The already existing RF-N1C/RF-E3 project-side carrier-scale candidate uses

\[
\boxed{M_\star=\epsilon_Q=\frac12\omega_Q}
\]

on its separately gated surface.

Therefore a source-pinned energy scale already exists inside RFC for comparison with a scaled information coordinate,

\[
\boxed{E_{I,s}^{cand}=\epsilon_0\,\Phi(x_s).}
\]

This equation is a typed candidate comparison coordinate. Physical promotion requires the independently gated identification of the relevant carrier scale with the measured/rest-energy scale and a variational statement selecting this information cost as an energy contribution.

## 7. Action-selection frontier

RF-E16 establishes the exact common carrier. The next question is no longer algebraic coincidence but action selection:

```text
same R_s
 -> canonical phase energy      proportional to R_s or R_s^2
 -> relative-information cost   Phi(1/R_s)
 -> Legendre dual               Psi(s b)
```

RF-E17 must test the existing RFC matter action and permissible information-action couplings to determine which combination is a conserved Hamiltonian/Noether observable for a physical moving carrier.

## 8. Validation authority

Reference implementation: `src/rfc/adm_shift_noether_phase_energy.py`.
Reference tests: `tests/reference/test_rfe16_adm_shift_noether_phase_energy.py`.
Validation receipt: `validation/RF_E16_ADM_SHIFT_NOETHER_PHASE_ENERGY_V0_1.json`.

The physical shift map, project-side `M_star` promotion and experimental directional-energy comparison retain their explicit downstream gates.
