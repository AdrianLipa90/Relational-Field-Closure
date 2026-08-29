from __future__ import annotations

import math


class OnShellMatterInformationMassSpectralError(ValueError):
    pass


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise OnShellMatterInformationMassSpectralError(
            f"{name} must be positive finite"
        )
    return value


def tetra_fs_shape_coefficient() -> float:
    return 8.0 / (9.0 * math.sqrt(3.0) * math.pi)


def matter_information_mass_ratio(m_psi: float, m_i: float) -> float:
    m_psi = _positive("m_psi", m_psi)
    m_i = _positive("m_i", m_i)
    return m_psi / m_i


def onshell_matter_phase_frequency(c: float, m_psi: float) -> float:
    c = _positive("c", c)
    m_psi = _positive("m_psi", m_psi)
    return c * m_psi


def information_gap_frequency(c: float, m_i: float) -> float:
    c = _positive("c", c)
    m_i = _positive("m_i", m_i)
    return c * m_i


def spectral_ratio_from_frequencies(
    omega_phase_abs: float,
    omega_information: float,
) -> float:
    omega_phase_abs = _positive("omega_phase_abs", omega_phase_abs)
    omega_information = _positive("omega_information", omega_information)
    return omega_phase_abs / omega_information


def onshell_spectral_ratio(c: float, m_psi: float, m_i: float) -> float:
    return spectral_ratio_from_frequencies(
        onshell_matter_phase_frequency(c, m_psi),
        information_gap_frequency(c, m_i),
    )


def spectral_match_defect(rho_omega: float) -> float:
    rho_omega = _positive("rho_omega", rho_omega)
    return abs(rho_omega - 1.0)


def mass_match_defect(m_psi: float, m_i: float) -> float:
    return abs(matter_information_mass_ratio(m_psi, m_i) - 1.0)


def same_matter_target_ratio(m_psi: float, m_i: float) -> float:
    return matter_information_mass_ratio(m_psi, m_i)


def same_target_reduced_closure_defect(
    r_alpha: float,
    r_psi_i: float,
    zeta_s: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    r_psi_i = _positive("r_psi_i", r_psi_i)
    zeta_s = _positive("zeta_s", zeta_s)
    return (
        r_alpha * r_psi_i * zeta_s**3
        - 1.0 / tetra_fs_shape_coefficient()
    )


def required_zeta_same_matter_target(
    r_alpha: float,
    r_psi_i: float,
) -> float:
    r_alpha = _positive("r_alpha", r_alpha)
    r_psi_i = _positive("r_psi_i", r_psi_i)
    return (
        1.0
        / (tetra_fs_shape_coefficient() * r_alpha * r_psi_i)
    ) ** (1.0 / 3.0)


def rfs2_target_defect_on_matter_branch(
    r_alpha: float,
    r_psi_i: float,
    zeta_s: float,
) -> float:
    """RF-S2 target defect after rho_omega=r_m=r_PsiI.

    This is intentionally evaluated in the unreduced RF-S2 form to verify
    algebraic equivalence with `same_target_reduced_closure_defect`.
    """
    r_alpha = _positive("r_alpha", r_alpha)
    r_psi_i = _positive("r_psi_i", r_psi_i)
    zeta_s = _positive("zeta_s", zeta_s)
    c_shape = tetra_fs_shape_coefficient()
    return (
        r_alpha * r_psi_i**2 * zeta_s**3
        - r_psi_i / c_shape
    )


def phase_kinetic_energy_per_carrier(omega: float) -> float:
    omega = _positive("omega", omega)
    return 0.5 * omega


def total_onshell_energy_per_carrier(omega: float) -> float:
    return _positive("omega", omega)
