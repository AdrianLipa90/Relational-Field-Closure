# RF-GSC5F — CCMC W6 Real-Event Run Request Manifest v0.23

Status: CANDIDATE_ONLY / EXTERNAL_RUN_REQUEST_SPEC / NO_EXTERNAL_SUBMISSION / W6_SOURCE_ACQUISITION_READY / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.22 identifies a global magnetosphere MHD run as the preferred independent source route for W6.

The public CCMC archive contains magnetosphere runs on 2015-01-20 and 2015-01-21, but the indexed runs found do not cover the frozen W6 extraction interval

\[
2015\text{-}01\text{-}21T00{:}01{:}00Z
\rightarrow
2015\text{-}01\text{-}21T00{:}03{:}00Z.
\]

Therefore this note defines the minimum reproducible request manifest for a new real-event run.

It does not submit a request to CCMC.

## 2. Fixed science target

Target realization:

    RT218283.SP3@8013

Target extraction epochs:

    2015-01-21T00:01:00Z
    2015-01-21T00:03:00Z

Required extraction window:

\[
[2015\text{-}01\text{-}21T00{:}01{:}00Z,
2015\text{-}01\text{-}21T00{:}03{:}00Z].
\]

The simulation may start earlier and end later as required by model spin-up and numerical stability.

Model-specific warm-up duration is intentionally not invented here.

## 3. Preferred model

Primary request:

\[
\boxed{
\text{SWMF / Global Magnetosphere / BATSRUS}
}
\]

Request class:

    REAL_EVENT

Preferred output coordinate system:

    GSM

Secondary fallback:

    OpenGGCM

A fallback run must preserve the same target interval, source-lineage requirements and output-variable requirements.

## 4. External drivers

Preferred driver lineage:

    OMNI solar-wind / IMF data

Acceptable alternative:

    ACE Level-2 solar-wind / IMF data

The final run receipt must preserve the immutable driver-data identifier or digest actually used by CCMC.

Driver data are part of W6 source provenance.

## 5. Required output variables

Minimum required 3D fields:

    density
    pressure
    velocity_x
    velocity_y
    velocity_z
    magnetic_field_x
    magnetic_field_y
    magnetic_field_z

Preferred additional fields:

    current_density_x
    current_density_y
    current_density_z
    temperature
    internal_energy
    electric_field
    composition
    equation_of_state metadata

If electric field is not directly exported, any use of

\[
\mathbf E=-\mathbf v\times\mathbf B
\]

must be tied to an explicit ideal-MHD model declaration.

## 6. Required model metadata

The acquired run must record:

    run_id
    model_name
    model_version
    run_type
    start_time
    end_time
    output_coordinate_system
    solar_wind_input_source
    grid_description
    dipole_update_policy
    solver_name
    limiter
    timestep_or_time_control
    equation_of_state_or_closure
    density_convention
    pressure_convention

Unknown metadata must remain OPEN.

It must not be guessed by the adapter.

## 7. Output cadence

The run must provide enough temporal support to reconstruct the field at both target epochs.

Acceptable:

- exact snapshots at both epochs;
- bracketing snapshots with a declared interpolation receipt.

The acquisition contract does not impose an arbitrary global output cadence.

## 8. Spatial coverage

The requested magnetosphere output must cover the complete physical image of both atlas patches:

    SP3_STEREO_N
    SP3_STEREO_S

under the admitted chart-to-source-coordinate map and the source-to-GSM transform.

Anchor-only output is insufficient.

## 9. Frame transform

Before W6 construction, the pipeline must certify:

\[
\text{SP3 frame}
\to
\text{Earth/geocentric reference frame}
\to
\text{GSM}.
\]

The transform receipt must bind:

    epoch
    Earth orientation inputs
    transform implementation
    implementation version
    auxiliary data digests

IERS conventions / GEOPACK may supply this layer, but are not the W6 source tensor.

## 10. Requested artifact set

Minimum post-run acquisition bundle:

    RUN_METADATA.json
    DRIVER_DATA_OR_REFERENCE
    GRID_METADATA
    FIELD_SNAPSHOTS_OR_3D_OUTPUT
    OUTPUT_VARIABLE_DICTIONARY
    MODEL_CLOSURE_METADATA
    COORDINATE_FRAME_METADATA
    CCMC_RUN_ID
    IMMUTABLE_DIGESTS

The adapter then constructs:

    FRAME_TRANSFORM_RECEIPT
    INTERPOLATION_RECEIPT
    PATCH_COVERAGE_RECEIPT
    SOURCE_TENSOR_CONSTRUCTION_RECEIPT
    W6_N_PATCH_RECEIPT
    W6_S_PATCH_RECEIPT

## 11. No-submission boundary

This manifest is prepared for external execution but does not authorize submission under the repository owner’s identity.

External submission requires explicit operator authorization.

## 12. Current frontier

Closed:

- model family selection;
- required target interval;
- driver-data classes;
- required field set;
- metadata requirements;
- patch coverage rule;
- transform/interpolation/source-lineage requirements.

Open:

- actual CCMC run ID;
- actual run outputs;
- actual full-patch coverage;
- actual W6 source tensor;
- RF-E24 local-solution receipts;
- RF-E26 production promotion.
