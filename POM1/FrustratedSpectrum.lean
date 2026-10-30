import Mathlib

/-!
POM-2: finite-graph quadratic stability and a Landau energy bound.
These are model-specific polynomial identities, not derivations of
Lorentzian tetrads or gravity. The E8 Hessian input mE8 is not derived here.
-/

namespace POM1

noncomputable def triangleQuadratic (mE8 α K x y z : ℝ) : ℝ :=
  (mE8 - α) / 2 * (x^2 + y^2 + z^2) +
  K / 2 * ((x+y)^2 + (y+z)^2 + (z+x)^2)

theorem triangle_quadratic_decomposition (mE8 α K x y z : ℝ) :
    triangleQuadratic mE8 α K x y z =
    (mE8 - α + K) / 2 * (x^2 + y^2 + z^2) +
    K / 2 * (x+y+z)^2 := by
  unfold triangleQuadratic
  ring

theorem triangle_quadratic_nonneg (mE8 α K x y z : ℝ)
    (hK : 0 ≤ K) (hα : α ≤ mE8 + K) :
    0 ≤ triangleQuadratic mE8 α K x y z := by
  rw [triangle_quadratic_decomposition]
  have h1 : 0 ≤ (mE8 - α + K) / 2 := by linarith
  have h2 : 0 ≤ K / 2 := by linarith
  exact add_nonneg (mul_nonneg h1 (by positivity))
    (mul_nonneg h2 (sq_nonneg _))

theorem triangle_frustrated_mode_negative (mE8 α K : ℝ)
    (hα : mE8 + K < α) :
    triangleQuadratic mE8 α K 1 (-1) 0 < 0 := by
  have hcalc : triangleQuadratic mE8 α K 1 (-1) 0 = mE8 - α + K := by
    unfold triangleQuadratic
    ring
  rw [hcalc]
  linarith

def pentadLinks (a b c d e : ℝ) : ℝ :=
  (a+b)^2 + (a+c)^2 + (a+d)^2 + (a+e)^2 +
  (b+c)^2 + (b+d)^2 + (b+e)^2 +
  (c+d)^2 + (c+e)^2 + (d+e)^2

theorem pentad_links_decomposition (a b c d e : ℝ) :
    pentadLinks a b c d e =
    3 * (a^2+b^2+c^2+d^2+e^2) + (a+b+c+d+e)^2 := by
  unfold pentadLinks
  ring

noncomputable def pentadQuadratic (mE8 α K a b c d e : ℝ) : ℝ :=
  (mE8 - α) / 2 * (a^2+b^2+c^2+d^2+e^2) +
  K / 2 * pentadLinks a b c d e

theorem pentad_quadratic_decomposition (mE8 α K a b c d e : ℝ) :
    pentadQuadratic mE8 α K a b c d e =
    (mE8 - α + 3*K) / 2 * (a^2+b^2+c^2+d^2+e^2) +
    K / 2 * (a+b+c+d+e)^2 := by
  unfold pentadQuadratic
  rw [pentad_links_decomposition]
  ring

theorem pentad_quadratic_nonneg (mE8 α K a b c d e : ℝ)
    (hK : 0 ≤ K) (hα : α ≤ mE8 + 3*K) :
    0 ≤ pentadQuadratic mE8 α K a b c d e := by
  rw [pentad_quadratic_decomposition]
  have h1 : 0 ≤ (mE8 - α + 3*K) / 2 := by linarith
  have h2 : 0 ≤ K / 2 := by linarith
  exact add_nonneg (mul_nonneg h1 (by positivity))
    (mul_nonneg h2 (sq_nonneg _))

theorem pentad_frustrated_mode_negative (mE8 α K : ℝ)
    (hα : mE8 + 3*K < α) :
    pentadQuadratic mE8 α K 1 (-1) 0 0 0 < 0 := by
  have hcalc : pentadQuadratic mE8 α K 1 (-1) 0 0 0 = mE8 - α + 3*K := by
    unfold pentadQuadratic pentadLinks
    ring
  rw [hcalc]
  linarith

/- The variables uᵢ represent squared norms; Q is the squared norm of
the collective field sum. Its nonnegativity is a separate hypothesis. -/
noncomputable def pentadReducedEnergy (α λ K u₀ u₁ u₂ u₃ u₄ Q : ℝ) : ℝ :=
  (3*K-α)/2 * (u₀+u₁+u₂+u₃+u₄) +
  λ/4 * (u₀^2+u₁^2+u₂^2+u₃^2+u₄^2) + K/2*Q

theorem pentad_square_completion (λ K rSquared u₀ u₁ u₂ u₃ u₄ Q : ℝ) :
    pentadReducedEnergy (3*K+λ*rSquared) λ K u₀ u₁ u₂ u₃ u₄ Q =
    λ/4 * ((u₀-rSquared)^2+(u₁-rSquared)^2+(u₂-rSquared)^2+
      (u₃-rSquared)^2+(u₄-rSquared)^2) + K/2*Q -
    5*λ/4*rSquared^2 := by
  unfold pentadReducedEnergy
  ring

theorem pentad_lower_bound (λ K rSquared u₀ u₁ u₂ u₃ u₄ Q : ℝ)
    (hλ : 0 ≤ λ) (hK : 0 ≤ K) (hQ : 0 ≤ Q) :
    -(5*λ/4*rSquared^2) ≤
      pentadReducedEnergy (3*K+λ*rSquared) λ K u₀ u₁ u₂ u₃ u₄ Q := by
  rw [pentad_square_completion]
  have hsq : 0 ≤
      (u₀-rSquared)^2+(u₁-rSquared)^2+(u₂-rSquared)^2+
      (u₃-rSquared)^2+(u₄-rSquared)^2 := by positivity
  have h1 : 0 ≤ λ/4 *
      ((u₀-rSquared)^2+(u₁-rSquared)^2+(u₂-rSquared)^2+
       (u₃-rSquared)^2+(u₄-rSquared)^2) :=
    mul_nonneg (by positivity) hsq
  have h2 : 0 ≤ K/2*Q := mul_nonneg (by positivity) hQ
  linarith

theorem pentad_bound_saturated (λ K rSquared : ℝ) :
    pentadReducedEnergy (3*K+λ*rSquared) λ K
      rSquared rSquared rSquared rSquared rSquared 0 =
      -(5*λ/4*rSquared^2) := by
  rw [pentad_square_completion]
  ring

end POM1
