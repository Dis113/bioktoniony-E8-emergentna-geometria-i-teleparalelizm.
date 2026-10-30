import Mathlib

/-!
POM-4: exact algebraic tests for a coupled EM/GR environmental parameter
and the scalar pattern-potential V(s)=a*s-s²+s³, s≥0.

EM and GR inputs are formal dimensionless real parameters, NOT yet physical
field invariants derived from the bi-octonionic graph. Fermionic/bosonic
statistics are imposed separately; no spin-statistics theorem is re-proved.
-/

namespace POM1

noncomputable def coupledPatternCoefficient (em gr : ℝ) : ℝ :=
  (1/4 : ℝ) - 5/48 * em + gr/16 + em*gr/64

noncomputable def patternPotential (a s : ℝ) : ℝ :=
  a*s - s^2 + s^3

noncomputable def patternSlope (a s : ℝ) : ℝ :=
  a - 2*s + 3*s^2

noncomputable def patternCurvature (s : ℝ) : ℝ :=
  -2 + 6*s

/-- Exact mixed-field coexistence criterion in the toy model. -/
theorem coefficient_boundary (em gr : ℝ) :
    (coupledPatternCoefficient em gr - 1/4) * 192 =
      -20*em + 12*gr + 3*em*gr := by
  unfold coupledPatternCoefficient
  ring

theorem ordered_when (em gr : ℝ)
    (h : 12*gr + 3*em*gr < 20*em) :
    coupledPatternCoefficient em gr < 1/4 := by
  have hi := coefficient_boundary em gr
  linarith

theorem trivial_when (em gr : ℝ)
    (h : 20*em < 12*gr + 3*em*gr) :
    1/4 < coupledPatternCoefficient em gr := by
  have hi := coefficient_boundary em gr
  linarith

theorem em_favored_example :
    coupledPatternCoefficient 1 0 = (7/48 : ℝ) := by
  norm_num [coupledPatternCoefficient]

theorem coexistence_example :
    coupledPatternCoefficient 0 0 = (1/4 : ℝ) := by
  norm_num [coupledPatternCoefficient]

theorem gravity_favored_example :
    coupledPatternCoefficient 0 1 = (5/16 : ℝ) := by
  norm_num [coupledPatternCoefficient]

/-- At a=1/4 the two pattern minima are degenerate. -/
theorem coexistence_factor (s : ℝ) :
    patternPotential (1/4) s = s*(s-1/2)^2 := by
  unfold patternPotential
  ring

theorem coexistence_nonneg (s : ℝ) (hs : 0 ≤ s) :
    0 ≤ patternPotential (1/4) s := by
  rw [coexistence_factor]
  exact mul_nonneg hs (sq_nonneg _)

theorem coexistence_equal_minima :
    patternPotential (1/4) 0 = 0 ∧
    patternPotential (1/4) (1/2) = 0 := by
  constructor <;> norm_num [patternPotential]

/-- Exact stationary points for a=7/48 (ordered branch favored). -/
theorem ordered_slope_factor (s : ℝ) :
    patternSlope (7/48) s = 3*(s-1/12)*(s-7/12) := by
  unfold patternSlope
  ring

theorem ordered_curvatures :
    patternCurvature (1/12) < 0 ∧
    0 < patternCurvature (7/12) := by
  constructor <;> norm_num [patternCurvature]

theorem ordered_energies :
    patternPotential (7/48) (1/12) = (5/864 : ℝ) ∧
    patternPotential (7/48) (7/12) = (-49/864 : ℝ) := by
  constructor <;> norm_num [patternPotential]

/-- Exact stationary points for a=5/16 (nonzero branch metastable). -/
theorem metastable_slope_factor (s : ℝ) :
    patternSlope (5/16) s = 3*(s-1/4)*(s-5/12) := by
  unfold patternSlope
  ring

theorem metastable_curvatures :
    patternCurvature (1/4) < 0 ∧
    0 < patternCurvature (5/12) := by
  constructor <;> norm_num [patternCurvature]

theorem metastable_energies :
    patternPotential (5/16) (1/4) = (1/32 : ℝ) ∧
    patternPotential (5/16) (5/12) = (25/864 : ℝ) := by
  constructor <;> norm_num [patternPotential]

theorem metastable_barrier_above_local_min :
    patternPotential (5/16) (1/4) -
      patternPotential (5/16) (5/12) = (1/432 : ℝ) := by
  norm_num [patternPotential]

end POM1
