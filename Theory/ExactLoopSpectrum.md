# POM-11 — ścisłe widmo i odporna luka tej samej pętli POM-10

Status: 1 listopada 2026. To matematyczne wzmocnienie POM-10, nie wyprowadzenie fizycznego elektronu, 2D/3D pola elektromagnetycznego ani grawitacji TEGR.

## 1. Dokładna reprezentacja hermitowska zamkniętej pętli

Z POM-10 znamy niezmienniczy spinorowy iloczyn Bargmanna B=(2+i)/5 oraz kwadraty amplitud trzech krawędzi 1/2, 1/2, 4/5. Przy odpowiednim cechowaniu lokalnych faz można wybrać

\[
H_{\triangle}=
\begin{pmatrix}
0 &(1+i)/2 &(4-2i)/5\\
(1-i)/2 &0 &(1-i)/2\\
(4+2i)/5 &(1+i)/2&0
\end{pmatrix}.
\]

Rachunek dokładny na liczbach wymiernych zespolonych daje
\[
H_{01}H_{12}H_{20}=(2+i)/5,\quad
\det(\lambda I-H_{\triangle})=
\lambda^3-(9/5)\lambda-4/5
=(\lambda+1)(\lambda^2-\lambda-4/5).
\]

Wartości własne i minimalna luka poziomów tej **skończonej** pętli:
\[
\lambda_1=-1,\quad
\lambda_2=(5-\sqrt{105})/10,\quad
\lambda_3=(5+\sqrt{105})/10,
\]
\[
\boxed{\Delta_{\triangle}=(15-\sqrt{105})/10>47/100}.
\]

Dokładny charakterystyczny wielomian otrzymujemy z rachunku Gaussian-rational (Python fractions.Fraction) dla jawnej macierzy, niezależnie potwierdzonego w Sympy. Formalizacja Lean 4 POM1/LoopSpectrum.lean potwierdza faktoryzację *zdefiniowanego* wielomianu, jego pierwiastki, kolejność poziomów i dokładny dolny bound. Bezpośrednie twierdzenie Lean o Matrix.det pozostaje osobnym zadaniem.

## 2. Odporność, bez powielania twierdzenia Weyla

Dla każdego hermitowskiego zaburzenia o normie operatorowej co najwyżej 1/5 klasyczne twierdzenie Weyla zapewnia, że każda uporządkowana wartość własna przesuwa się najwyżej o 1/5. Wobec tego:

\[
\Delta'_{\triangle}
\ge \Delta_{\triangle}-2\|\delta H\|_{\rm op}
>47/100-2/5
=\boxed{7/100}.
\]

To modelowo-specyficzna, dodatnia dolna granica dla **wszystkich** zaburzeń spełniających podany warunek, a nie tylko dla wybranej próbki. Nie reprodukujemy znanego ogólnego dowodu Weyla. W Lean dowiedziono implikację z dwóch ograniczeń przesunięć do zachowanej luki.

Program Simulations/exact_loop_spectrum.py sprawdza dokładne niezmienniki, 80 niezależnych lokalnych transformacji fazowych U(1) oraz 160 hermitowskich zaburzeń o normie <=0.2.

## 3. Interpretacja i granice

To znacznie wzmacnia część POM-10 opartą na **tej samej pętli**: nie trzeba wprowadzać dodatkowo dwuwymiarowego operatora Qi–Wu–Zhanga, aby wykazać dodatnią, odporną lukę skończoną.

Luka skończona nie jest jednak luką topologiczną w nieskończonym materiale. POM-10 nadal zakłada istnienie 3 potencjalnych węzłów, trójkrawędziowe oddziaływanie chiralne, spinorowy opis lokalnych stanów oraz parametry mikroskopowe. Wynik działa w jednej wspólnej podalgebrze kwaternionowej, dlatego nie dowodzi konieczności pełnych bioktonionów. Nie wyprowadzono jeszcze fizycznego czasu, CAR, 3+1, Maxwell, tetrad ani teleparalelnego TEGR.

## 4. Co dalej

Zdefiniować jedną mikroskopową energię bioktonionową, z której wynikają trójkątny koszt chiralny, dozwolone pętle i operator propagacji; wykazać topologię i prawidłowe widmo przy powiększaniu grafu; dopiero potem budować fermiony, bozony oraz grawitację.

Znane twierdzenia Nivena, Weyla, Artina i Flato–Fronsdala są wykorzystywane i cytowane, nie dublowane.


## Sprostowanie zakresu po recenzji (2 listopada 2026)

Charpoly konkretnej 3×3 macierzy zostało ustalone dokładnym rachunkiem wymiernym w Pythonie; Lean dowodzi własności *zdefiniowanej* kubiki, nie ma jeszcze bezpośredniego twierdzenia Lean dotyczącego Matrix.det tej macierzy. Wzmocniona luka pozostaje **skończonym odstępem poziomów**, nie dowodzi topologii w granicy dużej sieci i nie czyni pełnych oktonionów koniecznymi. POM-10, z którego wzięto pętlę, zawiera wciąż ukryte oddziaływania przy wszystkich wyłączonych krawędziach (szczegóły: [korekta K1](../Research/CorrectionsAfterPeerReview2026.md)).
