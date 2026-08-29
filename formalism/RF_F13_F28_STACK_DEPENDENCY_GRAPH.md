# RF-F13 → RF-F28 Stacked Dependency Graph

Status: `STACKED_REFERENCE_FRONTIER / NONCANONICAL_SIDECAR / MAIN_ANCHOR_58655C7F / PHYSICAL_EVIDENCE_FRONTIER`

This sidecar records the validated stacked frontier above RFC `main` while preserving the canonical export/federation boundary.

Canonical main anchor:

`58655c7fe9d25d09c13545965e951f171316e6b2`

Canonical `DEPENDENCY_EXPORT.json` remains anchored to its earlier source state and explicit RF-F0→RF-F13 machine chain. This document extends the stacked reference view through RF-F28. Canonical export regeneration belongs after explicit source-stack merge authorization and exact post-merge source locking.

## 1. Stacked spine

```text
RF-F13 -> RF-F14 -> RF-F15 -> RF-F16 -> RF-F17 -> RF-F18
       -> RF-F19 -> RF-F20 -> RF-F21 -> RF-F22 -> RF-F23
       -> RF-F24 -> RF-F25 -> RF-F26 -> RF-F27 -> RF-F28
```

Each PR targets the immediately preceding RF-F branch.

## 2. Hosted validation ledger

| Gate | Role | PR | Current stacked head | Hosted validated head / suite |
|---|---|---:|---|---|
| RF-F13 | variational integrability / common action | #68 | `a14da535354f30ad8b0b672713863a9734970328` | `45659a5fbbcd0faa06ab2a7d8a81d1eb7215d4c0`, #321 SUCCESS; export head #322 SUCCESS |
| RF-F14 | microscopic Noether energy / EOS compatibility | #69 | `a46315fa118da4343dd4d0310b2b6c69df6769e1` | #324 SUCCESS |
| RF-F15 | microscopic scalar → phase-cell transport | #71 | `c3f7570827836e5ec071e88c72c3fc6408849dc6` | #326 SUCCESS |
| RF-F16 | vacuum split / dynamic-Λ common action | #72 | `42f1d7e0bb2d4c208338bac9a77cec37e36bfcf0` | `abe796f561b5235a7ba0233c3233b0fa4b081abc`, #330 SUCCESS |
| RF-F17 | state-dependent exchange projector | #73 | `110da304b83616fef5962413bcb21d4b59869c0b` | `f88012118a3209785a548cdc3771821a34b47ad1`, #332 SUCCESS |
| RF-F18 | IDT gauge-covariant phase-clock projector | #74 | `5705717e94293bba3b39719dde108eec2a3dbda8` | `f0d7d74ee3ce2a4c8a29b55faee43dc733bdab1a`, #340 SUCCESS |
| RF-F19 | independent rotor/lapse phase scale | #75 | `4c52bb17be0093661f20baf4e358348dcda4db25` | `c326b0ebbad2c180cfdde5ac11c157bd36d2c801`, #344 SUCCESS |
| RF-F20 | ABE/Euler off-shell metric response | #76 | `e537b81df0dae5d4b455e46090c61c7e4e8380b5` | `f4f22d2f77ef337768fef7ee55b185268b803dd3`, #351 SUCCESS |
| RF-F21 | independent IDT↔RFC phase-rate receipt | #77 | `e28584e6253507c6b5672396794cf7f1636c5513` | `71a7c1217533d4650f782d5ae01d5140c6cba98a`, #353 SUCCESS |
| RF-F22 | total Einstein source / Bianchi repartition | #78 | `24ff4dcbde9b5b069664f158da2661556da748fd` | `f3d7f504aa71d368b190502b85edab450558e2ab`, #355 SUCCESS |
| RF-F23 | phase-clock / material congruence alignment | #79 | stacked parent lineage before later sidecars | `241843acf8cc009d7f76a7cdb529d5615fea543a`, #357 SUCCESS |
| RF-F24 | executable current/measure realization | #80 | `0920cbd3664bc387cdd277a04c585c228a5f7c60` | `3b213f2df9e9528ec5fc42e1b07dfe959f4c120a`, #361 SUCCESS |
| RF-F25 | reduced-gravity cross-system universality | #81 | `70a9f28058a292ada1a22ff537cdd38027cad095` | `4b789af3b10a647dcdee0b5554f2ecb85d733a07`, #363 SUCCESS |
| RF-F26 | project coupling promotion firewall | #82 | `aac03a9b57525772f72e3da20f32ac897a1a2868` | `e6458abc145774810dfe7b226179026b809fe6bb`, #365 SUCCESS |
| RF-F27 | Gamma_DC / carrier-type identifiability | #83 | `fb6582c158142198362bf76ff881d2a7c0ee153d` | `3d051fc86f928b141f3801969e61aa4cf304fccb`, #367 SUCCESS |
| RF-F28 | tree-amplitude identifiability no-go | #84 | `cdec1646630ada83598916e15b3332e5b747bd74` | `d621df408aba1ac86d1448c54c0689fa2817918e`, #369 SUCCESS |

## 3. Dependency phases

### RF-F13 → RF-F16 — action/source ledger

The common action, microscopic EOS, phase-cell transport and vacuum/dynamic-Λ allocation are composed into one source ledger.

### RF-F17 → RF-F20 — state projector and metric response

The state-dependent exchange projector is bound to the existing IDT phase one-form, independently calibrated through rotor/lapse rate, and extended by the explicit ABE/scale off-shell metric-response coordinates.

### RF-F21 → RF-F24 — independent physical-interface receipts

Independent field/rotor rates, total Einstein source assembly, phase-clock/material congruence alignment, and current/measure realization are represented by fail-closed executable contracts.

### RF-F25 → RF-F28 — coupling universality and identifiability

RF-F25 tests cross-system reduced-gravity universality. RF-F26 enforces independent BCJ/Wilson/Gamma/carrier provenance and rejects GREMLIN candidate authority. RF-F27 shows that the source and horizon routes identify

\[
\boxed{
\frac{\Gamma_{DC}}{\zeta_M}
=\alpha_c\sqrt{\frac{\omega_Q\mathcal S_R}{j_Q}}
}
\]

and, for an independent horizon estimator,

\[
\boxed{
\frac{\Gamma_{DC}}{\zeta_M}
=\frac{\alpha_c\omega_Q}{2\sqrt{M_HT_H}}.
}
\]

RF-F28 establishes the exact positive scaling null direction

\[
(\Gamma_{DC},\zeta_M,M_\star)
\mapsto
(\lambda\Gamma_{DC},\lambda\zeta_M,\lambda M_\star)
\]

which preserves `kappa_g`, `kappa_E`, `Mbar_G`, and every tree prefactor `(kappa_g/2)^(n-2)` for `n>=3`.

Therefore the gravitationally identifiable project coordinate at this frontier is `Gamma_DC/zeta_M`; separate physical typing of `zeta_M` belongs to the carrier/matter evidence layer.

## 4. Stacked frontier verdict

```text
FORMAL_ACTION_LEVEL_EINSTEIN_SOURCE_ASSEMBLY         PASS
BIANCHI / DYNAMIC-LAMBDA REPARTITION                 PASS
REFERENCE FIELD↔ROTOR RATE CONTRACT                  PASS
REFERENCE PHASE-CLOCK↔MATERIAL ALIGNMENT CONTRACT    PASS
REFERENCE CURRENT/MEASURE REALIZATION CONTRACT       PASS
REDUCED-GRAVITY CROSS-SYSTEM TEST                     PASS REFERENCE CONTRACT
PROJECT BCJ/COUPLING PROMOTION FIREWALL              PASS REFERENCE CONTRACT
GAMMA/ZETA IDENTIFIABILITY THEOREM                   PASS
TREE-AMPLITUDE IDENTIFIABILITY NO-GO                 PASS
PHYSICAL COUPLING PROMOTION                          CONDITIONAL / EVIDENCE-GATED
```

## 5. Physical evidence frontier

The next promotion coordinates are empirical or independently typed inputs:

1. realized RF-F24 current/measure arrays with common slice/measure provenance;
2. realized RF-F21 field/rotor phase-rate receipt;
3. independently sourced RFC source-operator values `S_R`;
4. independently admitted `alpha_c` / Yang–Mills normalization provenance;
5. independent physical carrier-energy typing `M_star` / `zeta_M`;
6. realized RF-F20 response receipts when the active ABE/scale branch requires them;
7. optional logically independent horizon `M_H`, `kappa_H` or `T_H` provenance;
8. at least two admitted systems for the RF-F25 zero-fit universality test.

Once `zeta_M` is independently typed, RF-F27 converts the independently measured source/current/rate/alpha coordinates into a conditional `Gamma_DC`, and RF-F25 tests whether the resulting reduced gravity scale is source-independent.

## 6. Canonical promotion sequence

```text
explicit stacked-source merge authorization
-> exact post-merge RFC main commit
-> regenerate canonical DEPENDENCY_EXPORT.json
-> lock source_commit/export_commit freshness
-> federate the exact source state into FPDG
```

Until that sequence is executed, this file is the machine-adjacent human-readable description of the validated stacked frontier.