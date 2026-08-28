# RF-E6 — Lorentzian Matter Action / Maxwell Source Bookkeeping Firewall

Status: `EXACT_SIGNATURE_ACTION_ALIGNMENT / EXACT_MICROSCOPIC_CURRENT_SIGN / EXACT_STRESS_ENERGY_VARIATION / EXACT_SOURCE_BOOKKEEPING / MU_STAR_UNIT_BINDING_EXACT / FIRST_PRINCIPLES_ALPHA_EM_OPEN / TOTAL_MATTER_COMPOSITION_OPEN`

RF-E6 aligns the charged scalar/multiplet action with the canonical RFC metric signature fixed by RF-G0 and closes the source-bookkeeping interface between RF-M4, RF-N1B2P, RF-E0, RF-E4 and RF-E5.

The canonical spacetime convention is

\[
\boxed{\operatorname{signature}(g)=(-,+,+,+)}.
\]

## 1. Energy-positive charged matter action

Use the synchronized RFC gauge convention

\[
\Psi'=e^{iQ\Lambda/\hbar}\Psi,
\qquad
A'_\mu=A_\mu-\partial_\mu\Lambda,
\]

with

\[
\boxed{\mathcal D_\mu\Psi
=\nabla_\mu\Psi+\frac{i}{\hbar}A_\mu Q\Psi}.
\]

For the `(-,+,+,+)` metric, the energy-positive lowest-derivative complex multiplet action is written

\[
\boxed{
\mathcal L_m
=-(\mathcal D_\mu\Psi)^\dagger\mathcal D^\mu\Psi
-U(\Psi),
}
\]

where

\[
U(\Psi)=\Psi^\dagger\mathcal M^2\Psi+V_{inv}(\Psi),
\qquad
[\mathcal M^2,Q]=0.
\]

For a homogeneous free mode this convention gives a positive Hamiltonian density and reproduces the positive rotor/phase kinetic term used by RF-N1B2L after normal-flow reduction.

## 2. Charge-projected current and microscopic source sign

Retain the charge-projected Noether current

\[
\boxed{
\mathcal J_Q^\mu
=i\left[
(\mathcal D^\mu\Psi)^\dagger Q\Psi
-\Psi^\dagger Q\mathcal D^\mu\Psi
\right].
}
\]

Varying the energy-positive matter action with respect to the covariant potential gives

\[
\boxed{
\frac{1}{\sqrt{-g}}\frac{\delta S_m}{\delta A_\mu}
=-\frac1\hbar\mathcal J_Q^\mu.
}
\]

The microscopic Maxwell + matter action is therefore

\[
\boxed{
S_{micro}
=\int d^4x\sqrt{-g}
\left[
-\frac{1}{4\mu_*}F_{\alpha\beta}F^{\alpha\beta}
+\mathcal L_m
\right].
}
\]

Stationarity in `A_mu` gives

\[
\boxed{
\nabla_\mu F^{\mu\nu}
=\mu_*J_{EM}^\nu,
\qquad
J_{EM}^\nu=\frac1\hbar\mathcal J_Q^\nu.
}
\]

For one charge eigenvalue `q`,

\[
\boxed{
J_{EM}^\mu=\frac q\hbar J_\vartheta^\mu.
}
\]

On the RF-N1B2K zero-defect carrier surface this composes to

\[
\boxed{
J_{EM}^\mu=\frac q\hbar J_{RFC,\vartheta}^\mu.
}
\]

For a charge-resolved multiplet,

\[
\boxed{
J_{EM}^\mu
=\frac1\hbar\Pi_Q[J_{RFC}]^\mu,
\qquad
\Pi_Q[J]^\mu=\sum_a q_aJ_a^\mu.
}
\]

The neutral control remains exact:

\[
Q=0\quad\Longrightarrow\quad J_{EM}^\mu=0
\]

while the unweighted matter carrier and matter stress-energy may remain finite.

## 3. One source coupling per action representation

RFC uses two equivalent source representations, each with a distinct role.

### Microscopic representation

The electromagnetic coupling is contained in `D_mu Psi` and the source follows from `delta S_m/delta A_mu`.

### Effective external-current representation

For a prescribed conserved current one may instead use

\[
\boxed{
S_{eff}[A;J]
=\int d^4x\sqrt{-g}
\left[
-\frac{1}{4\mu_*}F^2
-J_{EM}^\mu A_\mu
\right].
}
\]

Variation again gives

\[
\nabla_\mu F^{\mu\nu}=\mu_*J_{EM}^\nu.
\]

The action ledger admits one source representation at a time for the same microscopic carrier. This makes the current normalization unique and prevents a factor-of-two source duplication.

## 4. Charged-matter stress-energy tensor

With

\[
T_{\mu\nu}^{matter}
=-\frac{2}{\sqrt{-g}}
\frac{\delta S_m}{\delta g^{\mu\nu}},
\]

the complex multiplet gives

\[
\boxed{
T_{\mu\nu}^{matter}
=(\mathcal D_\mu\Psi)^\dagger\mathcal D_\nu\Psi
+(\mathcal D_\nu\Psi)^\dagger\mathcal D_\mu\Psi
+g_{\mu\nu}\mathcal L_m.
}
\]

On the charged-matter equations of motion,

\[
\boxed{
\nabla^\mu T_{\mu\nu}^{matter}
=+F_{\nu\lambda}J_{EM}^\lambda.
}
\]

The Maxwell tensor

\[
T_{\mu\nu}^{EM}
=\frac1{\mu_*}
\left(
F_{\mu\alpha}F_\nu{}^\alpha
-\frac14g_{\mu\nu}F^2
\right)
\]

obeys

\[
\boxed{
\nabla^\mu T_{\mu\nu}^{EM}
=-F_{\nu\lambda}J_{EM}^\lambda.
}
\]

Therefore

\[
\boxed{
\nabla^\mu
\left(T_{\mu\nu}^{matter}+T_{\mu\nu}^{EM}\right)=0.
}
\]

This supplies the explicit charged-matter tensor required by the RF-E0 Bianchi bridge.

## 5. RF-E4/RF-E5 signature transfer

For a single fixed-amplitude phase mode `psi=A exp(i vartheta)`, define

\[
q_\mu=D_\mu\vartheta.
\]

The `(-,+,+,+)` phase action is

\[
\boxed{
\mathcal L_{phase}=-A^2q_\mu q^\mu-V.
}
\]

Its stress tensor is

\[
\boxed{
T_{\mu\nu}^{phase}
=2A^2q_\mu q_\nu+g_{\mu\nu}\mathcal L_{phase}.
}
\]

For pure normal flow `q_hat=(r_n,0,0,0)`, let `K=A^2 r_n^2`. Then exactly as in RF-E4,

\[
\boxed{
\varepsilon=K+V,
\qquad
p=K-V,
\qquad
\varepsilon+3p=4K-2V.
}
\]

Thus the physical RF-E4 pressure firewall and the RF-E5 on-shell dust/factor-two results are preserved after transfer to the canonical RFC signature.

## 6. `mu_*` normalization

`mu_*` is the coefficient attached to the chosen physical normalization of `A_mu` and `J_EM`.

In rationalized Heaviside–Lorentz natural units with canonically normalized `-F^2/4`,

\[
\boxed{\mu_*=1}.
\]

In SI with the physical electromagnetic potential and current,

\[
\boxed{\mu_*=\mu_0}.
\]

The unit-independent electromagnetic coupling is carried by the fine-structure constant. In the SI normalization,

\[
\boxed{
\alpha_{EM}
=\frac{\mu_*e^2c}{4\pi\hbar},
\qquad
\mu_*
=\frac{4\pi\alpha_{EM}\hbar}{e^2c}.
}
\]

Therefore a frozen independent `alpha_EM` measurement fixes `mu_*` exactly within the selected unit convention. A first-principles RFC prediction of `alpha_EM` remains a separate promotion gate.

## 7. Promotion status

```text
RF-G0 canonical signature (-,+,+,+)                  PASS EXACT
energy-positive charged scalar/multiplet action      PASS EXACT CONVENTION
matter variation current sign                        PASS EXACT
RF-N1B2P charge-projected intertwiner sign            CORRECTED BY RF-E6
microscopic/effective source bookkeeping             PASS EXACT
charged-matter stress tensor                         PASS EXACT CONDITIONAL ON ACTION
EM/matter exchange cancellation                      PASS EXACT ON SHELL
RF-E4 physical epsilon/p equations                    PRESERVED EXACT
RF-E5 on-shell dust/factor-two results                PRESERVED EXACT
mu_* <-> alpha_EM/unit normalization                 PASS EXACT GIVEN UNIT CONVENTION
total matter composition beyond admitted multiplet   OPEN
first-principles alpha_EM prediction                  OPEN
dynamic Lambda0 matter/vacuum action                  OPEN
```
