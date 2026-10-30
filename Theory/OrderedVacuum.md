# POM-2 — uporządkowana próżnia, frustracja i ranga geometrii

**Data:** 2026-10-30  
**Status:** nowa hipoteza dynamiki bioktonionowej z algebraicznymi ograniczeniami i testami numerycznymi. Nie jest to wyprowadzenie fizycznej czasoprzestrzeni.

## 1. Co już wiadomo z recenzowanej literatury

Uporządkowanie 120-stopniowe na trójkątnej antyferromagnetycznej sieci XY oraz dwie przeciwne fazy chiralności były znane wcześniej. Przykład: Bach, Cicalese, Kreutz, Orlando, *Calculus of Variations and Partial Differential Equations* **60**, art. 149 (2021), DOI [10.1007/s00526-021-02016-3](https://doi.org/10.1007/s00526-021-02016-3). Nie przedstawiamy ich jako odkrycia POM-2. Nowy problem dotyczy konsekwencji **konkretnego** bioktonionowego hamiltonianu z potencjałem E8.

## 2. Zmodyfikowany hamiltonian

Dla komórek z 16 rzeczywistymi zmiennymi bioktonionowymi oraz pełnego, *założonego* grafu o n węzłach:

\[
H_2=\frac12\sum_i\|p_i\|^2-\frac\alpha2\sum_i\|\Psi_i\|^2
+\frac\lambda4\sum_i\|\Psi_i\|^4
+\frac K2\sum_{i<j}\|\Psi_i+\Psi_j\|^2
+\sum_i U_{E_8}(\Psi_i)+\gamma\sum_{(i,j,k)}\|\mathcal A_{ijk}\|^2.
\]

Przyjmujemy \(\lambda,K>0\), \(\epsilon,\gamma\ge0\), \(f>0\). Ujemna część kwadratowa i konkurencyjne sprzężenie są **nowymi założeniami POM-2**. Same w sobie nie wyprowadzają tetrad.

## 3. Próg przejścia z zerowej do uporządkowanej próżni

Dokładna tożsamość dla grafu pełnego:

\[
\sum_{i<j}\|\Psi_i+\Psi_j\|^2
=(n-2)\sum_i\|\Psi_i\|^2+\left\|\sum_i\Psi_i\right\|^2.
\]

Z rozwinięcia 240-pierwiastkowego potencjału wokół zera wynika wkład masowy
\(m_{E_8}^2=60\epsilon/f^2\). Asocjator daje pierwsze wkłady dopiero szóstego rzędu amplitudy.

Kwadratowa część energii ma dwa rodzaje modów:

\[
m_{\rm frustrated}^2 = 60\epsilon/f^2-\alpha+K(n-2),
\quad
m_{\rm uniform}^2=60\epsilon/f^2-\alpha+2K(n-1).
\]

Stąd próg:
\[
\boxed{\alpha_c=60\epsilon/f^2+K(n-2).}
\]

Jeśli \(\alpha>\alpha_c\), zerowy stan jest niestabilny w kierunku modów o sumie zerowej. Dodatni człon kwartczny zapewnia koercytywność skończeniewymiarowego hamiltonianu, więc globalne minimum jest osiągane w stanie niezerowym. Nie jest to twierdzenie o pełnej kwantowej próżni.

**Lean:** POM1/FrustratedSpectrum.lean formalizuje dokładną kwadratową formę i jej próg dla K3/K5. Symbol mE8 jest tam parametrem wejściowym — pełne formalne wyprowadzenie Hessego cosinusowego potencjału pozostaje otwarte.

## 4. Ścisła granica energii i problem wymiarowości

Dla \(\epsilon=0\) i \(r^2=[\alpha-K(n-2)]/\lambda>0\) dokładnie:

\[
V=\frac{\lambda}{4}\sum_i(\|\Psi_i\|^2-r^2)^2
+\frac{K}{2}\left\|\sum_i\Psi_i\right\|^2
-\frac{n\lambda r^4}{4}
+\gamma\sum\|\mathcal A\|^2.
\]

Warunki \(\|\Psi_i\|^2=r^2\), \(\sum_i\Psi_i=0\) oraz zerowe asocjatory osiągają globalne minimum

\[
V_{\min}=-\frac{n[\alpha-K(n-2)]^2}{4\lambda}.
\]

Dla **K5** istnieją dwie jawne rodziny w łącznej realnej podalgebrze kwaternionowej (j=0,...,4):

\[
\Psi_j^{(2)}=r\left(\cos\frac{2\pi j}{5},
\sin\frac{2\pi j}{5},0,0\right),
\]

\[
\Psi_j^{(4)}=\frac r{\sqrt2}
\left(\cos\frac{2\pi j}{5},\sin\frac{2\pi j}{5},
\cos\frac{4\pi j}{5},\sin\frac{4\pi j}{5}\right).
\]

Oba zestawy mają jednakową normę każdego stanu, zerową sumę oraz zerowe asocjatory. Ich macierze Grama mają rangi odpowiednio **2** i **4**. Dlatego dokładne minimum POM-2 nie wybiera jednoznacznie czterech niezależnych kierunków.

Uwaga: ranga dotyczy **wewnętrznej** euklidesowej przestrzeni stanów, nie liczby wymiarów czasoprzestrzeni. Nie otrzymaliśmy sygnatury Lorentza ani czterech niezależnych tetrad fizycznych.

## 5. Numeryczny test z dodatnim E8

Reprodukowalny program: Simulations/ordered_phase_probe.py.

- K3: \(\alpha=0.35,K=0.12,\lambda=0.7,\epsilon=0.001,f=1\). Próg \(\alpha_c=0.18\). W ograniczonej zespolonej podalgebrze znaleziono dwa stacjonarne stany o energii około **−0.0311636276** i przeciwnych obiegach **±0.6350112**. To nie jest dowód ich globalnej minimalności w całej algebrze 16D.
- K5: \(\alpha=0.55,K=0.12,\lambda=0.7,\epsilon=0.001,\gamma=0.01,f=1\). Próg \(\alpha_c=0.42\). Dla \(\epsilon=0\) obie konstrukcje osiągają dokładnie **−0.0644642857**. Po dodaniu E8 ich energie wynoszą około **−0.02429840696** (ranga 2) i **−0.02429840641** (ranga 4). Ponieważ są ujemne, zero nie jest globalnym minimum; nie ustalono jednak globalnego minimum przy \(\epsilon>0\).
- Dotychczasowy potencjał E8 **nie** jest niezmienniczy względem dowolnego globalnego obrotu zespolonej fazy U(1). Kontrprzykład numeryczny dla obrotu o \(\pi/4\): \(\Delta U\approx0.00047573119\).

Można wykazać złamanie U(1) także **analitycznie**, a nie tylko numerycznie.
W osi jednego rzeczywistego kierunku pierwiastkowego występuje 28 pierwiastków
o składowej \(\pm1\) i 128 pierwiastków o składowej \(\pm\tfrac12\).
Stąd \(\sum_{\alpha}\alpha_1^2=60\) oraz \(\sum_{\alpha}\alpha_1^4=36\).
Dla \((x,y)=(t e_1,0)\) i obrotu fazy o \(\pi/4\):

\[
U(t e_1,0)=\epsilon\left(30\frac{t^2}{f^2}
-\frac32\frac{t^4}{f^4}+O(t^6)\right),
\]

\[
U(t e_1/\sqrt2,t e_1/\sqrt2)=
\epsilon\left(30\frac{t^2}{f^2}
-\frac34\frac{t^4}{f^4}+O(t^6)\right).
\]

Dlatego

\[
\boxed{\Delta U=\frac{3\epsilon}{4}\frac{t^4}{f^4}
+O(t^6)\ne0}
\]

dla dostatecznie małych niezerowych \(t\) i \(\epsilon>0\). To jest
**model-specyficzna przeszkoda** w identyfikowaniu tej wersji E8
z elektromagnetyczną symetrią cechowania. Zatem nie jest to sam z siebie elektromagnetyczny potencjał cechowania U(1).

## 6. Kryteria następnego etapu

Nie powtarzamy recenzowanych dowodów znanych mechanizmów chiralności ani teleparalelizmu. Potrzebujemy nowych, **specyficznych dla POM** rezultatów:

1. Mechanizm selekcji czterech niezależnych kierunków bez ręcznej projekcji na 4 składowe.
2. Dynamiczne, a nie zadane z góry, relacje sąsiedztwa i efektywny wymiar grafu.
3. Pojawienie się fizycznej sygnatury \((-+++)\) i lokalnej symetrii Lorentza.
4. Lokalnie kowariantna koneksja spinowa, tensor torzji i działanie TEGR otrzymane przez uśrednianie mikrodynamiki.
5. Zgodność widma z obserwowaną propagacją i brak dodatkowych, wykluczonych polaryzacji.

**Wniosek:** POM-2 ma niezerowy stan podstawowy, ale nie wykazał dotąd fizycznej emergencji czasoprzestrzeni. Degeneracja rang 2/4 jest nowym ograniczeniem tej konkretnej konstrukcji.
