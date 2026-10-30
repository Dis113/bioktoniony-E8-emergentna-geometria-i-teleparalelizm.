"""POM-1: reproducible toy model of a bi-octonionic causal medium.

Requirements: numpy.  Optional for plots: matplotlib (not used here).

What is established in this program:
  * the 240 E8 roots and their exact second-moment identity;
  * a real 16-component field x+i*y with octonion associators;
  * a bounded-below, explicitly specified graph Hamiltonian;
  * local reversible leapfrog updates and energy checks;
  * benchmark cosmological background of the effective scalar theory.

What it does NOT establish:
  * emergence of Lorentz invariance or 3+1 spacetime,
  * derivation of SM chirality, Yang--Mills or confinement,
  * derivation of the effective gravitational action from the graph.

All microscopic quantities are dimensionless.  The cosmology section uses SI/eV.
"""
from __future__ import annotations

import itertools
import math
import numpy as np


def e8_roots() -> np.ndarray:
    roots = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (-1.0, 1.0):
                for sj in (-1.0, 1.0):
                    r = np.zeros(8)
                    r[i], r[j] = si, sj
                    roots.append(r)
    for signs in itertools.product((-1.0, 1.0), repeat=8):
        if sum(s < 0 for s in signs) % 2 == 0:
            roots.append(0.5 * np.array(signs))
    result = np.array(roots)
    assert result.shape == (240, 8)
    assert np.allclose(np.sum(result * result, axis=1), 2.0)
    assert np.allclose(result.T @ result, 60.0 * np.eye(8))
    return result


def qmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return np.array([
        aw*bw - ax*bx - ay*by - az*bz,
        aw*bx + ax*bw + ay*bz - az*by,
        aw*by - ax*bz + ay*bw + az*bx,
        aw*bz + ax*by - ay*bx + az*bw,
    ])


def qconj(a: np.ndarray) -> np.ndarray:
    out = a.copy()
    out[1:] *= -1
    return out


def omul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """One standard Cayley--Dickson octonion multiplication convention."""
    x, y = a[:4], a[4:]
    z, w = b[:4], b[4:]
    return np.r_[qmul(x, z) - qmul(qconj(w), y),
                 qmul(w, x) + qmul(y, qconj(z))]


def associator(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return omul(omul(a, b), c) - omul(a, omul(b, c))


def biomul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Complexified octonions: (x+i y)(u+i v)."""
    x, y, u, v = a[:8], a[8:], b[:8], b[8:]
    return np.r_[omul(x, u)-omul(y, v), omul(x, v)+omul(y, u)]


def bioassociator(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return biomul(biomul(a, b), c) - biomul(a, biomul(b, c))


ROOTS = e8_roots()
BASIS = np.eye(8)
BIO_BASIS = np.eye(16)


class GraphHamiltonian:
    def __init__(self, n: int = 5, mass_squared: float = .05,
                 hopping: float = .08, quartic: float = .02,
                 root_coupling: float = .001, root_scale: float = 1.,
                 associator_coupling: float = .01):
        if n < 3:
            raise ValueError("Use at least 3 sites")
        if min(mass_squared, hopping, quartic, root_coupling,
               associator_coupling) < 0 or root_scale <= 0:
            raise ValueError("Potential parameters must be nonnegative")
        self.n = n
        self.mu2 = mass_squared
        self.K = hopping
        self.lam = quartic
        self.eps = root_coupling
        self.f = root_scale
        self.gamma = associator_coupling
        # Undirected nearest-neighbor links on a ring.
        self.edges = [(i, (i+1)%n) for i in range(n)]
        # Ordered local triples, necessary for the nonassociative term.
        self.triples = [(i, (i+1)%n, (i+2)%n) for i in range(n)]

    def potential_and_gradient(self, psi: np.ndarray):
        """psi shape (n,16): first 8 octonion x, second 8 octonion y."""
        assert psi.shape == (self.n, 16)
        norm2 = np.sum(psi**2, axis=1)
        pot = (0.5*self.mu2*norm2 + 0.25*self.lam*norm2**2).sum()
        grad = self.mu2*psi + (self.lam*norm2)[:, None]*psi

        if self.eps:
            rx = psi[:, :8] @ ROOTS.T / self.f
            ry = psi[:, 8:] @ ROOTS.T / self.f
            pot += self.eps * np.sum(2.0-np.cos(rx)-np.cos(ry))
            grad[:, :8] += (self.eps/self.f) * (np.sin(rx) @ ROOTS)
            grad[:, 8:] += (self.eps/self.f) * (np.sin(ry) @ ROOTS)

        if self.K:
            for i, j in self.edges:
                d = psi[i] - psi[j]
                pot += 0.5*self.K*float(d @ d)
                grad[i] += self.K*d
                grad[j] -= self.K*d

        if self.gamma:
            for i, j, k in self.triples:
                a, b, c = psi[i], psi[j], psi[k]
                assoc = bioassociator(a, b, c)
                pot += self.gamma*float(assoc @ assoc)
                for idx in range(16):
                    e = BIO_BASIS[idx]
                    grad[i, idx] += 2*self.gamma * float(assoc @ bioassociator(e, b, c))
                    grad[j, idx] += 2*self.gamma * float(assoc @ bioassociator(a, e, c))
                    grad[k, idx] += 2*self.gamma * float(assoc @ bioassociator(a, b, e))
        return float(pot), grad

    def energy(self, psi: np.ndarray, momentum: np.ndarray) -> float:
        return .5*float(np.sum(momentum**2))+self.potential_and_gradient(psi)[0]

    def evolve(self, psi: np.ndarray, momentum: np.ndarray, dt: float = .025,
               steps: int = 40):
        """Symplectic, time reversible kick-drift-kick update.

        The integer step is a computational ordering, not yet physical proper time.
        Local graph coupling is given, but a finite signal-speed bound and Lorentz symmetry have NOT been proved.
        """
        psi = psi.copy()
        momentum = momentum.copy()
        trace = [self.energy(psi, momentum)]
        for _ in range(steps):
            _, grad = self.potential_and_gradient(psi)
            momentum -= 0.5*dt*grad
            psi += dt*momentum
            _, grad = self.potential_and_gradient(psi)
            momentum -= 0.5*dt*grad
            trace.append(self.energy(psi, momentum))
        return psi, momentum, np.asarray(trace)


def cosmic_benchmark():
    """Mean background of scalar oscillations (m >> H) plus constant V0."""
    H0_km_s_Mpc = 67.4
    omega_b, omega_dm, omega_de = .049, .266, .685
    m_eV = 1e-20  # Illustrative mass; NOT a measurement!
    sec_per_Mpc_per_km = 3.085677581491367e19
    H0 = H0_km_s_Mpc / sec_per_Mpc_per_km
    hbar_eVs = 6.582119569e-16
    reduced_Mp_eV = 2.435e27
    amplitude_eV = math.sqrt(6*omega_dm)*H0*hbar_eVs/m_eV*reduced_Mp_eV
    # Example scalar field w, excluding baryons and photons.
    samples=[]
    for z in [0, .5, 1, 2, 3]:
        rho_m=omega_dm*(1+z)**3
        rho_lambda=omega_de
        E=math.sqrt((omega_b+omega_dm)*(1+z)**3+rho_lambda)
        w_dark = -rho_lambda/(rho_lambda+rho_m)
        samples.append((z, rho_m, rho_lambda, E, w_dark))
    return dict(H0_s_inverse=H0, H0_eV=H0*hbar_eVs,
                m_eV=m_eV, amplitude_today_GeV=amplitude_eV/1e9,
                onset_acceleration_z=(2*omega_de/(omega_b+omega_dm))**(1/3)-1,
                columns=('z','rho_DM/rho_crit0','rho_DE/rho_crit0','H/H0','w_dark'),
                samples=samples)


def main():
    print('E8: 240 roots, 8 real coordinates, root length squared 2')
    print('Identity sum_{alpha} alpha alpha^T = 60 I_8: verified')
    # Check octonionic norm multiplication and nonassociativity.
    ea, eb, ec = BASIS[1], BASIS[2], BASIS[4]
    print('Octonion associator for basis e1,e2,e4: ',associator(ea,eb,ec))
    assert np.linalg.norm(associator(ea,eb,ec)) > 0
    rng=np.random.default_rng(20261030)
    for _ in range(5):
        u,v=rng.normal(size=(2,8))
        assert np.isclose(np.linalg.norm(omul(u,v)),
                          np.linalg.norm(u)*np.linalg.norm(v),rtol=1e-12)
    model=GraphHamiltonian()
    psi = .12*rng.normal(size=(model.n,16))
    momentum=.05*rng.normal(size=(model.n,16))
    energy,grad=model.potential_and_gradient(psi)
    # Analytic-gradient check with central differences.
    h=1e-6
    for i,j in [(0,0),(0,5),(2,9),(4,15)]:
        plus=psi.copy(); minus=psi.copy()
        plus[i,j]+=h; minus[i,j]-=h
        numeric=(model.potential_and_gradient(plus)[0]
                 -model.potential_and_gradient(minus)[0])/(2*h)
        assert np.isclose(numeric,grad[i,j],rtol=1e-6,atol=1e-8), (i,j,numeric,grad[i,j])
    after_psi,after_p,trace=model.evolve(psi,momentum)
    relative_drift=np.max(np.abs(trace-trace[0]))/abs(trace[0])
    print(f'Microscopic graph n={model.n}: 40 leapfrog steps, max relative energy drift = {relative_drift:.3g}')
    print('Cosmological benchmark (m=1e-20 eV is illustrative):')
    benchmark=cosmic_benchmark()
    print(f'  H0 = {benchmark["H0_s_inverse"]:.4e} 1/s')
    print(f'  field amplitude today = {benchmark["amplitude_today_GeV"]:.3g} GeV')
    print(f'  cosmic acceleration begins near z = {benchmark["onset_acceleration_z"]:.3f}')
    print('  z | rho_DM/rhoc0 | rho_DE/rhoc0 | H/H0 | dark w')
    for row in benchmark['samples']:
        print('  '+ ' | '.join(f'{x:7.3f}' for x in row))


if __name__ == '__main__':
    main()