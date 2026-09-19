# RF-GSC4H — SP3 RF-E25 Production-Packet Readiness v0.20

Status: CANDIDATE_ONLY / ALL_REQUIRED_PACKET_FIELDS_POPULATED / PROVENANCE_WRAPPER_EXECUTABLE / SOURCE_CONTROLLED_PROVENANCE_OPEN / PRODUCTION_ADMISSION_FALSE / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

V0.19 closes the mathematical RF-E25 atlas seam for the source-derived carrier and proves executable compatibility with the existing GSC4A / RF-E25 certifier.

RF-GSC4A still marks production admission open because production promotion is not a geometry problem. It requires source-owned records on one common physical realization.

This note audits the reduced production packet field by field and separates:

1. fields that can already be populated by the current source-derived candidate chain;
2. software/protocol operators that are already executable;
3. source-ownership and physical-production evidence that remains external.

## 2. Reduced RF-E25 source packet

RF-GSC4A reduces production input to six coordinates:

1. TIR spatial patch/coframe data \(e\);
2. TIR spatial overlap \(A,R\) and cocycle;
3. IDT shared clock and positive lapse \(N\);
4. GSC3 matching shift \(b\) and temporal drift \(v\);
5. source-owned patch / clock identifiers;
6. production overlap coverage.

The v0.13–v0.19 chain can populate all six fields structurally.

### 2.1 Spatial coframe

V0.16 and v0.19 provide the global quaternionic coframe and its north/south stereographic pullbacks

\[
T_N,\qquad T_S.
\]

Status:

\[
\boxed{\text{FIELD POPULATED AT CANDIDATE LEVEL}.}
\]

### 2.2 Spatial overlap

V0.19 gives

\[
q=S\frac{x}{|x|^2},
\qquad
A=\frac{\partial q}{\partial x},
\qquad
\det A>0,
\]

and uses the same global quaternionic frame on both charts, so

\[
R=I_3.
\]

Status:

\[
\boxed{\text{FIELD POPULATED AT CANDIDATE LEVEL}.}
\]

### 2.3 Shared clock / lapse

V0.17 gives the shared clock coordinate and the source-derived positive lapse

\[
N(y)=e^{L(y)}>0.
\]

Status:

\[
\boxed{\text{FIELD POPULATED AT CANDIDATE LEVEL}.}
\]

### 2.4 Matching shift / drift

V0.16 gives frame coefficients

\[
b^a=\frac{B^a}{c}.
\]

V0.19 converts them into chart shifts

\[
w_N=T_N^{-1}b,
\qquad
w_S=T_S^{-1}b,
\]

with

\[
w_S=Aw_N.
\]

The stationary chart transition has

\[
v=0.
\]

Status:

\[
\boxed{\text{FIELD POPULATED AT CANDIDATE LEVEL}.}
\]

### 2.5 Patch / clock identifiers

The frozen source supplies one reproducible realization identifier

\[
\texttt{physical:igs-sp3:sha256:...}
\]

and one reference clock identifier G01.

The stereographic chart IDs are deterministic descendants of the same source carrier.

Status:

\[
\boxed{\text{IDENTIFIERS POPULATED / SOURCE OWNERSHIP NOT PROMOTED}.}
\]

### 2.6 Coverage

The two stereographic domains satisfy

\[
U_N\cup U_S=S^3.
\]

Thus mathematical coverage is exact.

Status:

\[
\boxed{\text{CANDIDATE COVERAGE CLOSED}.}
\]

Production overlap coverage still requires a source-controlled production packet.

## 3. Shift provenance wrapper

The TIR-derived route is

\[
\boxed{\texttt{TIR\_BETA\_MATCH\_BOUND}.}
\]

It consumes:

- RF-GSC3D coefficient alias receipt;
- RF-GSC3E \(W=0\) source-binding receipt.

The existing executable provenance wrapper checks:

- exact patch coverage;
- common realization ID;
- common clock ID;
- route / source-owner typing;
- presence of GSC3D and GSC3E dependency receipts;
- unchanged downstream GSC4A / RF-E25 geometry.

V0.20 executes that wrapper using the candidate v0.19 north/south atlas packet.

Passing this wrapper proves dependency completeness.

It does not prove that the declared source references are production-controlled physical records.

## 4. Parent provenance firewalls

The parent receipts remain explicit.

RF-GSC3D leaves same-realization / same-patch / same-clock provenance as input.

RF-GSC3E states

\[
\boxed{\texttt{production\_source\_binding=OPEN\_SOURCE\_BINDING}.}
\]

RF-GSC4A provenance leaves

\[
\boxed{\texttt{SOURCE\_CONTROLLED\_PROVENANCE}}
\]

and

\[
\boxed{\texttt{PRODUCTION\_TIR\_IDT\_OR\_RFC\_SOURCE\_PACKET}}
\]

open.

Therefore an executable provenance-wrapper PASS cannot be interpreted as production promotion.

## 5. Legacy source-label firewall

The archived SP3 spatial payload contains an internal field

\[
\texttt{source\_class=PRODUCTION\_SOURCE}.
\]

However, the newer v0.13+ evidence chain explicitly classifies the same source lineage as

\[
\boxed{
\texttt{EXTERNAL\_OBSERVATIONAL\_ARCHIVE\_DERIVED\_MODEL\_LEVEL}
}
\]

with

\[
\boxed{\texttt{physical\_production\_claim=false}.}
\]

The newer explicit evidence boundary controls this candidate.

The legacy internal string cannot promote the evidence class.

## 6. Readiness theorem

If all six reduced packet coordinates are populated, the provenance wrapper passes, and GSC4A / RF-E25 geometry passes, then

\[
\boxed{
\text{missing software operators}=0.
}
\]

If source ownership / production binding remains open, then

\[
\boxed{
\text{production admission}=\mathrm{FALSE}.
}
\]

Thus the production frontier is no longer a missing mathematical or software operator.

It is an external evidence / source-authority gate.

## 7. Evidence boundary

Target classification:

\[
\boxed{
\texttt{PACKET\_READY / PRODUCTION\_AUTHORITY\_OPEN}.
}
\]

Closed:

- six-field packet structural population;
- chart geometry;
- lapse / shift binding;
- provenance route typing;
- executable GSC4A / RF-E25 compatibility;
- software operator completeness.

Open:

- source-controlled production provenance;
- RF-GSC3E physical production source binding;
- admitted production physical realization packet;
- RF-E26 global Einstein/source carrier.

No production promotion is made.
