import Mathlib
import POM1.SpectralLink

/-!
POM-9: EXACT finite POM-specific Fibonacci-sector hopping certificates.

The HOPPING LAW is a new ansatz of POM-9, using quaternion-projector
overlap q_AB=5/8 already verified in POM1.SpectralLink.

The continued-fraction expansion of golden alpha, Hofstadter/TKNN
gap-labeling/Chern and Harper operator results are PRIOR MATHEMATICS.
They are cited, NOT re-proved in this file.

These finite combinatorial certificates do not imply spontaneous
Fibonacci ordering, an emergent magnetic field or Planck-scale physics.
-/

namespace POM1

/-- Rational approximant mechanical word (prescribed, not a ground state).
    Division is Nat Euclidean division. -/
def finiteFibonacciWord (p q : ℕ) (i : Fin q) : ℕ :=
  ((i.val + 1) * p) / q - (i.val * p) / q

/-- Restrict a POM-3 quaternionic sector to either A or B according to
    the prescribed mechanical word. This is NOT dynamically selected. -/
def goldenSector (p q : ℕ) (i : Fin q) : Bool :=
  finiteFibonacciWord p q i = 1

/-- Overlap of two POM-3 sectors, qAA=qBB=1, qAB=5/8. -/
def finiteSectorOverlap (a b : Bool) : ℚ :=
  if a = b then 1 else 5 / 8

/-- POM-9 bond law t = 1+(1/5)*(overlap-1). -/
def fibonacciBond (a b : Bool) : ℚ :=
  1 + (1/5 : ℚ) * (finiteSectorOverlap a b - 1)

theorem equal_sector_bond (a : Bool) :
    fibonacciBond a a = (1 : ℚ) := by
  simp [fibonacciBond, finiteSectorOverlap]

theorem different_sector_bond (a b : Bool)
    (hab : a ≠ b) :
    fibonacciBond a b = (37/40 : ℚ) := by
  simp [fibonacciBond, finiteSectorOverlap, hab]
  norm_num

/-- The finite POM-9 model has only these two hopping magnitudes. -/
theorem bond_is_one_or_thirtyseven_fortieths (a b : Bool) :
    fibonacciBond a b = 1 ∨ fibonacciBond a b = (37/40 : ℚ) := by
  by_cases h : a = b
  · left
    simpa [h] using equal_sector_bond a
  · right
    exact different_sector_bond a b h

def fibonacciWeakCount (p q : ℕ) [NeZero q] : ℕ :=
  ∑ i : Fin q,
    if goldenSector p q i =
      goldenSector p q (i + 1) then 0 else 1

/-- Exact tests of *our* bond assignment, not general proofs of
    Fibonacci continued fractions or Sturmian word combinatorics. -/
theorem fibonacci_weak_count_3_5 :
    fibonacciWeakCount 3 5 = 4 := by
  native_decide

theorem fibonacci_weak_count_5_8 :
    fibonacciWeakCount 5 8 = 6 := by
  native_decide

theorem fibonacci_weak_count_8_13 :
    fibonacciWeakCount 8 13 = 10 := by
  native_decide

theorem fibonacci_weak_count_13_21 :
    fibonacciWeakCount 13 21 = 16 := by
  native_decide

theorem fibonacci_weak_count_21_34 :
    fibonacciWeakCount 21 34 = 26 := by
  native_decide

/-- A uniform, identical biquaternion sector has no variation of
    overlap-induced hopping, irrespective of assigned external flux. -/
theorem uniform_sector_no_bond_modulation (q : ℕ) (i : Fin q)
    (sector : Bool) :
    fibonacciBond sector sector = 1 := by
  simp [equal_sector_bond]

end POM1
