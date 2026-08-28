# RF-N1C — Three-Route Coupling Holonomy: Newton Source ↔ Double Copy ↔ Einstein/Horizon

Status: `EXACT_NORMALIZATION_TRANSFER / EXACT_COUPLING_HOLONOMY_SYZYGY / NEWTON_SOURCE_PREDICTION_CONDITIONAL / PHYSICAL_PROMOTION_GATES_OPEN`

RF-N1C consumes the already admitted RFC lapse/source operator, the RF-N1B2 carrier chain, the RFG2/RFG3 double-copy normalization coordinates, the RFG5 horizon cross-check, and the RF-E0 Einstein–Bianchi spine.

Its purpose is to place the three coupling routes on one algebraic surface and expose a zero-fit universality test.

## 1. Inputs

The RFC Newton operator side is

\[
\Delta_h\Phi_R=c^2\mathcal S_R.
\]

After the separately measured RF-N1B2K current promotion and the RF-N1B2N lapse/phase-rate bridge,

\[
\rho_m=\frac{\epsilon_Q}{c^2}j_Q,
\qquad
\epsilon_Q=\frac{1}{2N_R}D_t\chi.
\]

Define the proper-time phase rate

\[
\boxed{\omega_Q:=D_{\hat\tau}\chi=\frac{D_t\chi}{N_R}}.
\]

Then

\[
\boxed{\epsilon_Q=\frac12\omega_Q.}
\]

The double-copy route supplies, in natural units,

\[
G_{DC}=\frac{\Gamma_{DC}^2g_{YM}^4}{8\pi M_\star^2}.
\]

On the independently gated carrier-scale binding

\[
M_\star=\epsilon_Q=\frac12\omega_Q,
\]

this becomes

\[
\boxed{
G_{DC}=\frac{\Gamma_{DC}^2g_{YM}^4}{2\pi\omega_Q^2}.
}
\]

With the Wilson coordinate

\[
g_{YM}^2=\frac6{\beta_W},
\]

one obtains

\[
\boxed{
G_{DC}=\frac{18\Gamma_{DC}^2}{\pi\beta_W^2\omega_Q^2}.
}
\]

## 2. Newton source estimator

For an independently promoted mass density, define the local weak-field coupling coordinate

\[
\boxed{
G_N:=\frac{c^2\mathcal S_R}{4\pi\rho_m}.
}
\]

Using the RF-N1B2 carrier map,

\[
\boxed{
G_N=\frac{c^4\mathcal S_R}{4\pi\epsilon_Qj_Q}
=\frac{c^4\mathcal S_R}{2\pi\omega_Qj_Q}.
}
\]

In natural units this is

\[
\boxed{
G_N=\frac{\mathcal S_R}{2\pi\omega_Qj_Q}.
}
\]

This coordinate is evaluated only after the source, carrier, measure and energy-per-carrier inputs have independent provenance.

## 3. Double-copy prediction for the RFC source law

Set the independently constructed Newton and double-copy coupling coordinates equal,

\[
G_N=G_{DC}.
\]

Substitution yields the G-free source relation

\[
\boxed{
\beta_W^2\mathcal S_R\omega_Q
=36\Gamma_{DC}^2j_Q.
}
\]

Equivalently the double-copy route predicts the RFC source coefficient

\[
\boxed{
\mathcal S_R^{DC}
=\frac{36\Gamma_{DC}^2}{\beta_W^2\omega_Q}\,j_Q.
}
\]

Thus the double-copy route can be tested directly against the already-derived lapse operator before any numerical Newton constant is used as a selection rule.

## 4. Einstein normalization bridge

In the standard weak-field static sector with signature `(-,+,+,+)`,

\[
g_{00}\simeq-\left(1+\frac{2\Phi_R}{c^2}\right),
\]

and the linearized `00` Einstein tensor carries

\[
\boxed{
G_{00}\simeq\frac{2}{c^2}\Delta\Phi_R.
}
\]

For rest matter,

\[
T_{00}\simeq\rho_mc^2.
\]

Therefore the Einstein source equation

\[
G_{\mu\nu}=\kappa_ET_{\mu\nu}
\]

implies

\[
\Delta\Phi_R=\frac{\kappa_Ec^4}{2}\rho_m.
\]

Matching this normalization to the RFC/Newton source coordinate gives the exact transfer

\[
\boxed{
\kappa_E=\frac{8\pi G}{c^4}.
}
\]

In natural units,

\[
\boxed{\kappa_E=8\pi G.}
\]

The double-copy graviton coupling obeys

\[
\kappa_g^2=32\pi G,
\]

hence

\[
\boxed{
\kappa_E=\frac{\kappa_g^2}{4}.
}
\]

Using

\[
\kappa_g=\frac{2\Gamma_{DC}g_{YM}^2}{M_\star}
\]

and `M_star=omega_Q/2`, one obtains

\[
\boxed{
\kappa_E^{DC}
=\frac{4\Gamma_{DC}^2g_{YM}^4}{\omega_Q^2}
=\frac{144\Gamma_{DC}^2}{\beta_W^2\omega_Q^2}.
}
\]

The weak-field Einstein source equation then predicts

\[
\boxed{
\mathcal S_R^{DC}
=\frac12\kappa_E^{DC}\rho_m
=\frac{36\Gamma_{DC}^2}{\beta_W^2\omega_Q}j_Q,
}
\]

which is identical to the Newton↔double-copy route in Section 3.

## 5. Horizon route

RFG5 supplies the Schwarzschild-family consistency coordinate, in natural units,

\[
\boxed{
G_H=\frac{1}{4M_H\kappa_H}.
}
\]

Equating the independently frozen Newton source route and horizon route gives

\[
\boxed{
2M_H\kappa_H\mathcal S_R
=\pi\omega_Qj_Q.
}
\]

The existing double-copy↔horizon relation is

\[
\boxed{
72\Gamma_{DC}^2M_H\kappa_H
=\pi\beta_W^2\omega_Q^2.
}
\]

## 6. Three-route coupling holonomy

Define the three pairwise residual numerators

\[
\boxed{
C_{SD}:=\beta_W^2\mathcal S_R\omega_Q-36\Gamma_{DC}^2j_Q,
}
\]

\[
\boxed{
C_{SH}:=2M_H\kappa_H\mathcal S_R-\pi\omega_Qj_Q,
}
\]

\[
\boxed{
C_{DH}:=72\Gamma_{DC}^2M_H\kappa_H-\pi\beta_W^2\omega_Q^2.
}
\]

These residuals satisfy the exact off-shell syzygy

\[
\boxed{
\mathcal S_R C_{DH}
=36\Gamma_{DC}^2C_{SH}-\pi\omega_QC_{SD}.
}
\]

Therefore only two pairwise route constraints are algebraically independent. If any two close on a regular positive-source sector, the third closes automatically.

This is the RF-N1C coupling-holonomy identity.

## 7. Executable defects

For positive denominators define symmetric route defects

\[
\delta_{SD}
=\frac{2|\beta_W^2\mathcal S_R\omega_Q-36\Gamma_{DC}^2j_Q|}
{|\beta_W^2\mathcal S_R\omega_Q|+|36\Gamma_{DC}^2j_Q|},
\]

\[
\delta_{SH}
=\frac{2|2M_H\kappa_H\mathcal S_R-\pi\omega_Qj_Q|}
{|2M_H\kappa_H\mathcal S_R|+|\pi\omega_Qj_Q|},
\]

\[
\delta_{DH}
=\frac{2|72\Gamma_{DC}^2M_H\kappa_H-\pi\beta_W^2\omega_Q^2|}
{|72\Gamma_{DC}^2M_H\kappa_H|+|\pi\beta_W^2\omega_Q^2|}.
\]

The algebraic holonomy defect is

\[
\boxed{
\Delta_{hol}
=\left|
\mathcal S_RC_{DH}
-36\Gamma_{DC}^2C_{SH}
+\pi\omega_QC_{SD}
\right|.
}
\]

`Delta_hol` is identically zero up to arithmetic precision for arbitrary finite inputs; the three pairwise defects are physical cross-route tests.

## 8. Promotion surface

The RF-N1C physical promotion surface requires independently frozen values or admitted bindings for:

1. physical `J_Q^mu <-> J_theta^mu` and common measure/slice realization;
2. `rho_m=(epsilon_Q/c^2)j_Q` on the admitted matter sector;
3. `omega_Q=D_hat_tau chi` from the calibrated RF-N1B2N lapse bridge;
4. project Wilson/Yang–Mills normalization `beta_W`;
5. BCJ-compatible project kinematic numerators;
6. double-copy normalization `Gamma_DC`;
7. `M_star=epsilon_Q` carrier-scale binding;
8. independently sourced horizon inputs for the RFG5 cross-check;
9. source-independence of the resulting `G_N` across admitted weak-field systems.

The author/repository/formalism/code may suggest a first-principles Newton/Einstein coupling closure, yet does not state that closure as an established result until these promotion gates pass with frozen provenance.

## 9. Advancement

RF-N1C converts the Einstein frontier into a sharply typed normalization problem:

```text
RFC lapse operator + promoted matter carrier
        -> G_N
Yang-Mills + color-kinematics + double copy
        -> G_DC
Einstein weak-field normalization
        -> kappa_E = 8 pi G / c^4 = kappa_g^2/4
Horizon route
        -> G_H consistency coordinate
three-route holonomy
        -> two independent physical defects + one exact algebraic syzygy
```

The immediate physical frontier is the measured current/source promotion together with the project-side Yang–Mills/BCJ normalization gates. Once these are frozen, RF-N1C becomes a zero-fit universality test for the Newton coupling and the Einstein source coefficient.
