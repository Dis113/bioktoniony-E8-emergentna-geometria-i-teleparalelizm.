# POM-7 — Spontaniczny wybór uporządkowania sektorów

**Data: 2026-10-31. Status: warunkowy model badawczy; nie teoria znanych cząstek.**

## A. Dlaczego dotychczasowy POM-3 nie generuje dimeru?

Oryginalny hamiltonian H3 zawiera lokalne V3 o znanym minimum Vmin,
dodatnie K/2 razy sumę kwadratów różnic Ψ_i−Ψ_j oraz nieujemną karę
za kwadrat asocjatora przy gamma ≥ 0.

Na spójnym grafie przy K>0:

\[
H_3\ge N V_{\min}
\]

i równość jest osiągalna przez ten sam nieosobliwy, minimalizujący
stan bioktonionowy na każdym węźle. Wtedy wszystkie różnice krawędziowe
i asocjatory wynoszą zero. Każde minimum całego modelu ma
jednakowe Ψ_i na wszystkich połączonych węzłach. Wszystkie projektory
kwaternionowe są takie same i wszystkie overlepy q_ij = 1.

**Wniosek POM-specific:** hamiltonian H3 nie powoduje spontanicznej
dimerizacji potrzebnej w POM-6; nie wolno jej z góry przypisać próżni.

Lean: POM1/SpontaneousOrdering.lean zawiera warunkowy certyfikat
pojedynczej krawędzi. Pełny H3 nie został sformalizowany w całości.

## B. Znany z literatury mechanizm frustracji

Na **założonym** jednowymiarowym pierścieniu badamy zredukowaną
energię ANNNI:

\[
H_{\mathrm{red}}=-J_1\sum_i\sigma_i\sigma_{i+1}
+J_2\sum_i\sigma_i\sigma_{i+2},
\quad\sigma_i\in\{-1,+1\}.
\]

Przy J2>J1/2 w stanie podstawowym występuje znany
czteroelementowy antyporządek (++--), z czterema przesunięciami.
**Nie dowodzimy od nowa twierdzeń ANNNI**; zob. Stephenson–Betts,
Phys. Rev. B 2, 2702 (1970),
DOI https://doi.org/10.1103/PhysRevB.2.2702
oraz Hu–Charbonneau, Phys. Rev. B 104, 144429 (2021),
DOI https://doi.org/10.1103/PhysRevB.104.144429.

W POM-7 próba J1=J2=1 jest dokładnie rozwiązywana przez enumerację
wszystkich 2^8 i 2^12 etykiet oraz min-plus DP na 40 węzłach:
cztery stany o energii -N, bez ręcznego wstawiania wzoru (++--).
Programowanie dynamiczne jest **optymalizacją**, a nie hamiltonowską
ewolucją w fizycznym czasie.

## C. Własny most POM: energia z overlapów projektorów

Dla Ψ_i należących do minimów V3 wyznaczamy quaternionowy
projektor P_i, a z niego

\[
q_{ij}=\frac14\operatorname{Tr}(P_iP_j).
\]

Dwa wybrane sektory A,B z POM-6 spełniają
qAA=qBB=1, qAB=5/8. Dopiero po *ograniczeniu z góry*
do tych dwóch sektorów można nadać etykiety sigma_i=±1:

\[
q_{ij}=\frac{13}{16}+\frac{3}{16}\sigma_i\sigma_j.
\]

Dla tej redukcji wprowadźmy **NOWY POSTULAT** interakcji
projektorowej

\[
H_7^{\mathrm{proj}}=\frac{16}{3}\left[
-J_1\sum_i(q_{i,i+1}-13/16)
+J_2\sum_i(q_{i,i+2}-13/16)\right].
\]

Współczynniki są wszędzie takie same; dynamika nie zawiera
ręcznie naprzemiennych linków. Dla A/B dokładnie odtwarza
Hred. Ale łańcuch i redukcja do dwóch sektorów są nadal
*założone*, nie pochodzą ze starego hamiltonianu H3.

## D. Nowa przeszkoda: sektory nie są wybrane jednoznacznie

W realnych oktonionach Cayleya–Dicksona istnieje także
H_C=span{1,e1,e4,e5}, generowana przez e4,e5,
z qAC=1/2 < qAB=5/8.

Dla tej samej projektorowej energii na czterech węzłach
J1=J2=1:

\[
H_7^{\mathrm{proj}}(AABB)=-4,\qquad
H_7^{\mathrm{proj}}(AACC)=-16/3.
\]

Ścisły wniosek: **oryginalny B nie jest wyróżniony energetycznie
nawet wśród tych dwóch testowanych partnerów A.**
Nie jest to dowód globalnej minimalności C.

Lean POM1/SpontaneousOrdering.lean certyfikuje qAC=1/2,
porównanie z qAB=5/8 (korzystając ze starszego modułu
SpectralLink), tożsamość redukcji Isinga oraz cztery krawędziowe
energii. Nie powiela ogólnego twierdzenia ANNNI.

## E. Dokładny świadek z częściowo ciągłej przestrzeni sektorów

Można wybrać dwa stany POM-3:

\[
u_\pm=(4e_1\pm3e_4)/5,\quad
v_\pm=(4e_2\pm3e_5)/5
\]

o dobrze określonych, niedegenerowanych podalgebrach kwaternionowych.
Rachunek **dokładny na wymiernych** z iloczynem Cayleya–Dicksona
daje

\[
q_{+-}=178369/390625\approx0.45662464<1/2.
\]

Konfiguracja okresu czterech na pierścieniu 8 ma energię

\[
H_7^{\mathrm{proj}}=-4528128/390625=-11.59200768,
\]

poniżej modelu A/C (−10.66666...). Dodatkowa minimalizacja
8 kątów w jednoparametrowej rodzinie orientacji daje
lokalne minimum około −11.59973008. To nie jest dowód
globalnego minimum pełnej przestrzeni V2(R7).

Skrypt: Simulations/continuous_sector_frustration.py.
Własne nowe testy dotyczą wyłącznie zależności energii od
orientacji sektorów, nie ponownego dowodu własności oktonionów.

## F. Dwa zakończenia spektralne o tej samej energii próżni

Z dokładnych czterech minimów na pierścieniu 40 węzłów
otrzymujemy alternację overlapów silny/słaby.
Stosując **wciąż postulowaną** regułę t_ij=0.1+0.9 q_ij
z POM-6, dla otwartego łańcucha:

| Sektory | Zakończenie | minimalne |E| | Waga brzegowa | Winding SSH |
|---|---|---:|---:|---:|
| A/B | pierwszy słaby link | 0.000148852 | 0.561095 | −1 |
| A/B | pierwszy silny link | 0.355498 | 0.014701 | 0 |
| A/C | pierwszy słaby link | 0.00000447505 | 0.697500 | −1 |
| A/C | pierwszy silny link | 0.462065 | 0.010224 | 0 |

Dwa z czterech minimów przekładają się przy ustalonej granicy
na stan z modami brzegowymi, dwa na zakończenie trywialne.
Są to znane właściwości modelu SSH w *naszej* konkretnie
obliczonej sieci overlapów, a nie nowa teoria topologii.

Granica i wybór komórki elementarnej są istotne; nie wolno
ogłosić, że sama frustracja automatycznie produkuje fermion.

## G. Temperatura i ograniczenia wymiarowości

Skończony pierścień o translacyjnie niezmienniczej energii ma
zerową średnią dimerizacji w symetrycznej mierze Gibbsa.
Sprawdzono to przez dokładną enumerację dla N=8,12.
Jednowymiarowy klasyczny model o skończonym zasięgu nie posiada
trwałego porządku spontanicznego przy dodatniej temperaturze
w granicy termodynamicznej (znana fizyka statystyczna).

## H. Co zostało nierozwiązane

1. Wyprowadzić sektorowe oddziaływania konkurencyjne z jednego
   hamiltonianu na **pełnej** ciągłej przestrzeni bioktonionów,
   zamiast ograniczać stan do dwóch wybranych H_A/H_B.
2. Uzasadnić graf, sąsiedztwo, prędkość propagacji i liczbę wymiarów;
   z góry narzucony łańcuch 1D nie jest fizyczną czasoprzestrzenią.
3. Wyprowadzić operatory z poprawną lokalną symetrią ramy,
   fermionowe CAR, ładunki i chiralność.
4. Sprawdzić możliwość stabilnego porządku poza 1D i prawdziwe
   bozonowe wzbudzenia propagujące oraz ewentualny limit kontinuum.
5. Dopiero potem pytać o tetrady, kowariantną koneksję
   spinową, torzję oraz działanie teleparalizmu TEGR.

**Kryterium STOP:** bez punktów 1–5 model pozostaje poprawnym
warunkowym mostem od projektorów do znanych modów SSH,
a nie emergentną teorią materii lub grawitacji.
