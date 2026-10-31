import Mathlib

/-!
# POM-5: model-specific two-site singleton-sector selection rules

We assume local Rac/Di labels are determined by even/odd occupation
numbers of a TWO-BOSON-OSCILLATOR Fock model, as in the already published
metaplectic representation. These theorems concern ONLY the choice of
parity-conserving POM-5 inter-site coupling. We do NOT reprove the
Flato–Fronsdal tensor-product decomposition, the oscillator metaplectic
representation, or spin–statistics.

Important: a finite biquaternion M₂(C) is not the full infinite-dimensional
Fock space. This file says nothing about the existence of physical particles.
-/

namespace POM1

/-- Parity of the total oscillator occupation across two sites. -/
def totalSingletonParity (n m : ℕ) : ℕ := (n + m) % 2

/-- Global even parity means BOTH local oscillator parities coincide. -/
theorem even_total_iff_equal_site_parity (n m : ℕ) :
    totalSingletonParity n m = 0 ↔ n % 2 = m % 2 := by
  unfold totalSingletonParity
  omega

/-- A mixed Rac/Di label cannot occur in a globally even state. -/
theorem mixed_singleton_forbidden_in_even_sector (n m : ℕ)
    (hEven : totalSingletonParity n m = 0) :
    ¬ ((n % 2 = 0 ∧ m % 2 = 1) ∨
       (n % 2 = 1 ∧ m % 2 = 0)) := by
  have he := (even_total_iff_equal_site_parity n m).mp hEven
  omega

/-- Adding one oscillator quantum at EACH site preserves total parity. -/
theorem pair_source_preserves_total_parity (n m : ℕ) :
    totalSingletonParity (n+1) (m+1) =
      totalSingletonParity n m := by
  unfold totalSingletonParity
  omega

/-- A pair source maps two even local sectors to two odd sectors. -/
theorem pair_source_even_even_to_odd_odd (n m : ℕ)
    (hn : n % 2 = 0) (hm : m % 2 = 0) :
    (n+1) % 2 = 1 ∧ (m+1) % 2 = 1 := by
  omega

/-- Transport of one quantum from site j to i preserves total parity. -/
theorem single_hop_preserves_total_parity (n m : ℕ) (hm : 0 < m) :
    totalSingletonParity (n+1) (m-1) =
      totalSingletonParity n m := by
  unfold totalSingletonParity
  omega

/-- Moving one quantum between two initially even local sectors makes
    BOTH local sector labels odd when the source site is occupied. -/
theorem one_hop_changes_both_local_labels (n m : ℕ)
    (hn : n % 2 = 0) (hm : m % 2 = 0) (hpositive : 0 < m) :
    (n+1) % 2 = 1 ∧ (m-1) % 2 = 1 := by
  omega

/-- A globally odd state necessarily has distinct local parities,
    as required for mixed Rac⊗Di sectors in this model. -/
theorem odd_total_iff_mixed_parity (n m : ℕ) :
    totalSingletonParity n m = 1 ↔ n % 2 ≠ m % 2 := by
  unfold totalSingletonParity
  omega

end POM1
