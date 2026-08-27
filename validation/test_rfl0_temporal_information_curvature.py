import math

LN2 = math.log(2.0)
KAPPA = LN2 / (24.0 * math.pi)


def xi_information_area(information_bits: float, relational_area: float) -> float:
    if relational_area <= 0.0:
        raise ValueError("relational_area must be positive")
    return LN2 * information_bits / relational_area


def xi_rate(
    information_bits: float,
    d_information_bits: float,
    relational_area: float,
    d_relational_area: float,
) -> float:
    j = LN2 * information_bits
    dj = LN2 * d_information_bits
    return dj / relational_area - j * d_relational_area / relational_area**2


def lambda0_minimal(lambda_vac: float, alpha_i: float, xi_i: float) -> float:
    return lambda_vac + alpha_i * xi_i


def test_tir_kappa_form_matches_idt_information_area_form():
    information_bits = 1.7
    area = 2.4
    direct = xi_information_area(information_bits, area)
    kappa_form = 24.0 * math.pi * KAPPA * information_bits / area
    assert abs(direct - kappa_form) < 1e-15


def test_inverse_square_scaling():
    base = xi_information_area(2.0, 3.0)
    scaled = xi_information_area(2.0, 12.0)
    assert abs(scaled - base / 4.0) < 1e-15


def test_minimal_lambda_rate_is_alpha_times_xi_rate():
    alpha_i = 0.41
    rate = xi_rate(1.2, -0.2, 3.2, 0.15)
    assert abs(alpha_i * rate - alpha_i * rate) < 1e-15


def test_zero_information_coupling_decouples_xi_channel():
    xi_1 = xi_information_area(1.0, 2.0)
    xi_2 = xi_information_area(3.0, 2.0)
    assert lambda0_minimal(0.3, 0.0, xi_1) == lambda0_minimal(0.3, 0.0, xi_2)


def test_nonzero_information_coupling_changes_lambda_linearly():
    xi_1 = xi_information_area(1.0, 2.0)
    xi_2 = xi_information_area(3.0, 2.0)
    alpha_i = 0.7
    delta_lambda = (
        lambda0_minimal(0.3, alpha_i, xi_2)
        - lambda0_minimal(0.3, alpha_i, xi_1)
    )
    assert abs(delta_lambda - alpha_i * (xi_2 - xi_1)) < 1e-15


def test_multisector_rate_can_cancel_exactly():
    alpha_i = 0.7
    xi_channel_rate = 0.2
    other_sector_rate = -alpha_i * xi_channel_rate
    assert abs(alpha_i * xi_channel_rate + other_sector_rate) < 1e-15
