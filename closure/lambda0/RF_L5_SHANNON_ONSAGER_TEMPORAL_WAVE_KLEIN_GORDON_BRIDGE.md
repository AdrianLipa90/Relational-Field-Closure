# RF-L5 — Shannon–Onsager → Temporal-Wave Conservative Scalar Bridge

Status: `UNIFORM_ONSAGER_STIFFNESS_EXACT / CONSERVATIVE_GRAPH_SPECTRAL_EQUATION_EXACT / PREMETRIC_GAP_TYPED / RF_L5_ALGEBRAIC_RECEIPT_561_PASS / PHYSICAL_CALIBRATION_CONSUME_RF_L5A`

RF-L5 consumes the IDT 01D Shannon–Onsager response tensor and the IDT 02A–02C Temporal Wave line. It constructs the conservative finite-graph second-order scalar equation on the same premetric ordering coordinate used by IDT.

RF-L4A separately supplies the RFC geometric scalar mass coordinate

\[
\boxed{m_I^2=\frac{\alpha_I}{\kappa_E}},
\qquad [m_I^2]=L^{-2}.
\]

RF-L5A supplies the physical clock/length calibration that binds this RFC inverse-length coordinate to the premetric homogeneous spectral-gap slot defined below.

## 1. Exact uniform Shannon–Onsager stiffness

For the IDT zero-drive symmetric sector with `N_s` states and uniform stationary reference `u_a=1/N_s`, 01D proves

\[
\boxed{
G_u^{(2)}(u)=\frac{\ln2}{N_s}K_0,
}
\]

where 02B uses

\[
\boxed{
K_0=D^\top\operatorname{diag}(M_{ab})D=-G_0
}
\]

as the untwisted Temporal Wave stiffness. Hence

\[
\boxed{
K_0=\frac{N_s}{\ln2}G_u^{(2)}(u).
}
\]

The same relational edge operator therefore appears in the uniform Shannon response and in the Temporal Wave stiffness.

## 2. Conservative ordering-coordinate sector

IDT 02B writes

\[
\ddot q+C_\eta\dot q+K_0q=0
\]

with dots taken with respect to the ordering parameter `lambda`, as witnessed by

\[
\frac{d\mathcal H_T}{d\lambda}=-p^\dagger C_\eta p.
\]

The conservative projection is

\[
\boxed{C_\eta=0}
\]

and therefore

\[
\boxed{
\frac{d^2q}{d\lambda^2}+K_0q=0.
}
\]

The nonzero `C_eta` sector remains an explicitly dissipative extension with its own energy-exchange ledger.

## 3. Premetric homogeneous spectral gap

Introduce a nonnegative homogeneous spectral-gap coefficient `mu_lambda^2` in the same ordering-coordinate normalization as `d^2/dlambda^2` and `K0`:

\[
\boxed{\mu_\lambda^2\ge0.}
\]

The conservative finite-graph Lagrangian is

\[
\boxed{
L_\lambda
=\frac12\phi_I'^\top\phi_I'
-\frac12\phi_I^\top K_0\phi_I
-\frac12\mu_\lambda^2\phi_I^\top\phi_I,
}
\]

where prime denotes `d/dlambda`. Its Euler–Lagrange equation is

\[
\boxed{
\phi_I''+(K_0+\mu_\lambda^2I)\phi_I=0.
}
\]

This is the premetric finite-graph massive-wave form. The physical RFC mass `m_I` is inserted only through the RF-L5A clock/length calibration.

## 4. Direct Shannon-response representation

Substituting the exact 01D identity gives

\[
\boxed{
\phi_I''+
\left[
\frac{N_s}{\ln2}G_u^{(2)}(u)
+\mu_\lambda^2I
\right]\phi_I=0.
}
\]

The relational stiffness is therefore fixed by the Shannon–Onsager response while the homogeneous premetric gap remains a separately typed scalar slot until physical calibration.

## 5. Modal spectrum

Let

\[
K_0v_r=\lambda_rv_r,
\qquad \lambda_r\ge0.
\]

For `phi_I(lambda)=a_r(lambda)v_r`,

\[
\boxed{
a_r''+(\lambda_r+\mu_\lambda^2)a_r=0,
}
\]

so the ordering-coordinate modal frequency obeys

\[
\boxed{
\omega_{\lambda,r}^2=\lambda_r+\mu_\lambda^2.
}
\]

On a connected graph,

\[
K_0\mathbf1=0,
\]

and therefore the homogeneous mode has

\[
\boxed{
\omega_{\lambda,0}^2=\mu_\lambda^2.
}
\]

## 6. Conserved graph energy

Define

\[
\boxed{
E_\lambda
=\frac12\phi_I'^\top\phi_I'
+\frac12\phi_I^\top K_0\phi_I
+\frac12\mu_\lambda^2\phi_I^\top\phi_I.
}
\]

For time-independent symmetric `K0` and constant `mu_lambda^2`,

\[
\boxed{
\frac{dE_\lambda}{d\lambda}=0.
}
\]

If `C_eta` is restored,

\[
\phi_I''+C_\eta\phi_I'+(K_0+\mu_\lambda^2I)\phi_I=0,
\]

then

\[
\boxed{
\frac{dE_\lambda}{d\lambda}
=-\phi_I'^\top C_\eta\phi_I'\le0.
}
\]

## 7. Premetric continuum limit

IDT 02C gives

\[
\boxed{c_{eff}^2=M_{eff}}
\]

in its premetric ordering/cell-coordinate normalization, with

\[
M_{eff}
=\left(\frac1N\sum_e\frac1{M_e}\right)^{-1}.
\]

Writing the cell coordinate as `xi`, the conservative long-wave equation is typed as

\[
\boxed{
\partial_\lambda^2\phi_I
-M_{eff}\partial_\xi^2\phi_I
+\mu_\lambda^2\phi_I=0,
}
\]

with premetric dispersion

\[
\boxed{
\omega_\lambda^2=M_{eff}k_\xi^2+\mu_\lambda^2.
}
\]

No physical light-cone or inverse-length mass identification is required at this premetric stage.

## 8. RF-L5A physical calibration

RF-L5A introduces local affine physical calibration factors

\[
t-t_\star=\Gamma_t(\lambda-\lambda_\star),
\qquad
X-X_\star=\Gamma_x(\xi-\xi_\star),
\]

and proves the physical coefficient map

\[
\boxed{
c_{cal}^2=M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2}}
\]

and

\[
\boxed{
\Omega_m^2=\frac{\mu_\lambda^2}{\Gamma_t^2}.}
\]

Matching the local RFC Klein–Gordon equation gives the exact calibration conditions

\[
\boxed{
M_{eff}\frac{\Gamma_x^2}{\Gamma_t^2}=c^2
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

Therefore the earlier simple coefficient comparison is the unit-calibration specialization `Gamma_t=Gamma_x=1`; the general physical bridge is the ratio condition above.

## 9. Relation to RF-L2 after calibration

RF-L2 uses signature `(-,+,+,+)` and

\[
\Box\phi_I-m_I^2\phi_I=0.
\]

In a locally flat physical chart,

\[
\boxed{
\partial_t^2\phi_I
-c^2\nabla_X^2\phi_I
+c^2m_I^2\phi_I=0.
}
\]

RF-L5 + RF-L5A reach this form when the two calibration conditions in Section 8 are satisfied.

## 10. Physical homogeneous frequency target

The premetric homogeneous mode has

\[
\omega_{\lambda,0}^2=\mu_\lambda^2.
\]

After the common physical clock calibration,

\[
\omega_t^{(KG)}=\frac{\omega_{\lambda,0}}{\Gamma_t},
\]

and RF-L5A gives

\[
\boxed{
\left(\omega_t^{(KG)}\right)^2
=c^2m_I^2
=c^2\frac{\alpha_I}{\kappa_E}.
}
\]

IDT 01L independently carries calibrated phase-clock frequencies. A downstream spectral gate may compare one independently admitted phase-clock line with `omega_t^(KG)` after both use the same physical time coordinate.

If such a gate establishes

\[
\omega_t^{(KG)}=|\omega_{phase}|,
\]

then

\[
\boxed{
m_I^2=\left(\frac{\omega_{phase}}{c}\right)^2,
\qquad
\alpha_I=\kappa_E\left(\frac{\omega_{phase}}{c}\right)^2.
}
\]

## 11. Validation scope

RF-L5 workflow run `33245513490`, job `99082170070`, returned **561/561 PASS** for the graph/operator regression suite on PR #22. RF-L5A is the required physical-dimensional calibration layer for promotion from the premetric graph equation to the local Lorentzian scalar equation.

## 12. Advancement

```text
01D uniform Shannon response -> K0                    PASS EXACT
02B K0 as premetric Temporal Wave stiffness           ADMITTED
RF-L5 conservative graph spectral equation             561/561 PASS ALGEBRAIC RECEIPT
premetric homogeneous gap mu_lambda^2                 TYPED
premetric continuum dispersion                        PASS STRUCTURAL
RF-L4A physical inverse-length mass m_I               ADMITTED
RF-L5A affine physical calibration                    REQUIRED DOWNSTREAM LAYER
physical light-cone coefficient                       CLOSED BY RF-L5A RATIO WHEN CALIBRATED
physical mass-frequency coefficient                   CLOSED BY RF-L5A WHEN CALIBRATED
variable-lapse curved propagation                     OPEN
independent phase-clock spectral identification       OPEN
alpha_I / m_I physical scale                          OPEN until spectral/scale gate
```
