"""POM-3 model-specific test: a generic bi-octonion selects a local H_C.

Mathematical basis (NOT re-proved here): Artin's alternative-algebra theorem,
Knarr–Stroppel (Journal of Algebra 2025), and G2/SO4 for H subalgebras.
This does not produce physical 3+1-dimensional spacetime or TEGR.
"""
import numpy as np
from pom1_model import omul, biomul, bioassociator


def invariants(psi):
    x, y = psi[:8], psi[8:]
    u, v = x[1:], y[1:]
    a, b, c = float(u@u), float(v@v), float(u@v)
    t = float(x[0]**2+y[0]**2)
    return t+a+b, a*b-c*c, t, a, b, c


def vacuum_potential(psi, alpha=.45, lam=.8, eta=.2):
    if not lam > eta > 0 or not alpha > 0:
        raise ValueError("Stable ordered phase needs alpha>0, lam>eta>0")
    rho2, delta, *_ = invariants(psi)
    return -alpha/2*rho2 + lam/4*rho2**2 - eta*delta


def quaternion_sector(psi, tol=1e-10):
    """Orthonormal columns (1,u,v,u*v) generated from Im x and Im y."""
    rho2, delta, *_ = invariants(psi)
    if delta <= tol*max(1.,rho2*rho2):
        raise ValueError("No UNIQUE quaternion subalgebra for degenerate pair")
    one=np.zeros(8);one[0]=1
    u=np.copy(psi[:8]);u[0]=0
    v=np.copy(psi[8:]);v[0]=0
    e1=u/np.linalg.norm(u)
    e2=v-(e1@v)*e1
    e2/=np.linalg.norm(e2)
    e3=omul(e1,e2)
    basis=np.column_stack((one,e1,e2,e3))
    assert np.allclose(basis.T@basis,np.eye(4),atol=2e-11)
    return basis


def norm_13(time, space, basis):
    """Biquaternionic q=t+I*w, q*qbar=t²-|w|² (algebraic, not spacetime)."""
    q=np.zeros(16)
    qb=np.zeros(16)
    q[0]=time;qb[0]=time
    q[8:]=basis[:,1:]@space
    qb[8:]=-q[8:]
    product=biomul(q,qb)
    assert np.linalg.norm(product[1:])<1e-9
    return float(product[0])


def test():
    rng=np.random.default_rng(20261031)
    alpha, lam, eta=.45,.8,.2
    r2=alpha/(lam-eta)
    psi=np.zeros(16)
    psi[1]=np.sqrt(r2/2)
    psi[8+2]=np.sqrt(r2/2)
    bound=-alpha**2/(4*(lam-eta))
    assert np.isclose(vacuum_potential(psi,alpha,lam,eta),bound)
    B=quaternion_sector(psi)
    assert np.isclose(invariants(psi)[1],r2**2/4)
    for k in range(180):
        p=rng.normal(size=16)
        rho2, delta, t, a, b, c=invariants(p)
        gap=rho2*rho2-4*delta
        assert np.isclose(gap,t*t+2*t*(a+b)+(a-b)**2+4*c*c)
        surplus=(lam-eta)/4*(rho2-r2)**2+eta/4*gap
        assert np.isclose(vacuum_potential(p,alpha,lam,eta)-bound,surplus)
        assert surplus >= -1e-9
        Q=quaternion_sector(p)
        P=Q@Q.T
        assert np.linalg.norm((np.eye(8)-P)@p[:8])<1e-9
        assert np.linalg.norm((np.eye(8)-P)@p[8:])<1e-9
        for i in range(4):
            for j in range(4):
                assert np.linalg.norm((np.eye(8)-P)@omul(Q[:,i],Q[:,j]))<1e-9
        triple=[]
        for _ in range(3):
            z=np.zeros(16)
            z[:8]=Q@rng.normal(size=4)
            z[8:]=Q@rng.normal(size=4)
            triple.append(z)
        assert np.linalg.norm(bioassociator(*triple))<1e-8
        th=rng.uniform(-np.pi,np.pi)
        rotated=np.r_[np.cos(th)*p[:8]-np.sin(th)*p[8:],
                      np.sin(th)*p[:8]+np.cos(th)*p[8:]]
        assert np.isclose(vacuum_potential(rotated,alpha,lam,eta),
                          vacuum_potential(p,alpha,lam,eta))
        assert np.linalg.norm(quaternion_sector(rotated)@quaternion_sector(rotated).T-P)<1e-8
        t0=float(rng.normal());xyz=rng.normal(size=3)
        assert np.isclose(norm_13(t0,xyz,Q), t0*t0-xyz@xyz)
    for degenerate in (np.zeros(16),np.r_[np.array([0.,1.,0.,0.,0.,0.,0.,0.]),
                                           np.array([0.,2.,0.,0.,0.,0.,0.,0.])]):
        try:
            quaternion_sector(degenerate)
            raise AssertionError("Degenerate data must be rejected")
        except ValueError:
            pass
    distinct=[rng.normal(size=16) for _ in range(3)]
    across=float(np.linalg.norm(bioassociator(*distinct)))
    assert across>1e-6
    sep=float(np.linalg.norm((quaternion_sector(distinct[0])@
          quaternion_sector(distinct[0]).T) -
          (quaternion_sector(distinct[1])@quaternion_sector(distinct[1]).T)))
    assert sep>1e-6
    print("POM-3: 180 generic states: automatic C x H sector and closure PASS")
    print("POM-3: exact vacuum bound and global U(1) covariance PASS")
    print(f"Ground energy={bound:.9f}; rho²={r2:.9f}")
    print("POM-3: intrinsic Minkowski quadratic form on Hermitian subspace PASS")
    print(f"Cross-sector associator norm={across:.6f}; projector separation={sep:.6f}")
    print("LIMITATION: no physical clock, tetrad, spin connection, or TEGR derived.")


if __name__=="__main__":
    test()
