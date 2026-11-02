"""POM-12b: independent-frame invariant three-sector associator incentive.

Given local POM-3 quaternion sectors H_i, choose arbitrary orthonormal
bases (u_ia) of imaginary H_i and define the nonnegative scalar:

 I(H1,H2,H3) = sum_(a,b,c=1)^3 ||[u_1a,u_2b,u_3c]||² / 108.

Because the associator is trilinear and Euclidean norm invariant,
this sum is independent of the O(3) basis choice for EACH fixed H_i.
This is NOT covariance under independent G2 transformations of the
ambient octonion spaces on different nodes.

Harvey–Lawson's 1982 associator identity provides I in [0,1].
With H1=H2=span(1,e1,e2,e3) and H3=span(1,e1,e4,e5):
   integer sum=48, I=4/9.
For given edge energy mu=1/4 and gain=2, the CLOSED graph has exact
energy -5/36 whereas ANY three sectors in a single quaternion H have
ground energy zero (empty graph).

This is a conditional toy model, not a physical 3+1D emergence theorem.
"""
from fractions import Fraction as F
from itertools import product

import numpy as np
from pom1_model import associator
from sector_vacuum_probe import quaternion_sector, vacuum_potential

E=np.eye(8)


def ground_state(u,v):
    amp=np.sqrt(3/8)
    psi=np.r_[amp*u,amp*v]
    assert np.isclose(vacuum_potential(psi),-.084375)
    return psi


def local_frame(psi):
    return quaternion_sector(psi)[:,1:]


def basis_invariant_assoc(FA,FB,FC):
    total=sum(float(associator(u,v,w)@associator(u,v,w))
              for u in FA.T for v in FB.T for w in FC.T)
    return total/108


def real_orthogonal_3(rng):
    Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    return Q


def main():
    A=local_frame(ground_state(E[1],E[2]))
    B=local_frame(ground_state(E[2],E[3]))
    C=local_frame(ground_state(E[4],E[5]))
    q=basis_invariant_assoc(A,B,C)
    assert np.isclose(q,4/9,atol=1e-13)

    # EXACT integer-valued triple products and sum of 27 squared norms.
    integer_sum=0
    for u in A.T:
        for v in B.T:
            for w in C.T:
                assoc=associator(u,v,w)
                assert np.array_equal(assoc,np.rint(assoc))
                integer_sum+=int(round(assoc@assoc))
    assert integer_sum==48 and F(integer_sum,108)==F(4,9)

    # All three sites in one H form an associative control.
    assert abs(basis_invariant_assoc(A,B,A))<1e-14
    graphs=list(product([0,1],repeat=3))
    E_O=[F(sum(e),4)-2*int(all(e))*F(4,9) for e in graphs]
    E_H=[F(sum(e),4) for e in graphs]
    assert E_O[-1]==-F(5,36) and min(E_O)==-F(5,36)
    assert min(E_H)==0
    assert all(E_O[0]==0 for _ in range(1))

    rng=np.random.default_rng(12026)
    frame_max=0.
    for _ in range(500):
        f=basis_invariant_assoc(
          A@real_orthogonal_3(rng),
          B@real_orthogonal_3(rng),
          C@real_orthogonal_3(rng))
        frame_max=max(frame_max,abs(f-q))
    assert frame_max<3e-13

    # Independent central complex phase U(1) rotations of POM-3 states
    # mix the two generator columns but leave the quaternionic SUBALGEBRA.
    psis=[ground_state(E[1],E[2]),ground_state(E[2],E[3]),
          ground_state(E[4],E[5])]
    for _ in range(100):
        chosen=[]
        for psi,theta in zip(psis,rng.uniform(-np.pi,np.pi,3)):
            x,y=psi[:8],psi[8:]
            new=np.r_[np.cos(theta)*x-np.sin(theta)*y,
                      np.sin(theta)*x+np.cos(theta)*y]
            assert np.isclose(vacuum_potential(new),-.084375)
            chosen.append(local_frame(new))
        assert np.isclose(basis_invariant_assoc(*chosen),q,atol=1e-12)

    print("POM-12b PASS: exact integer associator tensor sum:",integer_sum)
    print("POM-12b exact 3-sector Q=4/9; O-loop E=-5/36, H-ground E=0")
    print("POM-12b 500 independent basis changes max |delta Q|:",frame_max)
    print("POM-12b 100 independent local POM3 U1 rotations PASS")
    print("LIMIT: no independent ambient G2 gauge covariance, no hbar/SM/TEGR")


if __name__=="__main__":main()
