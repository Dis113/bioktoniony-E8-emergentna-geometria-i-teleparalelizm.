# POM-6 — operator spektralny z relacji między bioktonionowymi sektorami

**Status (2026-10-31):** hipotetyczny, **skończenie wymiarowy** test połączenia POM-3 z topologicznymi modami fermionowymi. Nie wyprowadza prawdziwych elektronów, bozonów cechowania, czterowymiarowej czasoprzestrzeni, ani grawitacji teleparalelnej.

## 1. Dlaczego to test o wyższej wartości niż przypisywanie sektorom nazw Rac/Di?

Flato–Fronsdal jest twierdzeniem o reprezentacjach AdS4: ogranicza *dozwolone* spiny, lecz nie generuje operatorów propagacji, stabilności ani czasu życia. Nie unieważniamy go — zostaje jako ewentualny test szczególnych symetrii.

Zamiast zakładać pełną niezwartą grupę Sp(4,R) i reprezentacje singletonowe, testujemy związek:

\[
\Psi_i=x_i+Iy_i\in\mathbb C\otimes\mathbb O
\;\xrightarrow[\Delta_i>0]{\rm Artin}\;
\mathbb Q_i=\mathbb C\otimes\mathbb H_i\simeq M_2(\mathbb C)
\;\leadsto\;
D_\Psi=D_\Psi^\dagger .
\]

Twierdzenie Artina oraz struktura bikwaternionów są znane w literaturze.
**Nowym** zadaniem jest wyprowadzenie sprzężeń \(D_\Psi\) z faktycznie wybranych przez stan \(\mathbb H_i\).

## 2. Jawne dwa sektory i ich sprzężenia — nie wstawiamy od razu różnych t

W standardowej konwencji Cayleya–Dicksona modelu POM:

\[
\mathbb H_A=\operatorname{span}\{1,e_1,e_2,e_3\},\qquad
\mathbb H_B=\operatorname{span}\{1,u,v,uv\},
\]

\[
u=(e_1+e_4)/\sqrt2,\qquad v=(e_2+e_5)/\sqrt2.
\]

Oba pojawiają się z niedegenerowanych stanów POM-3. Ich ortogonalne projektory
\(P_A,P_B\in M_8(\mathbb R)\) dają

\[
\boxed{q_{AB}=\tfrac14\operatorname{Tr}(P_AP_B)=\tfrac58},\qquad
q_{AA}=q_{BB}=1.
\]

Macierz \(P_B\) ma przekątną
\((1,3/4,1/2,1/4,3/4,1/2,1/4,0)\); w Lean jest certyfikat sumy
jej iloczynów z przekątną \(P_A\). Powstanie tej przekątnej z rzeczywistego
iloczynu oktonionów sprawdza skrypt Python.

Jako **nową regułę modelową**, nie wyprowadzoną jeszcze z H3, przyjmujemy

\[
\boxed{t_{ij}=t_0+\kappa\,q_{ij}},
\quad q_{ij}=\tfrac14\operatorname{Tr}(P_iP_j),\quad
t_0=0.1,\ \kappa=0.9.
\]

Wtedy

\[
t_{\rm różne}=0.6625,\qquad t_{\rm takie\ same}=1.
\]

**Niezmienniczość:** q jest niezmienniczy przy wspólnej ortogonalnej zmianie
ram wszystkich sektorów, ale sama reguła nie zapewnia lokalnej
niezależności zmian \(\mathbb H_i\) ani pełnej kowariancji Lorentza.

## 3. Świadomie założony graf 1D i dwie fazy

Na łańcuchu 2N węzłów, N=20, ustawiamy *celowo* wzory sektorów:

- Wariant topologiczny: komórki parzyste \((A,B)\), nieparzyste \((B,A)\). Zatem wewnątrz komórki q=5/8, między komórkami q=1.
- Wariant trywialny: komórki parzyste \((A,A)\), nieparzyste \((B,B)\). Wewnątrz komórki q=1, między komórkami q=5/8.

Zatem w uproszczonym kanale skalarnym powstaje znany operator SSH:

\[
D_\Psi=\sum_{i=0}^{2N-2}t_{i,i+1}
\left(|i\rangle\langle i+1|+|i+1\rangle\langle i|\right),
\qquad \Gamma D_\Psi\Gamma=-D_\Psi,
\quad \Gamma_i=(-1)^i.
\]

Odpowiednie bloki spinorowe są \(\mathbb C^2\), a linki \(SU(2)\) pochodzą
z **postulowanego** najbliższego \(SO(3)\) obrotu ram i jego liftu SU2.
Oznacza to świadome wybranie na tym etapie grafu, dimerizacji i reguły
transportu. Nie otrzymaliśmy 1D ani 3+1 z samych bioktonionów.

W znanym modelu SSH funkcja Blocha

\[
h(k)=t_{\rm intra}+t_{\rm inter}e^{-ik}
\]

ma liczbę nawinięć \(|\nu|=1\), gdy \(t_{\rm inter}>t_{\rm intra}\);
w fazie odwrotnej \(\nu=0\). **To wynik z literatury, którego nie dowodzimy ponownie.**
Dla POM własną treścią jest pochodzenie wartości \(t\) z konkretnych projektorów:
\[
\boxed{\Delta_{\rm bulk}=2|t_{\rm inter}-t_{\rm intra}|
=0.675}
\]
w założonym łańcuchu. Gdy wszystkie sektory są identyczne, q=1 na
wszystkich linkach i wyłącznie z reguły overlap **nie powstaje** dimerizacja.
Ta przeszkoda jest wyraźnie zarejestrowana w Lean.

### Wyniki finite-size (nie idealne zera)

N=20, otwarta granica, dwa kanały spinorowe:

| Wzorzec | Minimalne \(|E|\) łańcucha 1-kanałowego | Waga dwóch krawędzi na stanie niskoenergetycznym | Znane \(\nu\) |
|---|---:|---:|---:|
| (A,B),(B,A),... | 0.00014885 | ≈0.5611 | −1 |
| (A,A),(B,B),... | 0.35550 | <0.05 | 0 |

Dla skończonego łańcucha dwa stany brzegowe **hybrydyzują** i mają
niezerowe rozszczepienie ±|E|. W granicy długiego łańcucha zmierza do zera.
To nie dowodzi istnienia fizycznych fermionów w 3+1 wymiarach.
Potrzebna byłaby jeszcze kwantyzacja CAR, energia/ładunek, spin i chiralność.

## 4. Bozony jako fluktuacje zbiorowe — osobna hipoteza

Dla **tych samych** linków definiujemy klasyczny grafowy operator

\[
L_{ii}=\sum_{j\sim i}t_{ij},\qquad L_{ij}=-t_{ij}\quad(i\sim j).
\]

Ma nieujemne wartości własne, pojedynczy zerowy mod dla spójnego łańcucha
i dodatnie wartości pozostałych. Jest to dobrze znany rachunek laplasjanu
grafowego (nie nowa matematyka POM). **Może** służyć jako model spektrum
kolektywnych oscylacji bozonowych, jeśli nadamy zmiennym fizyczną kinetykę.

**Nie uzyskaliśmy w ten sposób fotonu, bozonu cechowania ani grawitonu.**
Dodatkowe symetrie cechowania, fizyczne polaryzacje i prawo oddziaływań
pozostają do wyprowadzenia.

## 5. Odporność i wpływ środowiska

W eksperymencie operator jest hermitowski, ma symetrię chiralną
\(\Gamma D+D\Gamma=0\) i widmo zgodne ze znaną analizą SSH. Chiralnie
zgodne 4% zaburzenie amplitud linków nie niszczy niskoenergetycznego
charakteru modów brzegowych.

Zewnętrzny elektromagnetyczny \(U(1)\) można testować przez
\(D'=\operatorname{diag}(e^{i\theta_i})D\operatorname{diag}(e^{-i\theta_i})\);
widmo nie zmienia się. To test niezależności fazy ramy, nie wyprowadzenie
równań Maxwella.

Jeśli dodatkowo **postulujemy** zewnętrzny parametr deformacji
\(s_{\rm ext}\) mnożący międzykomórkowe linki przez \(e^{-s_{\rm ext}}\),
to krytyczna deformacja dla tego konkretnego łańcucha jest:

\[
s_{\rm crit}=\ln(1/0.6625)\simeq0.4117347.
\]

W punkcie krytycznym zamyka się luka **modelu 1D**, po przekroczeniu
zmienia się liczba nawinięć. Nie utożsamiamy \(s_{\rm ext}\) z torzją
teleparalelną bez dalszych równań.

## 6. Dlaczego „spektralna” nie znaczy „gotowa teoria Connesa”?

Formalna algebra skończona może być przyjęta jako
\(\mathcal A=\bigoplus_i M_2(\mathbb C)\),
\(\mathcal H=\bigoplus_i\mathbb C^2\) i opisany wyżej hermitowski \(D_\Psi\).
Wszystkie wielkości skończone mają dobrą definicję.

Nie dowiedziono jednak, że \((\mathcal A,\mathcal H,D_\Psi)\) z prawidłowym
\(J,\gamma\), warunkami pierwszego rzędu i orientowalnością jest pełnym
modelem spektralnym fizycznego świata. Co ważne: **standardowa** teoria
spektralna wykorzystuje *łączną* algebraiczną strukturę operatorową;
nie wolno po prostu wstawić niełącznej \(\mathbb C\otimes\mathbb O\)
jako zwykłej algebry C*.

Działanie spektralne Chamseddine’a–Connesa prowadzi do dobrze znanych
strukturalnych wyników, ale **nie** wyprowadza automatycznie TEGR
ani fizycznej sygnatury Lorentza z obecnego skończonego grafu.

## 7. Literatura — znane wyniki pozostają znane

- Su, Schrieffer, Heeger, *Solitons in Polyacetylene*, Phys. Rev. Lett. 42 (1979), DOI [10.1103/PhysRevLett.42.1698](https://doi.org/10.1103/PhysRevLett.42.1698).
- Ryu, Hatsugai, *Topological Origin of Zero-Energy Edge States...*, Phys. Rev. Lett. 89 (2002), DOI [10.1103/PhysRevLett.89.077002](https://doi.org/10.1103/PhysRevLett.89.077002).
- Teo, Kane, *Topological defects and gapless modes...*, Phys. Rev. B 82 (2010), DOI [10.1103/PhysRevB.82.115120](https://doi.org/10.1103/PhysRevB.82.115120).
- Chamseddine, Connes, *The Spectral Action Principle*, Comm. Math. Phys. 186 (1997), DOI [10.1007/s002200050126](https://doi.org/10.1007/s002200050126).
- Nielsen, Ninomiya, *A no-go theorem for regularizing chiral fermions*, Phys. Lett. B 105 (1981), DOI [10.1016/0370-2693(81)91026-1](https://doi.org/10.1016/0370-2693(81)91026-1).

## 8. Otwarte bramki matematyczno-fizyczne

1. **Wyprowadzić** graf, dimerizację, sposób liczenia połączeń i linki spinorowe z dynamiki bioktonionowych stopni swobody; obecnie te elementy są zadane.
2. W 3+1 wymiarach zbudować lokalną i unitarną teorię spinorową bez nieobserwowanych duplikacji chiralnych fermionów (twierdzenie Nielsen–Ninomiya ma zastosowanie, o ile spełnione są jego hipotezy).
3. Zidentyfikować fizyczne bozonowe polaryzacje i lokalne transformacje cechowania, nie tylko dodatni grafowy laplasjan.
4. Otrzymać czas, metrykę Lorentza, tetrady, płaską koneksję spinową i skalarną torzję TEGR z odpowiedniej granicy, a nie z zewnętrznego działania.
5. Porównać nowe przewidywania ze skalami rzeczywistymi i obserwacjami.

**Kryterium STOP:** jeśli tylko 1D SSH pozostaje uzyskiwany po wstawieniu grafu i dimerizacji, POM-6 jest modelem topologicznych analogów, nie teorią elementarnych cząstek.


## 9. Ważna przeszkoda w topologicznej stabilności defektów przestrzennych

Odpowiedź na pytanie, czy na podstawie samych sektorów H wolno wyprowadzić
stabilne trójwymiarowe defekty, znajduje się w
[VacuumTopologyAudit.md](VacuumTopologyAudit.md). W POM-3 pełna
rozmaitość minimów to \(V_2(\mathbb R^7)\), o \(\pi_2=0\), choć przestrzeń
samych sektorów kwaternionowych \(G_2/SO(4)\) ma \(\pi_2=\mathbb Z_2\).
Nie wolno utożsamiać tych dwóch fizycznych przestrzeni stanów bez
wyprowadzenia lokalnej symetrii ramy. Ta przeszkoda nie znosi
jednowymiarowego testu SSH, ale ogranicza jego interpretację jako źródła
stabilnych cząstek w 3+1D.
