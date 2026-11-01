"""POM-11: exact *finite* spectral certificate for the POM-10 triangle.

This checks the characteristic polynomial with exact rational arithmetic
(no numerical eigensolver needed for the characteristic coefficients);
tests its three eigenvalues numerically; and tests bounded Hermitian
perturbations and site-local U(1) gauge changes.

The general Weyl eigenvalue-perturbation theorem is reviewed prior art.
This script checks the specific finite POM-10 matrix, NOT a 2D Chern
bulk phase or physical particle stability. No Maxwell field is used.
"""
from fractions import Fraction as Q
import math
import numpy as np


def cmul(x, y):
    a,b=x
    c,d=y
    return (a*c-b*d,a*d+b*c)


def cconj(x):
    return (x[0], -x[1])


def cabs2(x):
    return x[0]*x[0]+x[1]*x[1]


def exact_invariants():
    a=(Q(1,2),Q(1,2))
    b=(Q(1,2),-Q(1,2))
    c=(Q(4,5),Q(2,5))
    # a=H01, b=H12, c=H20:
    B=cmul(cmul(a,b),c)
    e2=cabs2(a)+cabs2(b)+cabs2(c)
    e3=2*B[0]
    assert e2==Q(9,5)
    assert B==(Q(2,5),Q(1,5))
    assert e3==Q(4,5)
    # Characteristic polynomial:
    # lambda^3-(|a|^2+|b|^2+|c|^2)*lambda-2*Re(a*b*c)
    # =(lambda+1)*(lambda^2-lambda-4/5).
    assert Q(1)*Q(-4,5)==-e3
    assert Q(-1)+Q(-4,5)==-e2
    return a,b,c,B,e2,e3


def hermitian_triangle(a,b,c):
    H=np.zeros((3,3),dtype=complex)
    values=[complex(float(x),float(y)) for x,y in (a,b,c)]
    H[0,1],H[1,2],H[2,0]=values
    H[1,0],H[2,1],H[0,2]=np.conjugate(values)
    assert np.allclose(H,H.conj().T)
    return H


def test_exact_loop():
    a,b,c,B,e2,e3=exact_invariants()
    H=hermitian_triangle(a,b,c)
    eigenvalues=np.linalg.eigvalsh(H)
    sq=math.sqrt(105)
    exact=np.array([-1.,(5-sq)/10,(5+sq)/10])
    assert np.allclose(eigenvalues,exact,atol=2e-14)
    assert np.isclose(np.trace(H@H).real,float(2*e2),atol=1e-13)
    assert np.isclose(np.linalg.det(H).real,float(e3),atol=1e-13)
    gap=(15-sq)/10
    assert .47<gap<.48
    assert np.isclose(min(np.diff(eigenvalues)),gap,atol=1e-13)
    assert np.isclose(np.angle(complex(*map(float,B))),
                      math.atan(.5))
    # Random diagonal rephasings do not change spectrum or triangle
    # Wilson product; tests physical gauge invariance of the loop phase.
    rng=np.random.default_rng(20261101)
    for _ in range(80):
        phases=rng.uniform(-math.pi,math.pi,3)
        W=np.diag(np.exp(1j*phases))
        changed=W@H@W.conj().T
        invariant=changed[0,1]*changed[1,2]*changed[2,0]
        assert np.allclose(eigenvalues,np.linalg.eigvalsh(changed))
        assert np.isclose(invariant,complex(*map(float,B)),atol=1e-12)

    # Multiple *independent* test perturbations, each made Hermitian
    # and explicitly scaled by its actual operator norm. The analytic
    # guarantee, supplied by the standard Weyl theorem, is
    # perturbed spacing >= exact spacing - 2*||dH||.
    min_observed=float("inf")
    for _ in range(160):
        R=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        dH=(R+R.conj().T)/2
        dH*=.2/np.linalg.norm(dH,ord=2)
        E=np.linalg.eigvalsh(H+dH)
        assert np.max(np.abs(E-eigenvalues))<=.2+1e-12
        local_min=float(min(np.diff(E)))
        assert local_min > .07
        min_observed=min(min_observed,local_min)
    return exact,gap,min_observed,e2,e3,B


def main():
    values,gap,minimum,e2,e3,B=test_exact_loop()
    print("POM-11: EXACT Gaussian-rational 3-cycle link invariants PASS")
    print(" POM-specific |links|^2 total",e2,
          "2Re(B)",e3,"Berry B",B)
    print(" exact polynomial: (lambda+1)*(lambda^2-lambda-4/5)")
    print(" exact spectrum:",[float(x) for x in values])
    print(" exact smallest gap:",gap,"greater than 0.47")
    print(" conditional Hermitian ||delta H||<=0.2 gap lower bound: >0.07")
    print(" smallest measured gap across 160 random perturbations:",minimum)
    print(" 80 local U(1) rephasings preserve the Wilson loop and spectrum")
    print("LIMIT: no 2D topological band, 3+1 spacetime, physical matter or")
    print("Maxwell/TEGR derived; Weyl's general theorem is prior art.")


if __name__=="__main__":
    main()
