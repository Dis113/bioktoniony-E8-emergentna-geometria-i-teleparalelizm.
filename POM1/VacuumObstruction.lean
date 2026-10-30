import Mathlib

/-!
POM-1-specific mathematical diagnostics, not a proof of gravity.
The finite site space has 16 real coordinates per bi-octonion.
The actual POM-1 Hamiltonian is bounded below by its positive mass term
because the remaining onsite, link and associator contributions are nonnegative
in the parameter regime described in Theory/Model.md.
-/

namespace POM1

/-- Total squared Euclidean amplitude of the 16 real components at every site. -/
def fieldNormSq {n : ℕ} (ψ : Fin n → Fin 16 → ℝ) : ℝ :=
  ∑ i : Fin n, ∑ a : Fin 16, (ψ i a) ^ 2

theorem siteNormSq_nonneg {n : ℕ} (ψ : Fin n → Fin 16 → ℝ)
    (i : Fin n) : 0 ≤ ∑ a : Fin 16, (ψ i a) ^ 2 := by
  apply Finset.sum_nonneg
  intro a ha
  exact sq_nonneg (ψ i a)

theorem fieldNormSq_nonneg {n : ℕ} (ψ : Fin n → Fin 16 → ℝ) :
    0 ≤ fieldNormSq ψ := by
  unfold fieldNormSq
  apply Finset.sum_nonneg
  intro i hi
  exact siteNormSq_nonneg ψ i

/-- Zero total site norm means every real bi-octonion component vanishes. -/
theorem fieldNormSq_zero_implies_field_zero {n : ℕ}
    (ψ : Fin n → Fin 16 → ℝ) (h : fieldNormSq ψ = 0) :
    ∀ i : Fin n, ∀ a : Fin 16, ψ i a = 0 := by
  intro i a
  have hs : (∑ b : Fin 16, (ψ i b) ^ 2) ≤ fieldNormSq ψ := by
    unfold fieldNormSq
    exact Finset.single_le_sum (fun j hj => siteNormSq_nonneg ψ j) (Finset.mem_univ i)
  have ha : (ψ i a) ^ 2 ≤ ∑ b : Fin 16, (ψ i b) ^ 2 := by
    exact Finset.single_le_sum (fun b hb => sq_nonneg (ψ i b)) (Finset.mem_univ a)
  have hsq : (ψ i a) ^ 2 ≤ 0 := by
    linarith
  nlinarith [sq_nonneg (ψ i a)]

/-- Abstract form of the original positive-mass Hamiltonian:
    remainder includes the kinetic term and all other nonnegative terms. -/
def abstractEnergy {n : ℕ} (μ2 : ℝ) (ψ : Fin n → Fin 16 → ℝ)
    (remainder : ℝ) : ℝ := μ2 / 2 * fieldNormSq ψ + remainder

/-- Model-specific obstruction: with μ²>0, nonnegative remaining energy and
    total ground-state energy zero, the microscopic field must vanish. -/
theorem zero_energy_forces_trivial_field {n : ℕ}
    (ψ : Fin n → Fin 16 → ℝ) (μ2 remainder : ℝ)
    (hμ : 0 < μ2) (hr : 0 ≤ remainder)
    (hzero : abstractEnergy μ2 ψ remainder = 0) :
    ∀ i : Fin n, ∀ a : Fin 16, ψ i a = 0 := by
  have hμ2 : 0 < μ2 / 2 := half_pos hμ
  have hnorm : 0 ≤ fieldNormSq ψ := fieldNormSq_nonneg ψ
  have hbound : μ2 / 2 * fieldNormSq ψ ≤ 0 := by
    unfold abstractEnergy at hzero
    linarith
  have hnorm0 : fieldNormSq ψ = 0 := by
    by_contra hh
    have hpos : 0 < fieldNormSq ψ := lt_of_le_of_ne hnorm (Ne.symm hh)
    have hm := mul_pos hμ2 hpos
    linarith
  exact fieldNormSq_zero_implies_field_zero ψ hnorm0

/-- An antisymmetric link bilinear from a complex 1-plane, which embeds
    inside the (bio-)octonions. It is a diagnostic, not a physical coframe. -/
def channelCurrent (u v : ℝ × ℝ) : ℝ := u.1 * v.2 - u.2 * v.1

theorem channelCurrent_antisymmetric (u v : ℝ × ℝ) :
    channelCurrent u v = -channelCurrent v u := by
  unfold channelCurrent
  ring

def channelLoop (u v w : ℝ × ℝ) : ℝ :=
  channelCurrent u v + channelCurrent v w + channelCurrent w u

/-- A concrete 3-site configuration has nonzero circulation even in an
    associative complex subalgebra: nonassociativity is NOT necessary. -/
theorem channelLoop_witness :
    channelLoop (1, 0) (0, 1) (-1, 0) = (2 : ℝ) := by
  norm_num [channelLoop, channelCurrent]

end POM1
