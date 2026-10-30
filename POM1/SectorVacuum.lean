import Mathlib

/-!
# POM-3: vacuum potential that selects a quaternionic sector

These are model-specific real polynomial identities and inequalities.
Artin's theorem (two real octonions generate an associative subalgebra)
is prior published mathematics and is NOT re-proved here.

For Ψ=x+I*y with x,y in real octonions:
  t = Re(x)^2+Re(y)^2, a=|Im(x)|^2, b=|Im(y)|^2,
  c= <Im(x),Im(y)>.
The Gram determinant Δ=a*b-c^2 selects a unique quaternionic
subalgebra when it is positive (from known octonion facts).
-/

namespace POM1

/-- The squared real norm of Ψ is t+a+b; Δ=a*b-c² is Gram area². -/
noncomputable def sectorPotential
    (alpha lam eta normSquared delta : ℝ) : ℝ :=
  -alpha/2 * normSquared + lam/4 * normSquared^2 - eta*delta

/-- POM-3-specific polynomial identity behind the vacuum selection. -/
theorem sector_gap_identity (t a b c : ℝ) :
    (t+a+b)^2 - 4*(a*b-c^2) =
      t^2 + 2*t*(a+b) + (a-b)^2 + 4*c^2 := by
  ring

/-- Nonnegative gap for squared norms t,a,b. -/
theorem sector_gap_nonneg (t a b c : ℝ)
    (ht : 0 ≤ t) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    0 ≤ (t+a+b)^2 - 4*(a*b-c^2) := by
  rw [sector_gap_identity]
  have hprod : 0 ≤ t*(a+b) := mul_nonneg ht (add_nonneg ha hb)
  nlinarith [sq_nonneg t, sq_nonneg (a-b), sq_nonneg c]

/-- Exact completion of squares, with alpha=(lam-eta)*r. -/
theorem sector_potential_completion (lam eta r t a b c : ℝ) :
    sectorPotential ((lam-eta)*r) lam eta
      (t+a+b) (a*b-c^2) +
      (lam-eta)/4*r^2 =
    (lam-eta)/4*(t+a+b-r)^2 +
      eta/4*((t+a+b)^2 - 4*(a*b-c^2)) := by
  unfold sectorPotential
  ring

/-- POM-3-specific global lower bound. -/
theorem sector_potential_lower_bound (lam eta r t a b c : ℝ)
    (h_eta : 0 ≤ eta) (h_lam : eta < lam)
    (ht : 0 ≤ t) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    -(lam-eta)/4*r^2 ≤
      sectorPotential ((lam-eta)*r) lam eta (t+a+b) (a*b-c^2) := by
  have hgap := sector_gap_nonneg t a b c ht ha hb
  have hsquare : 0 ≤ (t+a+b-r)^2 := sq_nonneg _
  have hcoeff1 : 0 ≤ (lam-eta)/4 := by linarith
  have hcoeff2 : 0 ≤ eta/4 := by linarith
  have hterm1 := mul_nonneg hcoeff1 hsquare
  have hterm2 := mul_nonneg hcoeff2 hgap
  have hcompletion := sector_potential_completion lam eta r t a b c
  linarith

/-- Two independent, equally sized imaginary octonions attain the bound. -/
theorem sector_potential_witness (lam eta r : ℝ) :
    sectorPotential ((lam-eta)*r) lam eta
      (0+r/2+r/2) ((r/2)*(r/2)-0^2)
      = -(lam-eta)/4*r^2 := by
  unfold sectorPotential
  ring

/-- At nonzero amplitude the witness has nonzero Gram area. -/
theorem sector_witness_positive_area (r : ℝ) (hr : 0 < r) :
    0 < (r/2)*(r/2)-(0:ℝ)^2 := by
  nlinarith [sq_pos_of_pos hr]

/-- Necessary conditions for the internal Gram gap to vanish. -/
theorem sector_gap_zero_conditions (t a b c : ℝ)
    (ht : 0 ≤ t) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hzero : (t+a+b)^2 - 4*(a*b-c^2) = 0) :
    t = 0 ∧ a = b ∧ c = 0 := by
  have hprod : 0 ≤ t*(a+b) := mul_nonneg ht (add_nonneg ha hb)
  have h : t^2 + 2*t*(a+b) + (a-b)^2 + 4*c^2 = 0 := by
    rw [← sector_gap_identity]
    exact hzero
  constructor
  · nlinarith [sq_nonneg (a-b), sq_nonneg c, sq_nonneg t]
  constructor
  · nlinarith [sq_nonneg t, sq_nonneg c, sq_nonneg (a-b)]
  · nlinarith [sq_nonneg t, sq_nonneg (a-b), sq_nonneg c]

end POM1
