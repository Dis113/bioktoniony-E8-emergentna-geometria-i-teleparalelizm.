# POM-1 — model numeryczny

`pom1_model.py` jest **demonstratorem** grafowego hamiltonianu z 16
rzeczywistymi zmiennymi stanu na wierzchołek. Wykorzystuje:
- 240 pierwiastków układu E₈;
- iloczyn oktonionowy Cayleya–Dicksona i bioktonionowy asocjator;
- potencjał cosinusowy, oddziaływania między sąsiadami i energię asocjatora;
- numeryczną ewolucję symplektyczną leapfrog;
- niezależny benchmark kosmologiczny dla pola skalarnego.

Program sprawdza normy i momenty pierwiastków, normę iloczynu
oktonionowego, gradient energii i względny dryf energii w symulacji.

Uruchomienie z katalogu repozytorium:

```bash
python -m pip install -r Simulations/requirements.txt
python Simulations/pom1_model.py
```

**Ograniczenia:** nie wyprowadzono czasoprzestrzeni, pól Modelu
Standardowego, grawitacji ani prędkości światła z tego hamiltonianu.
Parametry i liczby kosmologiczne są ilustracyjne. Testy numeryczne nie są
dowodami Lean.

## Test emergencji krawędziowej (nie dowód grawitacji)

`emergent_geometry_probe.py` buduje z bioktonionowych prądów kandydat na
ramę krawędziową na **założonym** pięciowęzłowym grafie i śledzi jej
zmiany podczas dynamiki hamiltonianu. Sprawdza zanik prądów w stanie
zerowym, niezerowy obieg w stanach wzbudzonych i niejednoznaczność
wyboru czterech osi wewnętrznych.

```bash
python Simulations/emergent_geometry_probe.py
```

To nie jest jeszcze tetrada teleparalelna: brakuje lokalnej symetrii
Lorentza, płaskiej koneksji spinowej oraz fizycznego wyprowadzenia
sygnatury czasoprzestrzeni. Analiza: [Theory/EmergenceBridge.md](../Theory/EmergenceBridge.md).


## POM-2: badanie uporządkowanej próżni

Uruchom: python Simulations/ordered_phase_probe.py

Wymaga też biblioteki SciPy. Porównuje model K3 i K5, sprawdza zakresy niestabilności, dwie przeciwne gałęzie obiegu, stany o rangach 2 i 4 oraz brak ciągłej symetrii U(1) potencjału E8. To diagnostyka, nie dowód tetrad ani globalnego minimum pełnego układu przy dodatnim E8.


## POM-3 — wybór lokalnej podalgebry

Uruchom: python Simulations/sector_vacuum_probe.py

Skrypt sprawdza 180 losowych stanów C⊗O, jednoznaczny wybór
podalgebry H przy dodatnim wyznaczniku Grama, zamknięcie i asocjator
wewnątrz jednego C⊗H, przykłady oddziaływań między sektorami,
globalną U(1), normę Minkowskiego na realnym wycinku C⊗H,
dolną granicę potencjału i widmo 16×16 Hessianu w minimum
(11 płaskich i 5 sztywnych kierunków).

Jest to numeryczny test algebraicznej **kinematyki wewnętrznej**.
Nie wyprowadza fizycznych tetrad, zegarów, geometrii przestrzennej ani torzji.

## Dynamika sektorów POM-3

Uruchom: python Simulations/sector_motion_probe.py

Test rozwija stan na pięcioelementowym grafie przy nowym potencjale V3 i bada zmiany wyznaczonych z niego lokalnych projektorów kwaternionowych. Używa symplektycznej aktualizacji i sprawdza zachowanie energii oraz gradient. Zmiany projektora są zjawiskiem modelowym, a nie wyprowadzonym ruchem fizycznym lub torzją.


## POM-4 — Metastability of an EM/GR-coupled pattern

Run: python Simulations/emgr_metastability_probe.py

The script verifies the H_C ≅ M₂(C) representation in one chosen local sector, textbook two-mode CAR identities, 3 exact rational phase examples and 441 points on the prescribed dimensionless EM–GR parameter grid. It explicitly demonstrates that the chosen EM scalar invariants vanish on an ideal null wave. The script does not establish fermionic particle spectra or physical metastable lifetimes.


## POM-5: truncated Rac/Di-like channels

Run from the repository root:

    python Simulations/singleton_channel_probe.py
    python Simulations/singleton_sector_transport.py

The first script uses two bosonic oscillator modes per site at a finite cutoff to test a number-conserving link and an SU2-singlet pairing source. It verifies global parity, absence of mixed even-odd sectors from an even initial vacuum, and nonzero simultaneous odd-odd local excitations. Physical pair creation rates have NOT been computed. Finite matrices necessarily fail exact canonical commutation relations.

The second script constructs closest-SO3 overlap transport between the quaternionic frames selected in POM-3 and verifies the SU2 spin lift. This transport is a *postulate* selected from an overlap metric, not a derived physical Lorentz or Sp(4,R) connection.


## POM-6 — spectral graph diagnostic

    python Simulations/spectral_topological_probe.py

Two quaternion subalgebras are reconstructed from POM-3 bi-octonion states. Their normalized projector overlap q_AB=5/8 fixes a link strength t=t0+kappa*q. A **stipulated** 1D chain is arranged in two different sector orderings. The script checks the known SSH winding rule, chiral operator, nearly zero edge spectrum, chosen SU2 spin lifts, U1 phase covariance, positive bosonic graph Laplacian and a postulated strain switching threshold. These tests do NOT establish fermion spin-statistics, photons, spacetime dimension or teleparallel gravity.


## POM-7: does a sector pattern emerge from a proposed energy?

Run from the repository root:

    python Simulations/spontaneous_ordering_probe.py
    python Simulations/continuous_sector_frustration.py

The first script finds all 4 period-four ground states for N=8,12 by
exact enumeration, and for a 40-site periodic ring by exact min-plus
dynamic programming. It then maps each state to quaternionic projectors
and tests the known 1D SSH boundary modes under the link t=t0+kappa*q.
The FOUR bulk-ground phases have two topological and two trivial
open-chain terminations. It also verifies the original positive K
Hamiltonian favors a uniform sector and that symmetric thermal
averaging produces no selected dimer.

The second script produces an exact rational witness q=178369/390625
for two other valid quaternion sectors and numerically relaxes a small
continuous angle subfamily. It demonstrates that old A/B and A/C
sector choices are not uniquely preferred. No global minimization
over the full V2(R7) vacuum, physical particle, or spacetime follows.


## POM-8 — unrestricted POM-3 vacuum order parameter

Run: `python Simulations/full_vacuum_ordering_probe.py`.

The deterministic test uses the full local Stiefel V₂(R⁷) of ordered
orthonormal imaginary octonion pairs and their actual octonion product,
rather than predefined A/B projector labels.
It validates its analytic 7D gradient, optimizes N=8/12/16 rings
with several random starts, compares to period-four-restricted states,
verifies an exact rational eight-sector witness with Python Fraction,
computes a finite open-chain extended spectral mode (including IPR),
and tests an explicit small-associator trial even at gamma=10.

The graph, distance-two neighbors and projector energy are chosen
toy-model ingredients; the reported optima are local numerical results,
except for the rational witness's explicit strict inequality.


## POM-9 — Fibonacci/Planck-flux test

From the repository root:

    python Simulations/fibonacci_planck_flux.py

The script uses the POM-3 bi-octonion-selected quaternion sectors A/B
to create scalar hopping in {37/40,1} on a GIVEN 2D Hofstadter
magnetic unit cell with flux p/q in units h/e. Its 25x25
magnetic-momentum mesh measures the numerical Chern number
(Fukui–Hatsugai–Suzuki algorithm) and spectral gaps for five
Fibonacci approximants; a standard matrix perturbation bound yields
a conservative mesh-to-full-torus gap estimate. Independent
controls confirm that a uniform-bond Hofstadter model already
has the same Chern and that silver-mean approximants do too.

The 2D graph, magnetic flux, charge, Fibonacci sector word and
hopping law are externally set, NOT derived from POM's vacuum.
Samples are floating-point, not interval-certified exact eigenvalues.


## POM-10 — self-generated Berry holonomy (conditional toy)

Run: python Simulations/self_generated_flux_probe.py

The Python check takes POM-3 bi-octonion local ground-state
representatives from one common quaternion subalgebra. It enumerates
all 8 possible 3-edge Boolean graphs; checks an exact rational
energy witness; computes two opposite χ=±4/5 chiral configurations;
tests gauge invariance of the triangular spinor Bargmann invariant
(2±i)/5 with irrational phase ±atan(1/2); calculates the exact
FINITE triangle eigenvalues and their positive spacing; tests a
separate ASSUMED 2D QWZ bulk response with Chern ±1 and band gap
≥8/5, including a bounded mass perturbation. No external U(1)
magnetic flux is inserted.

Numerical QWZ Chern does NOT prove that the 3-node network generates
a 2D lattice, that the phase is physical Maxwell magnetic flux, or
that real fermionic particles exist. Spinor coherent-state
quantization and QWZ kinetic terms remain external hypotheses.


## POM-11 — exact three-node Hermitian loop

Run: python Simulations/exact_loop_spectrum.py

Verifies the exact Gaussian-rational 3-cycle Wilson invariant B=(2+i)/5 and characteristic polynomial (lambda+1)(lambda^2-lambda-4/5). The exact smallest level spacing (15-sqrt(105))/10 exceeds 0.47. Eighty independent node gauge rephasings preserve Wilson phase and eigenvalues; 160 Hermitian perturbations of norm 0.2 respect the known Weyl margin >0.07. This does NOT construct a bulk gap in 2D/3D.
