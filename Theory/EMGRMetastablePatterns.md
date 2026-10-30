# POM-4 — sieć bioktonionowa, wzbudzenia fermionowe/bozonowe i przełączanie stabilności przez EM–GR

**Status:** hipoteza efektywna i dokładnie policzalny model toy; **nie jest dowodem**, że znane cząstki są solitonami bioktonionów. Projekt pozostaje całkowicie niezależny od repozytorium Breit–Wheeler.

## 1. Trzy poziomy, których nie należy utożsamiać

1. **Mikrosieć możliwości:** lokalny stan \(\Psi_i=x_i+Iy_i\in\mathbb C\otimes\mathbb O\) i struktura sąsiedztwa, która nadal wymaga mikrodynamiki. Dla niedegenerowanego \(\Delta_i>0\) POM-3 wybiera lokalną podalgebrę \(\mathbb Q_i=\mathbb C\otimes\mathbb H_i\).
2. **Reprezentacje wzbudzeń:** \(\mathbb Q_i\simeq M_2(\mathbb C)\). Kandydat na spinor Weyla to element *lewego modułu* \(S_i\simeq\mathbb C^2\), ale aby był fizycznym **fermionem** potrzebne są stopnie swobody oddane przez CAR, spin połówkowy i prawidłowe kowariantne sprzężenia. Bozonowy parametr porządku lub pola złożone są stopniami parzystymi; sam tensor/bilinear spinora nie jest automatycznie fotonem. Kwantowe rozróżnienie spin–statystyka jest znane (Pauli 1940), nie powielamy jego dowodu.
3. **Konfiguracja i trwałość:** lokalne minimum efektywnego potencjału jest *klasycznie* stabilne na małe jednorodne zaburzenia. Metastabilność konfiguracji nie oznacza automatycznie metastabilnej cząstki. Trwałość fermionu wymaga m.in. normalizowalnego rozwiązania jego równania, zachowanych liczb kwantowych i wykluczonych kanałów zaniku; dla bozonowego solitonu konieczny jest odpowiedni profil przestrzenny, stabilność fluktuacji i często ładunek/topologia.

To oddziela nowe pytanie POM-4 od znanych wyników o spin–statystyce, fermionach związanych z solitonami (Jackiw–Rebbi) i stabilnych Q-ballach (Coleman).

## 2. Własny model POM-4: amplituda wzorca w tle sprzężonych pól

Niech \(s\ge0\) oznacza kwadrat **bezwymiarowej amplitudy bozonowego parametru porządku** danej konfiguracji bikwaternionowego sektora. W pierwszym przebiegu testujemy

\[
V(s;E,G)=a(E,G)s-s^2+s^3,
\quad
a(E,G)=\tfrac14-\tfrac5{48}E+\tfrac1{16}G+\tfrac1{64}EG.
\]

Wszystkie współczynniki są **parametrami demonstracyjnymi**, nie danymi z eksperymentu ani wynikami z E8. Skala energii całego potencjału jest oddzielna. Człon \(EG\) to kontrolowane, mieszane sprzężenie EM–GR; nie twierdzimy, że tak wygląda sprzężenie rzeczywistej materii.

Aby nie używać zależnych od układu odniesienia pól \(|\mathbf E|\) i „siły grawitacji”, proponujemy **nieujemne, bezwymiarowe proxy**:

\[
X_{\rm EM}=\ell_*^8\left[
(\tfrac12 F_{\mu\nu}F^{\mu\nu})^2+
(\tfrac12 F_{\mu\nu}\widetilde F^{\mu\nu})^2
\right],\quad E=\frac{X_{\rm EM}}{1+X_{\rm EM}},
\]

\[
X_{\rm GR}=\ell_*^4 T^2,\qquad
G=\frac{X_{\rm GR}}{1+X_{\rm GR}},
\]

w jednostkach naturalnych; \(T\) oznacza skalar torzji kowariantnego teleparalelizmu wraz z płaską koneksją spinową, a \(\ell_*\) jest postulowaną skalą mikroskopową. **To jeszcze zakłada tetrady i spinową koneksję jako zewnętrzne pola** — nie wyprowadza ich z sieci.

Uwaga krytyczna: dla **null** pola elektromagnetycznego oba lokalne skalary \(F^2\) i \(F\tilde F\) znikają, chociaż fala przenosi energię. Zatem to proxy **nie obejmuje wszystkich możliwych wpływów EM**. Sztuczne przyjęcie lokalnej gęstości energii EM wymagałoby wektora obserwatora, który też należy wyprowadzić.

## 3. Pełna analiza stabilności modelu jednorodnego

Dla zmiennej \(s\):

\[
\partial_s V=a-2s+3s^2,\qquad
\partial_s^2 V=-2+6s.
\]

Dla \(0<a<1/3\) istnieją dwa dodatnie pierwiastki:

\[
s_\pm=\frac{1\pm\sqrt{1-3a}}3;
\quad s_-:\text{bariera},\qquad s_+:\text{minimum niezerowe}.
\]

Stan \(s=0\) jest lokalnym minimum przy \(a>0\) (brzeg dziedziny \(s\ge0\)). Wartość energii w punkcie stacjonarnym:

\[
V(s_\pm)=s_\pm^2(1-2s_\pm).
\]

**Przełączenie globalnego minimum**:

\[
\boxed{a=\tfrac14,\qquad
V(s;\tfrac14)=s(s-\tfrac12)^2\ge0.}
\]

Jeżeli \(a<1/4\), niezerowa faza jest globalnie korzystniejsza, a \(s=0\) pozostaje metastabilne. Jeżeli \(1/4<a<1/3\), \(s=0\) jest globalne, a niezerowe \(s_+\) jest metastabilne. Dla \(a\ge1/3\) zanika oddzielne niezerowe minimum (przy równości zbiega się ze stanem siodłowym).

Z powyższego prawa sprzężenia:

\[
192(a-\tfrac14)=-20E+12G+3EG.
\]

Granica faz to:

\[
\boxed{12G+3EG=20E,\qquad
G_{\rm granica}(E)=\frac{20E}{3(4+E)}.}
\]

W zamkniętym benchmarku \(E,G\in[0,1]\): \(7/48\le a\le5/16\). Oznacza to istnienie *obu* lokalnych minimów na całym diagramie; zmienia się tylko globalne pierwszeństwo. Wartość \(1\) dla znormalizowanych niezmienników to idealizacja graniczna \(X\to\infty\).

**Trzy dokładne przykłady** (dowody algebraiczne w Lean):

| \((E,G)\) | \(a\) | \(s_-\) | \(s_+\) | \(V(s_-)\) | \(V(s_+)\) | Faza |
|---|---|---|---|---|---|---|
| (1,0) | 7/48 | 1/12 | 7/12 | 5/864 | −49/864 | Niezerowa globalna, zero metastabilne |
| (0,0) | 1/4 | 1/6 | 1/2 | 1/54 | 0 | Współistnienie |
| (0,1) | 5/16 | 1/4 | 5/12 | 1/32 | 25/864 | Zero globalne, niezerowa metastabilna |

W trzecim przypadku bariera ponad metastabilnym minimum wynosi \(1/432\) w przyjętych jednostkach. **Nie jest to czas życia**; potrzebne byłoby pełne działanie przestrzenno-czasowe i rachunek procesów przejścia.

## 4. Oba rodzaje wzbudzeń — dozwolony, ale wciąż nieudowodniony schemat

Fermiony modelujemy jako Grassmann-odd pola \(\psi_i\in S_i\simeq\mathbb C^2\) i poprawne antykomutatory CAR; bozony jako Grassmann-even pola lub parametry porządku, z odpowiednimi reprezentacjami i działaniem.

W rozważanej skutecznej teorii \(s\) oznacza **otoczenie i wzorzec**, a nie samą fermionową liczbę cząstek. Możliwe masy zależne od tła:

\[
m_f(s)=m_{f0}+y_f s,\qquad
m_b^2(s)=m_{b0}^2+\lambda_b s.
\]

Te funkcje są tylko przykładem postulowanej odpowiedzi spektralnej. Powstanie normalizowalnego fermionowego modu związanego i stabilnego bozonowego wzbudzenia musi być **osobno wyprowadzone** z operatorów Diraca i fluktuacji. Nie utożsamiamy lokalnych minimów potencjału z elektronami lub fotonami.

Liniowe przenoszenie spinorów między lokalnymi sektorami wymaga \(U^{\rm EM}_{ij}\in U(1)\) i \(L_{ij}\in SL(2,\mathbb C)\), a także map sektorowych \(\mathbb H_i\to\mathbb H_j\). Tych połączeń **nie wyprowadzono jeszcze** z mikroskopowego asocjatora ani z układu E8.

## 5. Możliwe działanie efektywne (nie wyprowadzone z sieci)

Zewnętrzna geometria i pole EM służą na tym etapie do sondowania wpływu na wzorzec:

\[
S_{\rm eff}=\int d^4x\,e\left[
-\tfrac{M_P^2}{2}T-\tfrac14 F_{\mu\nu}F^{\mu\nu}
-\tfrac{Z}{2}g^{\mu\nu}\partial_\mu\chi\partial_\nu\chi
-\Lambda^4 V(\chi^2;E,G)
+\bar\psi(i\gamma^a e_a{}^\mu D_\mu-m_f(\chi^2))\psi
+\mathcal L_{\rm bos}
\right].
\]

\(\chi\) jest bezwymiarowym **bozonowym parametrem porządku**. Zależność \(E,G\) od pól wymaga zmieniania ich razem przy wyprowadzaniu równań ruchu. W szczególności nie można zakładać dowolnego sprzężenia z \(T\) i jednocześnie deklarować pełnej równoważności z GR bez przeliczenia równań. Recenzowane ramy skalar–torzja opracowali Hohmann, Järv i Ualikhanova, *Phys. Rev. D* 97, 104011 (2018), DOI [10.1103/PhysRevD.97.104011](https://doi.org/10.1103/PhysRevD.97.104011).

Przyjęte pola EM i GR są więc **zewnętrznym krokiem efektywnym**, a nie dowodem emergencji z próżni bioktonionowej.

## 6. Znane wyniki, których POM-4 nie powtarza

- **Pauli (1940)**: związek spinu i statystyki w relativistycznej QFT, *Physical Review* 58, 716, DOI [10.1103/PhysRev.58.716](https://doi.org/10.1103/PhysRev.58.716).
- **Jackiw–Rebbi (1976)**: fermionowe mody związane z pewnymi solitonami, *Phys. Rev. D* 13, 3398, DOI [10.1103/PhysRevD.13.3398](https://doi.org/10.1103/PhysRevD.13.3398).
- **Coleman (1985)**: stabilne, naładowane konfiguracje Q-ball, *Nucl. Phys. B* 262, 263, DOI [10.1016/0550-3213(85)90286-X](https://doi.org/10.1016/0550-3213(85)90286-X).
- **Hohmann–Järv–Ualikhanova (2018)**: kowariantny teleparalelizm skalar–torzja, DOI [10.1103/PhysRevD.97.104011](https://doi.org/10.1103/PhysRevD.97.104011).

**Oryginalne, sprawdzalne zadanie POM-4** to wyprowadzić parametry \(a(E,G)\), skuteczne masy i przestrzenno-czasową strukturę wzbudzeń z dynamiki wybranego sektora \(\mathcal Q_i\) oraz zweryfikować ich zgodność z obserwacjami, zamiast dopasowywać wartości po fakcie.

## 7. Kryterium falsyfikacji obecnego wariantu

Jeśli model nie potrafi wyprowadzić spinorowej natury i antykomutacyjnych operatorów fermionowych, nie należy identyfikować wzbudzeń \(\chi\) z fermionami. Jeśli nie daje normalizowalnych stanów, stabilnych profili i prawidłowego sprzężenia z Maxwell/TEGR, diagram fazowy jest **diagramem potencjału toy**, nie katalogiem rzeczywistych cząstek.

**Najbliższy obowiązek:** zdefiniować operator przejścia między lokalnymi \(\mathbb Q_i\), znaleźć normalizowalne sektory fermionowe i dodatnie widmo fizycznych bozonowych fluktuacji przy niezerowym sprzężeniu EM/GR, bez wstawiania tych operatorów ręcznie.
