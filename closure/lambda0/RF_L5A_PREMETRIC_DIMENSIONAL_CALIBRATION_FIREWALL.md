# RF-L5A — Premetric Dimensional Calibration Firewall

Status: `RF_L5_ALGEBRAIC_CORE_PRESERVED / PREMETRIC_MASS_SLOT_RETYPED / AFFINE_CLOCK_LENGTH_CALIBRATION_EXACT / LIGHTCONE_RATIO_GATE_EXACT / RFC_MASS_FREQUENCY_BINDING_EXACT_GIVEN_CALIBRATION / VARIABLE_LAPSE_COVARIANT_EXTENSION_OPEN`

RF-L5A consumes the validated RF-L5 graph/operator bridge together with IDT 02B/02C and the IDT 05C clock/lapse interface. Its purpose is to separate the premetric spectral slots carried by the ordering coordinate from the physical inverse-length scalar mass carried by the RFC covariant action.

The RF-L5 algebraic identity

\[
K_0=\frac{N_s}{\ln2}G_u^{(2)}(u)
\]

remains unchanged. The refinement concerns the physical calibration of the second-order equation.

## 1. Premetric ordering equation

IDT 02B uses dot derivatives with respect to the ordering parameter `lambda` and writes

\[
\frac{d\mathcal H_T}{d\lambda}
=-p^\dagger C_\eta p.
\]

Accordingly, the conservative finite-graph scalar equation is typed at RF-L5A as

\[
\boxed{
\frac{d^2\phi_I}{d\lambda^2}
+\left(K_0+\mu_\lambda^2 I\right)\phi_I=0,
}
\]

where `mu_lambda^2` is the premetric homogeneous spectral-gap coefficient in the same ordering-coordinate normalization as `d^2/dlambda^2` and `K0`.

Using the exact 01D identity,

\[
\boxed{
\frac{d^2\phi_I}{d\lambda^2}
+\left[
\frac{N_s}{\ln2}G_u^{(2)}(u)
+\mu_\lambda^2 I
\right]\phi_I=0.
}
\]

The RFC geometric mass coordinate remains

\[
\boxed{
m_I^2=\frac{\alpha_I}{\kappa_E},
\qquad [m_I^2]=L^{-2},
}
\]

and is bound to `mu_lambda` only after clock/length calibration.

## 2. Local affine physical calibration

Take one local calibration patch on which the premetric ordering and cell coordinates `(lambda, xi)` are mapped affinely to physical coordinates `(t,X)`:

\[
\boxed{
t-t_\star=\Gamma_t(\lambda-\lambda_\star),
\qquad
X-X_\star=\Gamma_x(\xi-\xi_\star),
}
\]

with

\[
\Gamma_t>0,
\qquad
\Gamma_x>0.
\]

Then exactly

\[
\partial_\lambda=\Gamma_t\partial_t,
\qquad
\partial_\xi=\Gamma_x\partial_X,
\]

and therefore

\[
\partial_\lambda^2=\Gamma_t^2\partial_t^2,
\qquad
\partial_\xi^2=\Gamma_x^2\partial_X^2.
\]

## 3. Premetric continuum transformation

IDT 02C supplies the conservative long-wave premetric equation

\[
\boxed{
\partial_\lambda^2\phi_I
-M_{eff}\partial_\xi^2\phi_I
+\mu_\lambda^2\phi_I=0.
}
\]

Under the affine calibration above, division by `Gamma_t^2` gives

\[
\boxed{
\partial_t^2\phi_I
-c_{cal}^2\partial_X^2\phi_I
+\Omega_m^2\phi_I=0,
}
\]

where

\[
\boxed{
c_{cal}^2
:=M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2},
}
\]

and

\[
\boxed{
\Omega_m^2
:=\frac{\mu_\lambda^2}{\Gamma_t^2}.
}
\]

Thus the physical wave speed is determined by the premetric mobility coefficient together with the physical length/time calibration ratio.

## 4. Exact light-cone calibration condition

The locally flat RF-L2 scalar equation with signature `(-,+,+,+)` is

\[
\Box\phi_I-m_I^2\phi_I=0.
\]

Multiplying the locally flat equation by `c^2` gives

\[
\boxed{
\partial_t^2\phi_I
-c^2\nabla_X^2\phi_I
+c^2m_I^2\phi_I=0.
}
\]

Therefore the RF-L5A physical calibration conditions are

\[
\boxed{
M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2}=c^2
}
\]

and

\[
\boxed{
\frac{\mu_\lambda^2}{\Gamma_t^2}=c^2m_I^2.
}
\]

Equivalently,

\[
\boxed{
\frac{\Gamma_x}{\Gamma_t}
=\frac{c}{\sqrt{M_{eff}}}
}
\]

and

\[
\boxed{
\mu_\lambda^2
=\Gamma_t^2c^2m_I^2
=\Gamma_t^2c^2\frac{\alpha_I}{\kappa_E}.
}
\]

These two equations are the dimensional firewall between the premetric IDT wave chart and the RFC physical Lorentzian scalar chart.

## 5. Relation to IDT 05C clock calibration

IDT 05C gives

\[
d\tau_{ref}=\phi_{ref}\,d\lambda
\]

and an empirical physical clock conversion

\[
dt=T_{ref}\,d\tau_{ref}.
\]

On a fixed-reference local patch,

\[
\boxed{
\Gamma_t
:=\frac{dt}{d\lambda}
=T_{ref}\phi_{ref}>0.
}
\]

Therefore the premetric mass-gap coefficient becomes

\[
\boxed{
\mu_\lambda^2
=(T_{ref}\phi_{ref})^2c^2m_I^2.
}
\]

The IDT relational lapse

\[
N_R=\frac{d\tau_x}{d\tau_{ref}}
\]

remains available for the subsequent variable-lapse curved-spacetime extension. RF-L5A uses the fixed-reference affine patch required for the exact constant-coefficient calibration above.

## 6. Spatial calibration slot

Let one premetric cell-coordinate increment `d xi` correspond locally to the physical length increment

\[
dX=\Gamma_x\,d\xi.
\]

If a lattice cell of coordinate width `h` is assigned an independently calibrated physical width `L_h`, then

\[
\boxed{
\Gamma_x=\frac{L_h}{h}.
}
\]

The light-cone condition becomes

\[
\boxed{
\frac{L_h}{h\,T_{ref}\phi_{ref}}
=\frac{c}{\sqrt{M_{eff}}}.
}
\]

IDT 01L supplies the exact phase-clock length carrier

\[
\ell_\varphi=\frac{c}{|\omega_t|},
\]

which may enter a downstream cell/area calibration once the target cell geometry selects how `ell_phi` maps into `L_h`. RF-L5A keeps that spatial assignment as an explicit calibration interface.

## 7. Unit-gauge specialization

If a calibrated chart is chosen with

\[
\Gamma_t=1,
\qquad
\Gamma_x=1,
\]

then the general conditions reduce to

\[
\boxed{M_{eff}=c^2}
\]

and

\[
\boxed{\mu_\lambda^2=c^2m_I^2.}
\]

Thus the simple `M_eff=c^2` statement is retained as the unit-calibration specialization of the general ratio condition rather than as the general premetric identity.

In natural units `c=1`, the same specialization gives

\[
M_{eff}=1,
\qquad
\mu_\lambda^2=m_I^2.
\]

## 8. Correctly typed homogeneous frequency

The premetric connected-graph constant mode obeys

\[
\frac{d^2a_0}{d\lambda^2}
+\mu_\lambda^2 a_0=0.
\]

Its ordering-coordinate frequency is

\[
\omega_\lambda^2=\mu_\lambda^2.
\]

After physical clock calibration,

\[
\omega_t^{(KG)}
=\frac{\omega_\lambda}{\Gamma_t},
\]

so the exact physical mass-frequency relation is

\[
\boxed{
\left(\omega_t^{(KG)}\right)^2
=c^2m_I^2
=c^2\frac{\alpha_I}{\kappa_E}.
}
\]

A future comparison to an independently admitted IDT phase-clock spectral line must therefore compare frequencies only after they share the same calibrated physical time coordinate.

## 9. RF-L5 promotion repair

The RF-L5 validation receipt `561/561 PASS` remains the authority for the graph/operator algebra and its regression suite. RF-L5A adds the physical-coordinate typing required for promotion beyond the premetric graph level.

The corrected dependency is

```text
01D Shannon response
-> K0 premetric stiffness
-> graph conservative spectral equation in lambda
-> (Gamma_t, Gamma_x) physical calibration
-> local Lorentzian Klein-Gordon equation
-> curved variable-lapse covariant extension
```

## 10. Executable reference gates

RF-L5A tests verify:

1. affine derivative transformation under positive `Gamma_t`, `Gamma_x`;
2. calibrated wave coefficient `c_cal^2=M_eff Gamma_x^2/Gamma_t^2`;
3. calibrated mass-frequency coefficient `Omega_m^2=mu_lambda^2/Gamma_t^2`;
4. exact light-cone ratio `Gamma_x/Gamma_t=c/sqrt(M_eff)`;
5. exact mass-slot binding `mu_lambda^2=Gamma_t^2 c^2 alpha_I/kappa_E`;
6. 05C fixed-reference clock factor `Gamma_t=T_ref phi_ref`;
7. cell-width factor `Gamma_x=L_h/h`;
8. unit-gauge specialization;
9. physical homogeneous mass-frequency identity;
10. nonpositive/nonfinite calibration data fail closed.

## 11. Advancement

```text
RF-L5 graph/operator algebra                         561/561 PASS
premetric homogeneous gap mu_lambda^2               TYPED
physical RFC mass m_I^2=alpha_I/kappa_E             ADMITTED
local affine time calibration Gamma_t               PASS EXACT
local affine length calibration Gamma_x             PASS EXACT
c_cal^2=M_eff Gamma_x^2/Gamma_t^2                  PASS EXACT
light-cone ratio condition                           PASS EXACT
mu_lambda^2=Gamma_t^2 c^2 m_I^2                    PASS EXACT
05C Gamma_t=T_ref phi_ref                            PASS GIVEN 05C
unit-gauge M_eff=c^2 specialization                  PASS EXACT
spatial cell calibration L_h                        OPEN PHYSICAL BINDING
variable N_R / curved covariant propagation          OPEN
independent physical phase-clock spectral match      OPEN
alpha_I / m_I physical scale                         OPEN until spectral/scale gate
```
