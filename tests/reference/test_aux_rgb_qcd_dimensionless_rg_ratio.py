import math

KAPPA=math.log(2.0)/(24.0*math.pi)
PHI=(1.0+math.sqrt(5.0))/2.0
ALPHA_C=math.log(PHI)-KAPPA*math.log(2.0)

def b0(nf):
    return 11.0-2.0*nf/3.0

def inverse_g2(mu_over_mu0,nf,alpha0=ALPHA_C):
    return alpha0+b0(nf)/(8.0*math.pi**2)*math.log(mu_over_mu0)

def lambda_ratio(nf,alpha0=ALPHA_C):
    return math.exp(-8.0*math.pi**2*alpha0/b0(nf))

def test_fixed_nf_dimensionless_rg_ratio():
    assert abs(ALPHA_C-0.474839619052230)<1e-15

    r6=lambda_ratio(6)
    assert abs(r6-0.004719859618240724)<1e-15
    assert abs(inverse_g2(r6,6))<1e-14

    r0=lambda_ratio(0)
    assert abs(r0-0.03309581284558998)<1e-15
    assert abs(inverse_g2(r0,0))<1e-14

    # Asymptotic freedom: inverse g^2 increases toward the UV for b0>0.
    assert inverse_g2(10.0,6)>ALPHA_C
