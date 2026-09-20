# RF-GSC5E — SP3 W6 MHD Source Acquisition Route v0.22

Status: CANDIDATE_ONLY / EXTERNAL_SOURCE_ACQUISITION_PLAN / INDEPENDENT_MATTER_EM_SOURCE_ROUTE / NO_SOURCE_PACKET_YET / CANON_ALLOWED_FALSE

Date: 2026-09-20

## 1. Purpose

V0.21 defines the fail-closed W6 receipt schema.

The remaining task is no longer additional geometry. It is acquisition of an independently sourced physical field packet capable of constructing a rank-two stress-energy tensor over both admitted atlas patches:

\[
\mathrm{SP3\_STEREO\_N},
\qquad
\mathrm{SP3\_STEREO\_S}.
\]

This note defines the preferred source-acquisition route and the role of each external data family.

No external W6 packet is claimed here.

## 2. Fixed source epoch and realization

The current frozen observational realization is inherited from the SP3 parent:

\[
\texttt{RT218283.SP3@8013}
\]

with the two source epochs

\[
2015\text{-}01\text{-}21T00{:}01{:}00Z
\]

and

\[
2015\text{-}01\text{-}21T00{:}03{:}00Z.
\]

The acquisition route must cover at least this interval and the full spatial image of both atlas patches under the admitted chart-to-source coordinate map.

## 3. Source-role separation

The following source classes have different roles and must not be conflated.

### 3.1 IGS GNSS products

Role:

- source event positions;
- source event velocities / finite differences;
- satellite and station clocks;
- realization and timing provenance.

IGS data are not accepted as an independent stress-energy tensor by themselves.

They remain the geometry/clock observation lineage.

Reference family:

- IGS final orbit products in SP3 format;
- IGS final clock products;
- associated solution summaries and ERP products.

### 3.2 IERS / GEOPACK frame and time transformations

Role:

- Earth-fixed / inertial / geocentric frame bookkeeping;
- proper and coordinate time conventions;
- transformation between the source realization and geospace model coordinates.

These conventions are not a stress-energy source.

### 3.3 Earth gravity / geopotential models

Examples:

- EGM2008;
- WGS84 gravitational constants and frame definitions.

Role:

- independent geodetic/gravity context;
- frame and gravitational-potential cross-checks.

These are explicitly forbidden from being re-labelled as the W6 matter source tensor.

### 3.4 Earth interior matter models

Example:

- PREM density profile.

Role:

- independent material-density source model inside the Earth.

PREM does not by itself cover the current GNSS/magnetosphere patch domain and therefore cannot alone satisfy W6 for the present two-chart carrier.

### 3.5 Atmospheric / ionospheric empirical models

Examples:

- NRLMSIS;
- IRI.

Role:

- atmospheric and ionospheric matter/plasma context.

Their nominal altitude domains do not provide full coverage of the current GNSS-orbit source carrier and therefore they are auxiliary rather than sufficient W6 sources on this route.

### 3.6 Global magnetosphere MHD models

Preferred primary candidates:

- SWMF / GM = BATSRUS;
- OpenGGCM.

These models expose full three-dimensional fields including, depending on model/run:

\[
\rho,\quad
p,\quad
\mathbf v,\quad
\mathbf B,
\quad
\mathbf J
\]

and are driven by external solar-wind / IMF conditions rather than by the target TIR/RFC geometry.

Therefore they are the preferred route for constructing an independent matter-plus-electromagnetic source tensor on the current orbital-domain carrier.

## 4. Preferred primary source

Primary candidate:

\[
\boxed{
\text{NASA CCMC SWMF / GM = BATSRUS}
}
\]

Reason:

- global magnetosphere domain;
- time-dependent;
- outputs density, pressure, velocity, magnetic field and current;
- source is driven by external solar-wind plasma and magnetic-field conditions;
- model output is independent of the target RFC metric construction.

Secondary independent cross-check:

\[
\boxed{
\text{OpenGGCM}
}
\]

which exports an analogous global MHD field family.

No production preference is inferred from model branding alone.

The accepted packet must still satisfy v0.21 provenance, coverage and local RF-E24 residual checks.

## 5. Required external run interval

The model source packet must cover a time interval containing both frozen SP3 epochs.

Minimum:

\[
[2015\text{-}01\text{-}21T00{:}01Z,
\,
2015\text{-}01\text{-}21T00{:}03Z].
\]

Preferred acquisition includes a larger symmetric margin to support interpolation and derivative estimates.

The exact margin is acquisition metadata and is not hard-coded into the W6 theorem.

## 6. Required MHD variables

A usable run must expose, on the relevant model grid and times:

    mass_density or number_density with species/mass convention
    plasma_pressure
    velocity_x
    velocity_y
    velocity_z
    magnetic_field_x
    magnetic_field_y
    magnetic_field_z

Preferred additional variables:

    current_density_x
    current_density_y
    current_density_z
    electric_field or enough metadata to derive it under the declared model closure
    temperature
    composition
    internal_energy
    equation_of_state metadata
    adiabatic_index or equivalent closure metadata

A run lacking enough thermodynamic closure metadata cannot be promoted directly to a full source tensor.

## 7. Source tensor construction classes

The W6 adapter may accept one of two explicitly typed constructions.

### 7.1 Full relativistic MHD source

Preferred when the acquired model outputs and metadata are sufficient to define a covariant ideal/resistive relativistic-MHD tensor.

The construction receipt must state:

- signature convention;
- unit system;
- fluid four-velocity construction;
- enthalpy / equation of state;
- electromagnetic field tensor construction;
- pressure convention;
- mass-density convention;
- all conversions.

### 7.2 Nonrelativistic-MHD approximation packet

Permitted only at CANDIDATE_ONLY / MODEL_LEVEL authority.

The receipt must explicitly state:

\[
\texttt{RELATIVISTIC\_SOURCE\_APPROXIMATION}
\]

and quantify the expansion regime, including at minimum

\[
|\mathbf v|/c.
\]

This class cannot by itself satisfy a production W6 claim unless an independently justified approximation error budget is admitted by the production contract.

## 8. Ideal-MHD electric field

If the selected model/run does not export \(\mathbf E\) but declares ideal MHD, the adapter may derive

\[
\boxed{
\mathbf E
=
-\mathbf v\times\mathbf B.
}
\]

This is allowed only when the model/run provenance explicitly states the ideal-MHD closure used for that output.

The relation may not be silently assumed.

## 9. Coordinate pipeline

The source model and SP3 carrier need not share the same coordinates.

The adapter must emit an immutable transform receipt for

\[
\text{SP3 source coordinates}
\longrightarrow
\text{geocentric inertial / Earth-fixed intermediate}
\longrightarrow
\text{model frame}
\]

such as GSM when required by the selected MHD source.

The transform receipt must bind:

    source epoch
    source reference frame
    target model frame
    Earth orientation inputs
    transformation library/version
    transformation parameters
    digest of all auxiliary inputs

No implicit coordinate conversion is accepted.

## 10. Patch map and coverage

For each atlas chart point, the source-derived carrier provides an underlying source-coordinate point.

The W6 adapter must define

\[
\Pi_{\rm phys}:
\mathcal U_{N/S}
\to
\text{external model coordinates}.
\]

Coverage must be certified for the full admitted patch domain, not only the five SP3 anchors.

The adapter must reject:

- anchor-only coverage;
- extrapolation beyond declared model domain without a separate approximation receipt;
- coordinate points inside excluded model regions;
- time interpolation beyond declared run support.

## 11. Interpolation

The acquired MHD grid will generally not coincide with the source-derived atlas coordinates.

Any interpolation must be typed and immutable.

Minimum receipt fields:

    interpolation_method
    source_grid_metadata_digest
    temporal_interpolation_method
    spatial_interpolation_method
    boundary_behavior
    missing_value_policy
    interpolation_error_estimate
    implementation_digest

Interpolation cannot repair missing domain coverage.

## 12. Independent source lineage

The physical source lineage must be upstream of the target RFC geometry.

Accepted lineage form:

\[
\boxed{
\text{solar-wind / IMF observations}
\to
\text{independent MHD run}
\to
\text{MHD field packet}
\to
T_{\mu\nu}.
}
\]

Forbidden lineage:

\[
\boxed{
g
\to
G[g]
\to
T:=(G+\Lambda g)/\kappa_E.
}
\]

The latter remains an effective tensor identity and not independent W6 evidence.

## 13. Proposed acquisition bundle

The preferred bundle contains:

    SOURCE_A:
      IGS final SP3 orbit / clock realization

    SOURCE_B:
      IERS / frame-transform metadata

    SOURCE_C:
      SWMF/BATSRUS run for the source epoch
      or OpenGGCM equivalent

    SOURCE_D:
      immutable solar-wind / IMF driver data used by the MHD run

    SOURCE_E:
      optional IRI / NRLMSIS / empirical geospace cross-checks

    SOURCE_F:
      optional PREM / EGM context, explicitly non-W6-source

Only SOURCE_C plus its independent SOURCE_D lineage is the primary candidate for constructing the W6 tensor over the present orbital-domain carrier.

## 14. Acquisition gates

A candidate external run is admitted for W6 tensor construction only if all pass:

1. correct epoch coverage;
2. full patch spatial coverage;
3. density convention known;
4. pressure convention known;
5. velocity vector present;
6. magnetic field vector present;
7. equation-of-state / closure metadata sufficient;
8. coordinate transformation reproducible;
9. immutable model/run ID and digest available;
10. immutable driver-data lineage available;
11. interpolation receipt available;
12. target metric is not an input to source construction.

## 15. Current classification

Closed:

- W6 receipt schema;
- atlas patch identities;
- full-patch coverage requirement;
- independence firewall;
- preferred external source class;
- required variable set;
- coordinate/coverage/interpolation requirements.

Open external acquisition:

- actual SWMF/OpenGGCM run artifact for the frozen epoch;
- immutable driver-data artifact;
- full-patch model-domain coverage check;
- source tensor construction receipt;
- RF-E24 residual test on both patches.

Therefore:

\[
\boxed{
\text{W6 theory/infrastructure}
=
\text{CLOSED}
}
\]

while

\[
\boxed{
\text{W6 external physical evidence}
=
\text{OPEN}.
}
\]
