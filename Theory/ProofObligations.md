# POM-1 — otwarte obowiązki dowodowe

Statusy: **PROVED** = sprawdzane kompilacją Lean; **CHECKED** = obliczenia liczbowe;
**OPEN** = brak dowodu; **ASSUMPTION** = przyjęte założenie.

| ID | Twierdzenie / problem | Status | Kryterium |
|---|---|---|---|
| M01 | 240 pierwiastków, norma²=2 | PROVED (enumeracja) | `doubledRoot_norm_sq` |
| M02 | Macierz momentu `Σααᵀ=60I₈` | PROVED (enumeracja) | `root_second_moment` |
| M03 | Nieujemność potencjału cosinusowego | PROVED | `rootPotential_nonneg` |
| M04 | Hessian w zerze wynosi `(60ε/f²)I₁₆` | OPEN | Ścisły formalny rachunek różniczkowy |
| M05 | Wektory enumeracji są różne i zamknięte na odbicia | OPEN | Formalne twierdzenie w Lean, bez samej symulacji |
| M06 | Usunięcie zależności od `native_decide` | OPEN | Dowód kernelowy, audyt aksjomatów |
| D01 | Kwantyzacja dynamiki bioktonionowej | OPEN | Jednoznaczny Hamiltonian samosprzężony lub algebra obserwabli |
| D02 | Powstanie 3+1 wymiarów i sygnatury Lorentza | OPEN | Konstrukcja limitu kontinuum |
| D03 | Symetria Lorentza / wspólny stożek przyczynowy | OPEN | Wyprowadzenie oraz limity naruszeń |
| D04 | Pochodzenie tetrad i torzji | OPEN | Mapa `Ψ, G → e, ω` i dynamika TEGR |
| D05 | Chiralne fermiony i `SU(3)×SU(2)×U(1)` | OPEN | Odpowiednie reprezentacje i anomalie |
| D06 | Uwięzienie koloru | OPEN | Kryterium pętli Wilsona / napięcie struny |
| C01 | Parametry DM/DE z dynamiki mikroskopowej | OPEN | Nie arbitralnie dopasowane `m, V₀` |
| C02 | Przewidywania różniące POM-1 od GR+ΛCDM | OPEN | Falsyfikowalna obserwabla |

**Ograniczenie interpretacji:** potwierdzenie M01–M03 nie rozstrzyga D01–D06.
W szczególności nie dowodzi istnienia komórek próżni ani automatycznej
unifikacji z Modelu Standardowym.


## Wyniki audytu emergencji (2026-10-30)

| ID | Test | Status |
|---|---|---|
| V01 | Przy μ²>0 i pozostałej energii ≥0 zerowy stan podstawowy wymusza Ψ=0 | PROVED: warunkowy dowód `POM1/VacuumObstruction.lean`; pełnego H nie formalizowano |
| V02 | W takim stanie każdy biliniowy prąd Ψ_iΨ_j znika | CHECKED algebraicznie; obserwabla zbudowana w symulacji |
| V03 | W części liniowej masy są jednakowe w 16 kanałach, a człon asocjatora nie wnosi wkładu | DERIVED perturbacyjnie; CHECKED różnicami skończonymi |
| V04 | Prądy mogą wytworzyć niezerowy obieg na trójkącie | PROVED świadek w łącznej płaszczyźnie; CHECKED numerycznie na bioktonionach |
| V05 | Nieosobliwa 4D tetrada w stanie próżni bez arbitralnej projekcji i narzuconej sygnatury | OPEN |
| V06 | Fizyczna torzja zgodna z lokalną symetrią Lorentza | OPEN |
| V07 | Działanie TEGR z limitu mikroskopowego | OPEN |

Szczegóły oraz ograniczenia: [EmergenceBridge.md](EmergenceBridge.md).


## POM-2 (2026-10-30)

| ID | Problem | Status |
|---|---|---|
| P201 | Formy kwadratowe K3/K5 i próg α_c | Formalizacja Lean, identyfikacja mE8 z Hessego pozostaje poza modułem |
| P202 | Ukończenie kwadratów i dolne ograniczenie energii K5 | Formalizacja Lean |
| P203 | Równa energia stanów rangi 2 i 4 dla epsilon=0 | Dowód algebraiczny + test Python; ranki nie są jeszcze udowodnione w Lean |
| P204 | Dodatnie epsilon: istnienie niezerowego globalnego minimum | Analityczny próg + ujemne stany próbne; pełny kształt minimum otwarty |
| P205 | Jednoznaczna selekcja rangi 4 | OPEN |
| P206 | Fizyczne tetrady z sygnaturą Lorentza | OPEN |
| P207 | Globalna U(1) potencjału E8 | FALSE: analityczne rozwinięcie do czwartego rzędu + niezależny kontrprzykład numeryczny |

Patrz [OrderedVacuum.md](OrderedVacuum.md). Zjawiska frustracji XY są już opisane w recenzowanej literaturze.


| P208 | Pełna symetria Weyla E8 przy dodatnim sprzężeniu asocjatora | FALSE dla zastosowanego działania R8: jawny kontrprzykład e1,e2,e4; obliczenie Python, opisana różnica energii 0.04 przy gamma=0.01 |


## POM-4 — coupled EM–GR pattern stability

| ID | Test | Status |
|---|---|---|
| P401 | Exact coexistence and rational barrier energies for V(s)=as−s²+s³ | LEAN: CoupledMetastability.lean (mathematical toy potential) |
| P402 | Mixed coefficient a(E,G), transition boundary 12G+3EG=20E | LEAN algebra; coefficients are inputs, not predictions |
| P403 | 441-grid-point phase consistency | CHECKED via Python, not continuous physical data |
| P404 | Biquaternion matrix representation and fermionic CAR in finite example | KNOWN; numerical consistency check, NOT new spin-statistics proof |
| P405 | Derive bosonic spectrum and spinor bound states for stable patterns | OPEN |
| P406 | Quantify decay lifetime including spatial profiles and tunneling | OPEN |
| P407 | Derive EM field, TEGR tetrad, transport and mixed couplings from microscopic graph | OPEN |
| P408 | Gauge covariance, backreaction, local Lorentz symmetry and conservation laws | OPEN |
| P409 | EM null-wave response without additional preferred frame | OPEN — present scalar proxy blind to null EM waves |

See [EMGRMetastablePatterns.md](EMGRMetastablePatterns.md). Known spin–statistics, Jackiw–Rebbi, Q-balls, and covariant scalar–torsion results are cited, not reproved.


## POM-5 — Di/Rac singleton channel gates (2026-10-31)

| ID | Statement / obligation | Current status |
|---|---|---|
| P501 | Published Rac⊗Rac, Di⊗Di, Rac⊗Di decomposition | REVIEWED, not re-proved |
| P502 | Published even/odd metaplectic Fock decomposition into Rac/Di | REVIEWED, not re-proved |
| P503 | Global parity of POM-5 two-site hopping and SU2-singlet pair source | Lean arithmetic selection + finite matrix test |
| P504 | A globally even state has no single mixed local Rac–Di sector under even evolution | Lean and Python conditional result |
| P505 | Finite biquaternion M2(C) is not an exact two-oscillator Fock representation | Known finite-dimensional CCR trace obstruction, numerically shown |
| P506 | Choose internal SU2 link from two POM-3 sector frames by Procrustes | CHECKED numerically, choice is POSTULATED |
| P507 | Derive intersite transport with a COMMON full Sp(4,R) action | OPEN |
| P508 | Derive the oscillator CCR and energy grading from the graph Hamiltonian | OPEN |
| P509 | Derive AdS4 curvature/scale or a valid alternative to apply singleton theorems | OPEN |
| P510 | Distinguish odd oscillator occupation from physical fermionic CAR | OPEN, not assumed |
| P511 | Photon/electron/graviton existence, production rates and lifetimes | OPEN |
| P512 | Derive EM/GR-dependent pair coupling and backreaction | OPEN |

See [SingletonChannelBridge.md](SingletonChannelBridge.md) for exact scope and links to reviewed literature. POM5 computations do not prove the creation of Standard Model particles.

| P513 | SU2-singlet pair from two local Di doublets has E0=2, total spin0 and is annihilated by diagonal lowering operators (finite low-level witness) | CHECKED numerically; published Di⊗Di contains D(2,0). Not a proof of full module or physical scalar |


## POM-6 — spectral/topological bridge, 2026-10-31

| ID | Mathematical/physical task | State |
|---|---|---|
| P601 | Exact overlap q_AB=5/8 of two explicit quaternion sectors (diagonal projector data) | Lean rational certificate + Python Cayley-Dickson check |
| P602 | Parameter-dependent bond contrast, vanishing contrast for uniform sector | Lean POM-specific algebra |
| P603 | SSH winding/edge-mode theorem and topology | REVIEWED published mathematics, NOT re-proved |
| P604 | Two finite-size spectral phases, edge localization and bulk gaps | Python numerical test on stipulated 1D chain |
| P605 | Local SU2 spin lift and U1 phase covariance | Python conditional test; connection chosen by overlap Procrustes |
| P606 | Nonnegative bosonic graph Laplacian | KNOWN math, checked numerically; no photons yet |
| P607 | Emergence of local 3+1D graph, chirality and Lorentzian propagation from Psi | OPEN |
| P608 | Fully dynamical Dirac and gauge transport from bi-octonion Hamiltonian, not chosen link rule | OPEN |
| P609 | Local gauge spinor CAR, correct SM charges and anomaly cancellation | OPEN |
| P610 | TEGR, torsion and tetrad action from continuum limit | OPEN |
| P611 | Prove overlap dimerization is selected by a global vacuum energy, not manually prepared sectors | OPEN |

Read [SpectralTopologicalBridge.md](SpectralTopologicalBridge.md) before interpreting the 1D results as physical matter.
