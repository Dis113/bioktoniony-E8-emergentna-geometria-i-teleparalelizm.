# POM-1 — otwarte obowiązki dowodowe

Statusy: **PROVED** = sprawdzane kompilacją Lean; **CHECKED** = obliczenia liczbowe;
**OPEN** = brak dowodu; **ASSUMPTION** = przyjęte założenie.

| ID | Twierdzenie / problem | Status | Kryterium |
|---|---|---|---|
| M01 | 240 pierwiastków, norma²=2 | PROVED (enumeracja) | `doubledRoot_norm_sq` |
| M02 | Macierz momentu `Σααᵀ=60I₈` | PROVED (enumeracja) | `root_second_moment` |
| M03 | Nieujemność potencjału cosinusowego | PROVED | `rootPotential_nonneg` |
| M04 | Hessian w zerze wynosi `(60ε/f²)I₁₆` | OPEN | Ścisły formalny rachunek różniczkowy |
| M05 | Wektory enumeracji są różne i zamknięte na odbicia | OPEN | Formalne twierdzenie w Lean, bez samej symulacji |
| M06 | Usunięcie zależności od `native_decide` | OPEN | Dowód kernelowy, audyt aksjomatów |
| D01 | Kwantyzacja dynamiki bioktonionowej | OPEN | Jednoznaczny Hamiltonian samosprzężony lub algebra obserwabli |
| D02 | Powstanie 3+1 wymiarów i sygnatury Lorentza | OPEN | Konstrukcja limitu kontinuum |
| D03 | Symetria Lorentza / wspólny stożek przyczynowy | OPEN | Wyprowadzenie oraz limity naruszeń |
| D04 | Pochodzenie tetrad i torzji | OPEN | Mapa `Ψ, G → e, ω` i dynamika TEGR |
| D05 | Chiralne fermiony i `SU(3)×SU(2)×U(1)` | OPEN | Odpowiednie reprezentacje i anomalie |
| D06 | Uwięzienie koloru | OPEN | Kryterium pętli Wilsona / napięcie struny |
| C01 | Parametry DM/DE z dynamiki mikroskopowej | OPEN | Nie arbitralnie dopasowane `m, V₀` |
| C02 | Przewidywania różniące POM-1 od GR+ΛCDM | OPEN | Falsyfikowalna obserwabla |

**Ograniczenie interpretacji:** potwierdzenie M01–M03 nie rozstrzyga D01–D06.
W szczególności nie dowodzi istnienia komórek próżni ani automatycznej
unifikacji z Modelu Standardowym.


## Wyniki audytu emergencji (2026-10-30)

| ID | Test | Status |
|---|---|---|
| V01 | Przy μ²>0 i pozostałej energii ≥0 zerowy stan podstawowy wymusza Ψ=0 | PROVED: warunkowy dowód `POM1/VacuumObstruction.lean`; pełnego H nie formalizowano |
| V02 | W takim stanie każdy biliniowy prąd Ψ_iΨ_j znika | CHECKED algebraicznie; obserwabla zbudowana w symulacji |
| V03 | W części liniowej masy są jednakowe w 16 kanałach, a człon asocjatora nie wnosi wkładu | DERIVED perturbacyjnie; CHECKED różnicami skończonymi |
| V04 | Prądy mogą wytworzyć niezerowy obieg na trójkącie | PROVED świadek w łącznej płaszczyźnie; CHECKED numerycznie na bioktonionach |
| V05 | Nieosobliwa 4D tetrada w stanie próżni bez arbitralnej projekcji i narzuconej sygnatury | OPEN |
| V06 | Fizyczna torzja zgodna z lokalną symetrią Lorentza | OPEN |
| V07 | Działanie TEGR z limitu mikroskopowego | OPEN |

Szczegóły oraz ograniczenia: [EmergenceBridge.md](EmergenceBridge.md).


## POM-2 (2026-10-30)

| ID | Problem | Status |
|---|---|---|
| P201 | Formy kwadratowe K3/K5 i próg α_c | Formalizacja Lean, identyfikacja mE8 z Hessego pozostaje poza modułem |
| P202 | Ukończenie kwadratów i dolne ograniczenie energii K5 | Formalizacja Lean |
| P203 | Równa energia stanów rangi 2 i 4 dla epsilon=0 | Dowód algebraiczny + test Python; ranki nie są jeszcze udowodnione w Lean |
| P204 | Dodatnie epsilon: istnienie niezerowego globalnego minimum | Analityczny próg + ujemne stany próbne; pełny kształt minimum otwarty |
| P205 | Jednoznaczna selekcja rangi 4 | OPEN |
| P206 | Fizyczne tetrady z sygnaturą Lorentza | OPEN |
| P207 | Globalna U(1) potencjału E8 | FALSE: analityczne rozwinięcie do czwartego rzędu + niezależny kontrprzykład numeryczny |

Patrz [OrderedVacuum.md](OrderedVacuum.md). Zjawiska frustracji XY są już opisane w recenzowanej literaturze.
