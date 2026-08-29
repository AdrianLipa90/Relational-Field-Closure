from __future__ import annotations

import math


class RadialInformationMatterActionError(ValueError):
    pass


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise RadialInformationMatterActionError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise RadialInformationMatterActionError(f"{name} must be positive")
    return value


def _nonnegative(name: str, value: float) -> float:
    value = _finite(name, value)
    if value < 0.0:
        raise RadialInformationMatterActionError(f"{name} must be nonnegative")
    return value


def canonical_matter_radial(amplitude: float) -> float:
    amplitude = _nonnegative("amplitude", amplitude)
    return math.sqrt(2.0) * amplitude


def fisher_information_radial(bar_xi: float) -> float:
    bar_xi = _nonnegative("bar_xi", bar_xi)
    return math.sqrt(2.0 * bar_xi)


def amplitude_information_defect(amplitude: float, bar_xi: float) -> float:
    amplitude = _nonnegative("amplitude", amplitude)
    bar_xi = _nonnegative("bar_xi", bar_xi)
    a2 = amplitude * amplitude
    denom = a2 + bar_xi
    if denom <= 0.0:
        raise RadialInformationMatterActionError(
            "amplitude-information defect requires nondegenerate support"
        )
    return abs(a2 - bar_xi) / denom


def original_complex_scalar_lagrangian(
    amplitude: float,
    grad_amplitude_sq: float,
    phase_covector_sq: float,
    m_psi: float,
) -> float:
    amplitude = _nonnegative("amplitude", amplitude)
    grad_amplitude_sq = _finite("grad_amplitude_sq", grad_amplitude_sq)
    phase_covector_sq = _finite("phase_covector_sq", phase_covector_sq)
    m_psi = _positive("m_psi", m_psi)
    return (
        -grad_amplitude_sq
        - amplitude**2 * phase_covector_sq
        - m_psi**2 * amplitude**2
    )


def reclassified_radial_phase_lagrangian(
    phi_r: float,
    grad_phi_r_sq: float,
    phase_covector_sq: float,
    m_i: float,
) -> float:
    phi_r = _nonnegative("phi_r", phi_r)
    grad_phi_r_sq = _finite("grad_phi_r_sq", grad_phi_r_sq)
    phase_covector_sq = _finite("phase_covector_sq", phase_covector_sq)
    m_i = _positive("m_i", m_i)
    return (
        -0.5 * grad_phi_r_sq
        - 0.5 * phi_r**2 * phase_covector_sq
        - 0.5 * m_i**2 * phi_r**2
    )


def radial_potential_matter(amplitude: float, m_psi: float) -> float:
    amplitude = _nonnegative("amplitude", amplitude)
    m_psi = _positive("m_psi", m_psi)
    return m_psi**2 * amplitude**2


def radial_potential_information(phi_i: float, m_i: float) -> float:
    phi_i = _nonnegative("phi_i", phi_i)
    m_i = _positive("m_i", m_i)
    return 0.5 * m_i**2 * phi_i**2


def mass_ratio_from_radial_potential_match(
    amplitude: float,
    bar_xi: float,
    m_psi: float,
    m_i: float,
) -> float:
    """Return m_Psi/m_I after validating the nondegenerate radial binding surface.

    The function does not force equality. It verifies A^2=barXi and exposes the
    remaining mass ratio; action equality holds iff the returned ratio is 1.
    """
    if amplitude_information_defect(amplitude, bar_xi) > 1.0e-12:
        raise RadialInformationMatterActionError(
            "radial source binding A^2=bar_xi is not satisfied"
        )
    m_psi = _positive("m_psi", m_psi)
    m_i = _positive("m_i", m_i)
    return m_psi / m_i


def radial_potential_relative_defect(
    amplitude: float,
    bar_xi: float,
    m_psi: float,
    m_i: float,
) -> float:
    if amplitude_information_defect(amplitude, bar_xi) > 1.0e-12:
        raise RadialInformationMatterActionError(
            "radial source binding A^2=bar_xi is not satisfied"
        )
    phi_i = fisher_information_radial(bar_xi)
    u_psi = radial_potential_matter(amplitude, m_psi)
    u_i = radial_potential_information(phi_i, m_i)
    denom = u_psi + u_i
    if denom <= 0.0:
        raise RadialInformationMatterActionError(
            "potential defect requires nonzero radial support"
        )
    return abs(u_psi - u_i) / denom


def alpha_i_from_mass(kappa_e: float, m_i: float) -> float:
    kappa_e = _positive("kappa_e", kappa_e)
    m_i = _positive("m_i", m_i)
    return kappa_e * m_i**2


def lambda_shift_from_radial_potential(
    kappa_e: float,
    m_i: float,
    amplitude: float,
) -> float:
    kappa_e = _positive("kappa_e", kappa_e)
    m_i = _positive("m_i", m_i)
    amplitude = _nonnegative("amplitude", amplitude)
    return kappa_e * m_i**2 * amplitude**2


def lambda_shift_from_information(
    alpha_i: float,
    bar_xi: float,
) -> float:
    alpha_i = _positive("alpha_i", alpha_i)
    bar_xi = _nonnegative("bar_xi", bar_xi)
    return alpha_i * bar_xi


def validate_single_radial_representation(
    radial_terms_in_base: bool,
    radial_terms_in_closure: bool,
) -> bool:
    if radial_terms_in_base == radial_terms_in_closure:
        raise RadialInformationMatterActionError(
            "exactly one radial kinetic/potential representation must be active"
        )
    return True
