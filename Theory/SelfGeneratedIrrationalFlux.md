# POM-10 — Czy próżnia sama wybiera niewymierną fazę, pętlę i lukę?

**1 listopada 2026.** Wynik: konstrukcja **warunkowa** z trzema potencjalnymi komórkami, warunkowym wyborem aktywacji trzech krawędzi przy istniejących już oddziaływaniach spinów i chiralną orientacją kwaternionową. Pokazuje, że **nie ma matematycznej przeszkody** do jednoczesnego wyboru niewymiernej fazy Berry'ego i zamkniętego obiegu bez zewnętrznego pola EM. Nie jest wyprowadzeniem lokalnego grafu z nieoddziałujących węzłów ani wynikiem oryginalnego POM-3/8/9; **2D operator widmowy jest nadal postulowany**.

## 0. Czego nie powielamy

- Konkurencyjne sprzężenia i niewspółmierne spirale znane są z klasycznych modeli magnetycznych J1–J2 i Frenkla–Kontorowej, np. Aubry, *Physica D* 7 (1983), 240–258, DOI https://doi.org/10.1016/0167-2789(83)90129-X. Nie dowodzimy ponownie ogólnych twierdzeń o fazach incommensurate.
- Wartość cos(θ)=3/5 wymusza θ/π niewymierne na mocy **znanego twierdzenia Nivena**. Biblioteka mathlib ma już formalny dowód w module Mathlib.NumberTheory.Niven. POM wyłącznie stosuje ten lemat.
- Kalibracja asocjatywna G2 i nierówności formy trójliniowej octonionów są znane, np. Harvey–Lawson oraz przeglądy G2, DOI https://doi.org/10.1007/s00220-024-05052-0. W Lean ich analityczna nierówność jest **jawną hipotezą**, a nie nowym dowodem.
- Faza Bargmanna/Pancharatnama dla trzech spinorów i geometryczny strumień od chiralnych tekstur były już badane m.in. przez Ohgushi–Murakami–Nagaosa, *Phys. Rev. B* 62, R6065 (2000), DOI https://doi.org/10.1103/PhysRevB.62.R6065.
- Efekt Halla bez zewnętrznego pola magnetycznego: Haldane, *Phys. Rev. Lett.* 61, 2015 (1988), DOI https://doi.org/10.1103/PhysRevLett.61.2015; spontaniczny kwantowy anomalny efekt Halla w modelu oddziaływań: Raghu–Qi–Honerkamp–Zhang, *Phys. Rev. Lett.* 100, 156401 (2008), DOI https://doi.org/10.1103/PhysRevLett.100.156401.
- Znany 2D dwupasmowy model Qi–Wu–Zhang: *Phys. Rev. B* 74, 085308 (2006), DOI https://doi.org/10.1103/PhysRevB.74.085308. Nie rekonstruujemy jego ogólnej topologii od nowa.

## 1. Definicja nowej dynamiki (POSTULATY)

Zostają tylko trzy **potencjalne** węzły. Ich obecność oraz możliwość utworzenia każdej z trzech krawędzi są *założone*. Same krawędzie mają dynamiczne zmienne zajętości a12,a23,a31 ∈ {0,1}.

Na każdym węźle stan POM-3 minimalizuje V3 i wyznacza lokalny sektor Q_i=C⊗H_i. Niech u_i będą znormalizowanymi częściami urojonymi jego pierwszego oktonionu, u_i ∈ Im O, |u_i|=1. Definiujemy G2-inwariantną skalarną chiralność

\[
\chi(u_1,u_2,u_3)=
-\operatorname{Re}[(u_1u_2)u_3].
\]

Dla c=<u1,u3>, a=<u1,u2>, b=<u2,u3> mamy z **znanej** kalibracji

\[
\chi^2\le\det\operatorname{Gram}(u_1,u_2,u_3)\le 1-c^2.
\]

**Nowy hipotetyczny potencjał spinowo-grafowy:**

\[
E_{\rm tot}(u,A)=a^2+b^2+c^2-6c-3\chi^2
+\frac{1}{10}(a_{12}+a_{23}+a_{31})
-a_{12}a_{23}a_{31}\,\chi^2.
\]

Ważne: składnik z iloczynem trzech krawędzi **premiuje zamkniętą pętlę**. To założona interakcja trójkątna, a nie wynik poprzedniego hamiltonianu POM; odpowiada na pytanie o możliwość, nie o już udowodnioną emergencję.

Współczynniki 6,3 i 1/10 dobrano do dokładnie rozwiązywalnego przykładu. Nie są parametrami dopasowanymi do pomiarów.

## 2. Dokładna selekcja trójkąta i chiralności

Dla niezamkniętego grafu produkt a12 a23 a31 = 0, a liczba krawędzi m∈{0,1,2}. Znierówności kalibracji:

\[
E_{\rm open}\ge4c^2-6c-3+\frac m{10}
=4(c-\tfrac34)^2-\frac{21}{4}+\frac m{10}
\ge-\frac{21}{4}.
\]

Dla wszystkich trzech krawędzi:

\[
E_{\rm closed}\ge 5c^2-6c-4+\frac3{10}
=5(c-\tfrac35)^2-\frac{11}{2}
\ge-\frac{11}{2}.
\]

Oba dolne ograniczenia są osiągalne dla odpowiednich stanów kwaternionowych. W szczególności wybór

\[
u_1=e_1,\quad u_2=e_2,\quad
u_3=\frac35e_1\pm\frac45e_3,\qquad e_1e_2=e_3,
\]

daje c=3/5, a=b=0, χ=±4/5 i energię dokładnie

\[
\boxed{E_{\rm min}=-11/2}
\]

przy **zamkniętym** trójkącie. Każdy otwarty graf ma energię co najmniej -21/4. Luka energetyczna na rzecz pętli wynosi **1/4**, więc niezależne, jednostajne błędy energii mniejsze niż 1/8 na każdej gałęzi nie zmienią wyboru grafu.

Stany o χ=+4/5 i χ=-4/5 są energetycznie równoważne: model nie wstawia zewnętrznego magnetycznego pola, ale dopuszcza spontaniczne złamanie dyskretnej symetrii chiralnej. Wynik dotyczy dokładnie modelu trzech potencjalnych węzłów, nie **sieci przestrzennej 3D**.

Lean: POM1/SelfGeneratedFlux.lean dowodzi modelowych granic energii **przy założeniu** χ²≤1-c², bez duplikowania znanego twierdzenia o kalibracji G2.

## 3. Samorzutnie wybrany NIEWYMIERNY strumień Berry'ego

Przy minimalizującej konfiguracji trzy spinory koherentne w wybranym sektorze kwaternionowym H (z n_i=u_i w osi e1,e2,e3) mają znany, cechowaniowo niezależny niezerowy iloczyn Bargmanna

\[
B_{123}=
\langle z_1|z_2\rangle
\langle z_2|z_3\rangle
\langle z_3|z_1\rangle
=\frac{2\pm i}{5}.
\]

Zatem **wewnętrzna** faza obiegu:

\[
\boxed{\phi=\arg B_{123}=\pm\arctan(1/2)}
\]

i

\[
\cos(2\phi)=3/5.
\]

Gdyby φ/π było wymierne, twierdzenie Nivena dopuszczałoby
dla cos(2φ) tylko 0, ±1/2, ±1, a nie 3/5. Stąd:

\[
\boxed{\phi/(2\pi)\notin\mathbb Q}.
\]

To wymierne współczynniki potencjału wybrały **niewymierny kąt**, nie odwrotnie. W Pythonie faza |φ|≈0.463647609, a |φ|/(2π)≈0.0737918088.

Faza nie wynika z arbitralnych trzech skalarów z oddzielnymi fazami U(1): wtedy produkt linków jest 1 (czyste cechowanie). Potrzebna jest **nieplanarna tekstura CP1**. Spinorowa przestrzeń i interpretacja z=|n,+⟩ są tutaj **dodatkową hipotezą reprezentacyjną**, nie dowodem istnienia fizycznych fermionów.

Ta konfiguracja leży **całkowicie w jednym wspólnym H**; wybór samych bioktonionów nie jest kluczowy. To uczciwy NEGATYWNY test unikatowości algebry. Jeśli identyczny mechanizm działa w H bez O, nie jest jeszcze specyficznym wyprowadzeniem z pełnej bioktonionowej próżni.

## 4. Przerwa widmowa — DWIE różne wersje

### A. Dokładna skończona pętla (ta sama trójka węzłów)

Definiujemy na zamkniętym trójkącie hermitowski operator z krawędziami
H_ij=⟨z_i|z_j⟩ dla połączonych węzłów i H_ii=0.
Jego wartości własne w obu chiralnych stanach:

\[
\boxed{\operatorname{spec}H_\triangle=
\left\{-1,\frac{5-\sqrt{105}}{10},\frac{5+\sqrt{105}}{10}\right\}.}
\]

Minimalny odstęp między poziomami:

\[
\Delta_{\rm finite}=\frac{15-\sqrt{105}}{10}
\approx 0.475305>0.
\]

To **odporna na niewielkie perturbacje rozdzielczość poziomów**
skończonego układu. **Nie** jest topologiczną luką pasmową w
nieskończonym materiale ani dowodem stabilności cząstki.

### B. Topologiczna luka PASMOWA — osobna hipoteza rozszerzenia 2D

Dodatkowo zakładamy, że ta sama wybrana χ pojawia się jako parametr
masowy w znanym modelu Qi–Wu–Zhang na **zewnętrznie przyjętej siatce 2D**:

\[
H_{\rm QWZ}(k_x,k_y)=\sin k_x\sigma_x+\sin k_y\sigma_y+
[\chi+\cos k_x+\cos k_y]\sigma_z.
\]

Tu **nie wstawiamy zewnętrznego pola B ani fazy Peierlsa**, ale
sam dwuwymiarowy operator kinetyczny i sprzężenie masy z χ są
POSTULATAMI. Otrzymujemy dokładną, czysto algebraiczną tożsamość dla
\(x=\cos k_x,y=\cos k_y\):

\[
\begin{split}
E(k)^2&=(1-x^2)+(1-y^2)+(m+x+y)^2\\
&=m^2+(1+m)(1+x)(1+y)+(1-m)(1-x)(1-y).
\end{split}
\]

Dla |m|≤1 i x,y∈[-1,1] wszystkie dodatkowe składniki są nieujemne,
więc E²≥m². Przy m=χ=±4/5:

\[
\boxed{\Delta_{\rm 2bands}\ge 2|m|=8/5=1.6.}
\]

Jeśli dodamy Hermitowskie zaburzenie o normie operatorowej
\(\|\delta H\|\le0.2\), znana nierówność Weyla zachowuje
\(\Delta\ge1.2\). Zgodnie z **już opublikowanym** modelem QWZ
Chern dolnego pasma wynosi tu ±1 (zależnie od znaku χ i przyjętej
orientacji). Test numeryczny FHS daje Chern ±1 na siatce 31×31
oraz pozostaje niezerowy po perturbacji.

**Kontrola negatywna:** dla χ=0 model QWZ zamyka lukę w
punktach Diraca. Oznacza to, że sam dobór masy chiralnej ma znaczenie.
Nie jest to dowód, że hamiltonian grafowy trzech węzłów wyprowadza
QWZ i fizyczne dwuwymiarowe pole fermionowe.

## 5. Częstotliwości i ułamki łańcuchowe — test dodatkowy

W znanym modelu frustracji J1–J2, dla ustalonego jednorodnego
kąta skrętu θ między sąsiednimi kierunkami:

\[
E_{\rm spiral}(\theta)=-12\cos\theta+5\cos2\theta
=10(\cos\theta-3/5)^2-43/5.
\]

Minimum odpowiada cosθ=3/5, a z twierdzenia Nivena
θ/π jest niewymierne. Wprawdzie tutaj θ=2|φ|, ale
równość udziału 3/5 obu niezależnych sprzężeń została
**dobrana modelowo**, nie wyprowadzona z jednej
uniwersalnej stałej mikrostruktury.

W skończonym zamkniętym łańcuchu niewymierny stały skręt
nie jest dokładnie periodyczny — ułamki łańcuchowe organizują
przybliżenia na większych rozmiarach. Żaden wybrany
ułamek ani złota proporcja nie jest automatycznie uprzywilejowany.

## 6. Rozstrzygnięcie i lista obowiązków

**Co udało się w nowym TOY modelu:**
1. Dynamiczne wybieranie trzech krawędzi z ośmiu dostępnych grafów.
2. Samorzutne wybieranie dwóch przeciwchiralnych konfiguracji, bez EM.
3. Niewymierna faza Berry'ego φ/(2π) z wymiernych współczynników.
4. Ścisła luka poziomów tej samej zamkniętej pętli.
5. Warunkowa, stabilna topologiczna luka w oddzielnie **zadanym**
   operatorze 2D.

**Czego nie udało się wyprowadzić z dotychczasowej teorii POM:**
- Liczby potencjalnych węzłów, ich dostępnych krawędzi,
  chiralnej interakcji trójkątnej i współczynników.
- Lokalnych fizycznych spinorów ze statystyką Fermiego,
  fizycznego h i związku fazy Berry'ego z elektromagnetyzmem.
- Z takiej małej pętli **pełnej sieci przestrzeni 3+1**,
  operatora QWZ z wymuszonej mikrodynamiki i prawdziwych
  topologicznych pasm w realnym Wszechświecie.
- Lokalnej symetrii Lorentza, tetrad, spinowej koneksji,
  torzji i działania TEGR.
- Specyficzności dla bioktonionów względem zwykłych
  kwaternionów (obecny kontrprzykład działa we wspólnym H).

**Werdykt:** trzy warunki są wzajemnie zgodne i można je
matematycznie spełnić bez zewnętrznego strumienia na
minimalnym modelu. Jednak oryginalne POM-3/8/9 nie
wyprowadzają jeszcze tej dynamiki. To program badań,
nie potwierdzona teoria fundamentalnej próżni.


## POM-11 correction: exact spectral certificate for this SAME triangle

[ExactLoopSpectrum.md](ExactLoopSpectrum.md) now provides an independent exact Gaussian-rational calculation of the Hermitian 3-node triangle charpoly, and formal Lean polynomial-root and lower-gap inequalities. The exact spacing >0.47 survives Hermitian perturbations of norm <=0.2 with margin >0.07 (conditional on the classical Weyl theorem). This is a stronger result than the earlier numerical finite-spectrum test, but it is STILL a finite-loop level spacing, not a 2D bulk Chern gap or physical electron.


## Korekta K1 po recenzji naukowej (2 listopada 2026)

W historycznym E_10 składniki a²+b²+c²-6c-3χ² nie są mnożone przez binarne zmienne krawędzi. **Nawet przy a12=a23=a31=0 występują więc oddziaływania między trzema stanami**. Przykładowo stany (e1,e2,e1) i (e1,e2,-e1), przy wyłączonych krawędziach, mają energie odpowiednio **-5** i **+7**. To ścisły modelowo-specyficzny kontrprzykład dla interpretacji „wyprowadzono lokalną sieć z pustego, nieoddziałującego grafu”.

Wszystkie historyczne nierówności selekcji trójkąta pozostają poprawne **dla dokładnie podanej energii**, ale ich interpretacja jest węższa: model wybiera zajętość krawędzi w obecności zadanego, nielokalnego sprzężenia tła. Przedefiniowanie E_10 jako sumy *tylko* aktywnych interakcji wymaga nowej analizy minimum.

Ponadto chiralny świadek jest w jednej H, a **dokładna niewymierność** fazy z Nivena nie jest sama przez się stabilna na dowolne małe zmiany parametrów. Bibliografia kalibracji: Harvey–Lawson, *Acta Math.* 148 (1982) 47–157, DOI [10.1007/BF02392726](https://doi.org/10.1007/BF02392726).

Zob. [pełne korekty](../Research/CorrectionsAfterPeerReview2026.md) i [formalny audyt pustego grafu](../POM1/GraphLocalityAudit.lean).
