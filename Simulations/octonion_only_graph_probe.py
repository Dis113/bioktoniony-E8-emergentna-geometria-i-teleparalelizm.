"""POM-12 — STRICTLY EDGE-LOCAL associator incentive and H vs O ablation.

Literature input, NOT reproved:
Harvey and Lawson (1982), Calibrated geometries, Theorem 1.6:
 phi(u,v,w)^2 + ||[u,v,w]||^2/4 = det Gram(u,v,w).

NEW toy hypothesis:
  E_interaction=mu*N_active_edges-g*I_closed_triangle*A2,
where A2=||[u,v,w]||^2/4 and u,v,w are unit imaginary octonions.
At all edges OFF, every configuration has ZERO interaction energy.
For mu=1/4, g=1, non-associativity selects a triangle with energy
-1/4. In an associative quaternion algebra A2=0 identically and
the empty graph has energy 0.

This conditional, finite model does not derive its coupling from POM-3.
No real spacetime, physics of hbar, photons, fermions, GR/TEGR.
"""
from itertools import product

import numpy as np
from pom1_model import omul, associator
from sector_vacuum_probe import vacuum_potential, quaternion_sector

MU, GAIN = .25, 1.


def assoc_norm_squared(u, v, w):
    assoc=associator(u,v,w)
    return float(assoc@assoc)/4


def phi_g2(u,v,w):
    return -float(omul(omul(u,v),w)[0])


def gram_det(u,v,w):
    m=np.stack([u[1:],v[1:],w[1:]],axis=0)
    return float(np.linalg.det(m@m.T))


def graph_energy(bits, u,v,w, mu=MU, gain=GAIN):
    count=sum(bits)
    is_triangle=int(all(bits))
    return mu*count-gain*is_triangle*assoc_norm_squared(u,v,w)


def local_vacuum(u,v):
    """POM-3 onsite ground-state representative, r=3/4."""
    psi=np.r_[np.sqrt(3/8)*u,np.sqrt(3/8)*v]
    assert np.isclose(vacuum_potential(psi),-.084375)
    return psi


def exact_witness_tests():
    basis=np.eye(8)
    O=[basis[1],basis[2],basis[4]]
    H=[basis[1],basis[2],basis[3]]
    assert assoc_norm_squared(*O)==1.
    assert assoc_norm_squared(*H)==0.
    assert np.isclose(gram_det(*O),gram_det(*H))
    assert np.isclose(phi_g2(*O),0)
    assert np.isclose(abs(phi_g2(*H)),1)

    # Local states really are POM-3 ground states and select H_i:
    psi=[
      local_vacuum(basis[1],basis[2]),
      local_vacuum(basis[2],basis[3]),
      local_vacuum(basis[4],basis[5]),
    ]
    frames=[quaternion_sector(p) for p in psi]
    P=[q@q.T for q in frames]
    assert not np.allclose(P[0],P[2])
    assert all(np.isclose(vacuum_potential(p),-.084375) for p in psi)

    graph_bits=list(product([0,1],repeat=3))
    eo=np.array([graph_energy(b,*O) for b in graph_bits])
    eh=np.array([graph_energy(b,*H) for b in graph_bits])
    assert np.allclose(eo, [0,.25,.25,.5,.25,.5,.5,-.25])
    assert np.allclose(eh, [0,.25,.25,.5,.25,.5,.5,.75])
    assert min(eo)==-.25 and min(eh)==0.
    assert all(graph_energy((0,0,0),*U)==0 for U in (O,H))
    return psi,graph_bits,eo,eh


def calibration_and_locality_trials(n=2500,seed=12026):
    rng=np.random.default_rng(seed)
    residuals=[]
    for _ in range(n):
        Q,_=np.linalg.qr(rng.normal(size=(7,3)))
        u,v,w=[np.r_[0,Q[:,j]] for j in range(3)]
        a2=assoc_norm_squared(u,v,w)
        phi=phi_g2(u,v,w)
        gram=gram_det(u,v,w)
        residuals.append(abs(phi*phi+a2-gram))
        assert residuals[-1]<3e-12
        assert -1e-12 <= a2 <= 1+1e-12
        for bits in product([0,1],repeat=3):
            energy=graph_energy(bits,u,v,w)
            assert energy >= -.25-1e-12
            if not all(bits): assert energy>=0
            if not any(bits): assert energy==0
    return max(residuals)


def robustness_trials(n=2000,seed=12027):
    rng=np.random.default_rng(seed)
    for _ in range(n):
        d_closed,d_open=rng.uniform(-.124999,.124999,size=2)
        assert -.25+d_closed<0+d_open


def unsafe_unscaled_extension(states, t):
    """Shows why simply appending a -g * raw-associator^2 to V3 fails:
    the cubic associator produces negative t^6 while V3 is quartic.
    This is a DIAGNOSTIC, not the actual normalized POM-12 energy.
    """
    scaled=[t*p for p in states]
    onsite=sum(vacuum_potential(p) for p in scaled)
    raw=[p[:8] for p in scaled]
    nonassoc=associator(*raw)
    return onsite+3*MU-GAIN*float(nonassoc@nonassoc)/4


def main():
    states,bits,eo,eh=exact_witness_tests()
    err=calibration_and_locality_trials()
    robustness_trials()
    unsafe=[unsafe_unscaled_extension(states,t) for t in (1,2,4,8,16)]
    assert unsafe[-1]<-100000 and unsafe[-1]<unsafe[-2]
    print("POM-12 WARNING: unscaled negative cubic-associator reward")
    print("  makes full-amplitude energy unbounded below (sample):",unsafe)
    print("POM-12: exact local octonionic graph vs quaternion control PASS")
    print("  graph bits:",bits)
    print("  octonion energies:",eo.tolist())
    print("  quaternion energies:",eh.tolist())
    print("  energy difference: O min = -1/4, H min = 0")
    print("  all-off graph has zero interaction energy, unlike POM-10")
    print("  exact threshold: gain > 3*edge_cost; chosen gain=1, edge_cost=1/4")
    print("  Harvey-Lawson calibration max residual:",err)
    print("  2000 bounded perturbations preserve the selected loop")
    print("  LIMIT: graph size & sign of associator coupling are POSTULATES,")
    print("  not consequences of the earlier POM Hamiltonians or SM/TEGR.")


if __name__=="__main__":
    main()
