from fractions import Fraction

CA=Fraction(3,1)
TF=Fraction(1,2)

def gauge_vector_effective_trace_coeff():
    # a4 vector bracket: -5/3 tr_ad(Fcal^2), times +1/2 logdet
    return Fraction(-5,6)

def ghost_effective_trace_coeff():
    # a4 scalar bracket: +1/12 tr_ad(Fcal^2), times -1 for complex FP ghost
    return Fraction(-1,12)

def pure_gauge_counterterm_group_coeff():
    # tr_ad(Fcal^2) = - C_A F^a F^a.
    # Effective F^2 coefficient is therefore +(11/12) C_A.
    # Convert Gamma coefficient to delta(1/g^2) by multiplying by 4.
    trace_coeff=gauge_vector_effective_trace_coeff()+ghost_effective_trace_coeff()
    return -4*trace_coeff*CA

def dirac_counterterm_group_coeff(nf):
    # Standard Dirac heat-kernel effective coefficient:
    # +(1/3) tr_R(Fcal^2) = -(1/3) T_F F^aF^a.
    # Multiply by 4 to convert to delta(1/g^2).
    return -Fraction(4,3)*TF*nf

def b0(nf):
    return pure_gauge_counterterm_group_coeff()+dirac_counterterm_group_coeff(nf)

def test_heat_kernel_group_coefficients():
    assert gauge_vector_effective_trace_coeff()==Fraction(-5,6)
    assert ghost_effective_trace_coeff()==Fraction(-1,12)
    assert gauge_vector_effective_trace_coeff()+ghost_effective_trace_coeff()==Fraction(-11,12)

    assert pure_gauge_counterterm_group_coeff()==11
    assert b0(0)==11
    assert b0(6)==7
    assert b0(16)==Fraction(1,3)

    # General SU(3) QCD one-loop result.
    for nf in range(17):
        assert b0(nf)==Fraction(33-2*nf,3)
