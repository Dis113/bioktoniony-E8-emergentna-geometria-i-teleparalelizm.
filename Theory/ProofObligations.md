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
