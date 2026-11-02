"""Critical regression checks AFTER review of POM-1 through POM-11.

Tests limitations of the CURRENT models, not physical predictions.
References: original POM-3 V3, POM-10 three-node polynomial, and
known octonion multiplication in pom1_model.py.

No new proof of Artin, Niven, G2 or spin-statistics is attempted.
"""
import math
from fractions import Fraction

import numpy as np
from pom1_model import omul, associator


def gram_potential(x, y, alpha=.45, lam=.8, eta=.2):
    u,v=x[1:],y[1:]
    s=float(x@x+y@y)
    delta=float((u@u)*(v@v)-(u@v)**2)
    return -alpha*s/2+lam*s*s/4-eta*delta


def chi(vectors):
    a,b,c=vectors
    return -float(omul(omul(a,b),c)[0])


def original_pom10_energy(vectors, edges):
    a,b,c=vectors
    x,y,z=float(a@b),float(b@c),float(a@c)
    chir=chi(vectors)
    return (x*x+y*y+z*z-6*z-3*chir**2+
            sum(edges)/10-int(all(edges))*chir**2)


def run():
    e=np.eye(8)
    rng=np.random.default_rng(20261102)
    errors=[]
    # POM-3 local potential depends on Euclidean Gram invariants;
    # hence it has O(7) symmetry on imaginary coordinates, not only G2.
    for _ in range(80):
        x,y=rng.normal(size=(2,8))
        Q,_=np.linalg.qr(rng.normal(size=(7,7)))
        xr,yr=x.copy(),y.copy()
        xr[1:]=Q@x[1:];yr[1:]=Q@y[1:]
        errors.append(abs(gram_potential(x,y)-gram_potential(xr,yr)))
    assert max(errors)<1e-11
    # A generic imaginary O(7) rotation is not an octonion automorphism:
    # e1,e2,e3 associative, whereas e1,e2,e4 non-associative.
    assocA=associator(e[1],e[2],e[3])
    assocB=associator(e[1],e[2],e[4])
    assert np.linalg.norm(assocA)<1e-12
    assert np.linalg.norm(assocB)>1
    # CRUCIAL PHYSICAL AUDIT: with all graph edges OFF, the original
    # POM-10 formula still has long-range spin couplings.
    no_edges=(0,0,0)
    empty_parallel=original_pom10_energy([e[1],e[2],e[1]],no_edges)
    empty_antiparallel=original_pom10_energy([e[1],e[2],-e[1]],no_edges)
    assert np.isclose(empty_parallel,-5)
    assert np.isclose(empty_antiparallel,7)
    assert np.isclose(empty_antiparallel-empty_parallel,12)
    # POM-10's selected chiral witness is entirely contained in H:
    # it uses no nonzero associator, so full O is not needed for it.
    witness=[e[1],e[2],(3*e[1]+4*e[3])/5]
    assert np.isclose(chi(witness),4/5)
    assert np.linalg.norm(associator(*witness))<1e-12
    assert np.isclose(original_pom10_energy(witness,(1,1,1)),-5.5)
    assert np.isclose(original_pom10_energy(witness,no_edges),-5.16)
    # Irrationality of the exact Berry angle is an arithmetic
    # property of a tuned model, not open under arbitrary perturbations.
    phi=math.atan(.5)
    vals=[]
    for bound in [100,10_000,1_000_000]:
        r=Fraction(phi/math.pi).limit_denominator(bound)
        delta=abs(phi-math.pi*float(r))
        vals.append((str(r),delta))
    assert vals[-1][1]<2e-6
    print("POM review: local V3 O(7) Gram invariance PASS")
    print("POM review: associator breaks generic O(7) PASS")
    print("POM review: empty graph has residual spin-energy difference 12 PASS")
    print("POM review: chiral POM-10 witness lies in associative H PASS")
    print("POM review: nearby rational pi multiples:",vals)
    print("LIMIT: original graph-locality and octonion necessity remain OPEN.")


if __name__=="__main__":
    run()
