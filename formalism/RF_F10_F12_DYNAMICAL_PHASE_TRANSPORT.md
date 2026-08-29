# RF-F10–RF-F12 — Dynamical Phase Transport, EOS Integration and FLRW Limit

Status: `PHASE_ENERGY_CURVATURE_EXACT / DUST_TRANSPORT_EXACT / FLRW_SCALING_EXACT_CONDITIONAL`

RF-F10–RF-F12 are stacked on the RF-F0–RF-F9 foundational spine. They identify where bulk phase-source dynamics live, derive the exact comoving phase-energy transport equation, integrate the constant-`w` source family, and recover the homogeneous-isotropic scale-factor laws.

Let

\[
X:=\Phi_C+\kappa,
\qquad
\Omega:=\mathscr D\vartheta,
\qquad
\epsilon_G=B\omega X,
\qquad
\omega=u^\mu\Omega_\mu.
\]

The RF-F5 phase-energy one-form is

\[
\boxed{\Theta_G=BX\Omega}.
\]

---

## RF-F10 — Phase-energy curvature and boundary-flux theorem

Take the exterior derivative:

\[
 d\Theta_G
=d(BX)\wedge\Omega+BX\,d\Omega.
\]

On the local relational-lift branch

\[
 d\Phi_C=\Omega,
\qquad
 d\Omega=\mathcal F_-,
\]

so

\[
 d(BX)=X\,dB+B\Omega.
\]

Because `Omega wedge Omega=0`, the exact phase-energy curvature is

\[
\boxed{
\mathcal K_G
:=d\Theta_G
=
X\,dB\wedge\Omega
+BX\mathcal F_-.
}
\]

Thus the phase-energy one-form carries bulk curvature through two explicit channels:

\[
\boxed{dB\wedge\Omega}
\qquad\text{and}\qquad
\boxed{\mathcal F_-}.
\]

On a constant-`B`, flat-connection patch,

\[
\boxed{\mathcal K_G=0}.
\]

### F10.1 Source as a current contraction

RF-F6 gives

\[
\rho_G=BXJ^\mu\Omega_\mu.
\]

On the local branch `Omega=dX`, define the flux current

\[
\boxed{
\mathcal F_G^\mu
:=\frac12BX^2J^\mu.
}
\]

Direct differentiation gives

\[
\boxed{
\nabla_\mu\mathcal F_G^\mu
=
\rho_G
+
\frac12X^2J^\mu\nabla_\mu B
+
\frac12BX^2\nabla_\mu J^\mu.
}
\]

Hence

\[
\boxed{
\rho_G
=
\nabla_\mu\mathcal F_G^\mu
-
\frac12X^2J^\mu\nabla_\mu B
-
\frac12BX^2\nabla_\mu J^\mu.
}
\]

On the constant-`B`, conserved-current branch this reduces to the exact boundary-flux identity

\[
\boxed{
\rho_G=\nabla_\mu\mathcal F_G^\mu.
}
\]

The bulk source ledger is therefore carried by the phase-energy curvature, `B` transport, current exchange, and the independently admitted Hamiltonian/potential terms.

---

## RF-F11 — Comoving phase-energy transport

From

\[
\epsilon_G=B\omega X,
\qquad
\dot X=\omega,
\]

the comoving derivative is

\[
\boxed{
\dot\epsilon_G
=
\dot B\,\omega X
+B\dot\omega X
+B\omega^2.
}
\]

RF-F7 gives the dynamic-`Lambda0` dust balance

\[
\dot\epsilon_G
=-\frac{\dot\Lambda_0}{\kappa_E n}.
\]

Therefore the exact transport equation is

\[
\boxed{
X(\dot B\,\omega+B\dot\omega)
+B\omega^2
=
-\frac{\dot\Lambda_0}{\kappa_E n}.
}
\]

### F11.1 Constant-Lambda dust branch

For

\[
\dot\Lambda_0=0,
\]

we obtain

\[
\boxed{
\frac{d}{d\tau}(B\omega X)=0.
}
\]

Thus

\[
\boxed{B\omega X=\epsilon_0}
\]

is a comoving invariant.

For constant `B`,

\[
\boxed{
X\dot\omega+\omega^2=0.
}
\]

Equivalently,

\[
\boxed{\omega X=C}.
\]

Since `dot X=omega`,

\[
X\dot X=C
\]

and therefore

\[
\boxed{
X^2(\tau)
=
X_0^2+2C(\tau-\tau_0).
}
\]

This is the exact constant-`B` pressureless phase-transport solution.

### F11.2 Integrated constant-w family

RF-F8 gives

\[
\frac{d\ln|BX|}{d\ln|\omega|}=3w_G-1.
\]

For constant `w_G`, integration gives

\[
\boxed{
BX=C_w|\omega|^{3w_G-1}.
}
\]

Hence

\[
\boxed{
\epsilon_G
=
\operatorname{sgn}(\omega)
C_w|\omega|^{3w_G}.
}
\]

On a positive-orientation branch:

\[
\boxed{
\epsilon_G=C_w\omega^{3w_G}.
}
\]

The three canonical surfaces become

\[
\boxed{w_G=0:\quad BX\propto|\omega|^{-1},\quad\epsilon_G=\mathrm{const}},
\]

\[
\boxed{w_G=\frac13:\quad BX=\mathrm{const},\quad\epsilon_G\propto|\omega|},
\]

\[
\boxed{w_G=-1:\quad BX\propto|\omega|^{-4},\quad\epsilon_G\propto|\omega|^{-3}}.
\]

---

## RF-F12 — Homogeneous-isotropic phase-clock limit

On a homogeneous-isotropic comoving congruence,

\[
\boxed{\theta=3H=3\frac{\dot a}{a}}.
\]

RF-F8 number-current continuity gives

\[
\theta=-3\frac{d\ln|\omega|}{d\tau}.
\]

Therefore

\[
\frac{\dot a}{a}
=-\frac{d\ln|\omega|}{d\tau},
\]

so

\[
\boxed{
\frac{d}{d\tau}\ln(a|\omega|)=0
}
\]

and

\[
\boxed{a|\omega|=\mathrm{const}}.
\]

Thus

\[
\boxed{|\omega|\propto a^{-1}}.
\]

The RF-F3 phase-cell geometry then scales as

\[
\boxed{\ell_\phi\propto a},
\]

\[
\boxed{\mathcal A_R\propto a^2},
\]

\[
\boxed{V_R\propto a^3}.
\]

Combining with RF-F8,

\[
\rho_G\propto|\omega|^{3(1+w_G)},
\]

gives

\[
\boxed{
\rho_G\propto a^{-3(1+w_G)}.
}
\]

Therefore the canonical phase-cell branch reproduces the standard homogeneous perfect-fluid density laws:

\[
\boxed{w_G=0:\quad\rho_G\propto a^{-3}},
\]

\[
\boxed{w_G=\frac13:\quad\rho_G\propto a^{-4}},
\]

\[
\boxed{w_G=-1:\quad\rho_G=\mathrm{const}}.
\]

The corresponding phase-rate relation

\[
\boxed{a\omega=\mathrm{const}}
\]

holds with signed `omega` on a fixed-orientation branch.

---

## Canonical advancement

```text
Theta_G=B X Dtheta                                  PASS PARENT
K_G=dTheta_G=X dB^Dtheta + B X F_minus             PASS EXACT LOCAL
constant-B flat-connection K_G=0                   PASS EXACT
source/boundary-flux divergence identity            PASS EXACT
phase-energy derivative                             PASS EXACT
dynamic-Lambda phase transport                      PASS EXACT PARENT COMPOSITION
constant-Lambda epsilon_G invariant                 PASS EXACT
constant-B dust X*omega invariant                   PASS EXACT
constant-B dust X^2 affine in proper time           PASS EXACT
constant-w BX scaling family                        PASS EXACT CONDITIONAL
FLRW a|omega| invariant                             PASS EXACT CONDITIONAL
phase-cell length/area/volume scale as a/a^2/a^3   PASS EXACT CONDITIONAL
rho_G proportional to a^[-3(1+w)]                  PASS EXACT CONDITIONAL
physical common phase-cell cosmological binding     OPEN INPUT
physical EOS receipt                                OPEN INPUT
physical B transport law                            OPEN INPUT
physical Lambda exchange receipt                    OPEN INPUT
```

## Validation authority

Reference implementation: `src/rfc/dynamical_phase_transport.py`.

Reference tests: `tests/reference/test_rff10_f12_dynamical_phase_transport.py`.

Validation receipt: `validation/RF_F10_F12_DYNAMICAL_PHASE_TRANSPORT_V0_1.json`.
