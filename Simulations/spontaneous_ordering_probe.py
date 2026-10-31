"""POM-7: spontaneous sector-pattern test in a restricted, binary vacuum.

Known ANNNI period-4 ordering and SSH boundary modes are PRIOR PUBLISHED
RESULTS, not rediscovered here. This script tests only the POM-specific
projector-overlap map, exact finite-ring minimizers, and an H3 obstruction.

Crucial limitations:
- The 1D periodic graph and next-nearest interaction are POSTULATES.
- Two quaternionic orientations (A/B or A/C) are restricted by hand;
  the full continuous POM-3 vacuum has many more possibilities.
- A period-4 pattern is an exact zero-temperature state in this reduced
  energy; two translational phases are topological on an open termination,
  two are trivial. Neither is forced at a boundary.
- One-dimensional, finite-range equilibrium systems do not have
  finite-temperature spontaneous Ising order in the thermodynamic limit.
- No physical 3+1D particles, gauge bosons, tetrads, torsion or TEGR.
"""
from itertools import product
import numpy as np
from spectral_topological_probe import (
    sector_state, concrete_sectors, winding)
from sector_vacuum_probe import quaternion_sector, vacuum_potential


def ising_ring_energy(spins, j1=1, j2=1):
    s=np.asarray(spins,dtype=np.int64)
    return int(-j1*np.sum(s*np.roll(s,-1)) +
               j2*np.sum(s*np.roll(s,-2)))


def exact_ring_minimizers(n):
    """Exhaustive small-ring check, no imposed period-4 pattern."""
    best=None
    best_states=[]
    for candidate in product([-1,1],repeat=n):
        energy=ising_ring_energy(candidate)
        if best is None or energy < best:
            best=energy
            best_states=[candidate]
        elif energy==best:
            best_states.append(candidate)
    assert best == -n
    assert len(best_states)==4
    assert all(all(s[(i+2)%n]==-s[i] for i in range(n))
               for s in best_states)
    return best,best_states


def exact_transfer_minimizers(n):
    """Exact min-plus dynamic programming on a PERIODIC ANNNI ring.

    The first two spins are enumerated, then the last two retained as
    states. Closing two bonds handles the periodic nearest/next-nearest
    interactions. No sector-pattern initial condition is supplied.
    """
    if n < 4 or n % 4:
        raise ValueError("n should be a positive multiple of four >=4")
    solutions=[]
    for first,second in product([-1,1],repeat=2):
        dp={(first,second):(-first*second,(first,second))}
        for _ in range(2,n):
            next_dp={}
            for (last2,last1),(energy,history) in dp.items():
                for new in (-1,1):
                    candidate=(energy-last1*new+last2*new,
                               history+(new,))
                    key=(last1,new)
                    if key not in next_dp or candidate[0] < next_dp[key][0]:
                        next_dp[key]=candidate
            dp=next_dp
        completions=[]
        for (penultimate,last),(energy,history) in dp.items():
            closed=energy-last*first+penultimate*first+last*second
            completions.append((closed,history))
        solutions.append(min(completions,key=lambda z:z[0]))
    assert len({s for _,s in solutions})==4
    assert all(energy==-n and ising_ring_energy(s)==-n
               for energy,s in solutions)
    return solutions


def projectors():
    e=np.eye(8)
    (BA,BB),(PA,PB),qAB,_=concrete_sectors()
    psiA=sector_state(e[1],e[2])
    psiB=sector_state((e[1]+e[4])/np.sqrt(2),
                      (e[2]+e[5])/np.sqrt(2))
    psiC=sector_state(e[4],e[5])
    BC=quaternion_sector(psiC)
    PC=BC@BC.T
    qAC=float(np.trace(PA@PC)/4)
    assert np.isclose(qAB,5/8)
    assert np.isclose(qAC,1/2,atol=1e-12)
    assert np.array_equal(np.diag(PC),np.array([1.,1.,0.,0.,1.,1.,0.,0.]))
    for psi in (psiA,psiB,psiC):
        assert np.isclose(vacuum_potential(psi),-.084375)
    return (psiA,psiB,psiC),(PA,PB,PC),(qAB,qAC)


def overlap(a,b):
    return float(np.trace(a@b)/4)


def projected_periodic_energy(spins,p0,p1,coeff=16/3):
    """Frame-invariant overlap function on a two-orientation restriction.

    At qAB=5/8, this equals the J1=J2=1 Ising energy exactly.
    At qAC=1/2, it equals 4/3 of that Ising energy; all orientations
    beyond these two states remain unexamined.
    """
    P=[p0 if s==1 else p1 for s in spins]
    q1=sum(overlap(P[i],P[(i+1)%len(P)]) for i in range(len(P)))
    q2=sum(overlap(P[i],P[(i+2)%len(P)]) for i in range(len(P)))
    return coeff*(q2-q1)  # constant terms cancel at J1=J2=1


def h3_vacuum_energy(psi):
    """The original POM-3 positive-neighbor Hamiltonian on a ring."""
    K=.08
    minimum=sum(vacuum_potential(p) for p in psi)
    link=K/2*sum(np.linalg.norm(psi[i]-psi[(i+1)%len(psi)])**2
                 for i in range(len(psi)))
    return minimum+link  # gamma=0; gamma>0 only increases link pattern cost


def spectral_termination(spins,p0,p1,offset=.1,stiffness=.9):
    P=[p0 if s==1 else p1 for s in spins]
    hoppings=np.array([offset+stiffness*overlap(P[i],P[i+1])
                       for i in range(len(P)-1)])
    H=np.diag(hoppings,1)+np.diag(hoppings,-1)
    e,vec=np.linalg.eigh(H)
    indexes=np.argsort(abs(e))[:2]
    edge_weight=min(float(np.sum(abs(vec[:2,j])**2)+
                          np.sum(abs(vec[-2:,j])**2)) for j in indexes)
    w=winding(hoppings[0],hoppings[1])  # known SSH bulk winding, no proof
    return dict(winding=w,minabs=float(max(abs(e[indexes]))),
                edge_weight=edge_weight,first_two=hoppings[:2])


def run():
    assert exact_ring_minimizers(8)[0]==-8
    assert exact_ring_minimizers(12)[0]==-12
    solutions=exact_transfer_minimizers(40)
    states,projectors_,q=projectors()
    pa,pb,pc=projectors_
    assert np.allclose(q,(5/8,1/2),atol=1e-12)

    counts={}
    modes={}
    for sector_name,sector in [("B",pb),("C",pc)]:
        summaries=[]
        for energy,pattern in solutions:
            actual=projected_periodic_energy(pattern,pa,sector)
            expected=energy if sector_name=="B" else (4/3)*energy
            assert np.isclose(actual,expected,atol=1e-10)
            modes0=spectral_termination(pattern,pa,sector)
            summaries.append((pattern[:4],actual,modes0))
            counts[modes0["winding"]]=counts.get(modes0["winding"],0)+1
        assert sum(t[2]["winding"]==-1 for t in summaries)==2
        assert sum(t[2]["winding"]==0 for t in summaries)==2
        for item in summaries:
            if item[2]["winding"]==-1:
                assert item[2]["minabs"]<2e-4
                assert item[2]["edge_weight"]>.55
            else:
                assert item[2]["minabs"]>.3
                assert item[2]["edge_weight"]<.04
        modes[sector_name]=summaries

    # H3 with nonnegative gamma and positive link stiffness always admits
    # uniform minimum; the AACC/ABBA ordering is more expensive.
    uniform=[states[0]]*40
    patterned=[states[0] if s==1 else states[2] for s in solutions[0][1]]
    h_uniform=h3_vacuum_energy(uniform)
    h_pattern=h3_vacuum_energy(patterned)
    assert h_pattern>h_uniform+.1
    # POM-6's B is not even a global minimum among these two admissible
    # period-four AABB test families: sector C gives smaller projector
    # overlap and therefore lower frustration energy.
    assert modes["C"][0][1] < modes["B"][0][1]
    assert np.isclose(modes["B"][0][1],-40.)
    assert np.isclose(modes["C"][0][1],-160/3)

    print("POM-7: unrestricted labels within TWO-sector reduction, exact ED N=8,12 PASS")
    print("POM-7: min-plus DP N=40 gives exactly four period-4 ground phases PASS")
    print("POM-7: q_AB=5/8, q_AC=1/2 from POM-3 sector projectors PASS")
    print("H3 uniform energy vs patterned:",h_uniform,h_pattern)
    for key,results in modes.items():
        print("Sector",key)
        for phase,energy,sp in results:
            print(" phase",phase,"projector energy",energy,
                  "winding",sp["winding"],"edge |E|",sp["minabs"],
                  "edge weight",sp["edge_weight"])
    print("POM-7: topology depends on boundary termination, not just bulk order")
    print("POM-7: C is energetically preferable to B in test frustration,")
    print("so POM-6 choice B was NOT dynamically selected.")
    print("LIMIT: 1D graph, two-sector restriction, competing J1/J2 and")
    print("spectral hopping rule remain assumed; no real fermions or GR.")


if __name__=="__main__":
    run()
