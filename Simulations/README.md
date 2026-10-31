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
