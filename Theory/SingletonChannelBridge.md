# POM-5 — Dirac singletons Rac/Di as a conditional channel mechanism

**Status (2026-10-31):** experimental, theory-first, no identification with observed elementary particles. The 1978 Flato–Fronsdal theorem and later published generalizations are **cited, not re-proved**. Model-specific selection and transport hypotheses are separately tested in Lean 4 and Python.

## 1. What is firmly known and not new to POM

For the 4D anti-de Sitter isometry algebra so(3,2) ≅ sp(4,R), positive-energy singletons are

\[
\mathrm{Rac}=D(\tfrac12,0),\qquad\mathrm{Di}=D(1,\tfrac12).
\]

Published, **un-symmetrized** tensor-product decompositions:

\[
\begin{aligned}
\mathrm{Rac}\otimes\mathrm{Rac}
 &= \bigoplus_{s=0}^{\infty}D(s+1,s),\\
\mathrm{Di}\otimes\mathrm{Di}
 &=D(2,0)\oplus\bigoplus_{s=1}^{\infty}D(s+1,s),\\
\mathrm{Rac}\otimes\mathrm{Di}
 &=\bigoplus_{n=0}^{\infty}D(n+\tfrac32,n+\tfrac12).
\end{aligned}
\]

These are **representation-content identities, not dynamical particle production**.

The scalar \(D(1,0)\) and \(D(2,0)\) are different AdS4 scalar boundary-condition/lowest-weight representations, and the latter is not an additional massless spin-1 vector. For identical scalar singleton channels, symmetric/antisymmetric projections restrict integer spins (even/odd respectively). The full spin-1 tower should **not** be interpreted as an automatic photon from identical real Rac fields without the required internal factors.

Main sources:
- Flato and Fronsdal, *One massless particle equals two Dirac singletons*, Lett. Math. Phys. **2** (1978) 421–426, DOI [10.1007/BF00400170](https://doi.org/10.1007/BF00400170).
- Angelopoulos, Flato, Fronsdal, Sternheimer, *Massless particles, conformal group, and de Sitter universe*, Phys. Rev. D **23** (1981) 1278, DOI [10.1103/PhysRevD.23.1278](https://doi.org/10.1103/PhysRevD.23.1278).
- Pang, Sezgin, Zhu, *One-loop tests of the supersymmetric higher spin AdS4/CFT3 correspondence*, Phys. Rev. D **95** (2017) 026008, DOI [10.1103/PhysRevD.95.026008](https://doi.org/10.1103/PhysRevD.95.026008).
- Basile, Bekaert, Joung, *Twisted Flato–Fronsdal theorem for higher-spin algebras*, JHEP 07 (2018) 009, DOI [10.1007/JHEP07(2018)009](https://doi.org/10.1007/JHEP07(2018)009).

### Variations: distinct established constructions

1. **Rac ⊕ Di as a supersingleton of osp(1|4)**: well studied in Fronsdal, *Dirac supermultiplet*, Phys. Rev. D **26** (1982) 1988, DOI [10.1103/PhysRevD.26.1988](https://doi.org/10.1103/PhysRevD.26.1988). A grading-changing supercharge must be part of the algebra, not merely assumed from the presence of two sectors.
2. **Higher-order Rac and Di**: published generalized tensor products yield partly-massless fields. Higher-order representations can be nonunitary and do not automatically describe stable particles; Basile, Bekaert, Boulanger, JHEP 11 (2014) 131, DOI [10.1007/JHEP11(2014)131](https://doi.org/10.1007/JHEP11(2014)131).
3. **Higher-rank/multiple singleton products**: published work treats more than two Fock-singleton factors and higher-spin currents; Gelfond, Vasiliev, JHEP 10 (2016) 067, DOI [10.1007/JHEP10(2016)067](https://doi.org/10.1007/JHEP10(2016)067).
4. **Internal multiplicities and type A/B/AB**: different singlet projections and internal symmetry labels change which spin channels actually occur. A tensor-product tower alone does not show a realistic particle spectrum.

## 2. The sharp distinction: finite local biquaternions vs singleton Hilbert spaces

The POM-3 vacuum selects a local quaternionic algebra \(\mathbb H_i\) and its complexification

\[
\mathbb Q_i=\mathbb C\otimes\mathbb H_i\simeq M_2(\mathbb C).
\]

The natural left module is \(\mathbb C^2\), **not** a Rac or Di singleton. The latter require an infinite-dimensional unitary positive-energy representation of the noncompact group Sp(4,R).

A two-bosonic-mode oscillator Fock space gives an **already known** realization:

\[
\mathcal F_i=\mathcal F(\mathbb C^2),\quad
[a_{i\alpha},a^\dagger_{j\beta}]=\delta_{ij}\delta_{\alpha\beta},\quad
N_i=\sum_{\alpha=1}^2 a^\dagger_{i\alpha}a_{i\alpha}.
\]

The operators quadratic in the oscillators realize sp(4,R); even total occupation \((-1)^{N_i}=+1\) is Rac, odd is Di. The lowest energies and spins are
\(E_{\rm Rac}=\tfrac12,\ j_{\rm Rac}=0\) and \(E_{\rm Di}=1,\ j_{\rm Di}=\tfrac12\).

This is *not* proved by POM-5; see Basile–Bekaert–Joung (2018). A **new and still unproved map**

\[
\boxed{\Psi_i\ \longmapsto\ (\mathcal F_i,\text{CCR},\text{local Sp(4,R) generators})}
\]

must be obtained dynamically. Using a finite local matrix algebra as if it itself satisfied exact CCR would be incorrect: the trace of any finite-dimensional commutator vanishes whereas the trace of the identity is nonzero. The finite cutoff in our Python test is a diagnostic, **not** an exact singleton.

Also: Di is a spinor representation, but **odd parity of bosonic oscillator number alone does not establish physical fermionic CAR statistics**. Physical spin/statistics and the relevant superselection rules require a separate QFT construction.

## 3. The specific POM-5 graph model: two sites and transport

Assume two local fibers \(\mathcal F_i,\mathcal F_j\), potentially arising from differently oriented local quaternionic sectors. A common diagonal Sp(4,R) representation across sites requires an **intertwiner**; taking a tensor product of unrelated local modules without a common group action does not invoke Flato–Fronsdal.

As a first *postulate*, a number-preserving link and an even pair source are

\[
\begin{aligned}
H_{\rm link}&=-t\sum_{\alpha}
(a^\dagger_{i\alpha}a_{j\alpha}+a^\dagger_{j\alpha}a_{i\alpha}),\\
H_{\rm pair}&=\kappa(\mathcal I_{\rm EM},\mathcal I_{\rm GR})
\sum_{\alpha}
(a^\dagger_{i\alpha}a^\dagger_{j\alpha}
+a_{i\alpha}a_{j\alpha}).
\end{aligned}
\]

The link above uses an **identified oscillator basis**; a model with varying \(\mathbb H_i\) needs an additional unitary transport matrix \(U_{ij}\). The function \(\kappa\) is **not** derived from E8 or teleparallel gravity. It is a controlled proxy for potential environmental dependence.

The parity operator \(\Pi=(-1)^{N_i+N_j}\) commutes with each of these quadratic terms. This implies the model-specific rules:

- Even–even initial sectors can become odd–odd under hopping or pair excitation; the *total* parity is unchanged.
- A single mixed even–odd Rac⊗Di sector has odd global parity, and cannot arise from a globally even vacuum under a parity-even Hamiltonian.
- An initially empty state is unaffected by number-conserving hopping; a pair source can populate odd–odd local sectors.
- A physically fermionic bulk field in the mixed Rac⊗Di tower therefore needs a suitable parity-odd initial source/sector or more elaborate supermultiplet coupling; the elementary source cannot be inferred from an EM/GR scalar invariant alone.

This parity bookkeeping is *specific to the proposed coupling*. We do not re-prove the metaplectic construction, the Flato–Fronsdal theorem, or the physical spin–statistics theorem. See POM1/SingletonSectorSelection.lean.

**Important limitation:** an odd–odd pair of bosonic-oscillator Fock sectors is *not* evidence of actual production of physical fermion pairs. The relevant quantum field/BRST constraints have not been built.

## 4. A candidate internal geometric transport, still not a physical connection

From a nondegenerate POM-3 vacuum state \(\Psi_i\), an oriented imaginary quaternionic frame \(B_i^{(3)}\in\mathbb R^{7\times3}\) is determined. For neighboring frames use the overlap \(M_{ji}=B_j^\top B_i\), and **postulate** its closest orientation-preserving orthogonal matrix

\[
R_{ji}=\operatorname{polar}_{SO(3)}(M_{ji})\in SO(3).
\]

It has a double-valued spin lift \(U_{ji}\in SU(2)\), which can act on the two oscillator channels. This is a natural **candidate selected by overlap geometry**, not a derivation of the connection from the Hamiltonian. It is only the compact rotation subgroup, not the noncompact Sp(4,R), SL(2,C), or the flat teleparallel spin connection. Loop holonomy does not by itself prove gravitational curvature/torsion.

Reproducible experiment: Simulations/singleton_sector_transport.py.

## 5. Relation to the POM-4 EM/GR stability potential

POM-4 already defines a **phenomenological** parameter \(a(E,G)\) and a potential \(V(s)=a s-s^2+s^3\), which determines whether a *field pattern* is stable or metastable. It does not assign actual fermionic lifetimes.

POM-5 adds a separate optional pair source \(\kappa(E,G)\). Its numerical value is freely specified in the present toy model. A field may modify the *occupation probabilities* and the *relative pattern energies*, but these are different observables:

- Pattern stability: local Hessian and barriers of \(V(s;E,G)\).
- Representation eligibility: spin/energy modules of SO(3,2), if a common action exists.
- Dynamical production: nonzero matrix elements of \(H_{\rm pair}\), proper initial state and evolution.
- Actual fermionic or bosonic particles: canonical statistics, normalizability, gauge constraints and physically correct propagation.

Without these independent checks, a tensor product is not a prediction of a creation rate or lifetime.

## 6. The AdS versus observed-cosmology gap

The identities are stated for the 4-dimensional **anti-de Sitter group** SO(3,2), with a curvature radius and a negative cosmological constant. The POM-3 internal Minkowski-signature 1+3 slice does not supply this group. Nor does a teleparallel description of our late-time expanding universe automatically give a global AdS4 vacuum.

For POM one must either **derive an AdS4-effective phase** with a common SO(3,2) action, or find a rigorous contraction/alternative. Importing AdS4 singleton spectra without this step is not a derivation of the observed photon, electron, or graviton.

## 7. New mathematical checks and open physical obligations

**Implemented:** finite-truncation Fock sanity checks, global-parity-preserving pair and hopping transitions, the *absence* of mixed Rac–Di probability from an even initial sector, and SU2 internal-sector transport. The Lean module certifies arithmetic consequences of the proposed parity selection rule only.

**Unproved:** originating canonical CCR from the POM-3 bi-octonionic Hamiltonian, local or global Sp(4,R), AdS4 curvature, gauge-invariant composite operators, physical fermionic CAR, exact intersite dynamics, realistic EM/GR pair production, mass stability, and reduction to Maxwell/TEGR.

### Explicit STOP criterion

If no shared positive-energy Sp(4,R) action can be generated, the names Rac/Di label **analogous parity sectors only**. The exact Flato–Fronsdal theorem cannot be applied to the POM graph and no physical massless field has been derived.
