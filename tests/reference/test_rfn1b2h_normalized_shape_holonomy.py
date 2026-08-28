from fractions import Fraction


def normalize(values):
    total = sum(values)
    assert total > 0
    return tuple(Fraction(v, total) for v in values)


def lift(profile, scale):
    return tuple(scale * p for p in profile)


def relative_l1_defect(original, reconstructed):
    numerator = sum(abs(Fraction(a) - Fraction(b)) for a, b in zip(original, reconstructed))
    denominator = sum(abs(Fraction(a)) for a in original)
    return numerator / denominator


def test_positive_scaling_preserves_normalized_shape_exactly():
    q1 = (2, 3, 5)
    q2 = (4, 6, 10)
    assert normalize(q1) == normalize(q2) == (
        Fraction(1, 5),
        Fraction(3, 10),
        Fraction(1, 2),
    )


def test_scale_aware_lift_closes_holonomy_exactly():
    for q in ((2, 3, 5), (4, 6, 10)):
        profile = normalize(q)
        reconstructed = lift(profile, sum(q))
        assert reconstructed == tuple(Fraction(v) for v in q)
        assert relative_l1_defect(q, reconstructed) == 0


def test_scale_blind_unit_lift_has_exact_extensive_defect():
    q1 = (2, 3, 5)
    q2 = (4, 6, 10)
    assert relative_l1_defect(q1, lift(normalize(q1), 1)) == Fraction(9, 10)
    assert relative_l1_defect(q2, lift(normalize(q2), 1)) == Fraction(19, 20)


def test_general_positive_sector_defect_formula():
    q = (3, 7, 10)
    total = sum(q)
    profile = normalize(q)
    for scale in (1, 5, 20, 35):
        lhs = relative_l1_defect(q, lift(profile, scale))
        rhs = abs(Fraction(1) - Fraction(scale, total))
        assert lhs == rhs


def test_energy_conversion_rescales_amount_and_preserves_shape():
    q = (2, 3, 5)
    rho_eps1 = tuple(Fraction(v) for v in q)
    rho_eps3 = tuple(Fraction(3 * v) for v in q)
    assert normalize(rho_eps1) == normalize(rho_eps3)
    assert sum(rho_eps3) == 3 * sum(rho_eps1)


def test_combined_source_mass_factorization_is_exact_at_cell_level():
    q = (2, 3, 5)
    q_total = sum(q)
    profile = normalize(q)
    epsilon_over_c2 = Fraction(7, 11)
    total_mass_scale = epsilon_over_c2 * q_total

    direct_cell_mass = tuple(epsilon_over_c2 * Fraction(v) for v in q)
    factorized_cell_mass = tuple(total_mass_scale * p for p in profile)
    assert direct_cell_mass == factorized_cell_mass
