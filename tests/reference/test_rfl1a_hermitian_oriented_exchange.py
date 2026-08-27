import cmath
import math

HBAR = 1.054571817e-34


def exchange_matrix(E, tau):
    J = E * cmath.exp(1j * tau)
    return [
        [0j, 0j, 0j, 0j],
        [0j, 0j, J, 0j],
        [0j, J.conjugate(), 0j, 0j],
        [0j, 0j, 0j, 0j],
    ]


def evolve_single_excitation(a01, a10, E, tau, dt):
    J = E * cmath.exp(1j * tau)
    r = abs(J)
    phi = r * dt / HBAR
    c = math.cos(phi)
    s = math.sin(phi)
    unit = J / r
    return (
        c * a01 - 1j * s * unit * a10,
        c * a10 - 1j * s * unit.conjugate() * a01,
    )


def concurrence_01_10(a01, a10):
    return 2.0 * abs(a01 * a10)


def test_exchange_matrix_is_hermitian():
    H = exchange_matrix(3.0, 0.71)
    for i in range(4):
        for j in range(4):
            assert abs(H[i][j] - H[j][i].conjugate()) < 1e-15


def test_single_excitation_spectrum_closes_to_source_energy():
    E = 2.7
    tau = 1.2
    J = E * cmath.exp(1j * tau)
    spectral_radius = abs(J)
    assert math.isclose(spectral_radius, abs(E), rel_tol=2e-15, abs_tol=2e-15)


def test_quarter_exchange_generates_unit_concurrence_from_10():
    E = 4.2
    tau = 0.44
    dt = math.pi * HBAR / (4.0 * abs(E))
    a01, a10 = evolve_single_excitation(0j, 1 + 0j, E, tau, dt)
    assert math.isclose(abs(a01) ** 2 + abs(a10) ** 2, 1.0, rel_tol=2e-15, abs_tol=2e-15)
    assert math.isclose(concurrence_01_10(a01, a10), 1.0, rel_tol=2e-15, abs_tol=2e-15)


def test_half_exchange_transfers_population():
    E = 4.2
    tau = 0.44
    dt = math.pi * HBAR / (2.0 * abs(E))
    a01, a10 = evolve_single_excitation(0j, 1 + 0j, E, tau, dt)
    assert math.isclose(abs(a01) ** 2, 1.0, rel_tol=2e-15, abs_tol=2e-15)
    assert math.isclose(abs(a10) ** 2, 0.0, abs_tol=2e-15)


def test_orientation_reversal_preserves_population_and_changes_phase():
    E = 3.1
    tau = 0.63
    dt = math.pi * HBAR / (4.0 * abs(E))
    p01, p10 = evolve_single_excitation(0j, 1 + 0j, E, tau, dt)
    n01, n10 = evolve_single_excitation(0j, 1 + 0j, E, -tau, dt)
    assert math.isclose(abs(p01) ** 2, abs(n01) ** 2, rel_tol=2e-15, abs_tol=2e-15)
    assert math.isclose(abs(p10) ** 2, abs(n10) ** 2, rel_tol=2e-15, abs_tol=2e-15)
    phase_delta = cmath.phase(p01 / n01)
    assert math.isclose(phase_delta, 2.0 * tau, rel_tol=2e-15, abs_tol=2e-15)


def test_pauli_quadratures_reconstruct_complex_exchange():
    E = 5.0
    tau = -0.81
    jx = E * math.cos(tau)
    jy = E * math.sin(tau)
    reconstructed = complex(jx, jy)
    direct = E * cmath.exp(1j * tau)
    assert abs(reconstructed - direct) < 2e-15


if __name__ == "__main__":
    tests = [name for name, obj in globals().items() if name.startswith("test_") and callable(obj)]
    for name in tests:
        globals()[name]()
    print(f"PASS {len(tests)}/{len(tests)}")
