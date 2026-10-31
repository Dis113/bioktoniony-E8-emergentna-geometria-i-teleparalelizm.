"""POM-8: FULL continuous POM-3 vacuum-manifold optimization and exact witness.

This is not a 3+1 spacetime derivation, not QCD or TEGR.
Onsite V3 is minimized exactly by x=amp*u, y=amp*v, u,v orthonormal
imaginary octonions. The 11-dimensional local Stiefel manifold V_2(R7)
is sampled *without* preselecting two quaternion sectors.

The graph topology (periodic 1D n-site ring), projector frustration and
spectral hopping rule are POSTULATED. ANNNI and SSH are published prior art.
Lean independently verifies one specific finite rational ring inequality.

Results are numerical local optima unless labeled EXACT.
"""
from __future__ import annotations

from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize
from pom1_model import omul, bioassociator

EYE = np.eye(8)
# Imaginary Cayley-Dickson octonion structure constants C_{ab}^c
C = np.stack([omul(EYE[i], EYE[j])[1:]
              for i in range(1, 8) for j in range(1, 8)]).reshape(7, 7, 7)
assert np.allclose(C, np.rint(C))


def frames(values):
    """Turn each unrestricted pair of raw 7-vectors into an orthonormal
    associative quaternionic 3-frame (u,v,uv) by Gram-Schmidt.
    """
    p = np.asarray(values, dtype=float).reshape(-1, 2, 7)
    x, y = p[:, 0], p[:, 1]
    normu = np.linalg.norm(x, axis=1, keepdims=True)
    assert np.min(normu) > 1e-7
    u = x / normu
    parallel = np.sum(u * y, axis=1, keepdims=True)
    b = y - parallel * u
    normv = np.linalg.norm(b, axis=1, keepdims=True)
    assert np.min(normv) > 1e-7
    v = b / normv
    w = np.einsum("na,nb,abc->nc", u, v, C)
    frame = np.stack([u, v, w], axis=1)
    assert np.max(abs(frame @ frame.transpose(0, 2, 1) - np.eye(3))) < 2e-10
    return frame, u, v, normu, normv, parallel, y


def overlap(f, i, j):
    m = f[i] @ f[j].T
    return (1 + np.sum(m*m)) / 4


def objective_and_gradient(x):
    """Analytic gradient of the projector-frustration energy.
    E = 16/3 sum_i [q(i,i+2)-q(i,i+1)] on a periodic ring.
    """
    f, u, v, nu, nv, parallel, rawv = frames(x)
    n = len(f)
    grad_f = np.zeros_like(f)
    energy = 0.0
    for jump, coef in ((1, -16/3), (2, 16/3)):
        for i in range(n):
            j = (i + jump) % n
            m = f[i] @ f[j].T
            energy += coef * (1 + np.sum(m*m)) / 4
            grad_f[i] += coef/2 * (m @ f[j])
            grad_f[j] += coef/2 * (m.T @ f[i])
    gu = grad_f[:, 0] + np.einsum("nc,nb,abc->na",
                                  grad_f[:, 2], v, C)
    gv = grad_f[:, 1] + np.einsum("nc,na,abc->nb",
                                  grad_f[:, 2], u, C)
    gb = (gv - np.sum(gv*v, axis=1, keepdims=True)*v) / nv
    gy = gb - np.sum(gb*u, axis=1, keepdims=True)*u
    gu -= parallel*gb + np.sum(gb*u, axis=1, keepdims=True)*rawv
    gx = (gu - np.sum(gu*u, axis=1, keepdims=True)*u) / nu
    return float(energy), np.stack([gx, gy], axis=1).ravel()


def optimize(x0, steps=400):
    return minimize(objective_and_gradient, np.asarray(x0).ravel(),
                    method="L-BFGS-B", jac=True,
                    options={"maxiter": steps, "ftol": 1e-12, "gtol": 5e-8})


def q_statistics(x):
    f, *_ = frames(x)
    q1 = np.array([overlap(f, i, (i+1) % len(f))
                   for i in range(len(f))])
    q2 = np.array([overlap(f, i, (i+2) % len(f))
                   for i in range(len(f))])
    return q1, q2


# Fixed SHORT INTEGER data, not a floating-point optimizer certificate:
# each row is an ordered pair of 7D Householder reflection normals.
# Multiplication and all resulting q-values are evaluated with Fraction.
EXACT_NORMALS = [
    ([6,0,-1,0,3,1,-2], [0,1,-1,0,-2,1,1]),
    ([2,2,1,-1,0,0,2], [0,3,0,-1,0,1,-3]),
    ([4,-1,1,1,3,-3,0], [0,4,0,1,-2,0,-3]),
    ([3,1,-1,1,-2,2,-2], [0,3,-2,0,0,3,2]),
    ([2,1,-1,1,0,3,-2], [0,7,2,-1,-1,-1,-1]),
    ([6,-1,0,0,-1,-3,2], [0,8,-1,-1,-1,0,0]),
    ([4,1,-1,0,-2,-2,2], [0,1,2,0,-1,-1,0]),
    ([5,-2,2,-1,-2,0,0], [0,5,1,1,-2,-3,1]),
]


def fraction_dot(x, y):
    return sum((a*b for a,b in zip(x,y)), F(0))


def rational_householder(z):
    vec = [F(int(t)) for t in z]
    norm = fraction_dot(vec, vec)
    assert norm > 0
    return [[F(i == j) - 2*vec[i]*vec[j]/norm
             for j in range(7)] for i in range(7)]


def rational_matrix_product(a, b):
    return [[fraction_dot(a[i],[b[k][j] for k in range(7)])
             for j in range(7)] for i in range(7)]


def exact_octonion_imag_product(u, v):
    coefficients = np.rint(C).astype(int)
    return [sum((u[i]*v[j]*int(coefficients[i,j,k])
                 for i in range(7) for j in range(7)), F(0))
            for k in range(7)]


def exact_rational_counterexample():
    """EXACT arithmetic witness: projectors from valid quaternion frames
    have ring energy strictly below -12, not a global minimum proof.
    """
    gram_frames = []
    for z1,z2 in EXACT_NORMALS:
        matrix = rational_matrix_product(rational_householder(z1),
                                          rational_householder(z2))
        u = [matrix[k][0] for k in range(7)]
        v = [matrix[k][1] for k in range(7)]
        w = exact_octonion_imag_product(u, v)
        assert fraction_dot(u,u) == fraction_dot(v,v) == fraction_dot(w,w) == 1
        assert fraction_dot(u,v) == fraction_dot(v,w) == fraction_dot(u,w) == 0
        gram_frames.append([u,v,w])
    def q(i,j):
        return (1 + sum((fraction_dot(x,y)**2
                     for x in gram_frames[i] for y in gram_frames[j]),F(0)))/4
    n = 8
    q1 = [q(i,(i+1)%n) for i in range(n)]
    q2 = [q(i,(i+2)%n) for i in range(n)]
    energy = F(16,3)*(sum(q2,F(0))-sum(q1,F(0)))
    assert energy < F(-12)
    assert -13 < energy < -12
    return energy, q1, q2


# An explicit eight-sector NON-DIMERIZED trial with extremely small
# bio-octonion associator cost after internal frame reorientation.
# The decimals are input DATA, not a proof of exact zero associators.
GAMMA_TRIAL = np.array([
[[.255063,-.802165,-.273780,-.284017,-.257596,.076359,-.252325],
 [.515184,.006906,-.060060,.518733,-.426506,.218801,.481732]],
[[-.296164,.607958,.119997,-.297109,.643308,-.027756,-.159332],
 [-.325515,-.633264,-.131302,-.643779,.127295,.054695,-.205255]],
[[.239330,-.140628,.055151,.657055,-.655350,-.241240,.022389],
 [.358629,.804679,.068522,.307130,.295178,-.079432,-.177240]],
[[-.390690,-.523677,.123387,.272846,-.631987,-.247350,.151214],
 [.399402,.351718,.055609,.576265,-.236584,-.372098,-.432630]],
[[.695022,.350730,-.183141,.011859,.290917,-.003146,-.524985],
 [.128807,.026722,-.157922,-.467155,.435753,.572575,.470955]],
[[-.159790,-.009043,.110496,.210078,-.194234,-.593273,-.726873],
 [.783327,.018915,-.302250,-.154052,.224206,.149941,-.445201]],
[[-.790316,.291565,.358259,.179908,-.033944,-.267808,.238328],
 [-.153533,-.129520,.014868,-.110440,.014479,-.491511,-.839906]],
[[.179733,-.530341,-.226344,-.380747,.011317,-.142045,-.685515],
 [.698097,-.293802,-.259399,.126605,-.260215,.401128,.338245]],
], dtype=float)


def associator_trial():
    f,*_ = frames(GAMMA_TRIAL)
    psi = np.zeros((8,16))
    amp = np.sqrt(.75/2)
    psi[:,1:8] = amp*f[:,0,:]
    psi[:,9:16] = amp*f[:,1,:]
    penalty = sum(np.linalg.norm(bioassociator(
        psi[i],psi[(i+1)%8],psi[(i+2)%8]))**2 for i in range(8))
    energy, _ = objective_and_gradient(GAMMA_TRIAL)
    assert penalty >= 0
    assert penalty < 1e-6
    assert energy+10*penalty < -12.8
    return energy, penalty, energy+10*penalty


def spectral_test(raw):
    # Repeat the eight-site optimized orientation motif five times,
    # and use the POM-6 postulated link rule on an OPEN 40-site chain.
    q1,_ = q_statistics(raw)
    repeated = np.tile(q1, 5)[:39]
    t = .1 + .9*repeated
    h = np.diag(t,1)+np.diag(t,-1)
    values,vectors = np.linalg.eigh(h)
    low = np.argsort(abs(values))[:2]
    edge = [sum(abs(vectors[:2,k])**2)+sum(abs(vectors[-2:,k])**2)
            for k in low]
    # Uniform open-chain low modes are EXTENDED, with edge occupancy
    # close to 4/40 (four measured edge sites out of forty).
    # This should not be mistaken for the localized SSH edge occupancy >0.55.
    ipr = [float(np.sum(abs(vectors[:,k])**4)) for k in low]
    assert np.max(abs(values[low])) > .05
    assert .07 < min(edge) < max(edge)+1e-8 < .13
    assert max(ipr) < .06
    return float(np.max(abs(values[low]))),float(max(edge)),float(max(ipr))


def check_gradient():
    rng = np.random.default_rng(20261031)
    sample = rng.normal(size=(8,2,7)).ravel()
    val, g = objective_and_gradient(sample)
    h = 1e-6
    for j in [0,3,11,22,35,60,87,111]:
        x1=sample.copy();x2=sample.copy()
        x1[j]+=h;x2[j]-=h
        derivative=(objective_and_gradient(x1)[0]-
                    objective_and_gradient(x2)[0])/(2*h)
        assert abs(derivative-g[j])<2e-7,(j,derivative,g[j])


def period_four_test(rng):
    def f(x):
        raw = np.tile(x.reshape(4,2,7),(2,1,1))
        val,grad=objective_and_gradient(raw)
        return val,grad.reshape(2,4,2,7).sum(axis=0).ravel()
    results=[]
    for _ in range(5):
        trial=minimize(f,rng.normal(size=4*2*7),jac=True,
                       method="L-BFGS-B",
                       options={"maxiter":250,"ftol":1e-12})
        results.append(trial.fun)
    assert min(results) <= -11.99999
    return min(results)


def run():
    check_gradient()
    certificate,q1,q2=exact_rational_counterexample()
    print("POM-8 EXACT rational 8-site energy < -12:", float(certificate))
    print("POM-8 EXACT trial q1:",np.round([float(x) for x in q1],6).tolist())
    print("POM-8 EXACT trial q2:",np.round([float(x) for x in q2],6).tolist())

    rng = np.random.default_rng(20261031)
    best8 = None
    for n,restarts in ((8,4),(12,3),(16,2)):
        energies=[]
        optima=[]
        for _ in range(restarts):
            fit = optimize(rng.normal(size=(n,2,7)),
                           steps=400)
            energies.append(fit.fun)
            optima.append(fit.x)
        k=int(np.argmin(energies))
        f,qnext,qfar=frames(optima[k])[0],*q_statistics(optima[k])
        print("POM-8 full Stiefel order N=%d, best E=%.10f, "
              "mean q1=%.8f, std q1=%.7f, mean q2=%.8f"%
              (n,energies[k],qnext.mean(),qnext.std(),qfar.mean()))
        assert np.isfinite(energies[k])
        if n==8:
            assert energies[k] < -12.80 and qnext.std() < 2e-4
            best8 = optima[k]
        if n==12: assert energies[k]<-19.
        if n==16: assert energies[k]<-25.7
    p4=period_four_test(rng)
    assert abs(p4+12)<1e-4
    print("POM-8 period-4-restricted numerical best:",p4)
    gap,edge,ipr=spectral_test(best8)
    print("POM-8 non-dimerized repeat-40 chain low mode |E|:",gap,
          "edge weight",edge,"inverse participation ratio",ipr)
    e,cost,total=associator_trial()
    print("POM-8 explicit gamma=10 trial: link E=",e,
          "associator cost=",cost,"total=",total)
    print("POM-8 RESULT: full-sector competitor defeats period-4 POM-7 trial.")
    print("LIMIT: local optimization is NOT global proof; 1D graph and")
    print("projector Hamiltonian are assumed; no fermions, EM, GR or TEGR.")


if __name__=="__main__":
    run()
