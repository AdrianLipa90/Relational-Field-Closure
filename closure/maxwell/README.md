# Maxwell closure

Current sequence:

1. physical AB one-form connection
   \[
   \mathfrak a_{AB}=\frac{q}{\hbar}A
   \]
   — **PASS at RF-M1 for admitted nonzero probe charge**;
2. curvature reconstruction
   \[
   F=dA=\frac{\hbar}{q}d\mathfrak a_{AB}
   \]
   — **PASS**;
3. gauge redundancy `A -> A+dLambda` and closed-loop AB invariance — **PASS**;
4. homogeneous Maxwell identity
   \[
   dF=0
   \]
   — **PASS locally on regular gauge patches**;
5. sourced equation from the admitted lowest-derivative gauge action
   \[
   \nabla_\mu F^{\mu\nu}=\mu_*J^\nu
   \]
   — **CONDITIONAL ACTION THEOREM**;
6. charge-current conservation — **CONDITIONAL PASS with sourced action/current binding**;
7. electromagnetic stress-energy tensor — **CONDITIONAL PASS from metric variation of the same action**;
8. empirical vacuum coupling/unit normalization `mu_*` — **OPEN**;
9. physical RFC/IDT current `J_Q^mu <-> J_EM^mu` — **OPEN**.

The AB route removes the free potential-rescaling coordinate that remained in the earlier generic Berry-to-Maxwell binding. Berry, Euler and electromagnetic connections remain separately typed.

**Current status:** `HOMOGENEOUS_MAXWELL_EXACT_FROM_AB / SOURCED_MAXWELL_CONDITIONAL / VACUUM_COUPLING_AND_CURRENT_BINDING_OPEN`.
