# POM-9 — Stała Plancka, teoria liczb, ułamki łańcuchowe i stabilność widmowa

**31 października 2026. Status: test modelowy, nie wyprowadzenie rzeczywistych cząstek, elektromagnetyzmu, grawitacji ani wartości stałej Plancka.**

## 1. Rozróżnienie h od długości Plancka

Stała Plancka h=2πℏ jest kwantem działania. W zjawiskach kwantowych występuje faza exp(iS/ℏ). **Nie można wyprowadzić jej wartości SI z ułamka łańcuchowego** bez niezależnego fizycznego prawa i skali działania.

Długość Plancka l_P=sqrt(ℏG/c³) jest osobną wielkością. Użycie ℏ nie oznacza, że wyznaczono odległość między węzłami sieci POM lub dynamikę w skali l_P.

Konkretna, **znana** realizacja kwantowego fazowania dotyczy magnetycznego strumienia przez oczko siatki dla nośnika o ładunku e:

\[
\exp(i e\Phi/\hbar)=\exp(2\pi i\alpha),\quad
\alpha=\frac{e\Phi}{h},\quad \Phi_0=\frac h e.
\]

Jest to faza Peierlsa–Aharonova–Bohma. Model POM-9 PRZYJMUJE zewnętrzny strumień i ładunek jako dane, a nie generuje ich z bioktonionów.

## 2. Ułamki łańcuchowe jako kontrolowany limit

Wybieramy niewymierny, bezwymiarowy parametr

\[
\alpha_*=(\sqrt5-1)/2=[0;1,1,\ldots].
\]

Jego zbieżne ułamki łańcuchowe tworzą ciąg Fibonacciego:

\[
3/5,\quad5/8,\quad8/13,\quad13/21,\quad21/34.
\]

Przy każdym p/q sprawdzamy osobną magnetyczną komórkę o q podkomórkach. Nigdy nie utożsamiamy skończonego q z dokładnie niewymiernym strumieniem. Teoria jego aproksymantów, topologii widm i małych mianowników jest ZNANA. Ułamki łańcuchowe nie gwarantują same w sobie stabilności fizycznej materii.

Dla kontroli obliczamy też ciąg srebrny: sqrt(2)-1=[0;2,2,2,...], z wymiernymi przybliżeniami 2/5, 5/12 i 12/29. **Wyniki nie dowodzą uprzywilejowania złotej proporcji.**

## 3. Nowy POM-specific element: link od bioktonionowych podalgebr

Dla dwóch konkretnych sektorów POM-3, A oraz B, wcześniej obliczono

\[
q_{AB}=\frac14\operatorname{Tr}(P_AP_B)=5/8,\quad q_{AA}=q_{BB}=1.
\]

Na **założonej** siatce 2D narzucamy wymierne słowo Sturmowskie

\[
w_m(p,q)=\lfloor (m+1)p/q\rfloor-\lfloor mp/q\rfloor\in\{0,1\}.
\]

Sektor m to A lub B stosownie do w_m. Ta konfiguracja NIE została wyprowadzona jako minimum pełnego hamiltonianu POM (POM-8 pokazał, że tego nie można przyjmować bez testów).

Wprowadzamy jawne, również jeszcze postulowane, sprzężenie:

\[
t_m=1+\tfrac15[\operatorname{Tr}(P_mP_{m+1})/4-1]
=\begin{cases}1& w_m=w_{m+1}\\37/40&w_m\ne w_{m+1}.\end{cases}
\]

Własne twierdzenia Lean w POM1/FibonacciFluxLinks.lean sprawdzają ten przepis i dokładne liczby słabszych linków (4,6,10,16,26) w pierwszych pięciu przybliżeniach. **Nie** formalizują od nowa klasycznej teorii ułamków łańcuchowych ani grupy Chern.

## 4. Znany Harper–Hofstadter plus kontrolowana nowa modyfikacja POM

Na magnetycznej komórce q×q definiujemy:

\[
H_{mm}=-2\cos(k_y+2\pi pm/q)+\delta\sin(2\pi m/q),
\]

\[
H_{m,m+1}=-t_m,\qquad H_{q-1,0}=-t_{q-1}e^{i\phi},
\quad \phi=q k_x.
\]

To operator Harpera z *wyliczonymi z projektorów*, lecz postulowanymi jako fizyczne, amplitudami t_m. Zakładamy zarówno samą siatkę, jak i zewnętrzne pole magnetyczne.

Testujemy przerwę między p-tą i (p+1)-szą wartością własną. Znane twierdzenie TKNN wiąże otwarte luki z całkowitymi liczbami Chern. W implementacji POM-9 liczba Chern obliczana jest numeryczną, opublikowaną metodą Fukui–Hatsugai–Suzuki; nie dowodzimy na nowo TKNN ani metody FHS.

## 5. Dokładniejsze badanie odporności

Obliczenia na równomiernej siatce 25×25 parametrów (phi,k_y) dają:

| alpha | q | Chern (konwencja kodu) | Próbkowany gap | Zachowawcze dolne oszacowanie |
|---|---:|---:|---:|---:|
| 3/5 | 5 | -1 | 1.483497 | 0.729515 |
| 5/8 | 8 | -1 | 1.555261 | 0.801278 |
| 8/13 | 13 | -1 | 1.578348 | 0.824365 |
| 13/21 | 21 | -1 | 1.585463 | 0.831481 |
| 21/34 | 34 | -1 | 1.586000 | 0.832018 |

Ostatnia kolumna wynika z **znanego** twierdzenia Weyla o przesunięciu
wartości własnych oraz jawnej zależności macierzy od kątów:

\[
\|H(\phi,k_y)-H(\phi_0,k_{y0})\|
\le t_{\max}|\phi-\phi_0|+2|k_y-k_{y0}|.
\]

Najbliższy punkt siatki różni się o najwyżej pi/N w każdej zmiennej,
więc przy N=25 i t_max=1:

\[
\min_{BZ}\Delta_p \ge \min_{\mathrm{grid}}\Delta_p-6\pi/25.
\]

**Granice te są matematycznie prawidłowymi warunkowymi oszacowaniami,
ale same próbki wartości własnych są liczbami zmiennoprzecinkowymi,
nie formalnym rachunkiem przedziałowym.** Nie ogłaszamy pełnego
certyfikatu jądrowego luki widma.

Dodatkowe zewnętrzne zaburzenie diagonalne delta*sin(2pi m/q),
|delta|<=0.08, ma normę operatorową <=0.08. Z twierdzenia Weyla
otwarta luka przy delta=0 zmniejsza się najwyżej o 0.16.
Przy powyższych dodatnich oszacowaniach znana zasada
niezmienniczości homotopijnej liczby Chern zapewnia jej stabilność
w takim przedziale, o ile numeryczne oszacowania luki są poprawne.
Program oblicza także Chern przy delta=0.08 i otrzymuje ten sam wynik.

## 6. Kontrole negatywne ważniejsze od dopasowania liczb

**A. Chern nie pochodzi od bioktonionów:** przy wyłączeniu
modulacji projektorowej, kappa=0, jednorodny Hofstadter nadal
daje C=-1 przy alpha=8/13. Topologia wynika więc już z
ustalonej fizyki magnetycznej, nie z odkrycia POM.

**B. Złota proporcja nie jest jedyną stabilną liczbą:** srebrna
sqrt(2)-1 i aproksymanty 2/5, 5/12 i 12/29 również
mają C=-1 i dodatnie dolne oszacowania luki. Nie należy
utożsamiać złotej proporcji z wartością h ani twierdzić,
że jest koniecznym warunkiem istnienia cząstek.

**C. Różne klasy stabilności:** niewymierność utrudnia dokładne
rezonanse w pewnych układach dynamicznych (teoria KAM), zaś
zachowanie luki topologicznej to odrębne twierdzenie o widmie.
Sam stosunek liczbowy nie daje trwałości cząstki w 3+1D.

## 7. Recenzowane rezultaty używane bez dublowania

- D. R. Hofstadter, Physical Review B 14, 2239 (1976);
  DOI https://doi.org/10.1103/PhysRevB.14.2239
- Thouless, Kohmoto, Nightingale, den Nijs, Physical Review Letters 49, 405 (1982);
  DOI https://doi.org/10.1103/PhysRevLett.49.405
- Fukui, Hatsugai, Suzuki, Journal of the Physical Society of Japan 74, 1674 (2005);
  DOI https://doi.org/10.1143/JPSJ.74.1674
- Kraus, Zilberberg, Physical Review Letters 109, 116404 (2012);
  DOI https://doi.org/10.1103/PhysRevLett.109.116404
- Jitomirskaya, Liu, Annals of Mathematics 187, 721 (2018);
  DOI https://doi.org/10.4007/annals.2018.187.3.3

Nie formalizujemy ponownie tych twierdzeń.

## 8. Kryteria przejścia od modelu POM-9 do hipotezy materii

1. Wyprowadzić samą strukturę siatki i wzór sektorów z pełnego H_8,
   bez narzuconych złotych czy srebrnych ułamków; problem
   nierówności energii POM-8 pozostaje aktualny.
2. Wyprowadzić fizyczny ładunek e, lokalne U(1), pole EM,
   fazę Peierlsa i skalę h zamiast podstawiać je ręcznie.
3. Ustalić spinory z fermionowym CAR, ładunki, normalizowalność,
   masy, stabilność czasową i kwantowe oddziaływania w 3+1.
4. Wyprowadzić czasoprzestrzeń, tetrady, płaską koneksję
   spinową, tensor torzji i działanie TEGR.
5. Zaproponować nową, falsyfikowalną obserwablę
   odróżniającą POM od znanego modelu Harper–Hofstadter.

**Wniosek POM-9:** liczby i ułamki łańcuchowe rzeczywiście
organizują pewne kwantowe widma oraz odporne luki.
Nie dowodzą jednak same w sobie Planckowskiej próżni,
ani nie generują fundamentalnej stałej h.
