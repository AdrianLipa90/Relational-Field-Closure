# PREMETRIC TEMPORAL–SPATIAL TRANSVERSALITY v0.5

Status: **CANDIDATE / EXACT TRACE–TRACELESS TRANSVERSALITY THEOREM**

Scope: close the pre-RF-G0 local dimension gate without assuming a metric,
an ADM decomposition, a zero-shift spacetime ansatz, or a four-dimensional base.

## 1. Upstream carriers

TIR supplies the local spatial translation carrier

\[
V_S
=
\operatorname{Herm}_0(2)
=
\operatorname{span}_{\mathbb R}
\{\sigma_1,\sigma_2,\sigma_3\}.
\]

The temporal-trace candidate supplies the complementary scalar carrier

\[
V_T=\mathbb RI.
\]

The full primitive observable carrier is

\[
V=\operatorname{Herm}(2).
\]

## 2. Exact direct-sum theorem

For every \(X\in\operatorname{Herm}(2)\), define

\[
P_T(X)
=
\frac12\operatorname{Tr}(X)\,I
\]

and

\[
P_S(X)
=
X-\frac12\operatorname{Tr}(X)\,I.
\]

Then

\[
\operatorname{Tr}P_S(X)=0,
\]

so

\[
P_T(X)\in\mathbb RI,
\qquad
P_S(X)\in\operatorname{Herm}_0(2),
\]

and exactly

\[
\boxed{
X=P_T(X)+P_S(X).
}
\]

The intersection is trivial. If

\[
\lambda I\in\operatorname{Herm}_0(2),
\]

then

\[
0=\operatorname{Tr}(\lambda I)=2\lambda,
\]

hence

\[
\lambda=0.
\]

Therefore

\[
\boxed{
\operatorname{Herm}(2)
=
\mathbb RI
\oplus
\operatorname{Herm}_0(2).
}
\]

This is a premetric algebraic decomposition.

## 3. Canonical coordinates and dual coframe

Write

\[
X=x^0I+\sum_{i=1}^3x^i\sigma_i.
\]

The coefficients are recovered uniquely by

\[
\boxed{
x^0=\frac12\operatorname{Tr}X,
}
\]

\[
\boxed{
x^i=\frac12\operatorname{Tr}(X\sigma_i).
}
\]

Define the basis vectors

\[
e_0:=I,
\qquad
e_i:=\sigma_i,
\]

and dual one-forms

\[
\theta^0(A):=\frac12\operatorname{Tr}A,
\]

\[
\theta^i(A):=\frac12\operatorname{Tr}(A\sigma_i).
\]

Using

\[
\operatorname{Tr}\sigma_i=0,
\qquad
\frac12\operatorname{Tr}(\sigma_i\sigma_j)=\delta_{ij},
\]

one obtains exactly

\[
\boxed{
\theta^0(e_0)=1,
\qquad
\theta^0(e_i)=0,
}
\]

and

\[
\boxed{
\theta^i(e_0)=0,
\qquad
\theta^i(e_j)=\delta^i{}_j.
}
\]

Thus the temporal and spatial legs are algebraically transverse:

\[
\boxed{
V_T\cap V_S=\{0\}.
}
\]

No metric orthogonality premise is used.

## 4. Four-volume / rank closure

The evaluation matrix is

\[
[\theta^\mu(e_\nu)]
=
I_4.
\]

Hence

\[
\boxed{
\det[\theta^\mu(e_\nu)]=1.
}
\]

Equivalently,

\[
\boxed{
\theta^0\wedge\theta^1\wedge\theta^2\wedge\theta^3
(e_0,e_1,e_2,e_3)
=1\ne0.
}
\]

Therefore

\[
\boxed{
\operatorname{rank}
\{\theta^0,\theta^1,\theta^2,\theta^3\}
=4.
}
\]

This establishes the local carrier dimension before any Lorentzian metric is defined.

## 5. Relation to IDT temporal elapsed scale

IDT 00E supplies one positive elapsed scalar/one-form, and 01AD supplies after clock calibration

\[
d\hat\tau=N_Rdt,
\qquad
\mathcal E^0=N_Rc\,dt=c\,d\hat\tau.
\]

The temporal-trace lift gives the unique positive-Hermitian recovery map

\[
X=\ell\rho,
\qquad
\operatorname{Tr}X=\ell.
\]

Once the IDT length-valued elapsed scale is bound to the trace coordinate by

\[
\ell \propto c\hat\tau
\]

(or infinitesimally \(d\ell\propto\mathcal E^0\)), the IDT temporal one-form is proportional to \(\theta^0\). Scaling by a nonzero scalar does not alter its kernel:

\[
\ker\mathcal E^0
=
\ker\theta^0
=
\operatorname{Herm}_0(2).
\]

Thus

\[
\boxed{
\mathcal E^0(e_i)=0
}
\]

follows from tracelessness, not from a metric ansatz.

## 6. Relation to the TIR/RFC spatial coframe

Every spatial leg is a covector on the three-dimensional carrier \(\operatorname{Herm}_0(2)\). Extend such a covector to \(\operatorname{Herm}(2)\) by precomposition with the canonical spatial projector \(P_S\):

\[
\widetilde E^i:=E^i\circ P_S.
\]

Since

\[
P_S(I)=0,
\]

one has exactly

\[
\boxed{
\widetilde E^i(e_0)=0.
}
\]

If \(\{E^1,E^2,E^3\}\) has rank three on the TIR/RFC spatial carrier, its canonical extension remains rank three and acquires no temporal component.

Therefore the full premetric cross-leg conditions are consequences of the trace/traceless typing:

\[
\boxed{
\mathcal E^0(e_i)=0,
\qquad
\widetilde E^i(e_0)=0.
}
\]

## 7. Important distinction: transversality versus worldline motion

For the canonical event lift

\[
X=\ell\rho,
\]

differentiation along a path gives

\[
dX=\rho\,d\ell+\ell\,d\rho.
\]

At fixed normalized state \(\rho\), the path tangent \(\rho\,d\ell\) generally contains both scalar and traceless components whenever \(\rho\ne I/2\).

Therefore:

- the theorem above establishes **carrier/coframe transversality**;
- it does not assert that every physical trajectory has zero spatial velocity;
- a moving worldline can have nonzero spatial components in a transverse spacetime coframe.

This firewall prevents conflating a basis decomposition with a dynamical zero-velocity or zero-shift statement.

## 8. Corrected dependency before RF-G0

The dimension chain can now be written

\[
\boxed{
\mathbb C^2
\to
\operatorname{Herm}_0(2)
\to
r_S=3
}
\]

and

\[
\boxed{
\mathrm{IDT}
\to
\text{one elapsed scalar}
\to
\mathbb RI
\to
r_T=1.
}
\]

The exact trace/traceless decomposition gives

\[
\boxed{
\mathbb RI\oplus\operatorname{Herm}_0(2)
=
\operatorname{Herm}(2),
}
\]

with exact dual transversality and

\[
\boxed{D=4}.
\]

Only after this rank theorem should RFC apply the determinant/temporal-reflection step to obtain Lorentzian signature.

## 9. Status ledger

| Claim | Status |
|---|---|
| `Herm(2) = RI ⊕ Herm_0(2)` | EXACT |
| temporal/spatial intersection is trivial | EXACT |
| Pauli/identity dual evaluation matrix is `I4` | EXACT |
| premetric four-volume is nonzero | EXACT |
| spatial covectors canonically extend by `P_S` and kill `I` | EXACT |
| trace covector kills all TIR traceless spatial directions | EXACT |
| carrier/coframe transversality | EXACT |
| arbitrary worldline has zero spatial component | not asserted |
| IDT elapsed scale is physically the Hermitian trace scale | PHYSICAL BINDING CANDIDATE |
| local spacetime-base dimension is 4 after that binding | EXACT CONSEQUENCE |
| Lorentzian signature | downstream RF-G0 consequence |

No canon or `main` write is performed by this candidate.

## 10. Executable reference validation

Reference implementation:

`src/rfc/premetric_spacetime_rank.py`

Reference test:

`tests/reference/test_premetric_spacetime_rank.py`

Local isolated validation on 2026-08-30:

```text
8 passed in 0.08s
```

The executable checks:

1. exact identity dual-pairing matrix;
2. trace covector annihilation of all three Pauli spatial generators;
3. spatial dual covector annihilation of the identity direction;
4. complementary temporal/spatial projector reconstruction;
5. full premetric certificate closure;
6. the worldline firewall (a lifted event may carry nonzero spatial components);
7. positive trace-scale recovery;
8. fail-closed invalid/non-Hermitian/nonfinite/out-of-Bloch inputs.

This is a local reference test receipt, not hosted GitHub Actions authority.
