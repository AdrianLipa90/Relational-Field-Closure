# RF cross-repository EB orbital-phase crosswalk v0.1

Status: `CROSS_REPO_CANDIDATE / EXACT_PARENT_COMPOSITION / PHYSICAL_REALIZATION_OPEN`

## Scope

This note cross-references the RFC Noether/Hamiltonian source closure with the GREMLIN orbital-phase dependency gate. It does not alter RF-S22 or promote any physical carrier binding.

## RFC parent

RF-S22 supplies, on the matched-H branch,

```text
E_G = H_Phi^EB
N_tot = H_Phi^EB / epsilon_bar
sum_a V_a rho_G,a = H_Phi^EB.
```

The equality is conditional on the parent provenance and carrier-energy gates stated by RF-S22.

## GREMLIN source composition

GREMLIN orbit-source identifiability v0.8 uses

```text
mu_source = C_mu E_Sigma
```

with `C_mu` independently supplied.

If the admitted extensive source is the RF-S22 generator source,

```text
E_Sigma = E_G = H_Phi^EB,
```

then algebraically

```text
mu_source = C_mu H_Phi^EB.
```

This relation does not determine `C_mu` and does not identify RFC energy with gravitational mass by fiat.

## Orbital phase bridge

GREMLIN v0.9 composes the source with the role-separated orbital kernel and the informational-potential gradient:

```text
omega^2
 = C_mu H_Phi^EB eta_G/r^3
 + alpha_I/(m_I r kappa_E) dXi_I/dr.
```

Its phase-winding comparison is

```text
eta_phi^2 q_eff^2/(m_I^2 r^4)
 =
 C_mu H_Phi^EB eta_G/r^3
 + alpha_I/(m_I r kappa_E) dXi_I/dr,
```

with

```text
q_eff = n - gamma_B/(2*pi).
```

RFC is authoritative only for its source/current/Hamiltonian side of this crosswalk. GREMLIN owns the candidate orbital composition. The informational phase-optics repository owns the `Xi_I -> U_I -> phase` model interface.

## Open gates

- common physical realization linking the RFC phase carrier to the proposed condensate state;
- physical local current/measure receipt;
- source coefficient `C_mu`;
- physical ownership of `eta_G`;
- admission of `U_I` to the carrier Lagrangian;
- any metric identification `U_I -> g_mu_nu`.

No RF-S22 status is promoted by this cross-reference.

## External authority

GREMLIN:
`spec/GREMLIN_EB_CONDENSATE_ORBITAL_PHASE_BRIDGE_V0_9.md`

QHTRI phase optics:
`docs/PHASE_MECHANICS_GREMLIN_ORBITAL_EB_BRIDGE.md`
