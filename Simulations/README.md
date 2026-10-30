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
