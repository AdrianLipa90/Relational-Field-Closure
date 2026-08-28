import numpy as np


ALPHA_C = 0.47483961905223004
G_YM = ALPHA_C ** -0.5


def make_lambda3_links(n=64, a=0.1, mode=5, amp=0.2):
    x = np.arange(n) * a
    field = amp * np.cos(2.0 * np.pi * mode * np.arange(n) / n)
    theta = a * G_YM * field / 2.0
    links = np.zeros((n, 3, 3), dtype=complex)
    links[:, 0, 0] = np.exp(1j * theta)
    links[:, 1, 1] = np.exp(-1j * theta)
    links[:, 2, 2] = 1.0
    return x, field, links


def recover_field(links, a=0.1):
    theta = np.angle(links[:, 0, 0])
    return 2.0 * theta / (a * G_YM)


def dominant_mode(field):
    spectrum = np.fft.rfft(field)
    magnitudes = np.abs(spectrum)
    magnitudes[0] = 0.0
    return int(np.argmax(magnitudes)), spectrum


def test_links_are_su3():
    _, _, links = make_lambda3_links()
    eye = np.eye(3)
    for link in links:
        assert np.allclose(link.conj().T @ link, eye, rtol=0.0, atol=1e-14)
        assert abs(np.linalg.det(link) - 1.0) < 1e-14


def test_exact_field_recovery_on_principal_branch():
    _, field, links = make_lambda3_links()
    recovered = recover_field(links)
    assert np.max(np.abs(recovered - field)) < 2e-14


def test_fourier_mode_recovery():
    _, field, links = make_lambda3_links(mode=5)
    recovered = recover_field(links)
    mode, spectrum = dominant_mode(recovered)
    assert mode == 5
    signal = abs(spectrum[mode])
    leakage = max(abs(spectrum[j]) for j in range(len(spectrum)) if j not in (0, mode))
    assert leakage / signal < 1e-13


def test_two_mode_commuting_color_superposition():
    n = 128
    a = 0.08
    idx = np.arange(n)
    field = (
        0.17 * np.cos(2.0 * np.pi * 7 * idx / n)
        + 0.09 * np.cos(2.0 * np.pi * 13 * idx / n)
    )
    theta = a * G_YM * field / 2.0
    links = np.zeros((n, 3, 3), dtype=complex)
    links[:, 0, 0] = np.exp(1j * theta)
    links[:, 1, 1] = np.exp(-1j * theta)
    links[:, 2, 2] = 1.0
    recovered = recover_field(links, a)
    spectrum = np.abs(np.fft.rfft(recovered))
    spectrum[0] = 0.0
    assert set(np.argsort(spectrum)[-2:]) == {7, 13}


def test_transverse_polarization_witness():
    momentum = np.array([1.0, 0.0, 0.0])
    polarization = np.array([0.0, 1.0, 0.0])
    assert abs(np.dot(momentum, polarization)) < 1e-15


def test_generator_coordinate_q_equals_gA_over_two():
    _, field, links = make_lambda3_links(a=0.1, amp=0.2)
    q = np.angle(links[:, 0, 0]) / 0.1
    assert np.max(np.abs(q - G_YM * field / 2.0)) < 2e-14
