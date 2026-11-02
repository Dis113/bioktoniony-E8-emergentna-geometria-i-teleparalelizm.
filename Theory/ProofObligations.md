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


| P612 | \(\pi_2(V_2(\mathbb R^7))=0\) vs \(\pi_2(G_2/SO(4))\cong\mathbb Z_2\) | REVIEWED published topology; no duplicate proof |
| P613 | Derive local SO3 gauge redundancy so the physical vacuum is the quotient, or find alternative defect protection | OPEN; see [VacuumTopologyAudit.md](VacuumTopologyAudit.md) |


## POM-7 — spontaneous-sector-ordering gates (2026-10-31)

| ID | Task | Status |
|---|---|---|
| P701 | Old H3 with K>0 and gamma≥0 forces uniform global ground state | Analytical H3 proof; Lean conditional positive-link lemma |
| P702 | J1–J2 ANNNI period-four antiphase at J2>J1/2 | REVIEWED known result, do NOT re-prove |
| P703 | POM-3 projector overlap mapped to binary Ising labels | Lean model-specific identity |
| P704 | New projector frustration has 4 degenerate phases on N=8,12,40 rings | Exact enumeration + min-plus DP; not real-time dynamics |
| P705 | Two terminal spectra among four equal-energy ground translations | Python test of known SSH edge spectrum, 2 topological and 2 trivial |
| P706 | Sector C (q_AC=1/2) has lower trial energy than old B (q_AB=5/8) | Lean exact counterexample |
| P707 | A rational pair of continuous sector orientations has q=178369/390625 | Exact Fraction octonion calculation in Python |
| P708 | Global optimum on full continuous POM-3 vacuum manifold | OPEN: restricted 1-angle optimization not enough |
| P709 | Derive competing projector coupling and 1D graph from microscopic dynamics | OPEN |
| P710 | True 3+1D Lorentzian fermionic spectrum and universal TEGR dynamics | OPEN |
| P711 | Finite positive-temperature order of the 1D short-range model | Not supported; standard absence of finite-T ordering |
| P712 | Select a unique physical boundary termination and gauge transport | OPEN |

[Theory/SpontaneousSectorOrdering.md](SpontaneousSectorOrdering.md) contains the analysis and strict distinctions between mathematical tests and physical interpretations.


## POM-8 — pełna przestrzeń orientacji i certyfikat energii (2026-10-31)

| ID | Test | Status |
|---|---|---|
| P801 | Zredukować minimalizację H8 z gamma=0 do pełnego V₂(R⁷) bez wyboru A/B | ANALITYCZNY argument zastępowania stanu reprezentantem minimum V3; Lean OPEN |
| P802 | Ośmiowęzłowy dokładny wymierny świadek E<-12 | LEAN native_decide (compiler trust) + Fraction Python |
| P803 | Wykazać, że osiem ramek wymiernych jest ortonormalnych | LEAN native_decide + dokładna kontrola Fraction |
| P804 | Wielostartowa optymalizacja pełnego V₂(R⁷), N=8/12/16 | CHECKED numerycznie, nie globalny dowód |
| P805 | Test ograniczenia okresu czterech, N=8 | CHECKED numerycznie E≈−12; globalny dowód dla klasy okres4 OPEN |
| P806 | Niezdimerowany operator spektralny: mody rozciągnięte czy brzegowe | CHECKED energia, waga brzegowa i IPR |
| P807 | Wpływ gamma>0 na wybór sektora; jawny próbny stan gamma=10 | CHECKED modelowo, pełne minimum z gamma OPEN |
| P808 | Wyprowadzenie grafu, J1/J2 i overlap linków z mikrodynamiki | OPEN |
| P809 | Właściwe pola fermionowe, bozonowe, 3+1, EM i TEGR | OPEN |
| P810 | Termodynamiczny limit i dynamika przejść między konfiguracjami | OPEN |

Pełne szczegóły: [FullVacuumOrderAudit.md](FullVacuumOrderAudit.md).


## POM-9 — Planck constant and continued-fraction audit (2026-10-31)

| ID | Claim / task | Status |
|---|---|---|
| P901 | h enters a quantum phase through alpha=ePhi/h, not through h's numerical SI value | KNOWN Hofstadter/Peierls physics, cited |
| P902 | Golden CF approximants 3/5,5/8,8/13,13/21,21/34 | KNOWN number theory; used not reproved |
| P903 | POM-3 projector link hopping is 1 (same) or 37/40 (different) | LEAN exact model-specific identity |
| P904 | Exact weak-link counts 4,6,10,16,26 | LEAN native_decide finite certificates; compiler-trusted |
| P905 | C=-1 for five rational flux cells under proposed link law | Python FHS numerical; not Lean theorem |
| P906 | Sampled spectral gap and conservative full-BZ lower bound | Python + known operator Lipschitz/Weyl estimate; floating eigenvalues not interval-certified |
| P907 | Diagonal onsite perturbation |delta|<=0.08 preserves gap and Chern in this model | Conditional known homotopy/Weyl result + Python endpoint checks |
| P908 | External Hofstadter uniform-link Chern survives if POM overlap modulation is OFF | CHECKED (negative control): so index not generated by bi-octonions |
| P909 | Silver ratio sqrt2-1 has similar spectral stability | CHECKED (negative control): golden is not unique |
| P910 | Derive Fibonacci orientation from full POM-8 vacuum energy, not imposed word | OPEN |
| P911 | Derive EM field, electric charge e, physical time and quantum phase action from POM | OPEN |
| P912 | Derive 3+1 spinor field, particles, TEGR tetrad and proper Planck-length scale | OPEN |
| P913 | Provide interval-certified eigenvalue enclosures and formal model-specific topological stability | OPEN |

Full discussion in [PlanckContinuedFractions.md](PlanckContinuedFractions.md).


## POM-10 — no external magnetic field, but conditional dynamics (2026-11-01)

| ID | Claim | State |
|---|---|---|
| P1001 | Three-edge Boolean network favors closed triangle in the NEW chirality-favoring toy energy | LEAN conditional exact bound -11/2 versus -21/4; calibration inequality imported as hypothesis |
| P1002 | Two chiral signs ±4/5 with same minimal energy and octonion witness | ANALYTIC + Python; FULL POM3/8/9 derivation still OPEN |
| P1003 | Selected geometric Berry phase ±atan(1/2) has irrational φ/π | LEAN applying published Niven theorem under cos(2φ)=3/5; Python checks explicit Bargmann loop |
| P1004 | One 3-node loop has a positive finite-level spacing | Python exact eigenvalue formula check; NOT a thermodynamic band gap |
| P1005 | A separately assumed 2D QWZ operator coupled to χ=±4/5 has bulk gap ≥8/5 | LEAN algebraic identity and inequality; general QWZ topology is KNOWN published work |
| P1006 | Chern ±1 of QWZ when m=±4/5 and remains stable after bounded mass perturbation | Python FHS and KNOWN QWZ theorem; no original topology proof |
| P1007 | Derive possible vertices, link activation and three-edge coupling from earlier bi-octonion H | OPEN |
| P1008 | Derive coherent spinors with physical fermionic CAR rather than POSTULATING CP1 | OPEN |
| P1009 | Derive 2D/3+1 operator, its spatial structure and mass=χ coupling from network | OPEN |
| P1010 | Derive external EM / Planck action, physical hbar, Maxwell and TEGR | OPEN |
| P1011 | Show octonions are NECESSARY: model currently works inside a common quaternion subalgebra | FAILED uniqueness test / OPEN for alternate coupling |
| P1012 | Real time-dependent stability of loops, lifetimes, finite-T phases and full quantum theory | OPEN |

See [SelfGeneratedIrrationalFlux.md](SelfGeneratedIrrationalFlux.md). Do not mistake conditional 3-node dynamical selection for an emergent full 3+1D spacetime.


## POM-11 — finite loop spectral certificate

| ID | Result or obligation | Status |
|---|---|---|
| P1101 | Gaussian-rational Hermitian triangle Wilson invariant and charpoly | WYM exact Fraction Python, symbolic cross-check |
| P1102 | Polynomial factorization, roots and level spacing >47/100 | LEAN |
| P1103 | Conditional stability margin >7/100 given eigenvalue shifts <=1/5 | LEAN, using published Weyl inequality for operator perturbations |
| P1104 | 80 U(1) node rephasings, 160 Hermitian perturbations | NUM; not a proof of generic topological bands |
| P1105 | Fully formal Lean Matrix.det theorem for concrete 3x3 matrix | OPEN (exact polynomial checked independently) |
| P1106 | Derive spinor graph and QWZ/3+1 kinetic operators from microscopic bi-octonion H | OPEN |

See [ExactLoopSpectrum.md](ExactLoopSpectrum.md) and [SelfGeneratedIrrationalFlux.md](SelfGeneratedIrrationalFlux.md).


## Korekty po recenzji — obowiązki krytyczne (2 listopada 2026)

| ID | Obowiązek | Status |
|---|---|---|
| REV01 | Wykluczyć oddziaływania między węzłami, gdy wszystkie krawędzie są wyłączone | **FAIL w historycznym POM-10**: różnica energii 12; Lean + Python |
| REV02 | Odróżnić lokalną symetrię V3 = O(7) od automorfizmów pełnego O przy γ>0 | CHECKED w Python, dodatkowy zapis matematyczny |
| REV03 | Pokazać specyficzną konieczność oktonionów przez ablację H kontra O | OPEN; chiralny świadek POM-10 leży w H |
| REV04 | Ustalić globalne minimum pełnej przestrzeni POM-8 zamiast jednego świadka E<-12 | OPEN |
| REV05 | Stabilność niewymierności kąta przy kontrolowanych perturbacjach | OPEN; sama niewymierność nie jest własnością otwartą |
| REV06 | Bezpośredni certyfikat Lean Matrix.det konkretnego H_triangle | OPEN |
| REV07 | Jeden mikroskopowy hamiltonian i emergentne 3+1, CAR, Maxwell, TEGR | OPEN |

Audyt: [Research/CorrectionsAfterPeerReview2026.md](../Research/CorrectionsAfterPeerReview2026.md).
