import Mathlib

/-!
# POM-1: finite certificates for the E₈ root geometry

A mathematical experiment, not a derivation of spacetime or matter.
Integer coordinates are doubled: ordinary E₈ coordinates are obtained by / 2.
Type A: 112 roots with exactly two ±2 coordinates.
Type B: 128 roots with eight ±1 coordinates and even negative parity.
-/

namespace POM1

/-- The 28 unordered pairs of distinct coordinates in eight dimensions. -/
def coordinatePair : Nat → Fin 8 × Fin 8
  | 0 => (0, 1)
  | 1 => (0, 2)
  | 2 => (0, 3)
  | 3 => (0, 4)
  | 4 => (0, 5)
  | 5 => (0, 6)
  | 6 => (0, 7)
  | 7 => (1, 2)
  | 8 => (1, 3)
  | 9 => (1, 4)
  | 10 => (1, 5)
  | 11 => (1, 6)
  | 12 => (1, 7)
  | 13 => (2, 3)
  | 14 => (2, 4)
  | 15 => (2, 5)
  | 16 => (2, 6)
  | 17 => (2, 7)
  | 18 => (3, 4)
  | 19 => (3, 5)
  | 20 => (3, 6)
  | 21 => (3, 7)
  | 22 => (4, 5)
  | 23 => (4, 6)
  | 24 => (4, 7)
  | 25 => (5, 6)
  | 26 => (5, 7)
  | 27 => (6, 7)
  | _ => (0, 1)

/-- Extract one sign bit, with 0 ↦ +1, 1 ↦ -1. -/
def bitSign (code bit : Nat) : ℤ :=
  if (code / 2 ^ bit) % 2 = 0 then 1 else -1

/-- Coordinate of a doubled root, specified by an index among 240 possibilities. -/
def doubledRoot (root : Fin 240) (i : Fin 8) : ℤ :=
  if root.val < 112 then
    let pair := coordinatePair (root.val / 4)
    if i = pair.1 then 2 * bitSign root.val 0
    else if i = pair.2 then 2 * bitSign root.val 1
    else 0
  else
    let code := root.val - 112
    if i.val < 7 then bitSign code i.val
    else ∏ j : Fin 7, bitSign code j.val

/-- Each doubled root has squared norm 8; usual E₈ roots have norm² 2. -/
theorem doubledRoot_norm_sq :
    ∀ root : Fin 240,
      (∑ i : Fin 8, doubledRoot root i * doubledRoot root i) = 8 := by
  native_decide

/-- The exact integral second moment of the doubled root enumeration. -/
theorem doubledRoot_second_moment :
    ∀ i j : Fin 8,
      (∑ root : Fin 240, doubledRoot root i * doubledRoot root j) =
        if i = j then (240 : ℤ) else 0 := by
  native_decide

theorem enumeration_card : Fintype.card (Fin 240) = 240 := by
  simp

/-- The original (undoubled) coordinates are rational, not floating point. -/
def rootCoordinate (root : Fin 240) (i : Fin 8) : ℚ :=
  (doubledRoot root i : ℚ) / 2

/-- Sum of outer products for ordinary E₈ roots: 60 times the 8×8 identity. -/
theorem root_second_moment :
    ∀ i j : Fin 8,
      (∑ root : Fin 240, rootCoordinate root i * rootCoordinate root j) =
        if i = j then (60 : ℚ) else 0 := by
  intro i j
  have h := doubledRoot_second_moment i j
  have hQ :
      (∑ root : Fin 240, (doubledRoot root i : ℚ) * (doubledRoot root j : ℚ)) =
        if i = j then (240 : ℚ) else 0 := by
    exact_mod_cast h
  calc
    (∑ root : Fin 240, rootCoordinate root i * rootCoordinate root j) =
        ∑ root : Fin 240,
          ((doubledRoot root i : ℚ) * (doubledRoot root j : ℚ)) / 4 := by
        apply Finset.sum_congr rfl
        intro root hr
        unfold rootCoordinate
        ring
    _ = (∑ root : Fin 240, (doubledRoot root i : ℚ) *
          (doubledRoot root j : ℚ)) / 4 := by
        rw [Finset.sum_div]
    _ = if i = j then (60 : ℚ) else 0 := by
        rw [hQ]
        split_ifs <;> norm_num

noncomputable def rootAngle (r : Fin 240) (x : Fin 8 → ℝ) (f : ℝ) : ℝ :=
  (∑ i : Fin 8, ((doubledRoot r i : ℝ) / 2) * x i) / f

noncomputable def rootPotential (ε f : ℝ) (x y : Fin 8 → ℝ) : ℝ :=
  ε * (∑ r : Fin 240,
    (2 - Real.cos (rootAngle r x f) - Real.cos (rootAngle r y f)))

/-- Positivity is algebraic/analytic, not a claim about the physical vacuum. -/
theorem rootPotential_nonneg (ε f : ℝ) (x y : Fin 8 → ℝ)
    (hε : 0 ≤ ε) : 0 ≤ rootPotential ε f x y := by
  unfold rootPotential
  apply mul_nonneg hε
  apply Finset.sum_nonneg
  intro r hr
  have hx := Real.cos_le_one (rootAngle r x f)
  have hy := Real.cos_le_one (rootAngle r y f)
  linarith

theorem mass_shift_identity (ε f q : ℝ) :
    (30 * ε / f ^ 2) * q = (1 / 2 : ℝ) * (60 * ε / f ^ 2) * q := by
  ring

end POM1
