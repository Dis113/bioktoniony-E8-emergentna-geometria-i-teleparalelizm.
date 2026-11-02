# POM-13 — Gładki, globalnie stabilny model na pełnej przestrzeni bioktonionów

**Data: 2 listopada 2026 · Status: udowodniona własność nowego warunkowego hamiltonianu, NIE fizyczna teoria próżni.**

## 1. Jaki problem rozwiązujemy?

POM-12b porównywał energię oktonionową i kwaternionową wyłącznie przy
ustalonych lokalnych amplitudach z próżni POM-3. Gdyby wprost do pełnego
pola wprowadzić ujemny kwadrat nieznormalizowanego asocjatora, energia
miałaby człon \(-g t^6\), podczas gdy dodatni potencjał V3 wzrasta jak
\(t^4\). Energia byłaby nieograniczona od dołu.

Dodatkowo rzeczywisty projektor na H_Psi jest nieciągły / nieokreślony,
gdy części urojone x i y nie są liniowo niezależne. Użycie projektora
w hamiltonianie na całej 16-real-wymiarowej przestrzeni jest więc
bez dodatkowej konstrukcji nieuzasadnione.

POM-13 usuwa **oba** problemy za pomocą nowego, jawnego
zmiękczonego tensora sektorowego, bez sztucznego wyboru pierwszej
osi i z zachowaniem niezależnych centralnych rotacji U(1) w statycznej
energii.

## 2. Solidna podstawa w opublikowanej matematyce (nie dowodzimy ponownie)

**Harvey–Lawson (1982), Acta Math. 148, s. 47–157,
DOI https://doi.org/10.1007/BF02392726, Theorem IV.1.6:**
dla u,v,w w Im O ich asocjator spełnia

\[
\varphi(u,v,w)^2+\frac14\|[u,v,w]\|^2
=\det {\rm Gram}(u,v,w).
\]

W szczególności
\(\|[u,v,w]\|^2\le 4\|u\|^2\|v\|^2\|w\|^2\).
To ograniczenie wykorzystujemy, a nie formalizujemy ponownie.

**Knarr–Stroppel (2025), Journal of Algebra 664, 42–74,
DOI https://doi.org/10.1016/j.jalgebra.2024.10.004:**
klasyfikacja podalgebr realnych i rozszczepionych oktonionów, w tym
przypadków kwaternionowych. POM-3 używa znanego twierdzenia Artina.

**Grigorian (2017), Advances in Mathematics 308, 142–207,
DOI https://doi.org/10.1016/j.aim.2016.12.003:**
oktonionowe wiązki, koneksje, spinory i operator Diraca.
Wciąż NIE posiadamy w POM-13 analogicznego poprawnego
niezależnego transportu G2 między węzłami.

**Reehorst et al. (2025), SciPost Physics 18, 060,
DOI https://doi.org/10.21468/SciPostPhys.18.2.060:**
znana klasa modeli pola O(N)×O(2), pokrewna lokalnemu V3.

**Konopka–Markopoulou–Severini (2008), Phys. Rev. D 77, 104029,
DOI https://doi.org/10.1103/PhysRevD.77.104029:**
dynamiczne grafy i możliwość emergentnej lokalności,
której trójwęzłowy POM-13 jeszcze NIE wyprowadza.

**Giesel (preprint SSRN 7600498, 12 października 2026):**
znormalizowany asocjator, wybór próżni i jego widmo to
już niezależnie sformułowane pytania badawcze.
Źródło: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7600498.
To nierecenzowany rękopis; nie należy przypisywać POM
pierwszeństwa samej idei normalizowania asocjatora.
Nasza propozycja dotyczy konkretnego gładkiego tensora sektorowego
zachowującego symetrię centralnego U(1), a nie nowego ogólnego
twierdzenia z teorii oktonionów.

## 3. Nowa, gładka definicja sektora dla wszystkich 16 składowych

Niech \(\Psi=x+Iy\in\mathbb C\otimes\mathbb O\),
\(u=\operatorname{Im}x\), \(v=\operatorname{Im}y\in\mathbb R^7\)
i \(w=u\times v=\operatorname{Im}(uv)\).
Dla parametrów POM-3
\(\alpha=9/20,\lambda=4/5,\eta=1/5\) mamy
\(r=\alpha/(\lambda-\eta)=3/4\),
\(a=r/2=3/8\), \(V_{\min}=-27/320\).

Definiujemy dodatnio półokreśloną macierz

\[
M(\Psi)=uu^{\mathsf T}+vv^{\mathsf T}
+\frac1a ww^{\mathsf T},\qquad t=\operatorname{Tr}M,
\]

a następnie nowy miękki tensor

\[
\boxed{
R(\Psi)=\frac{36a}{(t+3a)^2}M(\Psi).
}
\]

**W przeciwieństwie do prawdziwego projektora, R jest określona
i gładka także przy u=v=0 oraz przy Δ=0.** Nie jest idempotentem
poza powierzchnią minimów POM-3.

Ponieważ
\((t+3a)^2-12at=(t-3a)^2\ge0\), dla każdego stanu

\[
R\succeq0,\qquad
0\le\operatorname{Tr}R=
\frac{36at}{(t+3a)^2}\le3.
\]

Dla prawdziwego minimum V3:
\(\|u\|^2=\|v\|^2=a,\ u\cdot v=0\),
wówczas \(M=aP_{\operatorname{Im}\mathbb H_\Psi}\)
i \(t=3a\), więc

\[
\boxed{R(\Psi_{\min})=P_{\operatorname{Im}\mathbb H_\Psi}.}
\]

Pod centralnym obrotem fazy w danym węźle,
\(u'=u\cos\theta-v\sin\theta\),
\(v'=u\sin\theta+v\cos\theta\):
macierz \(uu^T+vv^T\) pozostaje stała, a
\(u'\times v'=u\times v\).
Zatem **R jest niezmiennicza względem niezależnego lokalnego
U(1) w statycznym potencjale**. Nie wyprowadziliśmy jednak
lokalnej teorii cechowania dla pochodnych czasowych.

## 4. Nowy ograniczony funkcjonał trzech sektorów

Niech \(T_{abc}^{\ d}\) oznacza tensor asocjatora
na \(\operatorname{Im}\mathbb O\), z rzeczywistymi
współrzędnymi bazowymi.
Definiujemy

\[
\boxed{
Q(\Psi_1,\Psi_2,\Psi_3)=
\frac1{108}T_{abc}^{\ d}T_{efg}^{\ d}
R_1^{ae}R_2^{bf}R_3^{cg}.
}
\]

Jest to ciągły i gładki funkcjonał wszystkich 48 składowych
trzech lokalnych bioktonionów.

**Kluczowy, literaturowo ugruntowany bound:**
każda R_i jest PSD i ma ślad co najwyżej 3.
Po diagonalizacji każdej R_i i użyciu nierówności
Harveya–Lawsona dla trzech wektorów własnych dostajemy

\[
0\le
T_{abc}^{\ d}T_{efg}^{\ d}
R_1^{ae}R_2^{bf}R_3^{cg}
\le4\operatorname{Tr}R_1\operatorname{Tr}R_2
\operatorname{Tr}R_3\le108,
\]
czyli

\[
\boxed{0\le Q\le1}
\quad\text{dla wszystkich amplitud, również Δ=0.}
\]

Ta nierówność używa klasycznych twierdzeń o PSD i kalibracji,
nie jest ogólną nową teorią \(G_2\).
W Lean formalizujemy algebraiczny bound na ślad R i
energetyczne implikacje, przyjmując tensorowe Q∈[0,1]
jako jawnie opisany krok matematyczny.
Przypadki testowe kontroluje rzeczywisty iloczyn Cayleya–Dicksona.

## 5. POM-13: jeden stabilny, pełnoamplitudowy model trzech węzłów

Niech \(a_{12},a_{23},a_{31}\in\{0,1\}\). Definiujemy:

\[
\boxed{
H_{13}(\boldsymbol\Psi,\boldsymbol a)
=\sum_{i=1}^3\big[V_3(\Psi_i)-V_{\min}\big]
+\frac14(a_{12}+a_{23}+a_{31})
-2a_{12}a_{23}a_{31}\,Q(\Psi_1,\Psi_2,\Psi_3).
}
\]

Oba człony sprzężenia są bramkowane obecnością krawędzi:
**dla grafu pustego nie ma oddziaływań między różnymi węzłami.**
Lokalny potencjał V3 pozostaje aktywny jako energia każdej komórki.

Znana i już formalnie dowiedziona w POM-3 nierówność
\(V_3(\Psi_i)\ge V_{\min}\) oznacza, że energia
każdego grafu niepełnego jest nieujemna.
Przy trzech aktywnych krawędziach i Q≤1:

\[
H_{13}\ge3/4-2=-5/4.
\]

Ogólny bound dla wszystkich ośmiu grafów:

\[
\boxed{H_{13}\ge-5/4.}
\]

Co więcej, V3 rośnie co najmniej jak
\((\lambda-\eta)(\|\Psi\|^2-r)^2/4\) dla dużych amplitud,
podczas gdy Q pozostaje ograniczone.
Stąd H13 jest **koercywny** na
\(\mathbb R^{48}\) przy każdym wybranym grafie.
Z ciągłości i standardowego twierdzenia Weierstrassa
wynika istnienie **globalnego minimum** na sumie ośmiu
skończenie wymiarowych gałęzi.

To usuwa słabość POM-12: nie wymaga sztucznego
zamrożenia amplitud ani niedegenerowanych sektorów
przy definiowaniu energii.

## 6. Ścisłe rozdzielenie faz H i O na PEŁNYCH polach

Bierzemy stany lokalnie minimalizujące V3:

\[
\begin{aligned}
\Psi_1&=\sqrt a\,(e_1+I e_2),\\
\Psi_2&=\sqrt a\,(e_2+I e_3),\\
\Psi_3&=\sqrt a\,(e_4+I e_5).
\end{aligned}
\]

To dokładnie trzy podalgebry \(H_A,H_A,H_C\)
użyte wcześniej w POM-12b.
Dla tych stanów R=P_ImH, a POM-12b ustalił
dokładnie Q=4/9, więc

\[
H_{13}(\Psi_{\rm witness},\text{pełny trójkąt})
=3/4-2(4/9)
=\boxed{-5/36<0}.
\]

Dla wszystkich stanów należących do **jednej wspólnej**
łącznej podalgebry \(\mathbb C\otimes\mathbb H\)
mamy Q=0 i
\(H_{13}=\sum(V_3-V_{\min})+\frac14\,n_{\rm edge}\ge0\).
Pusty graf z lokalnymi minimami V3 realizuje
wartość zero.

**Nowy wynik POM-13 (warunkowy względem definicji H13):**

\[
\boxed{
-5/4\le\min_{\mathbb C\otimes\mathbb O}H_{13}
\le-5/36
<\min_{\text{jedna wspólna }\mathbb C\otimes\mathbb H}H_{13}=0.
}
\]

Ponieważ energia globalnego minimum w O jest ujemna,
a każdy graf niepełny ma energię nieujemną,
**każde globalne minimum tego modelu oktonionowego
ma aktywne wszystkie trzy krawędzie.**

Nie twierdzimy, że -5/36 jest globalnym minimum po stronie O:
to wartość dopuszczalnego stanu próbnego.
Nie twierdzimy również, że cały Wszechświat
powstaje z trzech węzłów ani że H13 wynika
bez postulowania z fundamentalnej akcji.

## 7. Weryfikacja numeryczna i Lean 4

Nowe pliki:
- [POM1/SmoothFullAmplitudeLoop.lean](../POM1/SmoothFullAmplitudeLoop.lean):
  scalar trace bound R, dokładny bound V3 z istniejącego
  POM-3, energia wszystkich gałęzi grafu, świadek
  -5/36 i wymuszona kompletność grafu dla ujemnej energii.
- [Simulations/smooth_full_amplitude_loop.py](../Simulations/smooth_full_amplitude_loop.py):
  pełny tensor 7×7×7×7 asocjatora, 150
  losowych 48-wymiarowych konfiguracji, zdegenerowane
  pola, 100 niezależnych faz lokalnych U1, 40
  przypadków wspólnej H i skalowanie amplitud.
  Weryfikuje też istnienie stanu Q=4/9,
  E=-5/36 oraz asymptotyczny wzrost energii.

**Uwaga formalna:** dowód ogólnej nierówności
tensorowej Q≤1 i pełne twierdzenie o koercywności
w przestrzeni macierzy nie zostały jeszcze
w całości sformalizowane w Lean. Są wykazane
analitycznie z cytowanych znanych wyników.
Tę lukę formalizacyjną pozostawiamy otwartą.

## 8. Krytyczna ocena nowości

Gładkie normalizowanie wielkości asocjatora jest
znane jako ogólna strategia w matematyce i
fizyce efektywnej. Niezależny preprint Giesela
z 12 października 2026 (SSRN 7600498)
również analizuje znormalizowane
inwarianty asocjatorowe.
Nie przypisujemy więc POM pierwszeństwa
samej idei normowania asocjatora ani
pierwszego użycia G2, kwaternionów czy
dynamicznego grafu.

**Własną propozycją POM-13** jest konkretny
gładki tensor R na pełnej przestrzeni
bioktonionów, zgodny z istniejącym POM-3
i ograniczeniem niełączności, oraz
ścisłe porównanie energii H/O bez
zamrażania amplitud.

Największe otwarte zadania pozostają:
geneza znaku i wartości sprzężenia
-2Q, lokalny transport G2 pomiędzy
niezależnymi włóknami, geometria
w dużych grafach i jej termodynamika,
prawidłowa kwantyzacja fermionów i bozonów,
fizyczny czas, tetrady, Maxwell i TEGR.

**Werdykt:** POM-13 znacząco poprawia
matematyczną spójność wcześniejszego
POM-12. Nadal pozostaje hipotetycznym
skończeniewymiarowym modelem,
a nie potwierdzoną teorią materii i grawitacji.
