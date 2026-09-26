import math

ALPHA_C=0.474839619052230

def b0(nf):
    return 11.0-2.0*nf/3.0

def lambda_over_mu0(nf):
    return math.exp(-8.0*math.pi**2*ALPHA_C/b0(nf))

def test_scale_binding_nonidentifiability():
    r=lambda_over_mu0(6)

    omega_Q=7.3  # arbitrary positive unit for structural test only
    mu_kin=omega_Q/2.0
    mu_rest=omega_Q

    lam_kin=r*mu_kin
    lam_rest=r*mu_rest

    # RF-N1C4's two admitted type surfaces leave an exact factor-two scale ambiguity.
    assert abs(mu_rest/mu_kin-2.0)<1e-15
    assert abs(lam_rest/lam_kin-2.0)<1e-15

    # A lattice cutoff only fixes a dimensionless Lambda*a unless a has
    # an independently supplied physical calibration.
    a=0.17
    mu0_reg=1.0/a
    lam_reg=r*mu0_reg
    assert abs(lam_reg*a-r)<1e-15
