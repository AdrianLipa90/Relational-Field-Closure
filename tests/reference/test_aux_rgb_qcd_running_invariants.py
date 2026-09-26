from fractions import Fraction

CA=Fraction(3,1)
TF=Fraction(1,2)
CF=Fraction(4,3)

def beta0(nf):
    return Fraction(11,3)*CA-Fraction(4,3)*TF*nf

def beta1(nf):
    return Fraction(34,3)*CA*CA-4*CF*TF*nf-Fraction(20,3)*CA*TF*nf

def test_qcd_group_invariant_running_gate():
    assert CA==3
    assert TF==Fraction(1,2)
    assert CF==Fraction(4,3)

    # Standard perturbative QCD coefficients after substituting the
    # RGB-Moire-reconstructed SU(3) group invariants.
    assert beta0(6)==7
    assert beta1(6)==26

    # Asymptotic-freedom sign for all integer nf <= 16.
    assert all(beta0(nf)>0 for nf in range(17))
    assert beta0(17)<0
