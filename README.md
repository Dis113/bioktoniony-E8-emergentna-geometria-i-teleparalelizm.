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
