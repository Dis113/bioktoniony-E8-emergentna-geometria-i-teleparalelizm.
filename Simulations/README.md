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
