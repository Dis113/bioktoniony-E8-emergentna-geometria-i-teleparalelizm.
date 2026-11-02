# POM-12 — Co wnosi niełączność? Lokalny graf i kontrola kwaternionowa

**2 listopada 2026 | status: model warunkowy, nie teoria cząstek.** Ten rozdział odpowiada na krytyczną recenzję POM-10: usuwa oddziaływanie spinów przy pustym grafie i daje ścisłą separację między modelem z rzeczywistymi oktonionami a identycznym modelem kwaternionowym.

## 1. Literatura, której nie dowodzimy ponownie

Harvey i Lawson, *Calibrated geometries*, Acta Math. 148 (1982), s. 47–157, [DOI 10.1007/BF02392726](https://doi.org/10.1007/BF02392726), twierdzenie IV.1.6:

\[
\varphi(u,v,w)^2+\frac14\|[u,v,w]\|^2
=\det\big(\langle u_i,u_j\rangle\big),\quad
[u,v,w]=(uv)w-u(vw).
\]

Stąd dla unitarnych wektorów u,v,w w Im(O) otrzymujemy
\(0\le R(u,v,w):=\|[u,v,w]\|^2/4\le1\).
To **opublikowany fakt**, przyjęty jako hipoteza Lean, nie nowe twierdzenie POM.

Powiązane recenzowane prace:
- Baez, *The Octonions*, Bull. AMS 39 (2002), DOI 10.1090/S0273-0979-01-00934-X: algebra, alternatywność, G2.
- Grigorian, *G2-structures and octonion bundles*, Adv. Math. 308 (2017), 142–207, DOI 10.1016/j.aim.2016.12.003: już istniejące oktonionowe koneksje, torzja, Dirac.
- Grigorian, *Smooth loops and loop bundles*, Adv. Math. 393 (2021) 108078, DOI 10.1016/j.aim.2021.108078: niełączne struktury cechowania.
- Konopka, Markopoulou, Severini, *Quantum graphity*, Phys. Rev. D 77 (2008) 104029, DOI 10.1103/PhysRevD.77.104029: dynamiczne krawędzie i emergentna lokalność.
- Levin, Wen, *Colloquium: Photons and electrons as emergent phenomena*, Rev. Mod. Phys. 77 (2005), 871, DOI 10.1103/RevModPhys.77.871: wcześniej opublikowana emergencja wzbudzeń.

## 2. Nowy model specyficzny dla POM

Rozważamy tylko 3 potencjalne węzły. Każdy lokalny stan POM-3 wybiera własny sektor H_i, zaś u_i jest znormalizowanym kierunkiem pierwszego urojonego oktonionu. Trzy bity a_12,a_23,a_31 włączają możliwe krawędzie.

Definiujemy **nową POSTULOWANĄ** energię kontaktu:

\[
E(\mathbf a,\mathbf u)=
\mu(a_{12}+a_{23}+a_{31})
-g\,a_{12}a_{23}a_{31}\,
\underbrace{\frac14\|[u_1,u_2,u_3]\|^2}_{R(\mathbf u)},
\qquad \mu>0,\ g>0.
\]

Ujemna premia za asocjator pojawia się wyłącznie na aktywnym całym trójkącie. Dla dowolnych u_i **E(0,0,0;u)=0**. To usuwa dokładnie wadę starego POM-10. NIE wyprowadza jednak trzech potencjalnych węzłów i nie jest jeszcze lokalne względem niezależnych zmian G2 ram na każdym węźle — brakuje odpowiedniej koneksji transportu.

## 3. Ścisły wynik i próg faz

Dla \(\mu=1/4,g=1\) wszystkie grafy niekompletne mają E>=0; graf pełny ma E=3/4-R>=-1/4.

Świadek w rzeczywistych oktonionach Cayleya–Dicksona:
\(u_1=e_1,\ u_2=e_2,\ u_3=e_4\), więc
\([e_1,e_2,e_4]=2e_7\) i R=1. To daje **E=-1/4**.
Każda komórka może niezależnie być minimum V3 z dwoma ortonormalnymi kierunkami, ale lokalne sektory tych trzech stanów nie należą wszystkie do jednej H.

Dla trójki we wspólnej, łącznej algebrze kwaternionowej H każdy asocjator znika. Przy **tych samych** mu,g i ośmiu grafach minimum wynosi **0**, dla pustego grafu.

Zatem:
\[
\min E_{\mathbb O}=\min(0,3\mu-g),\qquad
\min E_{\mathbb H}=0.
\]

Próg \(g=3\mu\) jest dokładny w tym skończonym modelu. Dla g>3mu model oktonionowy preferuje trójkąt, zaś kwaternionowy pusty graf. Przy mu=1/4,g=1 różnica minimum to 1/4; błędy energii mniejsze niż 1/8 na każdej z dwóch konkurencyjnych gałęzi nie odwracają preferencji.

**Nie jest to absolutne twierdzenie, że żadna teoria wektorowa nie może imitować efektu.** Wektorowy model z ręcznie dodanym tensorem kalibracji G2 może kodować to samo; to separacja H/O dla dokładnie podanego przepisu energii.

## 4. Granica bezpieczeństwa energii: nie rozszerzać naiwnie na pełne amplitudy

To szczególnie istotne. Zmienna u_i to jednostkowy kierunek na **rozmaitości minimów POM-3**, więc R∈[0,1].
Gdyby wstawić ujemny, *nieznormalizowany* kwadrat asocjatora bezpośrednio do hamiltonianu pełnych pól, skalowanie \(\Psi_i\mapsto t\Psi_i\) dałoby ujemny człon rzędu \(t^6\) przy dodatnim lokalnym V3 rzędu \(t^4\). Energia dążyłaby do **minus nieskończoności**.

Wobec tego POM-12 jest na razie teorią zadaną **na ustalonej sferze kierunków i minimów V3**. Pełny hamiltonian musi użyć osobno wyprowadzonej stabilizującej energii wyższego rzędu albo gładkiego ograniczonego niełącznego sprzężenia. Nie wolno przedstawić obecnego wyniku jako globalnej stabilności wszystkich bioktonionów.

## 5. Odtwarzalność, status dowodów i następne kroki

- POM1/HarveyLawsonLoopSelection.lean: własne nierówności 8 grafów, zero na pustym grafie, rozdzielenie H/O, próg i margines perturbacyjny. Nierówność Harveya–Lawsona jest jawnie założona, NIE dowodzona na nowo.
- Simulations/octonion_only_graph_probe.py: dokładny świadek Cayleya–Dicksona i lokalne minima V3, 2500 losowych testów tożsamości i wszystkich grafów, kontrola H i 2000 ograniczonych perturbacji.
- Otwarta praca: ogólne duże grafy; rzeczywiście lokalna koneksja G2; wyprowadzenie znaku i wielkości g z jednego fundamentalnego H; stabilność poza rozmaitością V3; transport fermionów i bozonów; 3+1 i teleparalelizm.
- Nie twierdzimy, że trójwęzłowy graf generuje wynik spektralny POM-11. Ten operator nadal jest osobnym założeniem i wymaga połączenia z POM-12.

**Najuczciwszy cel potencjalnego artykułu:** *Edge-gated associator interactions on finite graphs: a conditional octonion–quaternion ground-state separation.* To jest skoncentrowane i testowalne twierdzenie o modelu, a nie dowód unifikacji fundamentalnej fizyki.
