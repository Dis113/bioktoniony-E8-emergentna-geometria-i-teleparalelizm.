"""POM-13: a smooth ALL-AMPLITUDE frame-independent octonionic loop model.

This uses the ALREADY PUBLISHED Harvey--Lawson calibration inequality,
POM-3's exact onsite bound, and POM-12b's 27-associator contraction.
It does NOT derive the three available nodes, edge cost or negative
associator coupling from fundamental physics.

The normalized, smooth 7x7 matrix R(psi) is NOT an idempotent
projector away from the POM-3 vacuum; it reduces to one on that vacuum.
There is no singularity at psi=0 or at rank-deficient sectors.
Potential is invariant under independent STATIC local U(1) rotations;
this is not a gauge-covariant kinetic action.

No Maxwell, TEGR, fermion CAR, local G2 connection or 3+1 geometry.
"""
import numpy as np

from pom1_model import omul, associator

ALPHA = 9/20
LAM = 4/5
ETA = 1/5
RADIUS = ALPHA/(LAM-ETA)
A = RADIUS/2  # 3/8
MIN_V3 = -ALPHA**2/(4*(LAM-ETA))  # -27/320
EDGE_COST = 1/4
LOOP_GAIN = 2
E = np.eye(8)

T = np.array([associator(E[i+1], E[j+1], E[k+1])[1:]
              for i in range(7) for j in range(7) for k in range(7)]
             ).reshape(7,7,7,7)
C = np.array([omul(E[i+1],E[j+1])[1:]
              for i in range(7) for j in range(7)]).reshape(7,7,7)


def local_v3(psi):
    x,y=psi[:8],psi[8:]
    u,v=x[1:],y[1:]
    s=float(psi@psi)
    delta=float((u@u)*(v@v)-(u@v)**2)
    return -ALPHA/2*s+LAM/4*s*s-ETA*delta


def soft_sector(psi):
    """Smooth PSD matrix with tr<=3 for ALL 16-real-component states.

    M=uuT+vvT+(u×v)(u×v)T/a,
    R=36a M/(tr M+3a)^2.
    At V3's ordered vacuum R is the true imaginary-H projector.
    """
    u,v=psi[1:8],psi[9:16]
    w=np.einsum("i,j,ijk->k",u,v,C)
    M=np.outer(u,u)+np.outer(v,v)+np.outer(w,w)/A
    return 36*A*M/(float(np.trace(M))+3*A)**2


def reward(fields):
    """Already-known Harvey--Lawson inequality implies 0<=Q<=1."""
    mats=[soft_sector(p) for p in fields]
    return float(np.einsum("abcd,efgd,ae,bf,cg->",
                           T,T,*mats,optimize=True)/108)


def energy(fields,edges):
    excess=sum(local_v3(psi)-MIN_V3 for psi in fields)
    return excess+EDGE_COST*sum(edges)-LOOP_GAIN*int(all(edges))*reward(fields)


def local_ground(u,v):
    psi=np.r_[np.sqrt(A)*u,np.sqrt(A)*v]
    assert abs(local_v3(psi)-MIN_V3)<1e-12
    return psi


def rotate_central(psi,phi):
    x,y=psi[:8],psi[8:]
    return np.r_[np.cos(phi)*x-np.sin(phi)*y,
                 np.sin(phi)*x+np.cos(phi)*y]


def exact_witness():
    # Three sectors H_A, H_A, H_C from the earlier POM-12b witness.
    fields=[local_ground(E[1],E[2]),local_ground(E[2],E[3]),
            local_ground(E[4],E[5])]
    for p in fields:
        S=soft_sector(p)
        assert np.allclose(S@S,S,atol=1e-12)
        assert np.isclose(np.trace(S),3)
    assert np.isclose(reward(fields),4/9,atol=1e-12)
    assert np.isclose(energy(fields,(1,1,1)),-5/36,atol=1e-12)
    assert abs(energy(fields,(0,0,0)))<1e-12
    return fields


def run():
    fields=exact_witness()
    rng=np.random.default_rng(1313)
    qmin,qmax=1.,0.
    trace_max=0.

    # 150 arbitrary full-amplitude states include zero, scalar fields
    # and dependent local generators; no division by Gram determinant.
    for index in range(150):
        x=rng.normal(size=(3,16))*rng.uniform(.01,5)
        if index%5==0:x[0]=0
        if index%11==0:x[1,9:16]=x[1,1:8]
        for psi in x:
            R=soft_sector(psi)
            assert np.min(np.linalg.eigvalsh(R))>-1e-10
            assert np.trace(R)<=3+1e-10
            trace_max=max(trace_max,float(np.trace(R)))
            assert local_v3(psi)-MIN_V3 >-1e-10
        q=reward(x)
        assert -1e-10 <=q<=1+1e-10
        qmin,qmax=min(qmin,q),max(qmax,q)
        for edges in ((0,0,0),(1,0,0),(1,1,0),(1,1,1)):
            val=energy(x,edges)
            assert val>=-5/4-1e-8
            if not all(edges):assert val>=-1e-8
        transformed=[rotate_central(p,theta) for p,theta in zip(
                     x,rng.uniform(-np.pi,np.pi,3))]
        assert np.isclose(reward(transformed),q,atol=1e-9)
        assert np.isclose(energy(transformed,(1,1,1)),
                          energy(x,(1,1,1)),atol=1e-9)

    for _ in range(100):
        transformed=[rotate_central(p,th) for p,th in zip(
                     fields,rng.uniform(-np.pi,np.pi,3))]
        assert np.isclose(energy(transformed,(1,1,1)),-5/36,atol=1e-11)

    # Arbitrary off-vacuum shared quaternionic H implies Q=0.
    for _ in range(40):
        x=rng.normal(size=(3,16))*rng.uniform(.5,2)
        x[:,4:8]=0
        x[:,12:16]=0
        assert abs(reward(x))<1e-11
        assert energy(x,(0,0,0))>=-1e-10

    scales=[0.,.1,1.,2.,4.,8.,16.]
    vals=[energy([t*x for x in fields],(1,1,1)) for t in scales]
    assert vals[-1]>vals[-2]>vals[-3]
    assert reward([np.zeros(16)]*3)==0.

    print("POM-13 full-amplitude smooth octonionic energy PASS")
    print("Exact witness: Q=4/9, E=-5/36, quaternion shared-H ground E=0")
    print("Local U1: 150 random fields +100 vacuum samples PASS")
    print("Degenerate sectors/zero field defined everywhere; max trace:",
          trace_max,"numeric Q range:",(qmin,qmax))
    print("Large amplitude samples:",list(zip(scales,vals)))
    print("Mathematical claim: continuous coercive finite-dimensional model")
    print("has a GLOBAL ground state with a CLOSED loop and negative E.")
    print("LIMIT: still no dynamically derived edge law, local G2, CAR, SM or TEGR.")


if __name__=="__main__":
    run()
