import Mathlib

/-!
POM-10: a conditional three-potential-node extension, NOT an existing
derivation from the old POM-3/8/9 graph Hamiltonian.

The unknown octonion state is summarized by real numbers
  c=<u1,u3>, chiSq=chi(u1,u2,u3)^2.
The CALIBRATION INEQUALITY chiSq<=1-c^2 is an input proved in
published octonion mathematics, but NOT formalized here.
The witnesses are actual imaginary quaternion/octonion vectors
checked in the accompanying Python experiment.

The three possible edge variables, graph's triangular interaction,
spin energy coefficients, and two-band QWZ operator are assumptions.
We use the already formalized Niven theorem, NOT reprove it.
No physical spacetime, Maxwell, hbar, QFT or TEGR emerges here.
-/

namespace POM1

noncomputable def openTriangleEnergy (c chiSq edgeCount : ℝ) : ℝ :=
  c^2 - 6*c - 3*chiSq + edgeCount/10

noncomputable def closedTriangleEnergy (c chiSq : ℝ) : ℝ :=
  c^2 - 6*c - 4*chiSq + 3/10

/-- Model-specific lower bound for EVERY incomplete edge configuration. -/
theorem open_triangle_lower_bound (c chiSq edgeCount : ℝ)
    (hcalibration : chiSq ≤ 1-c^2) (hEdges : 0 ≤ edgeCount) :
    -(21/4 : ℝ) ≤ openTriangleEnergy c chiSq edgeCount := by
  unfold openTriangleEnergy
  nlinarith [sq_nonneg (c-(3/4:ℝ))]

/-- Exact lower bound for a COMPLETE closed graph of three edges. -/
theorem closed_triangle_lower_bound (c chiSq : ℝ)
    (hcalibration : chiSq ≤ 1-c^2) :
    -(11/2 : ℝ) ≤ closedTriangleEnergy c chiSq := by
  unfold closedTriangleEnergy
  nlinarith [sq_nonneg (c-(3/5:ℝ))]

theorem closed_triangle_exact_witness :
    closedTriangleEnergy (3/5) (16/25) = -(11/2 : ℝ) := by
  norm_num [closedTriangleEnergy]

/-- The closed chiral trial is strictly preferable to ANY incomplete
    edge configuration under the displayed known octonionic bound. -/
theorem loop_is_energetically_selected (c chiSq edgeCount : ℝ)
    (hcalibration : chiSq ≤ 1-c^2) (hEdges : 0 ≤ edgeCount) :
    closedTriangleEnergy (3/5) (16/25) <
      openTriangleEnergy c chiSq edgeCount := by
  rw [closed_triangle_exact_witness]
  have h := open_triangle_lower_bound c chiSq edgeCount hcalibration hEdges
  linarith

/-- The energetic preference 1/4 survives uniformly bounded
    imperfections whose magnitudes are separately strictly below 1/8. -/
theorem loop_preference_robust (dClosed dOpen : ℝ)
    (hC : dClosed < 1/8) (hO : -(1/8 : ℝ) < dOpen) :
    -(11/2 : ℝ) + dClosed < -(21/4 : ℝ) + dOpen := by
  linarith

/-- Independently known J1/J2 exchange form for a uniform infinite
    spiral. Its use here is a separate conditional consistency check. -/
noncomputable def spiralEnergy (c : ℝ) : ℝ :=
  -12*c + 5*(2*c^2-1)

theorem spiral_energy_square (c : ℝ) :
    spiralEnergy c + (43/5 : ℝ) = 10*(c-(3/5:ℝ))^2 := by
  unfold spiralEnergy
  ring

theorem spiral_selected_cosine (c : ℝ) :
    -(43/5 : ℝ) ≤ spiralEnergy c := by
  have h := spiral_energy_square c
  nlinarith [sq_nonneg (c-(3/5:ℝ))]

theorem spiral_exact_witness :
    spiralEnergy (3/5) = -(43/5 : ℝ) := by
  norm_num [spiralEnergy]

/-- Existing Niven theorem is REUSED from mathlib, not reproved.
    If a selected angle has cosine 3/5, angle/pi is irrational. -/
theorem irrational_chosen_twist (θ : ℝ)
    (hcos : Real.cos θ = (3/5 : ℝ)) :
    ¬ ∃ r : ℚ, θ = (r : ℝ) * Real.pi := by
  intro hr
  have hrat : ∃ r : ℚ, Real.cos θ = (r : ℝ) :=
    ⟨(3/5 : ℚ), by norm_num [hcos]⟩
  have hn := niven hr hrat
  norm_num [hcos] at hn

/-- Known Niven theorem, applied to the conditional Berry spinor
    identity cos(2 phi)=3/5. A half-angle geometric statement is
    checked independently in Python on a specific quaternion triad. -/
theorem irrational_berry_flux (φ : ℝ)
    (hcos : Real.cos (2*φ) = (3/5 : ℝ)) :
    ¬ ∃ r : ℚ, φ = (r : ℝ) * Real.pi := by
  intro h
  rcases h with ⟨r,hr⟩
  have hangle : (2*φ) = ((2*r : ℚ) : ℝ) * Real.pi := by
    rw [hr]
    push_cast
    ring
  exact irrational_chosen_twist (2*φ) hcos ⟨2*r,hangle⟩

/-- Exact two-band energy identity for a postulated QWZ spectral
    response. This is NOT a novel Chern theorem, nor a microscopic
    derivation of the physical fermionic kinetic operator. -/
theorem qwz_energy_decomposition (m x y : ℝ) :
    (1-x^2) + (1-y^2) + (m+x+y)^2 =
      m^2 + (1+m)*(1+x)*(1+y) +
        (1-m)*(1-x)*(1-y) := by
  ring

/-- Model-specific gap bound over the whole assumed 2D Brillouin torus
    whenever |m|<=1 and x=cos kx, y=cos ky. -/
theorem qwz_gap_lower_bound (m x y : ℝ)
    (hm1 : -1 ≤ m) (hm2 : m ≤ 1)
    (hx1 : -1 ≤ x) (hx2 : x ≤ 1)
    (hy1 : -1 ≤ y) (hy2 : y ≤ 1) :
    m^2 ≤ (1-x^2) + (1-y^2) + (m+x+y)^2 := by
  have ha : 0 ≤ (1+m)*(1+x)*(1+y) := by
    apply mul_nonneg
    · exact mul_nonneg (by linarith) (by linarith)
    · linarith
  have hb : 0 ≤ (1-m)*(1-x)*(1-y) := by
    apply mul_nonneg
    · exact mul_nonneg (by linarith) (by linarith)
    · linarith
  rw [qwz_energy_decomposition]
  linarith

theorem qwz_selected_chiral_gap (x y : ℝ)
    (hx1 : -1 ≤ x) (hx2 : x ≤ 1)
    (hy1 : -1 ≤ y) (hy2 : y ≤ 1) :
    (16/25 : ℝ) ≤
      (1-x^2)+(1-y^2)+((4/5:ℝ)+x+y)^2 := by
  convert qwz_gap_lower_bound (4/5) x y (by norm_num)
    (by norm_num) hx1 hx2 hy1 hy2 using 1 <;> norm_num

end POM1
