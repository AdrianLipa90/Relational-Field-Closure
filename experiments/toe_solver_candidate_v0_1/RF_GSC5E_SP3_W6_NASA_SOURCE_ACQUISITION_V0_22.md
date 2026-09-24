# RF-GSC5E — SP3 W6 NASA Source Acquisition Matrix v0.22

Status: CANDIDATE_ONLY / EXTERNAL_SOURCE_DISCOVERY / RAW_CDF_VALIDATION_OPEN / PATCH_COVERAGE_OPEN / NO_W6_PROMOTION / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.21 defines the fail-closed W6 source receipt contract. The remaining task is no longer a theorem gap but source acquisition.

This note records a concrete external-data route for the frozen SP3 epoch

- source epoch 1: 2015-01-21T00:01:00Z
- source epoch 2: 2015-01-21T00:03:00Z

using NASA Space Physics Data Facility / CDAWeb products from the Van Allen Probes.

The goal is to identify measurements that are independent of the target metric construction and could, after raw-file validation and coverage certification, contribute to an independently sourced stress-energy packet.

This note does not claim W6 completion.

## 2. Candidate external source family

Primary source archive:

NASA Space Physics Data Facility, CDAWeb.

Mission family:

Van Allen Probes / Radiation Belt Storm Probes (RBSP-A and RBSP-B).

The candidate route is attractive because it provides independent measurements of:

- magnetic field;
- electric field;
- plasma/electron density;
- particle moments and temperatures;
- particle fluxes;
- spacecraft position / orbit support data.

These are source-owned observables rather than quantities algebraically reconstructed from the RFC metric.

## 3. Web-verified dataset inventory

### 3.1 RBSP-A EMFISIS magnetic field

Dataset family:

RBSP-A MAGNETOMETER 4SEC GSM EMFISIS L3.

Public archive index contains the daily file

    rbsp-a_magnetometer_4sec-gsm_emfisis-l3_20150121_v1.3.3.cdf

Status:

    DAILY_FILE_METADATA_CONFIRMED
    RAW_CDF_BYTES_NOT_VALIDATED_IN_CURRENT_RUNTIME

Potential W6 role:

    independent electromagnetic field input B

### 3.2 RBSP-A EMFISIS density

Dataset family:

RBSP-A EMFISIS Density L4.

Public archive index contains

    rbsp-a_density_emfisis-l4_20150121_v1.5.18.cdf

Status:

    DAILY_FILE_METADATA_CONFIRMED
    RAW_CDF_BYTES_NOT_VALIDATED_IN_CURRENT_RUNTIME

Potential W6 role:

    independent electron-density / plasma-density input

### 3.3 RBSP-B EMFISIS density

Dataset family:

RBSP-B EMFISIS Density L4.

Public archive index contains

    rbsp-b_density_emfisis-l4_20150121_v1.5.16.cdf

Status:

    DAILY_FILE_METADATA_CONFIRMED
    RAW_CDF_BYTES_NOT_VALIDATED_IN_CURRENT_RUNTIME

Potential W6 role:

    independent second-spacecraft plasma-density input

### 3.4 RBSP-A / RBSP-B EFW L3 electric field

CDAWeb metadata lists

    RBSPA_EFW-L3
    RBSPB_EFW-L3

as spinfit DC electric-field products in M-GSE coordinates.

Status:

    DATASET_METADATA_CONFIRMED
    EXACT_2015_01_21_RAW_FILE_NOT_YET_VALIDATED

Potential W6 role:

    independent electromagnetic field input E

### 3.5 RBSP-A / RBSP-B ECT-HOPE moments

CDAWeb metadata lists

    RBSPA_REL04_ECT-HOPE-MOM-L3
    RBSPB_REL04_ECT-HOPE-MOM-L3

with particle moments including species-resolved temperatures and orbit / magnetic-coordinate support variables.

Status:

    DATASET_METADATA_CONFIRMED
    RAW_2015_01_21_PAYLOAD_NOT_YET_VALIDATED

Potential W6 role:

    independent plasma matter moments
    species density / temperature / anisotropy inputs
    particle source-model calibration

### 3.6 RBSP-A / RBSP-B HOPE science fluxes

CDAWeb lists spin-resolved and spin-averaged electron and ion flux products spanning the Van Allen Probes mission interval including 2015.

Status:

    DATASET_METADATA_CONFIRMED
    RAW_INTERVAL_EXTRACTION_OPEN

Potential W6 role:

    independent particle-distribution evidence
    cross-check of moment-derived source tensors

## 4. Candidate physical source decomposition

A physically independent candidate source packet may be decomposed as

[
T_{mu
u}^{m source}
=
T_{mu
u}^{m EM}
+
T_{mu
u}^{m plasma}
+
T_{mu
u}^{m energetic}
+cdots
]

with every term sourced by instrument data rather than by the target Einstein tensor.

### 4.1 Electromagnetic part

Measured E and B may supply the electromagnetic stress-energy tensor after:

1. common frame reconciliation;
2. unit normalization;
3. interpolation to the admitted source support;
4. uncertainty propagation;
5. immutable source-digest binding.

The construction receipt must retain the measured-field provenance.

### 4.2 Plasma matter part

Particle moments may supply density, bulk velocity and pressure information.

A relativistic or controlled nonrelativistic plasma stress-energy construction must explicitly declare:

- species included;
- moment closure;
- anisotropy treatment;
- frame convention;
- interpolation model;
- uncertainty budget.

No pressure tensor may be silently inferred from the RFC metric.

### 4.3 Energetic-particle correction

HOPE / MagEIS / REPT / RBSPICE products may be used to test whether the lower-energy moment packet misses a non-negligible energetic-particle contribution.

This is a completeness test, not automatically a required dominant term.

## 5. Same-time requirement

The W6 packet must be evaluated on a time support covering the frozen SP3 interval

[
[2015	ext{-}01	ext{-}21 00{:}01{:}00Z,,
 2015	ext{-}01	ext{-}21 00{:}03{:}00Z].
]

A dataset existing on the same UTC day is not sufficient by itself.

Required next validation:

    exact sample timestamps
    quality flags
    missing-data intervals
    coordinate-frame metadata
    spacecraft ephemeris at the samples

## 6. Spatial support problem

Two Van Allen Probe trajectories supply sparse one-dimensional measurement tracks through the magnetosphere.

That is not equivalent to full support on either stereographic atlas patch.

Therefore

    coverage_certified = false

until an independent and validated reconstruction supplies the full admitted patch support.

Permissible future routes include:

- multi-spacecraft assimilation;
- source-owned field interpolation with quantified error;
- physically justified axisymmetric / field-aligned reduction where applicable;
- independently calibrated global magnetospheric source model constrained by the observations.

Any such route must be validated independently of the target RFC metric.

## 7. Critical firewall

The following implication is forbidden:

    sparse probe observations
    -> arbitrary interpolation
    -> full patch T_mn
    -> W6 PASS

without an explicit source-domain coverage theorem or validated source model.

Similarly, the following remains forbidden:

[
T_{mu
u}
=
rac{G_{mu
u}+Lambda g_{mu
u}}{kappa_E}
]

as physical source evidence.

## 8. Current acquisition status

| Coordinate | Status |
|---|---|
| exact frozen SP3 epoch | FIXED |
| NASA independent source archive | FOUND |
| RBSP-A 2015-01-21 B-file metadata | CONFIRMED |
| RBSP-A 2015-01-21 density-file metadata | CONFIRMED |
| RBSP-B 2015-01-21 density-file metadata | CONFIRMED |
| EFW A/B dataset metadata | CONFIRMED |
| HOPE-MOM A/B dataset metadata | CONFIRMED |
| raw CDF byte validation | OPEN |
| exact 00:01–00:03 sample availability | OPEN |
| source-frame reconciliation | OPEN |
| independent T_mn construction | OPEN |
| full N/S patch source coverage | OPEN |
| W6 physical receipt | OPEN |
| RF-E26 production promotion | OPEN |

## 9. Minimal next executable task

The next executable source-acquisition stage is:

1. retrieve immutable raw CDFs for the exact interval;
2. hash each source file;
3. extract timestamps, quality flags, spacecraft positions and physical variables;
4. build a source-only observation packet;
5. reject the packet if exact interval coverage is absent;
6. construct E/B and plasma source components without using the RFC target metric as evidence;
7. test spatial support against the v0.19 atlas;
8. keep W6 OPEN unless full-patch coverage is independently certified.

## 10. Evidence boundary

This document records a concrete candidate acquisition route only.

It does not state that Van Allen Probe observations already satisfy W6.

It does not promote any model-derived source tensor.

It does not close RF-E26.

Current verdict:

    EXTERNAL_SOURCE_ROUTE_IDENTIFIED
    RAW_SOURCE_VALIDATION_OPEN
    PATCH_COVERAGE_OPEN
    W6_OPEN
