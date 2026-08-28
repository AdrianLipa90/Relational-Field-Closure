# RFG19 — Spin-2 Helicity Selection / Little-Group Gate

Status: `PURE_SPIN2_HELICITY_REFERENCE_PASS / TREE_SELECTION_RULE_PASS / LITTLE_GROUP_WEIGHT_2_PASS / FOUR_POINT_EINSTEIN_BRANCH_ADVANCED`

RFG19 consumes RFG15, RFG16 and the pure spin-2 external-state projection of RFG18. Its purpose is to test the physical helicity content of the projected four-point double-copy amplitude without using a gravity target to construct the project numerators.

## 1. Helicity basis

For each massless momentum choose an oriented orthonormal transverse frame `(u,v)`. Define

\[
\varepsilon_\pm
=\frac{u\pm i v}{\sqrt2}.
\]

These satisfy

\[
k\cdot\varepsilon_\pm=0,
\qquad
\varepsilon_\pm\cdot\varepsilon_\pm=0,
\qquad
\varepsilon_+\cdot\varepsilon_-=-1.
\]

The pure spin-2 helicity tensors are the same-helicity double-copy states

\[
\boxed{h_{+2}=\varepsilon_+\otimes\varepsilon_+,\qquad h_{-2}=\varepsilon_-\otimes\varepsilon_-.}
\]

They are symmetric, transverse and traceless.

## 2. Physical 2 -> 2 crossing convention

The project four-point numerator code uses all-incoming momenta. For a physical process `1+2 -> 3+4`, the outgoing gluon/graviton states on legs 3 and 4 are crossed to incoming states, so the all-incoming helicity label is

\[
h_i^{in}=h_i^{phys}\quad(i=1,2),
\qquad
h_i^{in}=-h_i^{phys}\quad(i=3,4).
\]

RFG19 freezes this map before evaluating selection rules.

## 3. Tree-level helicity selection gate

Using the actual RFG15 project numerators in both copies, the projected spin-2 amplitude satisfies on the tested physical kinematic surface

\[
\boxed{\mathcal M_4(++++)=0}
\]

and every physical single-minus configuration satisfies

\[
\boxed{\mathcal M_4(-+++)=0}
\]

up to the deterministic numerical tolerance of the executable reference.

The MHV sector is nonzero:

\[
\boxed{\mathcal M_4(--++)\neq0.}
\]

Its parity mirror is equal on the real scattering witness:

\[
\boxed{\mathcal M_4(--++)=\mathcal M_4(++--).}
\]

No helicity selection was used to tune the RFG15 numerators.

## 4. Little-group / transverse-frame weight

Rotate one external transverse frame by an angle `psi`:

\[
(u,v)\mapsto(u',v').
\]

Then

\[
\varepsilon_h\mapsto e^{-ih\psi}\varepsilon_h
\]

for the all-incoming helicity label `h = +/-1`. The corresponding same-helicity double-copy tensor transforms as

\[
\boxed{h_{2h}\mapsto e^{-2ih\psi}h_{2h}.}
\]

Because the four-point amplitude is multilinear in each external tensor state, rotating one external frame gives exactly the same doubled phase:

\[
\boxed{
\frac{\mathcal M_4(\psi)}{\mathcal M_4(0)}
=e^{-2ih\psi}.
}
\]

The executable reference verifies this relation independently on every leg for multiple positive and negative frame rotations.

## 5. Executable validation

The reference test checks:

1. transverse/null normalization of the complex helicity vectors;
2. vanishing physical all-plus spin-2 amplitude over 31 scattering angles;
3. vanishing of every physical single-minus placement over 23 scattering angles;
4. nonzero MHV `(--++)` sector and parity-mirror equality;
5. doubled external-frame phase `exp(-2 i h psi)` on all four legs;
6. symmetry, transversality and tracelessness of the lifted `h_{+2}` and `h_{-2}` tensors.

Local result:

```text
6 passed, 0 failed
```

## 6. Advancement

```text
RFG18 pure spin-2 external projector                 PASS
complex helicity vector basis                        PASS
h_+2 / h_-2 tensor typing                            PASS EXACT
physical ++++ tree selection                         PASS REFERENCE ZERO
physical single-minus tree selection                 PASS REFERENCE ZERO
physical MHV --++                                    PASS REFERENCE NONZERO
spin-2 little-group phase weight                      PASS EXACT NUMERICAL
explicit closed-form Einstein MHV ratio               NEXT CROSSCHECK
higher-point project spin-2 BCJ                       OPEN
```

RFG19 therefore provides a direct four-point spin-2 helicity signature for the projected project double-copy branch. The coupling normalization remains the RFG16/RFG17 `kappa_E` normalization.