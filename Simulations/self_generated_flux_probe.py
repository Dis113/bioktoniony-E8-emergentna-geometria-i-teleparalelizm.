"""POM-10: CONDITIONAL no-external-magnetic-field toy extension.

An octonionic G2-calibrated chirality on three pre-existing potential
nodes, with DYNAMIC Boolean graph edges, selects a closed triangle.
The Berry Wilson phase from the same quaternionic spinor frame has an
irrational flux/(2*pi). A separately ASSUMED QWZ two-band response
coupled to the selected chirality is fully gapped and has Chern ±1.

NONE of the three-sector graph energy, SU2 spinor quantum fiber,
2D kinetic QWZ operator, or physical hbar is derived from POM-3/9.
Haldane/QWZ topology, Pancharatnam-Berry and Niven theorem are
established published mathematics; no general theorems are re-proved.
"""
import itertools
import math
import numpy as np

from pom1_model import omul
from sector_vacuum_probe import quaternion_sector, vacuum_potential

PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex)
)


def octonion_chirality(vectors):
    a, b, c = vectors
    return -float(omul(omul(a, b), c)[0])


def graph_energy(edges, vectors):
    """The three possible edges are variables, not pre-filled links.

    Spins u_i are real imaginary unit octonions taken from the x part of
    POM-3. The graph's triangle product is 1 iff ALL 3 edges are present.
    """
    u, v, w = vectors
    a = float(u @ v)
    b = float(v @ w)
    c = float(u @ w)
    chi = octonion_chirality(vectors)
    return (a*a + b*b + c*c - 6*c - 3*chi*chi +
            sum(edges)/10 - int(all(edges))*chi*chi)


def chiral_vacuum(sign):
    """Two time-reversed vacua in a self-selected associative H sector."""
    e = np.eye(8)
    u1, u2 = e[1], e[2]
    u3 = (3*e[1] + sign*4*e[3])/5
    vectors = [u1, u2, u3]
    # The scalar part of x,y vanishes; each pair (u,v) is orthonormal.
    partners = [e[2], e[3], e[2]]
    amp = np.sqrt(.75/2)
    psis = []
    for u, v in zip(vectors, partners):
        psi = np.r_[amp*u, amp*v]
        assert np.isclose(vacuum_potential(psi), -.084375)
        psis.append(psi)
    projectors = [
        B @ B.T for B in (quaternion_sector(psi) for psi in psis)
    ]
    # All three local sectors lie in one common H (an important
    # NEGATIVE control: this mechanism is NOT uniquely octonionic).
    assert all(np.allclose(P, projectors[0]) for P in projectors)
    return vectors, psis


def spinor(n):
    """SU(2) coherent spinor in the dynamically common H of this witness."""
    operator = sum(n[j+1]*PAULI[j] for j in range(3))
    e, V = np.linalg.eigh(operator)
    assert np.allclose(e, [-1, 1])
    return V[:, 1]


def berry_loop(vectors):
    z = [spinor(n) for n in vectors]
    B = (np.vdot(z[0], z[1]) *
         np.vdot(z[1], z[2]) *
         np.vdot(z[2], z[0]))
    return B, float(np.angle(B)), z


def triangle_loop_spectrum(z):
    """Finite graph: all three edges carry state-derived complex overlaps.

    This has level spacings but NOT a 2D bulk topological band gap.
    For the explicit chiral witness the exact three eigenvalues are
    -1 and (5 ± sqrt(105))/10.
    """
    H = np.zeros((3, 3), dtype=complex)
    for i,j in ((0,1),(1,2),(2,0)):
        H[i,j] = np.vdot(z[i],z[j])
        H[j,i] = np.conj(H[i,j])
    eigenvalues=np.linalg.eigvalsh(H)
    exact=np.array([-1,(5-np.sqrt(105))/10,(5+np.sqrt(105))/10])
    assert np.allclose(eigenvalues,exact,atol=1e-12)
    local_gap=float(np.min(np.diff(eigenvalues)))
    assert np.isclose(local_gap,(15-np.sqrt(105))/10)
    assert local_gap > .47
    return eigenvalues,local_gap


def qwz(kx, ky, mass):
    """Given 2D QWZ spectral RESPONSE: no external Peierls/B field."""
    return (np.sin(kx)*PAULI[0] + np.sin(ky)*PAULI[1] +
            (mass+np.cos(kx)+np.cos(ky))*PAULI[2])


def chern_number(mass, grid=31):
    """Published FHS algorithm; checks this particular postulated response."""
    eigvecs = []
    min_gap = float("inf")
    for i in range(grid):
        row = []
        for j in range(grid):
            e, V = np.linalg.eigh(qwz(
                2*np.pi*i/grid, 2*np.pi*j/grid, mass))
            min_gap = min(min_gap, float(e[1]-e[0]))
            row.append(V[:, 0])
        eigvecs.append(row)
    links = np.zeros((grid, grid, 2), dtype=complex)
    for i in range(grid):
        for j in range(grid):
            links[i, j, 0] = np.vdot(
                eigvecs[i][j], eigvecs[(i+1) % grid][j])
            links[i, j, 1] = np.vdot(
                eigvecs[i][j], eigvecs[i][(j+1) % grid])
            assert np.min(abs(links[i,j])) > .95
            links[i,j] /= abs(links[i,j])
    total = 0.0
    for i in range(grid):
        for j in range(grid):
            total += np.angle(
                links[i,j,0] * links[(i+1)%grid,j,1] /
                (links[i,(j+1)%grid,0] * links[i,j,1]))
    chern = total/(2*np.pi)
    assert np.isclose(chern, round(chern), atol=1e-9)
    return int(round(chern)), min_gap


def run():
    rng = np.random.default_rng(20261101)

    # Standard octonionic calibration inequality is assumed in Lean
    # and independently sampled here; NOT newly proved.
    for _ in range(400):
        u = rng.normal(size=(3,7))
        u /= np.linalg.norm(u, axis=1)[:,None]
        vectors = np.pad(u, ((0,0),(1,0)))
        c = float(u[0] @ u[2])
        chi = octonion_chirality(vectors)
        assert chi*chi <= 1-c*c + 2e-13

    # All 8 Boolean graphs are compared; incomplete ones have an exact
    # global lower bound -21/4. The complete graph has ground -11/2.
    states = []
    for sign in (1,-1):
        vectors, psis = chiral_vacuum(sign)
        c = float(vectors[0]@vectors[2])
        chi = octonion_chirality(vectors)
        assert np.isclose(c,3/5) and np.isclose(chi,sign*4/5)
        for edges in itertools.product((0,1), repeat=3):
            e = graph_energy(edges, vectors)
            if all(edges):
                assert np.isclose(e,-11/2)
            else:
                assert e>=-21/4-1e-12
        B, phase, zs = berry_loop(vectors)
        assert np.isclose(B, (2+sign*1j)/5)
        assert np.isclose(phase, sign*math.atan(.5))
        assert np.isclose(np.cos(2*phase),3/5)
        # Local phase choices cannot affect the closed Wilson loop.
        for angles in rng.uniform(-np.pi,np.pi,size=(8,3)):
            gz=[z*np.exp(1j*a) for z,a in zip(zs,angles)]
            observed=np.vdot(gz[0],gz[1])*np.vdot(gz[1],gz[2])*np.vdot(gz[2],gz[0])
            assert np.isclose(observed,B)
        finite_levels, finite_gap = triangle_loop_spectrum(zs)
        top, gap=chern_number(chi)
        top2,gap2=chern_number(chi+sign*.2)
        assert top==top2==sign
        assert gap>=1.6-1e-10 and gap2>=1.2-1e-10
        states.append((sign,c,chi,B,phase,finite_gap,top,gap,gap2))

    # Exactly rational energy witness. There is no input rational flux.
    from fractions import Fraction as F
    c,d=F(3,5),F(16,25)
    spin=c*c-6*c-3*d
    closed=spin+3*F(1,10)-d
    assert closed == -F(11,2)
    assert -F(21,4)-closed==F(1,4)
    pitch=-12*c+5*(2*c*c-1)
    assert pitch == -F(43,5)

    # A vanishing chirality mass leaves a QWZ Dirac point at (0, pi).
    assert np.allclose(np.linalg.eigvalsh(qwz(0,np.pi,0)),[0,0],atol=1e-12)
    # This establishes the gap is not produced by the graph's positive
    # adjacency weights alone; a specified chiral response is required.

    # Pure site U(1) phases give trivial holonomy; CP1 spinors do not.
    phases=rng.uniform(0,2*np.pi,3)
    z=np.exp(1j*phases)
    assert np.isclose(np.prod([
        np.conj(z[i])*z[(i+1)%3] for i in range(3)]),1.)

    print("POM-10: EXACT closed-loop ground energy",closed,
          " vs best open graph -21/4; robust preference 1/4.")
    print("POM-10: J1=12,J2=5 spiral pitch cos(theta)=3/5,"
          " theta/pi=",math.acos(float(c))/math.pi)
    for sign,c,chi,B,phase,finite_gap,top,gap,gap2 in states:
        print(" POM-10 chirality",sign,"chi=",chi,
              "Bargmann=",B,"flux/2pi=",phase/(2*math.pi),
              "finite-3-level gap=",finite_gap,
              "Chern=",top,"2D band gap=",gap,"perturbed gap=",gap2)
    print("POM-10: no external Peierls magnetic field was used.")
    print("LIMIT: 3 potential nodes, chirality interaction, CP1 spinors,"
          " QWZ 2D kinetic operator, and exchange coefficients are inputs.")
    print("LIMIT: stable band gap != stability of physical particles;" 
          " no hbar, EM, GR, E8 or spacetime emergently derived.")


if __name__=="__main__":
    run()
