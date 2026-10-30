"""POM-4: environmental switching of stable/metastable patterns.

The scalar Landau potential is a phenomenological toy model.
EM/GR environments are background invariant proxies, not fields derived
from the bi-octonionic microscopic network.
Spin-statistics (Pauli), solitons (Coleman), and Jackiw-Rebbi modes
are established prior art, not discoveries of POM-4.
"""
import math
import numpy as np
from pom1_model import qmul


def em_invariant_proxy(E, B):
    """Nonnegative combination of the two familiar EM Lorentz invariants.
    c=1; inputs assumed appropriately normalized. Null plane waves score zero.
    """
    E, B = np.asarray(E, dtype=float), np.asarray(B, dtype=float)
    I = float(B@B - E@E)
    J = float(2*E@B)
    return I**2 + J**2


def normalized_fields(E, B, torsion_scalar):
    ie = em_invariant_proxy(E, B)
    ig = float(torsion_scalar)**2
    return ie/(1+ie), ig/(1+ig)


def coupled_a(em, gr):
    return 1/4 - 5*em/48 + gr/16 + em*gr/64


def potential(a, s):
    return a*s - s*s + s*s*s


def slope(a, s):
    return a - 2*s + 3*s*s


def curvature(s):
    return -2 + 6*s


def stationary_radii(a):
    disc = 1-3*a
    if disc < 0:
        return None
    d=math.sqrt(max(0,disc))
    return (1-d)/3, (1+d)/3


def phase(a, eps=1e-12):
    if a <= 0:
        return "zero-unstable"
    if a > 1/3+eps:
        return "zero-only"
    if abs(a-1/3) <= eps:
        return "spinodal"
    if a < 1/4-eps:
        return "ordered-global-zero-metastable"
    if abs(a-1/4) <= eps:
        return "coexistence"
    return "zero-global-ordered-metastable"


def local_values(a):
    roots=stationary_radii(a)
    if roots is None:
        return None
    s_minus, s_plus=roots
    return dict(s_barrier=s_minus,s_ordered=s_plus,
                energy_barrier=potential(a,s_minus),
                energy_ordered=potential(a,s_plus),
                curvature_barrier=curvature(s_minus),
                curvature_ordered=curvature(s_plus))


SIGMA = [
    np.array([[0,1],[1,0]],dtype=complex),
    np.array([[0,-1j],[1j,0]],dtype=complex),
    np.array([[1,0],[0,-1]],dtype=complex),
]
I2=np.eye(2,dtype=complex)


def biquaternion_matrix(q):
    """Isomorphism C⊗H -> M2(C) in fixed local associative sector."""
    return q[0]*I2 - 1j*sum((q[i+1]*SIGMA[i] for i in range(3)))


def anti(a,b):
    return a@b + b@a


def test_car_and_matrix_model():
    rng=np.random.default_rng(20261031)
    for _ in range(20):
        u=rng.normal(size=4)+1j*rng.normal(size=4)
        v=rng.normal(size=4)+1j*rng.normal(size=4)
        assert np.allclose(biquaternion_matrix(qmul(u,v)),
                           biquaternion_matrix(u)@biquaternion_matrix(v))
    # A spinor is an element of a chosen left module C^2;
    # fermion parity / CAR are added as quantization data, NOT inferred
    # merely from the associative algebra of complex quaternions.
    c=np.array([[0,1],[0,0]],dtype=complex)
    Z=np.diag([1,-1])
    f0=np.kron(c,I2)
    f1=np.kron(Z,c)
    I4=np.eye(4,dtype=complex)
    assert np.allclose(anti(f0,f0.conj().T),I4)
    assert np.allclose(anti(f1,f1.conj().T),I4)
    assert np.allclose(anti(f0,f1),0)
    assert np.allclose(anti(f0,f1.conj().T),0)
    n0=f0.conj().T@f0
    n1=f1.conj().T@f1
    assert np.allclose(n0@n1 - n1@n0,0)
    # Bilinear even observables do not by themselves imply
    # an elementary massless spin-1 boson.


def verify_bistable_examples():
    examples=[(1.,0.,7/48,7/12,-49/864,5/864,
               "ordered-global-zero-metastable"),
              (0.,0.,1/4,1/2,0.,1/54,"coexistence"),
              (0.,1.,5/16,5/12,25/864,1/32,
               "zero-global-ordered-metastable")]
    for em,gr,aa,root,Vordered,Vbarrier,phase_name in examples:
        a=coupled_a(em,gr)
        assert np.isclose(a,aa)
        assert phase(a)==phase_name
        d=local_values(a)
        assert np.isclose(d["s_ordered"],root)
        assert np.isclose(d["energy_ordered"],Vordered)
        assert np.isclose(d["energy_barrier"],Vbarrier)
        assert d["curvature_barrier"]<0<d["curvature_ordered"]
        assert np.isclose(slope(a,d["s_barrier"]),0)
        assert np.isclose(slope(a,d["s_ordered"]),0)
    # The phase boundary is analytic, not fitted:
    # 12*gr + 3*em*gr == 20*em.
    for em in np.linspace(0,12/17,20):
        gr=20*em/(3*(4+em))
        assert np.isclose(coupled_a(em,gr),.25,atol=1e-13)
    for em in np.linspace(0,1,21):
        for gr in np.linspace(0,1,21):
            a=coupled_a(em,gr)
            assert 0<a<1/3
            d=local_values(a)
            assert d is not None
            assert d["curvature_barrier"]<0<d["curvature_ordered"]
            assert (d["energy_ordered"]<0)==(a<.25)
    # EM null field: local electromagnetic scalar invariants vanish,
    # even though a propagating electromagnetic wave may be present.
    null_em=em_invariant_proxy([1,0,0],[0,1,0])
    assert np.isclose(null_em,0)
    return examples


def main():
    test_car_and_matrix_model()
    examples=verify_bistable_examples()
    print("POM-4: M2(C) biquaternion representation and two-mode CAR PASS")
    print("POM-4: mixed EM-GR coupling / 441-grid-point phase diagram PASS")
    print("POM-4: exact three phase examples:")
    for e,g,a,r,ener,bar,state in examples:
        print(f"  em={e:g}, gr={g:g}, a={a:.9g}, s+={r:.9g}, "
              f"V+={ener:.9g}, barrierV={bar:.9g}: {state}")
    print("POM-4: local EM scalar proxies do not detect a null EM wave.")
    print("LIMITATIONS: no fermionic bound state, gauge dynamics, universal")
    print("equivalence principle, tetrads, lifetime or physical particle derived.")


if __name__=="__main__":
    main()
