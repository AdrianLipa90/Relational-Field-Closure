# RF-N1B2N — Relational-Lapse Normal Phase-Rate Bridge

Status: `ZERO_SHIFT_LAPSE_NORMAL_RATE_EXACT_CONDITIONAL / PHYSICAL_CLOCK_CALIBRATION_GATE_INHERITED / RFC_CURRENT_PROMOTION_OPEN`

RF-N1B2N is the RFC-side consumer of IDT 01AD. It replaces the free normal-rate equality in RF-N1B2M with the already derived IDT relational lapse and the RF-N0 zero-shift temporal coframe.

## 1. Relational lapse input

IDT 05C supplies

\[
\boxed{N_R=d\tau_x/d\tau_{ref}>0.}
\]

After explicit reference-clock calibration to coordinate time `t`,

\[
\boxed{d\hat\tau=N_Rdt.}
\]

The ratio `N_R` remains the exact structural carrier; physical clock calibration is an inherited admission gate.

## 2. RF-N0 zero-shift coframe

RF-N0 supplies

\[
\boxed{\mathcal E^0=N_Rc\,dt}
\]

on the zero-shift patch. The dual temporal frame is

\[
\boxed{e_{\hat0}=(N_Rc)^{-1}\partial_t.}
\]

For the gauge-covariant phase one-form of RF-N1B2M,

\[
\mathscr D\vartheta=d\vartheta+\mathcal A^{ABE},
\]

define the normal proper-time phase rate

\[
\boxed{
r_n^{(\tau)}:=c\,e_{\hat0}\lrcorner\mathscr D\vartheta.}
\]

Therefore

\[
\boxed{r_n^{(\tau)}=N_R^{-1}\mathscr D_t\vartheta.}
\]

## 3. Coordinate-time pullback

RF-N1B2M supplies the common-U(1) pullback. With the trajectory parameterized by calibrated coordinate time,

\[
\boxed{
r_t:=q^*(\mathscr D\vartheta)(\partial_t)=D_t\chi.}
\]

Thus

\[
\boxed{r_n^{(\tau)}=r_t/N_R.}
\]

## 4. Proper-time rotor rate

From

\[
d\hat\tau=N_Rdt
\]

follows

\[
\boxed{
D_{\hat\tau}\chi
=\frac{1}{N_R}D_t\chi
=\frac{r_t}{N_R}.}
\]

Hence the zero-shift lapse/coframe bridge gives

\[
\boxed{
D_{\hat\tau}\chi
=r_n^{(\tau)}
=c\,e_{\hat0}\lrcorner\mathscr D\vartheta.}
\]

The corresponding exact coordinate-time identity is

\[
\boxed{r_t=N_Rr_n^{(\tau)}.}
\]

## 5. Executable defects

Define

\[
\boxed{
\Delta_{Nr}
=\frac{|r_t-N_Rr_n^{(\tau)}|}{|r_t|}}
\]

and

\[
\boxed{
\Delta_{\tau n}
=\frac{|D_{\hat\tau}\chi-r_n^{(\tau)}|}
{|D_{\hat\tau}\chi|}.}
\]

The theorem requires a common positive `N_R`, the same calibrated coordinate-time ID and the same zero-shift coframe ID.

## 6. Generator consequence

RF-N1B2L supplies the coefficient reduction

\[
I_A=I_\phi
\]

on the common scalar-field/rotor sector. Therefore

\[
Q_\vartheta=I_A r_n^{(\tau)},
\qquad
P_\Phi=I_\phi D_{\hat\tau}\chi,
\]

and the RF-N1B2N rate theorem yields

\[
\boxed{Q_\vartheta=P_\Phi.}
\]

After Euler/Berry closure,

\[
\boxed{Q_\vartheta^{EB}=P_\Phi^{EB}=J-J_I^{EB}.}
\]

## 7. RFC epsilon coordinate

On the positive common-generator sector,

\[
\epsilon_N^{EB}
=\frac{H_\Phi^{EB}}{Q_\vartheta^{EB}}
=\frac12D_{\hat\tau}\chi.
\]

The lapse form is therefore

\[
\boxed{
\epsilon_N^{EB}
=\frac{1}{2N_R}D_t\chi
=\frac{r_t}{2N_R}.}
\]

After the separately measured RF-N1B2K current promotion,

\[
Q_\Sigma=Q_\vartheta=P_\Phi^{EB}
\]

and the downstream source normalization is

\[
\boxed{\epsilon_Q=\epsilon_N^{EB}=r_t/(2N_R).}
\]

## 8. Admission surface

The exact conditional theorem uses:

- RF-N1B2M common U(1) bundle/patch/ABE connection;
- IDT 05C calibrated reference clock;
- RF-N0 zero-shift temporal coframe;
- the same positive `N_R` in elapsed and coframe roles;
- RF-N1B2L coefficient reduction;
- common finite-generator measure/support.

Physical `J_Q^mu <-> J_theta^mu` remains the measured downstream promotion gate.

## 9. PNCS target

Proposed contract:

`PNCS_PNV_RELATIONAL_LAPSE_NORMAL_PHASE_RATE_V0_1`

Proposed semantic loop:

`SOURCE.PHASE.NOETHER.RELATIONAL_LAPSE_NORMAL_RATE.ROUNDTRIP`
