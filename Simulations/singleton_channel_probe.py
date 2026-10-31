"""POM-5: toy two-site Rac/Di channels with parity-even pair creation.

Based on a PUBLISHED metaplectic two-bosonic-oscillator realization
of the Rac (even) and Di (odd) modules. This truncated finite matrix
calculation is NOT an exact singleton representation of Sp(4,R).
The Flato–Fronsdal theorem is NOT reproduced or proved.

New POM-5 question: does a proposed local coupling preserve TOTAL
singleton parity, and which local channel probabilities can be produced?
EM/GR-dependent coefficients below are external toy inputs, NOT derived
from the microscopic bi-octonion Hamiltonian.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm


def ladder(d: int) -> np.ndarray:
    a = np.zeros((d, d), dtype=complex)
    for n in range(1, d):
        a[n - 1, n] = np.sqrt(n)
    return a


def two_oscillator_local(d: int):
    a = ladder(d)
    I = np.eye(d, dtype=complex)
    return (np.kron(a, I), np.kron(I, a))


def model_matrices(d=3):
    """Two sites, two bosonic oscillator modes per site, finite cut-off."""
    local_a = two_oscillator_local(d)
    loc = d * d
    I = np.eye(loc, dtype=complex)
    A = [np.kron(a, I) for a in local_a]
    B = [np.kron(I, a) for a in local_a]
    occ = np.array([n0+n1 for n0 in range(d) for n1 in range(d)])
    parity = np.diag((-1.)**occ).astype(complex)
    R = (I + parity)/2   # local Rac-like even sector
    D = (I - parity)/2   # local Di-like odd sector
    glob = np.kron(parity, parity)
    RR = np.kron(R, R)
    DD = np.kron(D, D)
    MIXED = np.kron(R, D) + np.kron(D, R)
    N = sum(a.conj().T@a for a in A+B)
    return dict(A=A, B=B, N=N, P=glob, RR=RR, DD=DD, MIXED=MIXED,
                localR=R, localD=D, localParity=parity)


def hamiltonian(m, *, omega=0.6, hop=0.05, pair=0.12):
    H = omega*m["N"].copy()
    for ai,bj in zip(m["A"],m["B"]):
        H += -hop*(ai.conj().T@bj + bj.conj().T@ai)
    # Antisymmetric SU(2)-singlet pair. The earlier same-channel
    # pairing was NOT frame-covariant under general SU(2).
    ai0,ai1=m["A"]
    bj0,bj1=m["B"]
    pair_op=ai0.conj().T@bj1.conj().T - ai1.conj().T@bj0.conj().T
    H += pair*(pair_op+pair_op.conj().T)
    assert np.allclose(H,H.conj().T)
    assert np.linalg.norm(H@m["P"]-m["P"]@H)<1e-11
    return H


def test_su2_singlet_covariance(m):
    """Check two-channel scalar hopping and epsilon-singlet pair invariance."""
    theta=.61
    U=np.array([[np.cos(theta), np.sin(theta)],
                [-np.sin(theta), np.cos(theta)]],dtype=complex)
    assert np.allclose(U.conj().T@U,np.eye(2))
    def rotate(A):
        return [sum(U[i,j]*A[j] for j in range(2)) for i in range(2)]
    a,b=m["A"],m["B"]
    ar,br=rotate(a),rotate(b)
    def hopping(A,B):
        return sum(x.conj().T@y for x,y in zip(A,B))
    def singlet(A,B):
        return (A[0].conj().T@B[1].conj().T -
                A[1].conj().T@B[0].conj().T)
    assert np.allclose(hopping(a,b),hopping(ar,br),atol=1e-11)
    assert np.allclose(singlet(a,b),singlet(ar,br),atol=1e-11)


def test_di_di_scalar_lowest_weight(m, v):
    """Verify the pair singlet has E0=2, J=0 and vanishing AdS lowering
    generator action on low-occupation vectors of the TRUNCATED Fock space.
    This is a channel witness, NOT a proof of the full tensor-product theorem.
    """
    ai0,ai1=m["A"]
    bj0,bj1=m["B"]
    pair=ai0.conj().T@bj1.conj().T - ai1.conj().T@bj0.conj().T
    state=pair@v
    assert np.linalg.norm(state)>1e-8
    state/=np.linalg.norm(state)
    dim=state.size
    eye=np.eye(dim,dtype=complex)
    energy=(m["N"]+2*eye)/2
    Jz=(ai0.conj().T@ai0-ai1.conj().T@ai1+
        bj0.conj().T@bj0-bj1.conj().T@bj1)/2
    Jp=ai0.conj().T@ai1 + bj0.conj().T@bj1
    lowering=[
        (ai0@ai0+ai1@ai1+bj0@bj0+bj1@bj1)/2,
        -0.5j*(ai0@ai0-ai1@ai1+bj0@bj0-bj1@bj1),
        ai0@ai1+bj0@bj1
    ]
    assert np.linalg.norm((energy-2*eye)@state)<1e-11
    assert np.linalg.norm(Jz@state)<1e-11
    assert np.linalg.norm(Jp@state)<1e-11
    assert np.linalg.norm(Jp.conj().T@state)<1e-11
    assert all(np.linalg.norm(L@state)<1e-11 for L in lowering)
    return float(np.real(np.vdot(state,energy@state)))


def rate_proxy(em, gr, kappa0=.12):
    """External EM–GR toy drive, not a measured pair-production rate."""
    return kappa0*(1+0.3*em+0.15*gr+0.1*em*gr)


def probabilities(state, m):
    def p(P):
        return float(np.real(np.vdot(state,P@state)))
    return dict(RR=p(m["RR"]),DD=p(m["DD"]),mixed=p(m["MIXED"]),
                norm=float(np.real(np.vdot(state,state))))


def vacuum_vector(d=3):
    v=np.zeros(d**4,dtype=complex)
    v[0]=1
    return v


def evolve(H, v, tau):
    out=expm(-1j*tau*H)@v
    assert np.isclose(np.vdot(out,out),np.vdot(v,v),atol=1e-11)
    return out


def verify_existing_singleton_labels():
    # Known oscillator construction: E0=(n_a+n_b+1)/2,
    # J3=(n_a-n_b)/2, Rac even and Di odd Fock subspaces.
    energies=[]
    for na,nb in [(0,0),(1,0),(0,1),(1,1),(2,0)]:
        energy=(na+nb+1)/2
        j3=(na-nb)/2
        energies.append((na,nb,energy,j3,(na+nb)%2))
    assert energies[:3]==[(0,0,.5,0.,0),
                          (1,0,1.,.5,1),(0,1,1.,-.5,1)]
    # ACCEPTED, not demonstrated: Flato–Fronsdal tensor-product towers
    # (recorded as representation bookkeeping only).
    spins={
        "Rac_Rac":[0,1,2,3,4],
        "Di_Di":[0,1,2,3,4],  # s=0 means D(2,0), not D(1,0)
        "Rac_Di":[.5,1.5,2.5,3.5,4.5],
    }
    assert all(float(s).is_integer() for s in spins["Rac_Rac"])
    assert all(float(s).is_integer() for s in spins["Di_Di"])
    assert all(not float(s).is_integer() for s in spins["Rac_Di"])
    return spins


def verify_finite_cutoff_obstruction(d=3):
    a=ladder(d)
    comm=a@a.conj().T - a.conj().T@a
    assert np.allclose(comm,np.diag([1.]*(d-1)+[1.-d]))
    assert np.isclose(np.trace(comm),0.)
    assert np.linalg.norm(comm-np.eye(d))>1.
    return float(np.linalg.norm(comm-np.eye(d)))


def run():
    spins=verify_existing_singleton_labels()
    defect=verify_finite_cutoff_obstruction()
    d=3
    m=model_matrices(d)
    test_su2_singlet_covariance(m)
    v=vacuum_vector(d)
    scalar_weight=test_di_di_scalar_lowest_weight(m,v)
    assert np.isclose(np.trace(m["RR"]+m["DD"]+m["MIXED"]),d**4)
    assert np.isclose(probabilities(v,m)["RR"],1.)

    phases=[]
    for em,gr in [(0.,0.),(1.,0.),(0.,1.),(1.,1.)]:
        H=hamiltonian(m,hop=.07,pair=rate_proxy(em,gr))
        res=evolve(H,v,tau=.75)
        probs=probabilities(res,m)
        assert abs(probs["norm"]-1)<1e-10
        assert abs(probs["mixed"])<1e-12
        assert probs["DD"]>0.005
        phases.append((em,gr,probs["DD"]))
    assert phases[0][2]<phases[1][2]<phases[3][2]
    assert phases[0][2]<phases[2][2]<phases[3][2]

    # A number-preserving hopping term alone cannot excite the empty state.
    Hno=hamiltonian(m,hop=.07,pair=0.)
    pno=probabilities(evolve(Hno,v,.75),m)
    assert pno["DD"]<1e-12

    # Starting with even occupation 2 on site 0, hopping transfers one
    # quantum; BOTH local parities change even -> odd while global parity
    # remains even. This is a sector-label transition, NOT a fermion creation.
    occupied=np.zeros(d**4,dtype=complex)
    loc=d*d
    occupied[(2*d)*loc]=1.
    p1=probabilities(evolve(Hno,occupied,.75),m)
    assert p1["DD"]>0.001 and p1["mixed"]<1e-12

    print("POM-5 SU(2)-singlet pair and parity selection diagnostics PASS")
    print("Published Rac/Di spin tower bookkeeping:",spins)
    print("SU(2)-singlet DiDi source lowest weight: E0=",scalar_weight,"spin=0")
    print("Finite oscillator CCR cutoff error:",round(defect,8))
    print("POM-5 even vacuum -> Di_i x Di_j probabilities:",phases)
    print("Hopping from local Rac(Rac) occupation -> DiDi probability:",p1["DD"])
    print("Mixed RacDi probability from globally even vacuum: exactly zero")
    print("LIMIT: no exact AdS4 singleton modules, EM/GR pair rate,")
    print("physical fermions, physical boson production or TEGR derived.")


if __name__=="__main__":
    run()
