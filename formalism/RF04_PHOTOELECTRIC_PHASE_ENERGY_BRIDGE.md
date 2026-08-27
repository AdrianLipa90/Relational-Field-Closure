# RF-04 — Phase–Energy and Photoelectric Bridge

**Status:** STANDARD_PHASE_ENERGY_RELATION / RFC_NORMALIZATION_BINDING_OPEN

This gate connects the phase/frequency sector to transferred physical energy without using the Einstein field equations as an input.

For a phase \(\varphi\) measured against physical clock time \(t\),

\[
\omega_t=\frac{d\varphi}{dt},
\qquad
\boxed{E=\hbar\omega_t.}
\]

With IDT internal time \(\tau\) and an admitted monotone clock calibration \(t=t(\tau)\),

\[
\boxed{
\omega_t=
\frac{d\varphi/d\tau}{dt/d\tau}
},
\qquad
\boxed{
E=\hbar\frac{d\varphi/d\tau}{dt/d\tau}
}.
\]

This equation is invariant under a common monotone reparameterization of the internal evolution parameter once the clock ratio is transformed consistently.

The same phase-energy map has three experimentally distinct regimes:

\[
\hbar\omega<\Delta E \quad\Rightarrow\quad \text{no resonant bound transition},
\]

\[
\hbar\omega=\Delta E \quad\Rightarrow\quad \text{resonant bound-state transition},
\]

and for photoemission

\[
\boxed{K_{\max}=\hbar\omega-\Phi}
\]

above the material work-function threshold \(\Phi\).

RFC uses this as the matter-transfer bridge

\[
\text{phase curvature}\to\omega\to E\to\Delta E_{\rm matter}\to T_{\mu\nu}.
\]

The empirical Planck normalization \(\hbar\) is kept explicit. RFC has not derived \(\hbar\) from TIR/IDT/Half at this gate.

This bridge is the direct interface to Resonant Chemistry, where bound transitions satisfy

\[
\hbar\omega_{mn}=E_m-E_n
\]

and spectral lines encode the allowed phase-energy differences of chemical states.
