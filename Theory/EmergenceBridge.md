# POM-1 — test emergencji geometrii zamiast postulowania tetrad

**Data:** 2026-10-30  
**Status:** audyt matematyczny + numeryczny model diagnostyczny; **nie** gotowa teoria grawitacji.  
**Zasada:** recenzowane, ogólne twierdzenia cytujemy w [Research/PriorArt.md](../Research/PriorArt.md); formalizujemy tylko specyficzne dla POM-1 luki i testy.

## A. Ścisły wynik dla aktualnego hamiltonianu

Dla \(\Psi_i\in\mathbb C\otimes\mathbb O\simeq \mathbb R^{16}\) i sprzężeń \(\mu^2>0\), \(\lambda_\Psi,K,\epsilon,\gamma\geq0\), \(f>0\):

\[
H=\frac12\sum_i\|p_i\|^2+
\frac{\mu^2}{2}\sum_i\|\Psi_i\|^2+
\frac{\lambda_\Psi}{4}\sum_i\|\Psi_i\|^4+
\sum_i U_{E_8}(\Psi_i)
+\frac K2\sum_{ij}\|\Psi_i-\Psi_j\|^2+
\gamma\sum_{ijk}\|\mathcal A(\Psi_i,\Psi_j,\Psi_k)\|^2 .
\]

Ponieważ \(U_{E_8}\geq0\) dla \(\epsilon\geq0\), każdy inny składnik poza zerowym jest nieujemny, zatem

\[
H\geq \frac{\mu^2}{2}\sum_i\|\Psi_i\|^2\geq0.
\]

Równość \(H=0\) jest osiągnięta przy \(\Psi_i=p_i=0\). Dla \(\mu^2>0\)
jest to jedyne minimum (co do zmiennych \(\Psi,p\)).

**Wniosek POM-1-V1:** *każdy* biliniowy prąd między węzłami, np.
\(J_{ij}\sim\operatorname{Im}(\bar\Psi_i\Psi_j)\), znika w stanie podstawowym.
Nie ma wtedy nieosobliwego układu czterech wektorów brzegowych mogących
pełnić rolę tetrad. Dowód warunkowy dla dowolnej liczby węzłów znajduje
się w [POM1/VacuumObstruction.lean](../POM1/VacuumObstruction.lean).
W Lean „pozostała energia \(\geq0\)” jest jawnym założeniem,
a nie formalizacją całej algebry asocjatora.

To jest **model-specyficzna przeszkoda**, nie ogólne twierdzenie wykluczające
emergentną grawitację z jakiejkolwiek dynamiki bioktonionowej.

Dodatkowo, nawet jednorodny **niezerowy** kondensat \(\Psi_i=\Psi_\star\)
daje \(J_{ij}=0\). Zmiana jedynie znaku \(\mu^2\) nie wystarcza dla
tego konkretnego antysymetrycznego prądu, gdy energia nadal faworyzuje
stan przestrzennie jednorodny.

## B. Liniowe fale: co naprawdę wynika z E₈ i niełączności?

Wokół \(\Psi=0\) potencjał pierwiastkowy ma rozwinięcie

\[
U_{E_8}(\Psi)=\frac{30\epsilon}{f^2}\|\Psi\|^2+O(\|\Psi\|^4),
\]

a asocjator \(\mathcal A\) jest trójliniowy, więc
\(\gamma\|\mathcal A\|^2=O(\|\Psi\|^6)\).

Wynika stąd, że liniowa macierz mas w *każdym* z 16 kanałów jest

\[
m_{\rm eff}^2=\mu^2+\frac{60\epsilon}{f^2}
\]

i nie ma w niej wkładu od \(\gamma\). Nie pojawia się selekcja czterech
kierunków o odmiennym znaku normy ani masowy bezmasowy spin-2.

**Warunkowo**, na wstawionej z góry regularnej 3D sieci z odstępem \(a\)
oraz czasem parametryzującym ewolucję:

\[
\omega^2(\mathbf k)=m_{\rm eff}^2+
4K\sum_{\ell=1}^3\sin^2(k_\ell a/2)
=m_{\rm eff}^2+Ka^2|\mathbf k|^2+O(a^4k^4).
\]

Daje to prędkość kinematyczną \(c_{\rm eff}=a\sqrt K\) w jednostkach
mikroskopowego czasu. Jest to **metryka propagacji modów** znana z
grawitacji analogowej, nie dynamika tetrad i torzji TEGR.
Por. Barceló–Liberati–Visser, DOI [10.1088/0264-9381/18/17/313](https://doi.org/10.1088/0264-9381/18/17/313).

## C. Lokalna konstrukcja diagnostyczna z bioktonionów

Rozpisujemy \(\Psi_i=x_i+I y_i\), \(x_i,y_i\in\mathbb O\). Jedna z
możliwych *definicji testowej*, bez wstawiania niezależnego pola \(e\):

\[
J_{ij}^A=\frac12\operatorname{Im}_A
\left(
\bar x_i x_j+\bar y_i y_j-
\bar x_j x_i-\bar y_j y_i
\right),\qquad A=1,\ldots,7.
\]

Jest ona antysymetryczna \(J_{ji}=-J_{ij}\).
Aby dostać cztery kanały, trzeba jednak **wybrać** macierz projekcji
\(P:\mathbb R^7\to\mathbb R^4\):

\[
e^a_{ij}\overset{\text{def.}}{=}P^a{}_A J^A_{ij},
\quad a=0,\ldots,3.
\]

W tym miejscu cztery kierunki nie są jeszcze wyprowadzone. Jeśli
chcemy formalnie uzyskać \(g_{\mu\nu}=e^a_\mu\eta_{ab}e^b_\nu\),
musimy również **zadeklarować** \(\eta=\operatorname{diag}(-1,1,1,1)\).

Zdefiniowany w ustalonej ramie obieg trójkątny:

\[
C_{ijk}^a=e^a_{ij}+e^a_{jk}+e^a_{ki}.
\]

**Uwaga:** \(C\) jest jedynie *proxy* dla torzji. Fizyczna torzja
teleparalelna wymaga również płaskiej koneksji spinowej:
\(T^a=de^a+\omega^a{}_b\wedge e^b\) i prawidłowej kowariancji
względem lokalnych zmian ramek.

Dla przykładu w łącznej płaszczyźnie zespolonej prąd
\(J(z,w)=\mathrm{Im}(\bar z w)\) daje na trójkącie
\(z_0=1,\ z_1=i,\ z_2=-1\) obieg \(1+1+0=2\).
**Niełączność oktonionowa nie jest konieczna do niezerowego obiegu.**
Wersja testu znajduje się w Lean.

## D. Wynik eksperymentu numerycznego

[Simulations/emergent_geometry_probe.py](../Simulations/emergent_geometry_probe.py)
ewoluuje **oryginalny** hamiltonian POM-1 na pięciu węzłach grafu pełnego
(4-simplex). Geometria tego grafu jest **założona** dla diagnostyki.

Dla ustalonego ziarna generatora:
- macierz 4×4 biliniowych prądów krawędziowych ma rząd 4, \(\det e\approx0.913\);
- normy trójkątnego obiegu przed i po 12 krokach wynoszą odpowiednio
  około 5.97 i 5.82; same prądy i obiegi zmieniają się podczas dynamiki;
- zmiana projekcji 4 spośród 7 kanałów zmienia wyliczoną metrykę (norma
  różnicy ≈ 26.2); nie mamy fizycznego wyboru ramy;
- przypisana sygnatura Lorentza została wstawiona jako \(\eta\);
- w jedynym minimum przy \(\mu^2>0\) wszystkie te prądy znikają.

Zatem umiemy skonstruować **czasowo zmienne, zależne od pól kandydaty**
na dane geometryczne, ale nie wyprowadziliśmy fizycznej tetrady, torzji
ani czasoprzestrzeni. Model pozostaje diagnozą brakujących warunków.

## E. Decyzja architektoniczna dla POM-2

Najmniej arbitralna droga dalszego badania: **geometryczny operator
propagacji z dynamiki**, zamiast bezpośredniego definiowania tetrady
przez cztery ręcznie wybrane współrzędne wewnętrzne.

1. Zdefiniować z \(\Psi\) i grafu operator lokalnych wzbudzeń
   \(\mathcal D_\Psi\). Nie wprowadzać metryki ani tetrad jako niezależnych
   pól w jego definicji.
2. Zbadać jego niskoenergetyczny symbol \(\sigma(\mathcal D_\Psi)\).
   Występowanie izolowanych punktów Weyla nie jest zagwarantowane i
   wymaga nowych stopni swobody lub wykazanego mechanizmu wyłaniania.
3. Jeśli istnieje lokalna dyspersja Weyla, współczynniki liniowe w
   \(\sigma\) mogą określać tetradę. To znana konstrukcja (Laurila–Nissinen
   2020, [DOI](https://doi.org/10.1103/PhysRevB.102.235163)); **nie**
   będziemy ponownie dowodzić ogólnego twierdzenia.
4. Trzeba **osobno** wyprowadzić lokalną symetrię Lorentza, płaską
   koneksję spinową, wzór na tensor torzji i działanie efektywne,
   którego wyraz wiodący byłby \(-M_P^2 T/2\).
5. Sprawdzić bezmasową dynamikę spin-2, uniwersalność sprzężeń z materią
   oraz rygory twierdzeń Nielsen–Ninomiya i Weinberg–Witten **w
   zakresie, w którym spełnione są ich założenia**.

### Kryterium STOP

Jeżeli po wykazaniu niezerowej fazy uporządkowanej operator nie ma
jednoznacznego, czterowymiarowego niskoenergetycznego stożka
przyczynowego albo fluktuacje nie dają działania TEGR, to obecna
realizacja POM-1 nie jest emergentną teorią grawitacji.

**Nie należy utożsamiać wykazania obiegu biliniowego prądu z dowodem
teleparalelizmu.**
