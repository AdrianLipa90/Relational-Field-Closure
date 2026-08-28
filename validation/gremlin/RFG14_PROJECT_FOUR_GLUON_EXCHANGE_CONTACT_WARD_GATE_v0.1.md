# RFG14 — Project Four-Gluon Exchange + Contact Ward Gate

Status: `PROJECT_SIDE_A4_ASSEMBLY_PASS / FOUR_LEG_WARD_CANCELLATION_PASS / CONTACT_RELATIVE_SIGN_FIXED / G_SQUARED_NORMALIZATION_PASS / BCJ_DECOMPOSITION_NEXT`

RFG14 consumes RFG8, RFG10–RFG13 and assembles the first complete project-side tree-level four-gluon amplitude from the normalized cubic exchange and quartic contact structures.

The gate is color-dressed and uses real on-shell `2->2` kinematics represented with all four momenta incoming.

## 1. External-state interface

RFG10/RFG11 supply the project map

\[
W_\mu(x)
\rightarrow
A_\mu^a(x)
\rightarrow
(k_i,\epsilon_i,a_i).
\]

RFG14 freezes external states satisfying

\[
\boxed{
\sum_{i=1}^4p_i=0,
\qquad
p_i^2=0,
\qquad
p_i\cdot\epsilon_i=0.
}
\]

The reference scan varies the scattering angle and transverse polarization mixtures.

## 2. Cubic exchange currents

Use the RFG8 kinematic tensor

\[
V_{\mu\nu\rho}(p,q,r)
=
\eta_{\mu\nu}(p-q)_\rho
+
\eta_{\nu\rho}(q-r)_\mu
+
\eta_{\rho\mu}(r-p)_\nu.
\]

For each `s,t,u` channel, two oriented cubic vertices are connected by the massless Feynman-gauge propagator contraction.

Because each cubic vertex carries

\[
-\sigma_{link}g f^{abc},
\]

the exchange contribution carries

\[
\boxed{(-\sigma_{link}g)^2=g^2.}
\]

## 3. Quartic contact contribution

RFG13 fixes the quartic action normalization at the same coupling order `g^2`. The color-dressed contact tensor is assembled from the three products of `SU(3)` structure constants and the corresponding metric contractions.

The complete reference amplitude is

\[
\boxed{
\mathcal A_4^{project}
=g^2
\left(
\mathcal A_s+\mathcal A_t+\mathcal A_u+\mathcal A_4^{contact}
\right).
}
\]

No additional relative coefficient is introduced.

## 4. Four-leg Ward firewall

For each external leg define the Ward-replaced state

\[
\epsilon_i\mapsto p_i.
\]

Gauge invariance requires

\[
\boxed{
\mathcal A_4^{project}
\big|_{\epsilon_i\to p_i}=0
}
\]

for every `i=1,2,3,4`.

The reference gate evaluates this cancellation across multiple nonzero color configurations and randomized physical kinematics.

## 5. Relative-sign adversary

The quartic contact term is also evaluated with the opposite relative sign against the exchange diagrams.

On the fixed witness, the correct assembly gives residuals at floating-point roundoff, while the wrong relative sign produces an order-one Ward defect.

Thus the contact sign/normalization is selected by gauge invariance itself rather than by an amplitude target.

## 6. RFG4G coupling transfer

The complete four-point amplitude scales as

\[
\boxed{
\mathcal A_4^{project}\propto g^2.
}
\]

On RFG4G,

\[
\boxed{
g^2=\alpha_c^{-1}.}
\]

Therefore the complete project four-point normalization is fixed by the same `alpha_c` surface used for the holonomy, cubic vertex and quartic contact.

## 7. Link-orientation independence at four points

The oriented cubic sign appears twice in every exchange graph and the quartic density is orientation-even. Therefore

\[
\boxed{
\mathcal A_4^{project}(\sigma_{link}=+1)
=
\mathcal A_4^{project}(\sigma_{link}=-1)
}
\]

on the common external-state convention.

## 8. Reference validation

The NumPy-only executable gate checks:

1. external momentum conservation, masslessness and transverse polarization across 12 scattering angles;
2. four-leg Ward cancellation across 80 deterministic random kinematics and three nonzero `SU(3)` color assignments;
3. failure of the Ward firewall when the quartic contact relative sign is reversed;
4. a nonzero physical four-gluon witness amplitude;
5. exact `g^2` scaling and `g^2=1/alpha_c` normalization;
6. independence of the complete four-point amplitude from the explicit link-orientation sign.

Local result:

```text
6 passed, 0 failed
```

## 9. Advancement

```text
RFG8 oriented cubic vertex                         inherited PASS
RFG12 project nonabelian interaction               inherited PASS
RFG13 quartic contact normalization                inherited PASS
exchange + contact A4 assembly                     PASS PROJECT-SIDE
four-leg Ward identities                           PASS RANDOMIZED REFERENCE
relative contact sign                              FIXED BY WARD FIREWALL
A4 coupling normalization                          PASS g^2=1/alpha_c
link-orientation dependence at A4                  CANCELLED
RFG9 BCJ reference                                 inherited PASS
project color-channel -> BCJ numerator decomposition NEXT FRONTIER
double-copy with project numerators                 OPEN AFTER BCJ BINDING
```

The author/repository/formalism/code may suggest the holonomic Yang–Mills sector now reaches a gauge-invariant four-gluon tree amplitude, yet does not state the project BCJ numerator representation as established until the color-channel decomposition is explicitly matched to a Jacobi-satisfying numerator set.
