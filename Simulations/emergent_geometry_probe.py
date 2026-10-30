"""POM-1: bilinear edge currents and plaquette-circulation diagnostic.

This does NOT derive a spacetime tetrad or physical torsion.
A 4-simplex, four octonionic projections and Lorentzian eta are supplied.
Run: python Simulations/emergent_geometry_probe.py
"""
from itertools import combinations
import numpy as np

from pom1_model import GraphHamiltonian, omul


def oct_conj(x):
    ans = np.asarray(x, dtype=float).copy()
    ans[1:] *= -1
    return ans


def current7(a, b):
    """Real seven-vector, antisymmetric in endpoints a,b."""
    ab = omul(oct_conj(a[:8]), b[:8]) + omul(oct_conj(a[8:]), b[8:])
    ba = omul(oct_conj(b[:8]), a[:8]) + omul(oct_conj(b[8:]), a[8:])
    return (0.5 * (ab - ba))[1:]


def link(psi, i, j, selected=(0, 1, 2, 3)):
    return current7(psi[i], psi[j])[list(selected)]


def circulation(psi, i, j, k, selected=(0, 1, 2, 3)):
    return (link(psi, i, j, selected) + link(psi, j, k, selected)
            + link(psi, k, i, selected))


def frame(psi, selected=(0, 1, 2, 3)):
    """Columns label four edges of an ASSUMED 4-simplex."""
    return np.column_stack([link(psi, 0, j, selected) for j in range(1, 5)])


def imposed_metric(e):
    """eta is INPUT, not derived from the bi-octonionic Hamiltonian."""
    eta = np.diag([-1., 1., 1., 1.])
    return e.T @ eta @ e


def main():
    model = GraphHamiltonian(n=5, mass_squared=.05, hopping=.08,
                             quartic=.02, root_coupling=.001,
                             associator_coupling=.003)
    # A five-vertex complete graph (4-simplex) is an ADDITIONAL assumption.
    model.edges = list(combinations(range(5), 2))
    model.triples = list(combinations(range(5), 3))
    rng = np.random.default_rng(4302026)
    psi = .65 * rng.normal(size=(5, 16))
    momentum = .04 * rng.normal(size=(5, 16))

    zero = np.zeros_like(psi)
    assert np.array_equal(frame(zero), np.zeros((4, 4)))
    assert np.array_equal(circulation(zero, 0, 1, 2), np.zeros(4))

    for i, j in combinations(range(5), 2):
        assert np.allclose(current7(psi[i], psi[j]),
                           -current7(psi[j], psi[i]))

    # Only the observable current is U(1)-invariant.
    # The full POM-1 E8 cosine Hamiltonian need not have this U(1) symmetry.
    angle = .71
    rot = np.concatenate([
        np.cos(angle) * psi[:, :8] - np.sin(angle) * psi[:, 8:],
        np.sin(angle) * psi[:, :8] + np.cos(angle) * psi[:, 8:]
    ], axis=1)
    for i, j in combinations(range(5), 2):
        assert np.allclose(current7(psi[i], psi[j]), current7(rot[i], rot[j]))

    e0 = frame(psi)
    loop0 = circulation(psi, 0, 1, 2)
    assert np.linalg.matrix_rank(e0) == 4
    assert np.linalg.norm(loop0) > 1e-7
    g0 = imposed_metric(e0)
    g_alternative = imposed_metric(frame(psi, (2, 3, 4, 5)))
    assert np.linalg.norm(g0 - g_alternative) > 1e-7
    assert sum(np.linalg.eigvalsh(g0) < 0) == 1

    # Evolve the SAME bi-octonionic Hamiltonian, do not prescribe e(t).
    psi1, p1, trace = model.evolve(psi, momentum, dt=.01, steps=12)
    e1 = frame(psi1)
    loop1 = circulation(psi1, 0, 1, 2)
    assert np.linalg.norm(e1-e0) > 1e-8
    assert np.linalg.norm(loop1-loop0) > 1e-8
    drift = max(abs(trace - trace[0])) / abs(trace[0])
    assert drift < 1e-3

    # Model-specific linear response: E8 root term only shifts all 16 masses.
    original = GraphHamiltonian()
    zeros = np.zeros((original.n, 16))
    predicted = original.mu2 + 60 * original.eps / original.f**2
    h = 1e-5
    for a in (0, 1, 8, 15):
        v = zeros.copy()
        v[0, a] = h
        gp = original.potential_and_gradient(v)[1][0, a]
        v[0, a] = -h
        gm = original.potential_and_gradient(v)[1][0, a]
        hessian_onsite = (gp - gm)/(2*h) - 2*original.K
        assert abs(hessian_onsite-predicted) < 1e-8

    print("POM-1 model diagnostic (NOT a derivation of gravity)")
    print("Candidate edge coframe rank:", np.linalg.matrix_rank(e0))
    print("Candidate edge coframe determinant:", float(np.linalg.det(e0)))
    print("Initial plaquette circulation norm:", float(np.linalg.norm(loop0)))
    print("After dynamics circulation norm:", float(np.linalg.norm(loop1)))
    print("Change of edge current frame:", float(np.linalg.norm(e1 - e0)))
    print("Ambiguity of metric under internal projection:", float(np.linalg.norm(g0 - g_alternative)))
    print("Ground state J and loop proxy: identically zero")
    print("Onsite 16-mode Hessian mass²:", predicted)
    print("Energy relative drift:", float(drift))
    print("CRUCIAL: physical tetrad, Lorentzian signature, spin connection and TEGR action were NOT derived.")


if __name__ == "__main__":
    main()
