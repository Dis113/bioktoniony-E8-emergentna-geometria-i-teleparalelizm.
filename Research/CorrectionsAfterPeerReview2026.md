# Korekty naukowe POM-1–POM-11 po audycie (2 XI 2026)

**Cel:** wyraźnie zawęzić interpretacje, zachowując wyniki matematyczne, testy Lean i numeryczne. Historia POM-1–POM-11 obejmuje **różne alternatywne modele**, a nie jeden udowodniony mikroskopowy hamiltonian.

## K1 — POM-10: pusty graf ma wciąż nielokalne oddziaływania

Historyczny POM-10 definiuje energię trzech spinów i trzech binarnych krawędzi:

\[
E_{10}=a^2+b^2+c^2-6c-3\chi^2+
\frac{n_{\rm edge}}{10}-a_{12}a_{23}a_{31}\chi^2.
\]

Wszystkie krawędzie wyłączone nie oznaczają braku oddziaływania spinów. Dla realizowalnych danych
(u1,u2,u3)=(e1,e2,e1) energia wynosi -5, a dla (e1,e2,-e1) wynosi +7. Różnica wynosi dokładnie **12** mimo pustego grafu.

**Korekta:** poprawne jest zdanie „model wybiera zamknięty trójkąt w obecności już założonego sprzężenia tła”. Niepoprawne byłoby twierdzenie „wyprowadzono lokalną sieć z początkowo nieoddziałujących komórek”. Aby uzyskać takie twierdzenie, trzeba zdefiniować nowy hamiltonian, w którym odpowiednie interakcje są bramkowane aktywacją krawędzi, i ponownie wyznaczyć minimum. Nie przenosimy do niego automatycznie liczb -11/2 i -21/4.

Formalny test: POM1/GraphLocalityAudit.lean; niezależny test: Simulations/scientific_review_regression.py.

## K2 — POM-3: większa symetria potencjału lokalnego

Lokalny V3 zależy od s=norm(x)^2+norm(y)^2 i delty=norm(u)^2 norm(v)^2-(u·v)^2. Części urojone u,v należą do R7. Wspólny obrót z O(7) zachowuje V3 nawet wtedy, gdy **nie** jest automorfizmem mnożenia oktonionowego. Istnieje też odpowiednia symetria dwóch kolumn O(2). Zatem minimum V3 nie wyróżnia fizycznie G2.

**Uwaga:** pełny hamiltonian z dodatnim członem asocjatora nie musi mieć O(7). Na przykład (e1,e2,e3) jest trójką łączną, a (e1,e2,e4) nie. Potencjału lokalnego nie wolno mylić z pełnym hamiltonianem.

Najbliższa literatura: Reehorst, Rychkov, Sirois i van Rees (2025), DOI 10.21468/SciPostPhys.18.2.060. To pokrewna klasa modeli O(N)×O(2), nie dowód dokładnie V3.

## K3 — POM-10: pełne oktoniony nie są jeszcze konieczne

Świadek chiralności u1=e1, u2=e2, u3=(3e1±4e3)/5 należy do jednej kwaternionowej podalgebry. Asocjator tej trójki wynosi zero. Wynik fazowy i skończony spektrogram POM-11 można więc otrzymać bez niełącznej dynamiki pełnych oktonionów.

## K4 — POM-8: właściwa logika kontrprzykładu

Ścisły wymierny świadek z energią E<-12 dowodzi, że wcześniej wskazany konkretny stan o energii -12 nie jest globalnym minimum po dopuszczeniu całej przestrzeni orientacji. **Nie** dowodzi, że wszystkie stany okresu czterech mają E>=-12 ani że wynik L-BFGS-B jest globalny.

## K5 — POM-11: skończona luka i zakres formalizacji

Delta=(15-sqrt(105))/10>0.47 jest minimalnym odstępem między poziomami jawnej macierzy 3×3. Z ogólnego, wcześniej znanego twierdzenia Weyla wynika odporność Delta'>0.07 przy hermitowskich perturbacjach o normie operatorowej <=0.2. To **nie** jest luka pasmowa w granicy termodynamicznej ani dowód stabilności elektronu.

Lean formalizuje wielomian kubiczny, jego pierwiastki i ograniczenia. Bezpośrednie utożsamienie z charakterystycznym wielomianem konkretnej macierzy zweryfikowano niezależnie przez wymierne obliczenia Python; dowód pełnej tożsamości Matrix.det w Lean pozostaje otwarty.

## K6 — Niewymierny kąt nie oznacza automatycznej odporności

Dokładne phi=atan(1/2) jest niewymierną wielokrotnością pi na mocy znanego twierdzenia Nivena. Jednak wymierne wielokrotności pi są gęste, więc **dokładna niewymierność** nie jest otwartą własnością odporną na każde niewielkie zaburzenie. Stabilna może pozostawać luka, jeśli spełnione są jej inne warunki.

## K7 — Korekta bibliograficzna

Właściwym historycznym źródłem kalibracji G2 jest Harvey i Lawson, *Calibrated Geometries*, Acta Mathematica 148 (1982) 47–157, DOI https://doi.org/10.1007/BF02392726. Wcześniejszy odnośnik do pracy Aslana i Trinki (DOI 10.1007/s00220-024-05052-0) dotyczy innego, bardziej szczegółowego problemu G2 i nie powinien zastępować podstawowego źródła kalibracji.

Reehorst et al. (2025) badali pokrewne modele pola i punkty stałe renormalizacji, a nie specyficzny wzór POM. Lisi (2026), DOI 10.1007/s00006-026-01447-5, opublikował recenzowaną pracę o algebrach dzielenia i trialności, lecz nie dowodzi empirycznej unifikacji.

Pokrewne materiały Giesela z 2026 r. w SSRN pozostają preprintami bez potwierdzonej recenzji czasopisma (m.in. https://ssrn.com/abstract=7193998 i https://ssrn.com/abstract=7600498).

## K8 — Strategia na następną publikację

Zdefiniować jeden konkretny hamiltonian z **krawędziowo lokalnymi** oddziaływaniami, porównać O(7) versus H versus O przy tych samych parametrach, wykazać lub wykluczyć istotną rolę asocjatora, a dopiero następnie przejść do propagacji fermionów, fotonów i TEGR.

Wyniki Lean i CI dotyczą matematycznych implikacji danego modelu, nie obserwacyjnego potwierdzenia fundamentalnej teorii.

**Uwaga organizacyjna:** cały program POM pozostaje odrębny od badań Breit–Wheeler. Żadne pliki w tym drugim projekcie nie są modyfikowane.
