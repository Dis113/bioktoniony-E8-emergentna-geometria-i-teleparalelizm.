"""POM-2: ordered-vacuum diagnostic (NOT a derivation of gravity).
The complete K3 and K5 graphs and negative onsite quadratic term are
new hypotheses. Frustrated XY chirality is previously known:
Bach et al. (2021), DOI 10.1007/s00526-021-02016-3.
"""
from itertools import combinations
import numpy as np
from scipy.optimize import minimize
from pom1_model import ROOTS, bioassociator


def lattice_energy(psi, *, alpha, K, lam, eps=0.0, f=1.0, gamma=0.0):
    n = psi.shape[0]
    u = np.sum(psi*psi,axis=1)
    val = float(np.sum(-alpha/2*u + lam/4*u*u))
    val += K/2*sum(np.linalg.norm(psi[i]+psi[j])**2
                   for i,j in combinations(range(n),2))
    if eps:
        rx=psi[:,:8]@ROOTS.T/f
        ry=psi[:,8:]@ROOTS.T/f
        val += eps*float(np.sum(2-np.cos(rx)-np.cos(ry)))
    if gamma:
        val += gamma*sum(np.linalg.norm(bioassociator(psi[i],psi[j],psi[k]))**2
                         for i,j,k in combinations(range(n),3))
    return val


def xy_energy_gradient(z, *, alpha, K, lam, eps, f):
    """Exact E8 root potential restricted to the scalar complex plane."""
    z=np.asarray(z).reshape(3,2)
    u=np.sum(z*z,axis=1)
    val=float(np.sum(-alpha/2*u+lam/4*u*u))
    grad=(-alpha+lam*u)[:,None]*z
    for i,j in combinations(range(3),2):
        d=z[i]+z[j]
        val += K/2*float(d@d)
        grad[i]+=K*d
        grad[j]+=K*d
    if eps:
        p=z/f
        val += eps*float(np.sum(28*(2-np.cos(p[:,0])-np.cos(p[:,1]))
                             +128*(2-np.cos(p[:,0]/2)-np.cos(p[:,1]/2))))
        grad += eps/f*(28*np.sin(p)+64*np.sin(p/2))
    return val,grad.ravel()


def complex_embed(z):
    psi=np.zeros((len(z),16))
    psi[:,0]=z[:,0]
    psi[:,8]=z[:,1]
    return psi


def circulation(z):
    return float(sum(np.linalg.det(np.stack([z[i],z[(i+1)%3]])) for i in range(3)))


def triangle_test():
    alpha,K,lam,eps,f=.35,.12,.70,.001,1.
    critical=K+60*eps/f**2
    assert alpha>critical
    r=np.sqrt((alpha-K)/lam)
    angle=2*np.pi*np.arange(3)/3
    seed=np.column_stack((np.cos(angle),np.sin(angle)))*r
    e0=xy_energy_gradient(seed,alpha=alpha,K=K,lam=lam,eps=0.,f=f)[0]
    assert abs(e0+3*(alpha-K)**2/(4*lam))<1e-12
    full=lattice_energy(complex_embed(seed),alpha=alpha,K=K,lam=lam,eps=eps)
    reduced=xy_energy_gradient(seed,alpha=alpha,K=K,lam=lam,eps=eps,f=f)[0]
    assert abs(full-reduced)<1e-12
    negative=60*eps/f**2-alpha+K
    uniform=60*eps/f**2-alpha+4*K
    assert negative<0<uniform
    results=[]
    for candidate in (seed,seed*np.array([1,-1])):
        fit=minimize(
            lambda v:xy_energy_gradient(v,alpha=alpha,K=K,lam=lam,eps=eps,f=f),
            candidate.ravel(),jac=True,method="BFGS",
            options={"gtol":1e-10,"maxiter":300})
        assert np.linalg.norm(fit.jac)<1e-7
        z=fit.x.reshape(3,2)
        chi=circulation(z)
        assert fit.fun<-0.03 and abs(chi)>.5
        results.append((fit.fun,chi))
    assert results[0][1]*results[1][1]<0
    assert abs(results[0][0]-results[1][0])<1e-9
    return critical,negative,uniform,results


def pentad_rank_test():
    n=5
    alpha,K,lam,eps,gamma=.55,.12,.7,.001,.01
    r_squared=(alpha-3*K)/lam
    assert r_squared>0 and alpha>3*K+60*eps
    r=np.sqrt(r_squared)
    t=2*np.pi*np.arange(5)/5
    rank2=np.column_stack((np.cos(t),np.sin(t)))*r
    rank4=np.column_stack((np.cos(t),np.sin(t),np.cos(2*t),np.sin(2*t)))*r/np.sqrt(2)
    lower=-n*(alpha-3*K)**2/(4*lam)
    cases=[]
    for z in (rank2,rank4):
        psi=np.zeros((n,16))
        psi[:,:z.shape[1]]=z
        assert np.allclose(np.sum(psi*psi,axis=1),r_squared,atol=1e-12)
        assert np.linalg.norm(np.sum(psi,axis=0))<1e-12
        assert all(np.linalg.norm(bioassociator(psi[i],psi[j],psi[k]))<1e-12
                   for i,j,k in combinations(range(n),3))
        energy=lattice_energy(psi,alpha=alpha,K=K,lam=lam,gamma=gamma)
        assert abs(energy-lower)<1e-12
        with_E8=lattice_energy(psi,alpha=alpha,K=K,lam=lam,eps=eps,gamma=gamma)
        assert with_E8<0  # establishes nonzero minimum; not its exact shape
        rank=int(np.linalg.matrix_rank(psi@psi.T,tol=1e-10))
        cases.append((rank,energy,with_E8))
    assert cases[0][0]==2 and cases[1][0]==4
    assert abs(cases[0][1]-cases[1][1])<1e-12
    return lower,cases,3*K+60*eps


def u1_counterexample():
    assert np.isclose(np.sum(ROOTS[:,0]**2),60)
    assert np.isclose(np.sum(ROOTS[:,0]**4),36)
    params=dict(alpha=0.,K=0.,lam=0.,eps=.001)
    a=np.zeros((3,16));a[0,0]=.9
    b=np.zeros_like(a)
    b[0,0]=.9/np.sqrt(2)
    b[0,8]=.9/np.sqrt(2)
    diff=lattice_energy(b,**params)-lattice_energy(a,**params)
    assert abs(diff)>1e-5
    return diff


def weyl_reflection_counterexample():
    """A root reflection preserves U_E8 but not the octonion associator term."""
    root=np.array([1.,-1.,0.,0.,0.,0.,0.,0.])
    assert any(np.array_equal(a,root) for a in ROOTS)
    # Reflection in alpha=e0-e1 swaps octonion components 0 and 1.
    original=np.zeros((3,16))
    original[0,1]=1.; original[1,2]=1.; original[2,4]=1.
    reflected=original.copy()
    reflected[:,:8]=original[:,:8][:,[1,0,2,3,4,5,6,7]]
    aa=np.linalg.norm(bioassociator(*original))**2
    bb=np.linalg.norm(bioassociator(*reflected))**2
    assert np.isclose(aa,4.) and np.isclose(bb,0.)
    base=dict(alpha=0.,K=0.,lam=0.,eps=.001)
    a_e8=lattice_energy(original,**base)
    b_e8=lattice_energy(reflected,**base)
    assert np.isclose(a_e8,b_e8,atol=1e-12)
    gamma=.01
    a_total=lattice_energy(original,**base,gamma=gamma)
    b_total=lattice_energy(reflected,**base,gamma=gamma)
    assert np.isclose(a_total-b_total,4*gamma,atol=1e-12)
    return aa,bb,a_total-b_total


def main():
    critical,negative,uniform,branches=triangle_test()
    ground,cases,critical5=pentad_rank_test()
    delta=u1_counterexample()
    before,after,weyl_gap=weyl_reflection_counterexample()
    print("POM-2: ordered phase diagnostic (NOT emergence of gravity)")
    print("K3 critical alpha:",critical,"Hessian modes:",negative,uniform)
    print("K3 opposite chiral branches (energy,J):",branches)
    print("K5 critical alpha:",critical5,"exact epsilon=0 ground energy:",ground)
    print("K5 cases (rank, epsilon=0 energy, epsilon>0 energy):",cases)
    print("E8 potential global U(1) rotation delta:",delta)
    print("Weyl-reflection associator norm squares:",before,after,"full energy gap:",weyl_gap)
    print("OPEN: unique 4D rank, Lorentz signature, tetrads, torsion and TEGR.")


if __name__=="__main__":
    main()
