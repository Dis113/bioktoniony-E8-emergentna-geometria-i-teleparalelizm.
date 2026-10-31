# POM-8 — audyt nieograniczonej próżni kwaternionowych sektorów

**Status:** 31 października 2026. Jawny, spekulatywny model energii na **zadanym** jednowymiarowym pierścieniu. Własne certyfikaty POM: Lean 4 dla dokładnego wymiernego kontrprzykładu, SciPy dla pełnej ciągłej przestrzeni orientacji i testu członu asocjatora. Ogólne twierdzenia ANNNI i SSH są znane; **nie są powielane**.

## 1. Co dokładnie sprawdzamy?

W POM-3 pojedyncza komórka ma \(\Psi=x+Iy\in\mathbb C\otimes\mathbb O\), z

\[
V_3(\Psi)=-\alpha s/2+\lambda s^2/4-\eta\Delta,\qquad
s=\|x\|^2+\|y\|^2,
\quad\Delta=\|\operatorname{Im}x\|^2\|\operatorname{Im}y\|^2-
(\operatorname{Im}x\cdot\operatorname{Im}y)^2.
\]

Przy \(\alpha>0\), \(\lambda>\eta>0\) wszystkie minima lokalne (i globalne) mają
\(x=\sqrt{r/2}\,u\), \(y=\sqrt{r/2}\,v\), gdzie \(r=\alpha/(\lambda-\eta)\), \(u,v\in\operatorname{Im}\mathbb O\simeq\mathbb R^7\), \(\|u\|=\|v\|=1\), \(u\cdot v=0\).
Zatem pełna **orientacyjna** przestrzeń minimów jest \(V_2(\mathbb R^7)\), wymiar 11 na węzeł. Nie redukujemy jej do dwóch etykiet A/B.

Każdy stan wybiera \(\mathbb H_\Psi=\mathrm{span}\{1,u,v,uv\}\); przy odpowiednich podanych warunkach jest to rzeczywista kwaternionowa podalgebra oktonionów (twierdzenie Artina, już opublikowane). Nie dowodzimy ponownie alternatywności oktonionów ani ogólnej geometrii \(G_2\).

Niech \(P_i\) oznacza rzut ortogonalny na wybrany czterowymiarowy sektor i \(q_{ij}=\operatorname{Tr}(P_iP_j)/4\).
Na **narzuconym na razie** pierścieniu N węzłów badamy wersję
\[
H_8=\sum_i\left[\frac12\|p_i\|^2+V_3(\Psi_i)\right]
+\underbrace{\frac{16}{3}\sum_i(q_{i,i+2}-q_{i,i+1})}_{E_{\rm proj}}
+\gamma\sum_i\|\mathcal A(\Psi_i,\Psi_{i+1},\Psi_{i+2})\|^2,
\quad\gamma\ge0.
\]
To ta sama frustracja z POM-7 dla \(J_1=J_2=16/3\), zapisana z pominięciem nieistotnego stałego przesunięcia energii \(J_1 N\) w porównaniach faz. Sama reguła oddziaływania projektorów pozostaje postulatem, nie wynika z H3 ani z E8.

**Ważna redukcja dla \(\gamma=0\):** dla dowolnej konfiguracji z \(\Delta_i>0\), zachowując lokalne \(\mathbb H_i\), można zastąpić \(\Psi_i\) przez jego reprezentanta w minimum V3. Zmniejsza to energię lokalną i nie zmienia żadnego \(q_{ij}\). Wobec tego poszukiwanie globalnego minimum H8 przy \(\gamma=0\) faktycznie można ograniczyć *bez utraty minimum* do pełnego \(V_2(\mathbb R^7)^N\).
Przy \(\gamma>0\) ten argument nie obowiązuje bez dalszego dowodu, ale stany na lokalnym minimum V3 nadal są poprawnymi **stanami próbnymi** i dają ścisłe górne ograniczenia globalnego minimum.

## 2. Jawny, ścisły kontrprzykład wymierny (bez optymalizatora)

Osiem ramek (u_i,v_i) wygenerowano z **dwóch Householderów o całkowitych wektorach** na każdy węzeł. Wszelkie u_i,v_i,w_i=u_i v_i mają dokładnie wymierne współrzędne, a ich normy i wzajemne iloczyny skalarne są odpowiednio 1 i 0.
Jest to rzeczywista konfiguracja niedegenerowanych sektorów kwaternionowych, nie osiem dowolnych macierzy nakładania.

Dokładny rachunek w \(\mathbb Q\) (Python Fraction), niezależnie sprawdzany w [POM1/FullVacuumCounterexample.lean](../POM1/FullVacuumCounterexample.lean) przez finitywny certyfikat, daje

\[
\boxed{E_{\rm proj}({\rm wymierny\ świadek})\approx -12.092447158731742 < -12.}
\]

Nierówność jest **ścisła** i nie korzysta z błędów zaokrąglenia. Energia \(-12\) jest wartością optimum numerycznego dla wcześniej badanej klasy stanów wymuszonych do okresu 4 na N=8. Nie twierdzimy, że został formalnie udowodniony globalny dolny kres *wszystkich* stanów okresu 4.

Lean używa \`native_decide\` w certyfikacie wymiernym. To jawnie zależy od kompilatora Lean i nie jest w pełni kernelowo zredukowanym obliczeniem. Osobne twierdzenie weryfikuje ortonormalność wszystkich ośmiu wybranych baz (zależnie od wyniku finalnego CI).

## 3. Numeryczna optymalizacja na pełnym V₂(R⁷)

[Simulations/full_vacuum_ordering_probe.py](../Simulations/full_vacuum_ordering_probe.py) używa:
- niezdegenerowanych *dowolnych* par wektorów 7D na każdy węzeł;
- ortonormalizacji Gram–Schmidta i faktycznego oktonionowego iloczynu \(w_i=u_iv_i\);
- właściwego śladu projekcji \(q_{ij}\), a nie sztucznych etykiet A/B;
- analitycznego gradientu energii projektorowej (sprawdzanego różnicami centralnymi);
- wielu deterministycznych startów metody L-BFGS-B; to **lokalne** minima, nie dowód globalnego minimum.

| Liczba węzłów N | Najniższa znaleziona energia E_proj | Średni q_NN | Średni q_NNN | Czy naprzemienne NN? |
|---:|---:|---:|---:|---|
| 8 | −12.875805666 | 0.801776695 | 0.5000000 | Nie; odchylenie standardowe q_NN <10⁻⁶ |
| 12 | −19.084274221 | 0.7821135 | 0.4839218 | Nie; std q_NN ≈0.001255 |
| 16 | −25.757340925 | 0.7978530 | 0.4960092 | Nie; std q_NN <10⁻⁶ |

Przy N=8, osobna optymalizacja w klasie **okresu 4** znajduje energię \(-12.000000000\). Zatem otwarty zbiór orientacji zawiera niżej energetyczne, prawie jednorodne co do q_NN konfiguracje. Stan przypomina *wewnętrzną helisę sektorową*, lecz nazwa „helisa” jest opisem wzoru overlapów, nie jeszcze ścisłą klasyfikacją.

Literatura: helical order in frustrated continuous-spin chains jest od dawna znany — De Raedt & De Raedt, Phys. Rev. B **19**, 2595 (1979), DOI [10.1103/PhysRevB.19.2595](https://doi.org/10.1103/PhysRevB.19.2595). Nie odtwarzamy ich dowodów. Nasza nowa część to konkretne nakładania **kwaternionowych projektorów w oktonionach**.

## 4. Fizyka brzegów: mod rozciągnięty nie jest topologicznym fermionem

Przyjmując ponownie postulowaną POM-6 regułę \(t_{ij}=0.1+0.9 q_{ij}\) i pięciokrotnie powtarzając ośmiowęzłową orientację na **otwartym** 40-węzłowym łańcuchu, otrzymujemy niemal jednorodne linki. Najniższe energie są rzędu \(|E|\approx0.06294\), waga czterech skrajnych węzłów to około 0.098, a udział odwrotny (IPR) około 0.03659.

To typowe dla rozciągniętego, niemal jednorodnego stanu (udział brzegów ~4/40), a **nie** dla silnie zlokalizowanego modu brzegowego SSH z wagą >0.55 w POM-6.
Pomiar IPR jest tutaj konieczny: samo niezerowe natężenie przy brzegu i mała energia nie dowodzą topologicznej lokalizacji.

Nie wyprowadziliśmy fermionowego CAR ani istnienia elektronu w 3+1.

## 5. Człon niełączny nie gwarantuje ustalenia dimeru

Może się wydawać, że dodatnia kara \(\gamma\|\mathcal A\|^2\) automatycznie powinna faworyzować AABB, ponieważ w AABB każdy sąsiadujący trójelementowy fragment zawiera dwa identyczne stany i ma zerowy asocjator (z alternatywności, znany fakt).

To NIE wystarcza. Każdy sektor \(\mathbb H_i\) ma **wewnętrzne** swobody wyboru ramy \((u_i,v_i)\) bez zmiany projektora \(P_i\). Można w niektórych przykładach silnie zmniejszyć koszt asocjatora, zachowując prawie niezmienioną energię projektorową.

Jawna, odtwarzalna próba z **zespołu ośmiu 6-decymalnych ramek** ma:

\[
E_{\rm proj}\approx-12.8758056647,\qquad
\sum_i\|\mathcal A_i\|^2\approx1.21317\times10^{-9}.
\]

Dla \(\gamma=10\):

\[
\boxed{E_{\rm proj}+\gamma\sum_i\|\mathcal A_i\|^2
\approx -12.875805653 < -12.}
\]

Konfiguracja jest prawidłowym stanem próbnym z lokalnym V3 w minimum i daje wyraźnie niższą energię od próby AABB z -12 nawet przy tej dodatniej karze. To nie dowód, że żadna dimerowa konfiguracja nie może być jeszcze lepsza; jest jednak konkretnym kontrprzykładem dla **automatycznej** selekcji poprzednio badanego AABB przez sam człon asocjatora.
Przy dodatnim \(\gamma\) nie wykonano pełnej globalnej minimalizacji wszystkich amplitud i orientacji.

## 6. Dlaczego POM-8 nie wyprowadza jeszcze fizycznej czasoprzestrzeni?

- **Założyliśmy** pierścień 1D, liczbę węzłów i rozróżnienie pierwszych/drugich sąsiadów. To nie emergentna geometria.
- Reguła sprzężeń przez \(q_{ij}\) jest postulatem, nie mikroskopowym wynikiem z E8.
- Kinematiczny operator grafowy i jego brzegowe analogi nie stanowią fizycznego pola fermionowego ani bozonowego, nie gwarantują uniwersalnej prędkości ani lokalnej symetrii Lorentza.
- Nie skonstruowano tetrad i spinowej koneksji, a skalar torzji TEGR nie powstał z mikrodynamiki.
- \(\gamma=10\) jest ilustracyjnym parametrem bezwymiarowym, nie skalibrowaną wartością fizyczną.

## 7. Decyzja o następnym kierunku

Wynik POM-8 oznacza, że przed szukaniem chronionych fermionów trzeba znaleźć w pełnym modelu **mechanizm wyboru wymiaru, sąsiedztwa i rodzaju porządku**, nie tylko dopasować kolejne parametry przy zadanym łańcuchu.

**Pierwszy test falsyfikacyjny:** czy na dynamicznie tworzonych grafach 3D/4D i w pełnej przestrzeni sektorów istnieje stabilna faza z uniwersalnym stożkiem propagacji oraz fizycznie poprawnym spektrum? Jeśli nie, obecny program jest zbiorem analogowych modeli, a nie unifikacją.


## POM-9 follow-up: the Fibonacci word is not a minimum found by POM-8

POM-9 uses continued-fraction convergents to CREATE a prescribed
quasiperiodic arrangement of two quaternion sector projectors and
adds an external Peierls flux alpha=ePhi/h. It tests whether a
resulting gapped Hofstadter phase is robust, and it is.

However, the POM-8 counterexample still stands: the full
bi-octonionic vacuum model has not dynamically selected A/B,
the Fibonacci word, the 2D graph or an EM field.
This must not be advertised as spontaneous Planck-scale matter
creation. See [PlanckContinuedFractions.md](PlanckContinuedFractions.md).
