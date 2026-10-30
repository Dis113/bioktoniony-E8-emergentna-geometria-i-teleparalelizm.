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
