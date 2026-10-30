"""POM-3: evolve projectors of dynamically selected quaternion sectors.

All graph adjacency and evolution parameter are stipulated. Projector motion
is NOT a physical trajectory, tetrad, or teleparallel torsion.
"""
import numpy as np
from pom1_model import GraphHamiltonian, bioassociator
from sector_vacuum_probe import quaternion_sector


class SectorHamiltonian(GraphHamiltonian):
    """Replace old E8/positive-mass onsite potential with exact POM-3 V3."""
    def __init__(self, n=5, alpha=.45, lam=.8, eta=.2,
                 hopping=.06, gamma=.005):
        super().__init__(n=n, mass_squared=0, hopping=hopping, quartic=0,
                         root_coupling=0, associator_coupling=gamma)
        if not (alpha>0 and lam>eta>0):
            raise ValueError("Requires alpha>0 and lam>eta>0")
        self.alpha,self.lam3,self.eta=alpha,lam,eta

    def potential_and_gradient(self, psi):
        pot,grad=super().potential_and_gradient(psi)
        s=np.sum(psi**2,axis=1)
        u,v=psi[:,1:8],psi[:,9:16]
        a,b=np.sum(u*u,axis=1),np.sum(v*v,axis=1)
        c=np.sum(u*v,axis=1)
        delta=a*b-c*c
        pot+=float(np.sum(-self.alpha/2*s+self.lam3/4*s*s-self.eta*delta))
        grad+=(-self.alpha+self.lam3*s)[:,None]*psi
        grad[:,1:8]-=self.eta*(2*b[:,None]*u-2*c[:,None]*v)
        grad[:,9:16]-=self.eta*(2*a[:,None]*v-2*c[:,None]*u)
        return pot,grad


def projector(psi):
    B=quaternion_sector(psi)
    return B@B.T


def main():
    rng=np.random.default_rng(811)
    model=SectorHamiltonian(n=5)
    r2=model.alpha/(model.lam3-model.eta)
    amp=np.sqrt(r2/2)
    psi=np.zeros((5,16))
    for i,t in enumerate(np.linspace(0,np.pi/2,5)):
        psi[i,1]=amp
        psi[i,8+2]=amp*np.cos(t)
        psi[i,8+4]=amp*np.sin(t)
    momentum=.012*rng.normal(size=(5,16))
    P0=[projector(z) for z in psi]
    energy0,grad=model.potential_and_gradient(psi)
    h=1e-6
    for i,j in [(0,0),(0,1),(0,9),(2,12),(4,6)]:
        plus=psi.copy(); minus=psi.copy()
        plus[i,j]+=h;minus[i,j]-=h
        numerical=(model.potential_and_gradient(plus)[0]-
                   model.potential_and_gradient(minus)[0])/(2*h)
        assert np.isclose(numerical,grad[i,j],atol=2e-8)
    assoc=[np.linalg.norm(bioassociator(psi[i],psi[(i+1)%5],
                                      psi[(i+2)%5])) for i in range(5)]
    assert max(assoc)>1e-3
    after,momentum2,energy=model.evolve(psi,momentum,dt=.008,steps=50)
    drift=float(np.max(abs(energy-energy[0]))/max(1.,abs(energy[0])))
    P1=[projector(z) for z in after]
    movements=[float(np.linalg.norm(P1[i]-P0[i])) for i in range(5)]
    assert drift<1e-4 and max(movements)>1e-4
    print("POM-3 sector-projector evolution PASS")
    print("Relative Hamiltonian energy drift:",drift)
    print("Projector distances after evolution:",movements)
    print("Cross-sector associator norms:",[float(z) for z in assoc])
    print("LIMIT: no spacetime coordinates, Lorentz dynamics, or TEGR inferred")


if __name__=="__main__":
    main()
