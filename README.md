# POM-1 — Próżnia jako Ocean Możliwości

**Bioktoniony · E₈ · emergentna geometria · teleparalelizm**

Repozytorium projektu badawczego POM-1, poświęconego wyłącznie bioktonionom, geometrii E₈, emergencji czasoprzestrzeni i teleparalelizmowi.

## Cel

Sprawdzić, czy z jednej, dokładnie zdefiniowanej mikroskopowej struktury stanów
i relacji przyczynowych można wyprowadzić efektywną geometrię czasoprzestrzeni,
dynamikę pól oraz mierzalne przewidywania.

**Status: hipoteza badawcza, nie potwierdzona teoria fizyczna.** Formalne dowody
w Lean potwierdzają konkretne twierdzenia matematyczne o zdefiniowanych
strukturach; nie są dowodem istnienia fizycznego „oceanu próżni”.

## Organizacja

- `POM1/E8Roots.lean` — enumeracja pierwiastków E₈, dokładne tożsamości i potencjał.
- `POM1.lean` — moduł główny biblioteki Lean.
- `Theory/Model.md` — założenia, mikroskopowy hamiltonian i granica efektywna.
- `Theory/ProofObligations.md` — otwarte zadania dowodowe i fizyczne.
- `Theory/EmergenceBridge.md` — krytyczny test wyprowadzania geometrii z sieci.
- `Research/PriorArt.md` — recenzowana literatura; **bez dublowania znanych dowodów**.
- `.github/workflows/lean.yml` — niezależna kompilacja i kontrola dowodów Lean 4.
- `POM1/README.md` — zakres formalizacji i jej ograniczenia.
- `Simulations/pom1_model.py` — numeryczny demonstrator bioktonionowego hamiltonianu.
- `Simulations/README.md` — instrukcja uruchomienia i interpretacja testów.

## Matematyczne fakty wyjściowe

Dla 240 pierwiastków układu E₈ w standardowej normalizacji `‖α‖² = 2`:

```text
∑_(α ∈ Φ(E₈)) αᵢ αⱼ = 60 δᵢⱼ
```

Rozpatrywany jest nieujemny potencjał cosinusowy oparty na tej
konkretnej rodzinie pierwiastków. Wokół zera jego kwadratowa część
jest izotropowa, co **nie** wybiera automatycznie lekkiego modu próżni.

## Uruchomienie formalizacji

Wymaga `elan` / Lean 4 i mathlib (wersje określone w repozytorium).

```bash
lake update
lake exe cache get
lake build
```

Symulację numeryczną można uruchomić poleceniami:

```bash
python -m pip install -r Simulations/requirements.txt
python Simulations/pom1_model.py
python Simulations/emergent_geometry_probe.py
```

Wyniki kompilacji Lean i testów Pythona sprawdzaj w zakładce **Actions**. 
W części skończonych certyfikatów użyto `native_decide`, co polega na zaufaniu
do kompilatora Lean; docelowo chcemy przejść na małe dowody kernelowe.

## Co NIE zostało wyprowadzone

Brakuje przede wszystkim wyprowadzenia 3+1-wymiarowej geometrii Lorentza,
lokalnych tetrad i skalaru torzji z dynamiki sieci, a także Modelu
Standardowego, uwięzienia koloru i obserwacyjnie dopasowanego ciemnego sektora.

Wszystkie te zagadnienia pozostają jawnymi zadaniami, nie twierdzeniami.


## POM-2: faza uporządkowana i degeneracja rangi

- [Teoria i wyniki](Theory/OrderedVacuum.md): zmodyfikowany hamiltonian, dokładne dolne ograniczenie energii i otwarte ograniczenia.
- [Formalne twierdzenia Lean](POM1/FrustratedSpectrum.lean): specyficzne dla POM-2 formy kwadratowe K3/K5 i dolna granica energii.
- [Eksperyment Python](Simulations/ordered_phase_probe.py): przeciwne chiralności i dwa równoważne energetycznie stany rangi 2 i 4.

Ranga 4 w przestrzeni stanów NIE oznacza wyprowadzenia fizycznej tetrady czy sygnatury Lorentza.


## POM-3 (eksperymentalna gałąź): próżnia sektorów bikwaternionowych

**Nowy postulat:** bioktonionowy stan próżni nie jest tetradą ani cząstką.
Dla generycznego stanu x+Iy wybiera z własnych części urojonych lokalną
podalgebrę kwaternionową H, a wzbudzenia można opisywać w C⊗H.

- [Theory/BiquaternionSectorVacuum.md](Theory/BiquaternionSectorVacuum.md) — pełna definicja, ścisły warunek minimum, ograniczenia fizyczne i literatura.
- [POM1/SectorVacuum.lean](POM1/SectorVacuum.lean) — dowody specyficznego dla POM-3 potencjału, nie dowody znanego twierdzenia Artina.
- [Simulations/sector_vacuum_probe.py](Simulations/sector_vacuum_probe.py) — wybór sektora z x,y, norma Minkowskiego, U(1) i Hessian.
- [Research/PriorArt.md](Research/PriorArt.md) — recenzowane wyniki, których **nie powielamy**.

**Ostrzeżenie:** czterowymiarowy wycinek z normą Lorentza jest przestrzenią
wewnętrzną. Fizyczna czasoprzestrzeń, czas, tetrady i TEGR nie są jeszcze wyprowadzone.


## POM-4 — stabilność wzorców EM–GR (gałąź eksperymentalna)

Bikwaternionowa algebra C⊗H pozwala reprezentować sektory spinorowe oraz bosonowe operatory, ale nie przypisuje automatycznie statystyki fermionowej. Model POM-4 testuje *fenomenologiczną* zmianę lokalnych minimów energii wzorca przy zmianie niezmienników pola EM i skalaru torzji GR.

- [Theory/EMGRMetastablePatterns.md](Theory/EMGRMetastablePatterns.md) — ścisła analiza fazowa i ograniczenia fizyczne.
- [POM1/CoupledMetastability.lean](POM1/CoupledMetastability.lean) — model-specyficzne algebraiczne certyfikaty potencjału i jego barier.
- [Simulations/emgr_metastability_probe.py](Simulations/emgr_metastability_probe.py) — testy sprzężenia, CAR i 441 punktów diagramu fazowego.

Nie wyprowadzono jeszcze spektrum znanych cząstek, czasu ich życia, elektromagnetyzmu i grawitacji z mikrosieci.


## POM-5 — Rac/Di and Flato–Fronsdal channels (draft)

**Research target:** can a bi-octonion-selected biquaternion sector support a locally transported two-mode oscillator Fock representation, from which published Rac/Di tensor-product rules can be *applied*? The theorem itself is known and is NOT re-proven.

- [Theory/SingletonChannelBridge.md](Theory/SingletonChannelBridge.md) — reviewed SO(3,2) singleton rules, admissible bosonic/fermionic towers, representation vs physical production, exact limitations.
- [POM1/SingletonSectorSelection.lean](POM1/SingletonSectorSelection.lean) — POM-5-specific parity selection constraints, not an alternative to Flato–Fronsdal.
- [Simulations/singleton_channel_probe.py](Simulations/singleton_channel_probe.py) — finite-truncation pair excitation and hopping between Rac-like/Di-like parity sectors.
- [Simulations/singleton_sector_transport.py](Simulations/singleton_sector_transport.py) — **postulated** compact SU2 intersector transport from the state-selected quaternion frames.
- [Research/PriorArt.md](Research/PriorArt.md) — peer-reviewed prior theorems and variations.

**Do not conflate:** a finite biquaternion M2(C), the infinite-dimensional Rac/Di singleton Hilbert spaces, actual fermionic CAR, an AdS4 physical vacuum, or photon/electron creation. All these are distinct obligations.


## POM-6 — spectral/topological test (draft)

POM-6 asks a more directly falsifiable question than the singleton-label program: can the **quaternionic-sector projectors selected in POM-3** determine a selfadjoint graph Dirac operator, with distinct fermionic low-energy and bosonic collective modes?

- [Theory/SpectralTopologicalBridge.md](Theory/SpectralTopologicalBridge.md) — the exact POM-specific overlap coupling, 1D test results and physical limitations.
- [POM1/SpectralLink.lean](POM1/SpectralLink.lean) — projector-overlap and gap-contrast identities. Known SSH index theorems are **not** re-proven.
- [Simulations/spectral_topological_probe.py](Simulations/spectral_topological_probe.py) — numerical topological/trivial chain, SU2 spin-frame overlap and gauge-covariance checks.
- [Research/PriorArt.md](Research/PriorArt.md) — Su–Schrieffer–Heeger, Ryu–Hatsugai, Teo–Kane, Connes–Chamseddine and Nielsen–Ninomiya.

**Scope warning:** dimerization, one-dimensional graph and the SU2 lift are chosen for the toy test. No 3+1 Lorentz geometry, physical fermionic statistics, Maxwell photons, E8 particle assignments or teleparallel torsion have been derived.


## POM-6 — necessary topology warning

[POM-6 vacuum topology audit](Theory/VacuumTopologyAudit.md) compares the **full** POM-3 order-parameter manifold \(V_2(\mathbb R^7)\) to the quotient \(G_2/SO(4)\) of quaternionic sectors. Their \(\pi_2\) differs, so the quotient's possible \(\mathbb Z_2\) point-defect charge does not automatically protect an actual full bi-octonion vacuum configuration. Published homotopy facts are cited rather than reproved.


## POM-7 — can the bi-octonion vacuum select its own coupling pattern?

This draft extends POM-6 with a CONDITIONAL mechanism for spontaneous
sector ordering; it does not silently import an already alternating chain.

- [Theory/SpontaneousSectorOrdering.md](Theory/SpontaneousSectorOrdering.md):
  no-dimerization result for the old positive-link H3, known ANNNI
  frustration, exact finite energy tests, and the limitation caused by
  additional quaternion sector orientations.
- [POM1/SpontaneousOrdering.lean](POM1/SpontaneousOrdering.lean):
  model-specific projector overlaps and a counterexample to the
  prior A/B sector-selection assumption. The published general ANNNI
  ground-state theorem and SSH bulk-edge theorem are not re-proven.
- [Simulations/spontaneous_ordering_probe.py](Simulations/spontaneous_ordering_probe.py):
  exact enumeration of 8 and 12 sector-label configurations, dynamic
  programming for 40, projector-derived spectral phases and finite-T check.
- [Simulations/continuous_sector_frustration.py](Simulations/continuous_sector_frustration.py):
  rational Cayley–Dickson counterexample and restricted continuous
  orientation minimization.

**Limit:** 1D graph, nearest/next-nearest energy and binary sector
restriction are still assumed. Topological edge states appear only
for a boundary termination selected relative to the ordered phase.
No physical 3+1D matter or TEGR is derived.


## POM-8 — pełna ciągła przestrzeń sektorów próżni (robocze)

Wariant POM-8 usuwa *binarne* ograniczenie A/B z POM-7 i testuje na
zadanym pierścieniu pełną lokalną rozmaitość V₂(R⁷) bioktonionowych minimów V3.
Wynik dla N=8: znaleziony niedimerowy stan ma energię około −12.875806,
poniżej najlepszego znalezionego stanu okresu czterech (−12).
Istnieje także **dokładny wymierny kontrprzykład** z energią −12.092447…,
sprawdzony w Lean 4. Obliczenia pozostają warunkowe względem założonego grafu.

- [Theory/FullVacuumOrderAudit.md](Theory/FullVacuumOrderAudit.md) — wyprowadzenie, dokładny certyfikat, optymalizacja i ograniczenia.
- [POM1/FullVacuumCounterexample.lean](POM1/FullVacuumCounterexample.lean) — ośmiowęzłowa wymierna konfiguracja oktonionowa, kontrola ortonormalności i ścisła nierówność energii.
- [Simulations/full_vacuum_ordering_probe.py](Simulations/full_vacuum_ordering_probe.py) — pełne orientacje, gradient analityczny, dokładny rachunek Fraction, gamma i widmo.
- [Research/PriorArt.md](Research/PriorArt.md) — już opublikowane wyniki o helisach w sfrustrowanych układach; bez ich dublowania.

**Nie jest to powstanie elektronów ani teleparalizmu.** Nie wyprowadzono
grafu 3+1, dynamiki Lorentza, transportu spinorowego czy działania TEGR.


## POM-9 — Planck phase, number theory and continued fractions (experimental)

The quantum scale is Planck's constant h in the **dimensionless**
magnetic flux alpha=e*Phi/h, NOT a claim that h is a Fibonacci number.
The golden-ratio convergents 3/5,5/8,8/13,13/21,21/34 were tested
in a known Hofstadter model with link magnitudes computed from
POM-3 quaternion projector overlaps (qAB=5/8). The 2D lattice,
external magnetic flux, Fibonacci sector word and coupling law are
postulates; none is generated by the microscopic POM Hamiltonian.

- [Theory/PlanckContinuedFractions.md](Theory/PlanckContinuedFractions.md) — formulas, 25x25 sampled gaps, conservative mesh-to-continuum estimates and control tests.
- [POM1/FibonacciFluxLinks.lean](POM1/FibonacciFluxLinks.lean) — model-specific exact bond strengths and finite weak-bond counts, not a duplicate proof of number theory.
- [Simulations/fibonacci_planck_flux.py](Simulations/fibonacci_planck_flux.py) — POM-modulated Hofstadter gaps, FHS Chern and silver-ratio/uniform-bond negative controls.
- [Research/PriorArt.md](Research/PriorArt.md) — Hofstadter, TKNN, FHS, Kraus–Zilberberg, Jitomirskaya–Liu; prior theorems are cited rather than re-proven.

No physical stability of particles, Planck-length graph, EM or TEGR
has been derived from POM.


## POM-10 — self-selected closed loop and irrational Berry phase (DRAFT)

This is a CONDITIONAL mathematical extension, not a consequence of the
original POM-3/8/9 Hamiltonians. In a toy with three POSSIBLE vertices
and dynamic Boolean edges, a new chiral triangle interaction makes a
complete loop strictly favorable: exact ground energy -11/2 versus
a lower bound -21/4 for any incomplete graph. The chiral vacua have
χ=±4/5 and produce a gauge-invariant Berry phase ±atan(1/2), whose
ratio to 2π is irrational by the published Niven theorem (reused
from mathlib). No external Peierls magnetic field is supplied.

- [Theory/SelfGeneratedIrrationalFlux.md](Theory/SelfGeneratedIrrationalFlux.md) — exact assumptions, energy proof, Berry phase, spectrum and physical limitations.
- [POM1/SelfGeneratedFlux.lean](POM1/SelfGeneratedFlux.lean) — original conditional algebra, reusing Niven rather than reproving it.
- [Simulations/self_generated_flux_probe.py](Simulations/self_generated_flux_probe.py) — octonion witnesses, 3-edge graph enumeration, finite-loop level spacings and an OPTIONAL 2D QWZ spectral response.
- [Research/PriorArt.md](Research/PriorArt.md) — reviewed work on octonion calibration, Berry loop phases, chiral order, QWZ, and zero-field Chern insulators.

**Caveat:** the 2D kinetic QWZ model and coupling m=χ are STILL
ASSUMED; the 3-node graph does not itself have a 2D bulk Chern band.
This construction works inside a common quaternion H, therefore
octonions are not yet demonstrably necessary.


## POM-11 — Exact spectral gap of the SAME self-selected triangle

POM-11 removes the need for the separately postulated QWZ 2D operator when verifying a *finite* spectral gap for the closed 3-node chiral loop from POM-10. Exact rational link invariants determine its cubic characteristic polynomial; Lean proves root ordering, an exact lower gap >47/100, and a conditional robustness margin >7/100 under Hermitian operator perturbations of norm <=1/5. Known general Weyl results are cited, not reproved.

- [Theory/ExactLoopSpectrum.md](Theory/ExactLoopSpectrum.md) — full mathematical derivation and scope limits
- [POM1/LoopSpectrum.lean](POM1/LoopSpectrum.lean) — Lean polynomial roots and quantitative gap
- [Simulations/exact_loop_spectrum.py](Simulations/exact_loop_spectrum.py) — exact Gaussian-rational matrix invariants, local gauge tests, perturbation samples

The result remains a finite graph spacing, NOT an electron, a 2D topological band or TEGR.
