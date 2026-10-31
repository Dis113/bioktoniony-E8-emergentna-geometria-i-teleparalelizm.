"""POM-7: exact rational witness and restricted continuous orientation test.

This is an additional *counterexample* to a dynamically preferred A/B or A/C
sector pair. It does not determine the global minimum in the FULL continuous
POM-3 vacuum manifold, nor derive a 1D spatial graph.
"""
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize
from spectral_topological_probe import sector_state
from sector_vacuum_probe import quaternion_sector
from spontaneous_ordering_probe import exact_transfer_minimizers


def qmul(a,b):
    w,x,y,z=a
    W,X,Y,Z=b
    return [w*W-x*X-y*Y-z*Z,
            w*X+x*W+y*Z-z*Y,
            w*Y-x*Z+y*W+z*X,
            w*Z+x*Y-y*X+z*W]


def conj(a):
    return [a[0]]+[-x for x in a[1:]]


def omul(a,b):
    x,y=a[:4],a[4:]
    z,w=b[:4],b[4:]
    r=qmul(x,z)
    s=qmul(conj(w),y)
    v=qmul(w,x)
    z2=qmul(y,conj(z))
    return [a-b for a,b in zip(r,s)]+[a+b for a,b in zip(v,z2)]


def exact_quaternion_frame(sign):
    one=[F(int(i==0)) for i in range(8)]
    u=[F(0)]*8
    v=[F(0)]*8
    u[1]=F(4,5)
    u[4]=F(sign*3,5)
    v[2]=F(4,5)
    v[5]=F(sign*3,5)
    w=omul(u,v)
    basis=[one,u,v,w]
    for i in range(4):
        for j in range(4):
            dot=sum(a*b for a,b in zip(basis[i],basis[j]))
            assert dot==int(i==j)
    return basis


def exact_frame_overlap(first,second):
    return sum(
        (sum(x*y for x,y in zip(a,b))**2
         for a in first for b in second), F(0))/4


def angle_projector(angle):
    e=np.eye(8)
    u=np.cos(angle)*e[1]+np.sin(angle)*e[4]
    v=np.cos(angle)*e[2]+np.sin(angle)*e[5]
    B=quaternion_sector(sector_state(u,v))
    return B@B.T


def frustration_energy(thetas):
    P=[angle_projector(th) for th in thetas]
    n=len(P)
    qNN=sum(np.trace(P[i]@P[(i+1)%n])/4 for i in range(n))
    qNNN=sum(np.trace(P[i]@P[(i+2)%n])/4 for i in range(n))
    return float((16/3)*(qNNN-qNN))


def run():
    A=exact_quaternion_frame(1)
    B=exact_quaternion_frame(-1)
    q=exact_frame_overlap(A,B)
    assert q==F(178369,390625)
    assert q<F(1,2)<F(5,8)
    period_four=exact_transfer_minimizers(8)[0][1]
    theta=float(np.arctan2(3,4))
    angles=np.array([theta if s==1 else -theta for s in period_four])
    exact_ring_E=F(16,3)*4*(q-1)
    initial=frustration_energy(angles)
    assert np.isclose(initial,float(exact_ring_E),atol=1e-11)
    # Conditional minimization only along one continuous 1-parameter family.
    # Initialize with an analytic rational witness, not a global vacuum proof.
    result=minimize(frustration_energy,angles,method="BFGS",
                    options={"maxiter":250,"gtol":1e-7})
    assert np.isfinite(result.fun) and result.fun < initial-0.001
    assert result.fun < -8*(4/3)
    qNN=[]
    P=[angle_projector(th) for th in result.x]
    for i in range(8):
        qNN.append(float(np.trace(P[i]@P[(i+1)%8])/4))
    assert len(qNN)==8 and min(qNN)<.47 and max(qNN)>.99
    print("POM-7 exact rational sector-pair overlap:",q,"= %.9f"%float(q))
    print("POM-7 exact 8-ring energy witness:",exact_ring_E,"=",float(exact_ring_E))
    print("POM-7 continuous one-parameter family optimum (local numerical):",result.fun)
    print("POM-7 nearest-link overlaps after optimization:",
          np.round(qNN,6).tolist())
    print("LIMIT: even this improved 1D orientation family is not")
    print("the entire bi-octonionic vacuum; no physical spacetime is derived.")


if __name__=="__main__":
    run()
