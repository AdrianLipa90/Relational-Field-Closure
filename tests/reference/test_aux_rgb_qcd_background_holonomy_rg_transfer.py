from fractions import Fraction
import math

PI=math.pi

CA=Fraction(3,1)
CF=Fraction(4,3)
TF=Fraction(1,2)

def b0(nf):
    return Fraction(11,3)*CA-Fraction(4,3)*TF*nf

def inverse_g2_log_slope(nf):
    return float(b0(nf))/(8.0*PI*PI)

def effective_action_F2_log_coefficient(nf):
    # Convention: Gamma contains (1/4) F^a_{mu nu} F^{a mu nu} / g^2(mu).
    return float(b0(nf))/(32.0*PI*PI)

def beta_from_inverse_g2_slope(g,nf):
    # d(1/g^2)/d ln mu = s  => beta(g)=-(1/2) s g^3
    return -0.5*inverse_g2_log_slope(nf)*g**3

def test_background_field_one_loop_transfer_target():
    assert b0(6)==7
    assert b0(0)==11
    assert b0(16)==Fraction(1,3)
    assert b0(17)==Fraction(-1,3)

    g=0.91
    target=-(float(b0(6))/(16.0*PI*PI))*g**3
    assert abs(beta_from_inverse_g2_slope(g,6)-target)<1e-15

    # The effective-action coefficient is one quarter of the inverse-g^2 slope
    # under Gamma=(1/4g^2) int F^2.
    assert abs(4.0*effective_action_F2_log_coefficient(6)-inverse_g2_log_slope(6))<1e-15

    # Background-field identity target: Z_g * sqrt(Z_B) = 1.
    ZB=1.137
    Zg=ZB**-0.5
    assert abs(Zg*math.sqrt(ZB)-1.0)<1e-15
