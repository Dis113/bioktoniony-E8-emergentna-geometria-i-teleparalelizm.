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
