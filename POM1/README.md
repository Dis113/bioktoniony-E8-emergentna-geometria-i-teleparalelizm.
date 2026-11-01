# Formalizacja Lean POM-1

Ta biblioteka formalizuje **wyłącznie matematyczne podtwierdzenia** hipotezy
„Próżnia jako Ocean Możliwości”: bioktoniony, układ korzeniowy E₈,
emergentną geometrię i teleparalelizm.

## Moduł `E8Roots.lean`

- jawna lista 240 pierwiastków E₈ reprezentowanych przez podwojone
  całkowitoliczbowe współrzędne;
- dowód normy pierwiastków;
- tożsamość drugiego momentu `∑_α αᵢ αⱼ = 60 δᵢⱼ`;
- nieujemność zdefiniowanego potencjału cosinusowego;
- algebraiczna tożsamość dotycząca masy przy rozwinięciu kwadratowym.

**Nie ma tutaj dowodu, że E₈ opisuje próżnię fizyczną.**
Nie dowiedziono powstawania tetrad, torzji, metryki Lorentza, fermionów,
oddziaływań Modelu Standardowego ani granicy kontinuum.

## Status metody

Dwa twierdzenia o skończonej enumeracji wykorzystują `native_decide`.
Weryfikacja tych twierdzeń ufa wykonaniu skompilowanego kodu Lean; planowany
jest wariant bez tej zależności.

## Lokalna kompilacja

```sh
lake update
lake exe cache get
lake build
```

Szczegółowe warunki sukcesu: [Theory/ProofObligations.md](../Theory/ProofObligations.md).


## POM-2: progi niestabilności

Moduł FrustratedSpectrum.lean formalizuje kwadratowe formy K3/K5, ich znaki oraz dolną granicę energii dla pięciu węzłów. Parametr mE8 to jawna dana wejściowa; pełny rachunek różniczkowy E8 nie jest tutaj formalizowany. Kompilacja nie dowodzi emergencji metryki czy torzji.


## POM-3 — dynamika wyboru sektora

Moduł SectorVacuum.lean formalizuje dolną granicę i dopełnienie kwadratów
dla konkretnego potencjału modelu POM-3. Nie powiela twierdzenia Artina
ani klasyfikacji podalgebr oktonionowych.

Znany rezultat Artina jest **założonym faktem z literatury**,
potrzebnym do interpretacji Δ>0 jako wyboru H przez bioktonion.
Sama formalizacja Lean dowodzi tylko nierówności nad liczbami rzeczywistymi.


## POM-4 — exact conditional pattern potential

CoupledMetastability.lean formalizes only the **model-specific** coefficient a(E,G), a sixth-order scalar pattern potential and exact rational local extrema/energies. It does **not** reproduce Pauli spin-statistics theorem, prove physical particles, or derive the dynamical EM/GR fields.


## POM-5: singleton-sector selection, not the singleton theorem

SingletonSectorSelection.lean certifies only arithmetic parity constraints for the proposed two-site, quadratic oscillator couplings. It does not recreate the published Flato–Fronsdal decomposition or the metaplectic construction of the so(3,2) singletons. The physical existence of such oscillator Fock fibers in POM is still an unproved assumption.


## POM-6: spectral-link lemmas

The SpectralLink.lean module proves the specific rational overlap of two explicit quaternion projectors and the induced contrast of *assumed* scalar hopping amplitudes. It also shows that an everywhere identical sector gives equal hoppings and cannot dimerize using overlaps alone.

The published SSH bulk-edge theorem, Connes spectral action and Nielsen–Ninomiya no-go theorem are NOT re-proven. The result is conditional on a 1D bipartite graph, not a physical 3+1-dimensional spectral geometry.


## POM-7: sector-overlap and uniform-vacuum certificates

SpontaneousOrdering.lean (importing the already established POM1.SpectralLink
module) certifies the two-sector projector/Ising identity, a new exact
quaternion projector overlap q_AC=1/2, the lower trial energy of sector C
compared with the previously chosen sector B, and the positive-bond
constraint explaining why H3 cannot spontaneously dimerize.

Known ANNNI period-four antiphase, SSH index, and Ising phase diagrams
are cited rather than re-proved. The Lean lemmas are only finite
model-specific algebra, not 3+1D gravity or elementary particles.


## POM-8 — exact finite quaternion-sector counterexample

FullVacuumCounterexample.lean uses **eight exact rational Householder frames**
in imaginary octonion coordinates and the Cayley–Dickson cross-product
coefficient table. The theorem
`trial_full_vacuum_beats_binary_period_four` verifies a strict
model-specific inequality for the eight-site projector energy:
`E_trial < -12`. The separate theorem `trial_frame_orthonormal`
checks the eight three-dimensional imaginary bases. This is a
`native_decide`-based finite certificate (compiler trust). These
theorems do **not** prove a global minimum, republish known ANNNI
or SSH theory, or establish physical fermionic particles.


## POM-9 — finite exact Fibonacci-sector link certificates

FibonacciFluxLinks.lean imports the previously certified POM-6
qAB=5/8 and defines an ASSUMED hopping t=1+(overlap-1)/5. It proves
tAB=37/40 and tAA=1. Finite native_decide-based calculations verify
the five chosen convergents' weak-link counts 4,6,10,16,26.
This uses the compiler's native evaluator and is NOT a full kernel-
reduced certificate for those counts. General continued-fraction,
Hofstadter, TKNN and Chern theorems are NOT re-proved.


## POM-10 — conditional graph and chiral-flux bounds

SelfGeneratedFlux.lean proves POM-specific real-polynomial bounds on
closed versus open 3-edge graphs, a controlled energy-preference margin,
a known J1/J2-style rational selected cosine, and a quadratic lower
bound for the separately POSTULATED Qi-Wu-Zhang two-band response.

The octonion calibration inequality χ²≤1−c² is a hypothesis,
NOT formally reproven; a concrete octonion witness is tested
independently in Python. The irrational angle follows by invoking
the ALREADY EXISTING mathlib Niven theorem, not re-formalizing it.
No physical electromagnetic field or fermion Hilbert space is derived.


## POM-11 — LoopSpectrum proof scope

LoopSpectrum.lean proves the factorization and exact roots of the POM-specific cubic, the exact lower level spacing and its conditional perturbative margin. Gaussian-rational matrix invariants establishing the cubic as the triangle charpoly are calculated independently in Simulations/exact_loop_spectrum.py. No new proof of Weyl's general theorem or any real QFT gap is claimed.
