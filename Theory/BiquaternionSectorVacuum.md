# POM-3 — Próżnia bioktonionowych możliwości i sektory bikwaternionowej realizacji

**Status:** jawny, spekulatywny model pola ze sprawdzalnymi twierdzeniami i testami. Nie jest to potwierdzona teoria próżni, grawitacji ani emergentnego czasu.

## 1. Co jest wynikiem znanej matematyki

Nie dowodzimy ponownie twierdzenia Artina: dowolne dwa rzeczywiste oktoniony generują łączną podalgebrę. Skorzystamy z Baez, *The Octonions*, Bull. AMS (2002), DOI [10.1090/S0273-0979-01-00934-X](https://doi.org/10.1090/S0273-0979-01-00934-X), oraz Knarr–Stroppel, *Subalgebras of octonion algebras*, J. Algebra 664 (2025), DOI [10.1016/j.jalgebra.2024.10.004](https://doi.org/10.1016/j.jalgebra.2024.10.004).

Każdy bioktonion:

\[
\Psi=x+Iy,\quad x,y\in\mathbb O,\quad I^2=-1
\]

należy do co najmniej jednego sektora \(\mathbb Q=\mathbb C\otimes\mathbb H\subset\mathbb C\otimes\mathbb O\). Jeśli części urojone \(u=\mathrm{Im}\,x\), \(v=\mathrm{Im}\,y\) są liniowo niezależne, wyznaczają **jedyny minimalny** kwaternionowy sektor \(\mathbb H_\Psi\).

Wyróżnik:

\[
\Delta=\|u\|^2\|v\|^2-(u\cdot v)^2>0
\]

zapewnia jednoznaczność. Bazę wyznacza się *ze stanu*, bez narzucania czterech kierunków: \(a=u/\|u\|\), \(b=[v-(v\cdot a)a]/\|v-(v\cdot a)a\|\), \(c=ab\). Wówczas

\[
\mathbb H_\Psi=\mathrm{span}_{\mathbb R}\{1,a,b,c\},
\qquad\mathbb Q_\Psi=\mathbb C\otimes\mathbb H_\Psi.
\]

Przy \(\Delta=0\) sektor nie jest jednoznacznie wyznaczony. To wyklucza automatyczny wybór na przykład dla zerowej próżni POM-1 lub dla konfiguracji POM-2 z \(\operatorname{Im} y=0\).

Znana przestrzeń kwaternionowych podalgebr rzeczywistych oktonionów to \(G_2/SO(4)\), wymiar 8; por. Chemtov–Karigiannis, DOI [10.1016/j.exmath.2022.10.004](https://doi.org/10.1016/j.exmath.2022.10.004). Nie formalizujemy ponownie klasyfikacji.

## 2. Własny problem POM-3: czy dynamika może wybrać sektor?

Definiujemy **nowy hipotetyczny** potencjał komórki (16 współrzędnych rzeczywistych):

\[
V_3(\Psi)= -\frac{\alpha}{2}s +\frac{\lambda}{4}s^2-\eta\Delta,\quad
s=\|x\|^2+\|y\|^2,\quad\alpha>0,\quad\lambda>\eta>0.
\]

Nie ma w nim *z góry wybranego* \(\mathbb H\).

Przy \(t=(\operatorname{Re}x)^2+(\operatorname{Re}y)^2\), \(a_2=\|u\|^2\), \(b_2=\|v\|^2\), \(c_2=u\cdot v\):

\[
s=t+a_2+b_2,\qquad
s^2-4\Delta=t^2+2t(a_2+b_2)+(a_2-b_2)^2+4c_2^2\ge0.
\]

Po podstawieniu \(r=\alpha/(\lambda-\eta)>0\) otrzymujemy ścisłe dopełnienie kwadratów:

\[
\boxed{
V_3+\frac{\alpha^2}{4(\lambda-\eta)}
=\frac{\lambda-\eta}{4}(s-r)^2
+\frac{\eta}{4}(s^2-4\Delta)\ge0.
}
\]

**Wszystkie minima** mają

\[
\operatorname{Re}x=\operatorname{Re}y=0,\quad
\|u\|^2=\|v\|^2=r/2,\quad
u\cdot v=0,\quad\Delta=r^2/4>0.
\]

Zatem minimum energii **samo wybiera kwaternionowy sektor dla każdej komórki**. Kierunek sektora w przestrzeni oktonionowej pozostaje dynamicznie zdegenerowany: globalnego jednego \(\mathbb H\) nie wskazaliśmy ręcznie.

Moduł Lean: [POM1/SectorVacuum.lean](../POM1/SectorVacuum.lean) dowodzi tylko **modelowo-specyficznych** tożsamości i dolnej granicy; nie duplikuje twierdzenia Artina.

## 3. Rozszerzenie na sieć

Na razie graf pozostaje założony. Minimalny hamiltonian:

\[
H_3=\sum_i[\tfrac12\|p_i\|^2+V_3(\Psi_i)]
+\tfrac K2\sum_{(ij)}\|\Psi_i-\Psi_j\|^2
+\gamma\sum_{(ijk)}\|\mathcal A(\Psi_i,\Psi_j,\Psi_k)\|^2,
\quad K,\gamma\ge0.
\]

Wybór tej samej minimizującej komórki na każdym węźle osiąga dolną granicę całego modelu: wszystkie linki i asocjatory znikają. Nie tworzy to jeszcze torzji ani propagacji w czasoprzestrzeni.

Jeżeli trzy stany należą do **jednego** bikwaternionowego sektora, ich asocjator jest zerowy; przy różnych sektorach może być niezerowy. Dlatego człon z \(\gamma\) może diagnozować przejścia między sektorami, ale **nie jest** sam w sobie torzją, energią uwięzienia kwarków ani uniwersalną odległością sektorów.

Potencjał \(V_3\) jest niezmienniczy przy globalnym \(U(1)\) obracającym \(x,y\) i przy wspólnym \(G_2\) działającym na oktoniony. Nie daje jeszcze lokalnej symetrii cechowania.

## 4. Degeneracja 11 kierunków

Minima tworzą rozmaitość ortonormalnych 2-ram w \(\mathbb R^7\), tj. \(V_2(\mathbb R^7)\) o wymiarze 11. Sam wybór sektora \(\mathbb H_\Psi\) odpowiada 8-wymiarowemu \(G_2/SO(4)\), reszta to wewnętrzne ustawienie ramy.

Hessian w minimum ma (dla 16 rzeczywistych zmiennych) wartości własne:

\[
\underbrace{0,\ldots,0}_{11},
\quad\eta r,\eta r,\quad2\eta r,2\eta r,\quad2\alpha.
\]

Weryfikuje to niezależne numeryczne różniczkowanie **analitycznego gradientu** w skrypcie POM-3. Są to wewnętrzne płaskie kierunki próżni, a nie udowodnione cząstki bezmasowe propagujące przez fizyczną przestrzeń.

## 5. Bikwaternionowa kinematyka wzbudzenia

Z sektora wybranego przez \(\Psi\) możemy bez wyodrębniania dowolnych 4 z 16 współrzędnych zbudować **realny 4-wymiarowy wycinek**:

\[
\mathcal V_\Psi=\{q=\tau+Iw:\tau\in\mathbb R,\;w\in\operatorname{Im}\mathbb H_\Psi\}.
\]

Norma kwaternionowa daje znaną strukturę Lorentza:

\[
\boxed{q\bar q=\tau^2-\|w\|^2.}
\]

Algebra \(\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)\) realizuje tę strukturę także na macierzach hermitowskich 2×2 poprzez determinant. Jest to **znana matematyka**, nie nowe twierdzenie POM-3: Sangwine–Ell–Le Bihan, *Advances in Applied Clifford Algebras* (2011), DOI [10.1007/s00006-010-0263-3](https://doi.org/10.1007/s00006-010-0263-3); Morita, *Progress of Theoretical Physics* (2007), DOI [10.1143/PTP.117.501](https://doi.org/10.1143/PTP.117.501).

**Osiągnięcie wyłącznie kinematyczne:** POM-3 może wybrać sektor posiadający naturalną wewnętrzną przestrzeń 1+3. Nie wyprowadza to jeszcze fizycznego czasu, 3+1 wymiarów zdarzeń, pola tetrad ani równań Einsteina.

## 6. E8: ograniczenie spójności

Poprzedni cosinusowy potencjał \(U_{E_8}(x,y)\) **łamie** ciągłą globalną symetrię \(U(1)\) tego wariantu. Dlatego dokładne twierdzenia o minimach POM-3 wymagają \(\epsilon=0\). Nie można jednocześnie traktować poprzedniego \(U_{E_8}\) jako dokładnej dynamiki i utrzymywać identycznej degeneracji próżni bez dodatkowej analizy.

E8 pozostaje kandydatem do organizacji dyskretnych stanów lub struktur reprezentacji. Jego fizyczna rola nie została wyprowadzona.

## 7. Otwarte zadania

- Zbudować operator transportu i propagacji wzbudzeń między lokalnie wybranymi \(\mathbb H_{\Psi_i}\), **bez** narzuconej metryki.
- Wyprowadzić lokalny, wspólny stożek przyczynowy, a nie tylko wewnętrzną normę 1+3.
- Ustalić, czy lokalne sektory dostarczają fizycznych tetrad, jak działa spinowa koneksja i czy można wyprowadzić teleparalelne działanie TEGR.
- Zbadać, czy 11 płaskich kierunków daje niepożądane mody przy niskich energiach.
- Uzgodnić E8 i lokalne symetrie oraz znaleźć falsyfikowalne obserwable.

**Kryterium STOP:** jeśli powstaje jedynie wewnętrzna geometria kwaternionowa bez propagacji i uniwersalnej grawitacji, POM-3 jest modelem wewnętrznych sektorów, nie teorią czasoprzestrzeni.


## 8. Test dynamiki sektorów, a nie tylko stanów statycznych

[sector_motion_probe.py](../Simulations/sector_motion_probe.py) realizuje **nowy** hamiltonian sieci z potencjałem V3, dodatnim sprzężeniem sąsiednim K i karą za asocjator z gamma>0. Startuje z pięciu różnych sektorów generowanych przez u,v, nie z narzuconego pola tetrad. 50 kroków metody symplektycznej leapfrog pokazuje zmianę ortogonalnych projektorów na lokalne kwaternionowe podalgebry. W sprawdzonym biegu: odległości Frobeniusa projektorów po ewolucji wynosiły około 0.035–0.058, a względny dryf energii około 3.05×10⁻⁹; gradient zweryfikowano przez różnice centralne.

**Interpretacja ograniczona:** jest to ruch *wewnętrznego sektora* przy założonym grafie i zewnętrznym parametrze aktualizacji. Nie daje jeszcze fizycznej prędkości c, czasu własnego, metryki propagacji ani torzji. Liczby są wynikami deterministycznego testu, nie pomiarami fizycznymi.
