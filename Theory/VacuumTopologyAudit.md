# POM-6 — topologiczny test przeszkody: rzeczywisty stan próżni kontra sama podalgebra

**Status:** wniosek logiczny z *istniejących* twierdzeń topologicznych, nie nowy formalny dowód twierdzeń o grupie G₂. Rozstrzyga, kiedy wolno mówić o topologicznie chronionych defektach bioktonionowej próżni.

## 1. Dwa różne zbiory stanów z POM-3

Potencjał POM-3 miał minima z dwoma ortonormalnymi wektorami u, v w Im O ≅ R⁷:

\[
\mathcal M_{\rm pełna} \cong V_2(\mathbb R^7)
=\{(u,v):\|u\|=\|v\|=1,\ u\perp v\}.
\]

Ustalona skala normy nie zmienia typu topologicznego. To 11-wymiarowa rozmaitość Stiefela. Nie jest ona tożsama z przestrzenią niezorientowanych na ramę sektorów kwaternionowych

\[
\mathcal M_{\rm sektor}=G_2/SO(4),
\]

która ma wymiar 8. Stan pełny wybiera więcej niż samą podalgebrę: wskazuje także uporządkowaną ramę wewnętrzną. Istnieje naturalna mapa zapominająca ramę

\[
p:V_2(\mathbb R^7)\longrightarrow G_2/SO(4).
\]

Jeżeli wewnętrzne SO(3) przejścia nie są lokalną symetrią cechowania, para (u,v) jest **fizyczną zmienną modelu**, a nie tylko wyborem reprezentacji sektora.

## 2. Znana matematyka: nie dublujemy dowodów

- Akbulut i Kalafat, *Algebraic topology of G2 manifolds*, Expositiones Mathematicae **34** (2016), 106–129, DOI [10.1016/j.exmath.2015.03.004](https://doi.org/10.1016/j.exmath.2015.03.004). Omawia m.in. połączenia przestrzeni Stiefela i grassmannianów.
- Gayet i Witt, *Deformations of associative submanifolds with boundary*, Advances in Mathematics **226** (2011) 2351–2370, DOI [10.1016/j.aim.2010.09.014](https://doi.org/10.1016/j.aim.2010.09.014). W szczególności znana topologia przestrzeni G₂/SO(4).

Z tych wyników:

\[
\boxed{\pi_2(V_2(\mathbb R^7))=0},
\qquad
\boxed{\pi_2(G_2/SO(4))\cong\mathbb Z_2}.
\]

Pierwszy fakt: \(V_2(\mathbb R^7)\) jest 4-spójna. Drugi: \(G_2\) jest połączona i po prostu spójna oraz \(\pi_1(SO(4))=\mathbb Z_2\), więc standardowy długi ciąg homotopii rozstrzyga \(\pi_2\). **Nie dowodzimy od nowa** tych twierdzeń.

## 3. Wniosek specyficzny dla POM

W trójwymiarowej przestrzeni konfiguracje wokół punktowego defektu klasyfikuje mapa ze sfery S² do przestrzeni wartości parametru porządku. Przy **pełnym**, ciągłym i nieosobliwym polu par \((u,v)\) na otaczającej S² powstaje mapa

\[
S^2\longrightarrow V_2(\mathbb R^7).
\]

Jej klasa jest trywialna, a jej obraz w \(G_2/SO(4)\) również jest homotopijnie trywialny. **Nie można więc bez dodatkowej struktury wywnioskować topologicznie chronionych monopoli Z₂ z samego potencjału POM-3.**

Możliwość *nietrywialnego* \(\mathbb Z_2\) sektora wymaga czegoś więcej:
- fizyczny parametr porządku musi być rzeczywiście **samą podalgebrą**, czyli odpowiednim ilorazem przez lokalną redundancję ramy, lub
- pole (u,v) nie może posiadać globalnego gładkiego liftu przez defekt (potrzebna jest osobna konstrukcja wiązki/gauge i zgodność energii oraz ciągłości).

Tego nie mamy. Nie wystarczy arbitralnie „zapomnieć” orientacji ramy.

**To jest ostrzeżenie przeciw nadinterpretacji POM-6:** 1D liczba nawinięć operatora SSH jest dobrze zdefiniowana *w założonym 1D grafie*, lecz **nie** wynika z niej trwałość 3D punktowych defektów bioktonionowej próżni.

## 4. Co testować zamiast powielać znane dowody topologiczne

Nowy program POM ma wyprowadzić jedną z dwóch rzeczy:

1. Z mikroskopowego hamiltonianu **lokalną symetrię ramy** identyfikującą trzy wewnętrzne kierunki i ich połączenie; wtedy rzeczywistym parametrem porządku może być \(G_2/SO(4)\). Trzeba wykazać, że pozostałe tryby są gauge, a nie fizycznymi modami.
2. Jeśli ramy są fizyczne, to znaleźć *inny* mechanizm ochrony (np. symetrię indeksową konkretnego operatora Diraca), nie domniemany 3D topologiczny ładunek \(\pi_2\) próżni.

Dopiero potem testować normalizowalne mody Diraca na takich defektach i ich fermionową kwantyzację.

**STOP:** jeżeli własny potencjał V3 nie wybiera ilorazu ramy jako fizycznej przestrzeni próżni, nie wolno przypisywać stabilności cząstek niezerowemu \(\pi_2(G_2/SO(4))\).
