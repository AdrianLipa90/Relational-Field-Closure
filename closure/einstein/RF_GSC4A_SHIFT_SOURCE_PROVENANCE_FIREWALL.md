# RF-GSC4A — Shift-Source Provenance Firewall

Status: `EXACT_ROUTE_TYPING / EXECUTABLE_PROVENANCE_ADMISSION / GSC3E_REQUIRED_ON_TIR_DERIVED_ROUTE / SOURCE_OWNERSHIP_INPUT_OPEN`

Date: 2026-08-31

## Purpose

RF-GSC4A proves the exact source-to-RF-E25 atlas assembly from a positive lapse, spatial coframe, shift, and spatial overlap data. The geometric assembly admits two source routes for the shift carrier.

## Route A — RFC independent shift

`RFC_INDEPENDENT_SHIFT` admits a shift field supplied by an RFC-owned source record. This route uses the RF-E8 shift as an independent RFC input and therefore does not consume the TIR `beta_match` identity gate.

Required provenance fields are:

- common physical `realization_id`;
- common `clock_id`;
- patch identifier;
- RFC source reference.

The exact GSC4A overlap law remains

\[
 b_q=A_{qp}b_p-v_{qp}.
\]

## Route B — TIR beta_match bound shift

`TIR_BETA_MATCH_BOUND` admits a shift representing the TIR inter-leaf matching carrier. This route consumes two already separated candidate gates:

1. RF-GSC3D: the shared matching-one-form coefficient alias,
   \[
   \beta_\Theta=\alpha b_0;
   \]
2. RF-GSC3E: the realization-level source-binding firewall selecting
   \[
   W:=\beta_t-cb_0=0.
   \]

Its provenance packet therefore includes source references for both GSC3D and GSC3E on the declared realization.

## Route separation theorem

The RF-E25/GSC4A geometry depends on the admitted shift values and their overlap law. The provenance of those values is a separate typed coordinate. Therefore

```text
RFC independent b
    -> GSC4A geometry

TIR beta_match-derived b
    -> GSC3D alias
    -> GSC3E W=0 realization binding
    -> GSC4A geometry
```

are two admissible routes into the same exact geometric assembler.

This preserves the RFC-owned shift route while making the TIR-derived route explicitly consume the source-binding witness discovered by the GSC3E covariant-family theorem.

## Executable admission

Implementation:

`src/rfc/gsc4a_shift_source_provenance.py`

Reference tests:

`tests/reference/test_gsc4a_shift_source_provenance.py`

The production-facing wrapper first certifies:

- exact patch coverage;
- one common realization identifier;
- one common clock identifier;
- valid route/source-owner pairing;
- required GSC3D/GSC3E references on the TIR-derived route;

and then delegates unchanged geometry to

`assemble_source_shared_spacetime_atlas(...)`.

## Provenance boundary

`source_owner`, `source_reference`, and receipt identifiers are declared source-provenance inputs. Repository/source ownership remains controlled by the source records issuing those references. The executable layer certifies the declared route and its dependency completeness.

## Claim ledger

| Claim | Status |
|---|---|
| RFC independent shift is an admissible GSC4A input route | `EXACT TYPING` |
| TIR-derived shift consumes RF-GSC3D coefficient alias | `EXACT DEPENDENCY` |
| TIR-derived shift consumes RF-GSC3E `W=0` source-binding gate | `EXACT DEPENDENCY` |
| both admitted routes feed the same GSC4A geometry | `EXACT` |
| executable provenance admission | `HOSTED VALIDATION TARGET` |
| source ownership / production source records | `OPEN SOURCE INPUT` |
| RF-E25 production atlas coverage | `OPEN PRODUCTION INPUT` |

GREMLIN, Terminal36D and PhaseNav remain candidate/audit layers. Hosted deterministic validation remains the executable evidence surface.
