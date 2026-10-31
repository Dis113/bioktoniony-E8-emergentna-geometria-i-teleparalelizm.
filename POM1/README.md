# Formalizacja Lean POM-1

Ta biblioteka formalizuje **wyłącznie matematyczne podtwierdzenia** hipotezy
„Próżnia jako Ocean Możliwości”: bioktoniony, układ korzeniowy E₈,
emergentną geometrię i teleparalelizm.

## Moduł `E8Roots.lean`

- jawna lista 240 pierwiastków E₈ reprezentowanych przez podwojone
  całkowitoliczbowe współrzędne;
- dowód normy pierwiastków;
- tożsamość drugiego momentu `∑_α αᵢ αⱼ = 60 δᵢⱼ`;
- nieujemność zdefiniowanego potencjału cosinusowego;
- algebraiczna tożsamość dotycząca masy przy rozwinięciu kwadratowym.

**Nie ma tutaj dowodu, że E₈ opisuje próżnię fizyczną.**
Nie dowiedziono powstawania tetrad, torzji, metryki Lorentza, fermionów,
oddziaływań Modelu Standardowego ani granicy kontinuum.

## Status metody

Dwa twierdzenia o skończonej enumeracji wykorzystują `native_decide`.
Weryfikacja tych twierdzeń ufa wykonaniu skompilowanego kodu Lean; planowany
jest wariant bez tej zależności.

## Lokalna kompilacja

```sh
lake update
lake exe cache get
lake build
```

Szczegółowe warunki sukcesu: [Theory/ProofObligations.md](../Theory/ProofObligations.md).


## POM-2: progi niestabilności

Moduł FrustratedSpectrum.lean formalizuje kwadratowe formy K3/K5, ich znaki oraz dolną granicę energii dla pięciu węzłów. Parametr mE8 to jawna dana wejściowa; pełny rachunek różniczkowy E8 nie jest tutaj formalizowany. Kompilacja nie dowodzi emergencji metryki czy torzji.


## POM-3 — dynamika wyboru sektora

Moduł SectorVacuum.lean formalizuje dolną granicę i dopełnienie kwadratów
dla konkretnego potencjału modelu POM-3. Nie powiela twierdzenia Artina
ani klasyfikacji podalgebr oktonionowych.

Znany rezultat Artina jest **założonym faktem z literatury**,
potrzebnym do interpretacji Δ>0 jako wyboru H przez bioktonion.
Sama formalizacja Lean dowodzi tylko nierówności nad liczbami rzeczywistymi.


## POM-4 — exact conditional pattern potential

CoupledMetastability.lean formalizes only the **model-specific** coefficient a(E,G), a sixth-order scalar pattern potential and exact rational local extrema/energies. It does **not** reproduce Pauli spin-statistics theorem, prove physical particles, or derive the dynamical EM/GR fields.


## POM-5: singleton-sector selection, not the singleton theorem

SingletonSectorSelection.lean certifies only arithmetic parity constraints for the proposed two-site, quadratic oscillator couplings. It does not recreate the published Flato–Fronsdal decomposition or the metaplectic construction of the so(3,2) singletons. The physical existence of such oscillator Fock fibers in POM is still an unproved assumption.
