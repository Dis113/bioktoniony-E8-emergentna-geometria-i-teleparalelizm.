import Mathlib

/-!
POM-11: exact finite-loop spectral certificate.

This is an improvement of the OWN three-node chiral-loop witness from
POM-10, *not* a proof of the pre-existing general bulk-edge or Weyl
perturbation theorems.

The chosen 3x3 Hermitian link Hamiltonian has the same gauge-invariant
three-cycle Bargmann invariant (2+i)/5 and pairwise hopping moduli
as the POM-10 coherent-spinor witness. A local basis-phase change
maps one to the other. The eigenvalue *spacing* is finite-size
spectral stability, NOT an emergent 2D/3+1D bulk gap.

The conditional perturbation lemma assumes each eigenvalue shifts by
at most 1/5. Standard Weyl inequalities give that condition for a
Hermitian perturbation with operator norm ≤1/5; that general published
theorem is not duplicated here.
-/

namespace POM1

/-- Characteristic polynomial of the specific POM-10 triangle link graph. -/
noncomputable def loopCubic (z : ℝ) : ℝ :=
  z^3 - (9/5)*z - 4/5

theorem loop_cubic_factorization (z : ℝ) :
    loopCubic z = (z+1)*(z^2-z-4/5) := by
  unfold loopCubic
  ring

theorem loop_minus_one_root : loopCubic (-1) = 0 := by
  norm_num [loopCubic]

theorem loop_sqrt105_sq :
    Real.sqrt (105 : ℝ)^2 = 105 := by
  exact Real.sq_sqrt (by norm_num)

theorem loop_sqrt105_bounds :
    (10 : ℝ) < Real.sqrt 105 ∧ Real.sqrt 105 < 103/10 := by
  have h0 : 0 ≤ Real.sqrt (105 : ℝ) := Real.sqrt_nonneg _
  have hsq : Real.sqrt (105 : ℝ)^2 = 105 := loop_sqrt105_sq
  constructor <;> nlinarith

theorem loop_quadratic_lower_root :
    ((5-Real.sqrt (105 : ℝ))/10)^2 -
      (5-Real.sqrt (105 : ℝ))/10-(4/5 : ℝ) = 0 := by
  have hs := loop_sqrt105_sq
  nlinarith

theorem loop_quadratic_upper_root :
    ((5+Real.sqrt (105 : ℝ))/10)^2 -
      (5+Real.sqrt (105 : ℝ))/10-(4/5 : ℝ) = 0 := by
  have hs := loop_sqrt105_sq
  nlinarith

theorem loop_lower_eigenvalue_root :
    loopCubic ((5-Real.sqrt (105 : ℝ))/10) = 0 := by
  rw [loop_cubic_factorization, loop_quadratic_lower_root]
  ring

theorem loop_upper_eigenvalue_root :
    loopCubic ((5+Real.sqrt (105 : ℝ))/10) = 0 := by
  rw [loop_cubic_factorization, loop_quadratic_upper_root]
  ring

/-- The smallest exact level spacing of this 3-node model. -/
noncomputable def loopSmallGap : ℝ :=
  (15-Real.sqrt (105 : ℝ))/10

/-- An *exact* rational lower bound, without numerical diagonalization. -/
theorem loop_gap_exceeds_47_100 : (47/100 : ℝ) < loopSmallGap := by
  have h := loop_sqrt105_bounds
  unfold loopSmallGap
  linarith

theorem loop_levels_are_ordered :
    (-1 : ℝ) < (5-Real.sqrt (105 : ℝ))/10 ∧
    (5-Real.sqrt (105 : ℝ))/10 <
      (5+Real.sqrt (105 : ℝ))/10 := by
  have h := loop_sqrt105_bounds
  constructor <;> linarith

theorem loop_other_gap_is_larger :
    loopSmallGap <
      (5+Real.sqrt (105 : ℝ))/10 -
        (5-Real.sqrt (105 : ℝ))/10 := by
  have h := loop_sqrt105_bounds
  unfold loopSmallGap
  linarith

/-- Conditional perturbation stability: if two ordered Hermitian
    eigenvalues each move at most 1/5, the original POM-10 finite-loop
    gap stays > 7/100. Weyl's general theorem is prior art. -/
theorem loop_gap_survives_eigenvalue_perturbation
    (lower middle : ℝ)
    (hlo : |lower - (-1 : ℝ)| ≤ (1/5 : ℝ))
    (hmi : |middle - (5-Real.sqrt (105 : ℝ))/10|
       ≤ (1/5 : ℝ)) :
    (7/100 : ℝ) < middle - lower := by
  have hgap := loop_gap_exceeds_47_100
  have hlo' := (abs_le.mp hlo).2
  have hmi' := (abs_le.mp hmi).1
  unfold loopSmallGap at hgap
  linarith

end POM1
