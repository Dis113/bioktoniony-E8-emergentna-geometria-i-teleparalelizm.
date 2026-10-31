"""POM-6: prototype of an overlap-induced spectral operator on POM-3 sectors.

This is a finite, ASSUMED one-dimensional bipartite graph, NOT 3+1
spacetime, a physical electron, the Standard Model or TEGR.
Known SSH/edge-mode and spectral-triple results are not re-proved.
What is tested here: the specific link rule deriving hopping strengths
from POM-3 quaternion projector overlaps and a chosen SU(2) frame lift.
"""
import math
import numpy as np

from sector_vacuum_probe import quaternion_sector
from singleton_sector_transport import oriented_so3_overlap, spin_lift


def sector_state(u, v):
    """Minimum of V3 with r^2=3/4: x=√(r²/2) u, y=√(r²/2) v."""
    ua=np.asarray(u,dtype=float)
    va=np.asarray(v,dtype=float)
    ua=ua/np.linalg.norm(ua)
    va=va-(ua@va)*ua
    va=va/np.linalg.norm(va)
    amp=np.sqrt(.75/2)
    psi=np.zeros(16)
    psi[:8]=amp*ua
    psi[8:]=amp*va
    return psi


def concrete_sectors():
    e=np.eye(8)
    A=sector_state(e[1],e[2])
    B=sector_state((e[1]+e[4])/np.sqrt(2),
                   (e[2]+e[5])/np.sqrt(2))
    BA,BB=quaternion_sector(A),quaternion_sector(B)
    PA,PB=BA@BA.T,BB@BB.T
    q=float(np.trace(PA@PB)/4)
    assert np.isclose(q,5/8,atol=2e-12)
    assert np.allclose(np.diag(PB),
        [1,.75,.5,.25,.75,.5,.25,0.],atol=1e-12)
    _,sv=oriented_so3_overlap(BA,BB)
    assert min(sv)>0.3  # no degenerate Procrustes mapping here
    return (BA,BB),(PA,PB),q,sv


def sites(num_cells,kind):
    """Phase is in the orientation pattern, not arbitrary hardcoded bonds."""
    z=[]
    for j in range(num_cells):
        Ai=j%2
        Bi=1-Ai if kind=="topological" else Ai
        z.extend([Ai,Bi])
    return z


def edge_data(labels,bases,projectors,offset=.1,stiffness=.9):
    result=[]
    for a,b in zip(labels[:-1],labels[1:]):
        ov=float(np.trace(projectors[a]@projectors[b])/4)
        t=offset+stiffness*ov
        R,singular_values=oriented_so3_overlap(bases[a],bases[b])
        S=spin_lift(R)
        assert np.allclose(S.conj().T@S,np.eye(2),atol=1e-10)
        result.append((t,S,ov,singular_values))
    return result


def scalar_chain(edges):
    n=len(edges)+1
    H=np.zeros((n,n),dtype=complex)
    for j,(t,_,_,_) in enumerate(edges):
        H[j,j+1]=t
        H[j+1,j]=t
    return H


def spinor_chain(edges):
    """Spinor C² attached to each node: link spin lifts are assumed."""
    n=len(edges)+1
    H=np.zeros((2*n,2*n),dtype=complex)
    for j,(t,S,_,_) in enumerate(edges):
        H[2*j:2*j+2,2*j+2:2*j+4]=t*S
        H[2*j+2:2*j+4,2*j:2*j+2]=t*S.conj().T
    assert np.allclose(H,H.conj().T)
    gamma=np.kron(np.diag([1. if j%2==0 else -1. for j in range(n)]),
                  np.eye(2))
    assert np.linalg.norm(gamma@H+H@gamma)<1e-10
    return H


def boson_laplacian(edges):
    """Positive graph Laplacian is a CHOSEN collective-mode model."""
    n=len(edges)+1
    L=np.zeros((n,n))
    for j,(t,_,_,_) in enumerate(edges):
        L[j,j]+=t
        L[j+1,j+1]+=t
        L[j,j+1]-=t
        L[j+1,j]-=t
    return L


def winding(tin,tout):
    """Discretization of the KNOWN SSH winding formula, not its proof."""
    k=np.linspace(0,2*np.pi,2001)
    z=tin+tout*np.exp(-1j*k)
    if min(abs(z))<1e-10:
        return None
    phase=np.unwrap(np.angle(z))
    return int(np.rint((phase[-1]-phase[0])/(2*np.pi)))


def run():
    bases,projectors,q,singular=concrete_sectors()
    n=20
    result={}
    for kind in ("topological","trivial"):
        edges=edge_data(sites(n,kind),bases,projectors)
        scalar=scalar_chain(edges)
        H=spinor_chain(edges)
        ts=np.array([e[0] for e in edges])
        if kind=="topological":
            assert np.allclose(ts[::2],.1+.9*q)
            assert np.allclose(ts[1::2],1.)
        else:
            assert np.allclose(ts[::2],1.)
            assert np.allclose(ts[1::2],.1+.9*q)
        eig,vec=np.linalg.eigh(scalar)
        ii=np.argsort(abs(eig))[:2]
        low=np.max(abs(eig[ii]))
        edge_weights=[
            float(np.sum(abs(vec[:2,k])**2)+np.sum(abs(vec[-2:,k])**2))
            for k in ii
        ]
        lap=boson_laplacian(edges)
        boson=np.linalg.eigvalsh(lap)
        assert abs(boson[0])<1e-10 and min(boson[1:])>0
        assert np.allclose(np.sum(boson),2*sum(ts))
        eigspin=np.linalg.eigvalsh(H)
        assert np.allclose(eigspin[::2],np.linalg.eigvalsh(scalar),atol=1e-9) or \
           np.allclose(np.sort(eigspin),np.repeat(np.linalg.eigvalsh(scalar),2),atol=1e-9)
        t1,t2=ts[0],ts[1]
        w=winding(t1,t2)
        result[kind]=(low,min(edge_weights),w,float(boson[1]))
        if kind=="topological":
            assert w==-1 and low<2e-4 and min(edge_weights)>.55
        else:
            assert w==0 and low>.3 and max(edge_weights)<.05

    # Exact numerical gauge covariance for a local U(1) change of spinor basis.
    edges=edge_data(sites(12,"topological"),bases,projectors)
    H=spinor_chain(edges)
    rng=np.random.default_rng(20261031)
    theta=rng.uniform(-np.pi,np.pi,len(edges)+1)
    W=np.kron(np.diag(np.exp(1j*theta)),np.eye(2))
    Hnew=W@H@W.conj().T
    assert np.allclose(np.sort(np.linalg.eigvalsh(H)),
                       np.sort(np.linalg.eigvalsh(Hnew)),atol=1e-11)

    # Chiral bond disorder keeps two low edge modes separated from bulk.
    random_edges=[(t*(1+rng.uniform(-.04,.04)),S,ov,sv)
                  for (t,S,ov,sv) in edges]
    disturbed=scalar_chain(random_edges)
    assert np.linalg.norm(np.diag([1 if j%2==0 else -1 for j in range(24)])
                          @disturbed+disturbed@
                          np.diag([1 if j%2==0 else -1 for j in range(24)]))<1e-10
    assert min(abs(np.linalg.eigvalsh(disturbed)))<1e-2

    # Environment-induced STRAIN is a *postulate*, not derived gravity:
    # it changes the intercell bonds of an infinite Bloch toy chain.
    t_in=.1+.9*q
    t_out=1.
    critical=math.log(t_out/t_in)
    assert winding(t_in,t_out)==-1
    assert abs(t_out*np.exp(-critical)-t_in)<1e-12
    assert winding(t_in,t_out*np.exp(-critical)) is None
    assert winding(t_in,t_out*np.exp(-.8))==0

    print("POM-6: projector overlap=%.12f, singular values="%q,singular)
    for k,v in result.items():
        print(k, "min |E|=%.9g, edge probability=%.6f, winding=%s, "
              "bosonic Laplacian gap=%.9g"%v)
    print("POM-6: local U(1) covariance of the chosen Dirac graph PASS")
    print("POM-6: common SU2 spin transport and boson Laplacian PASS")
    print("POM-6: strain-induced 1D gap closure at parameter=%.8g"%critical)
    print("LIMIT: 1D SSH graph and transport are selected, not emergent;")
    print("not a 3+1D fermion, Maxwell gauge boson, or teleparallel gravity.")


if __name__=="__main__":
    run()
