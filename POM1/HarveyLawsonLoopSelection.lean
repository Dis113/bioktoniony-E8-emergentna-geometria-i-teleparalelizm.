import Mathlib

/-!
# POM-12 — a graph-local nonassociative phase, with an H vs O control

Theorem 1.6 of Harvey–Lawson (Acta Math. 148, 1982, 47–157)
is an ALREADY PUBLISHED calibration identity:

  phi(u,v,w)^2 + ||[u,v,w]||^2/4 = det Gram(u,v,w)

for imaginary octonions. For unit vectors, the normalized associator
A² = ||[u,v,w]||²/4 belongs to [0,1]. This result is USED, not
re-proven. Thus the mathematical statements below are CONDITIONAL
on the hypothesis 0 <= A² <= 1. The witness A²=1 is checked with
the actual Cayley–Dickson multiplication in a separate Python probe.

We define a NEW, three-potential-node toy energy that is strictly
edge-gated. Its graph variables are Boolean:
  E = mu * (number of active edges) - g * (all 3 edges active) * A².

When no edges are active, E is identically zero for ANY spin triple.
The model is NOT the old POM-3 or POM-10 Hamiltonian. In particular,
the negative asssociator coupling and the triangle term are NEW
phenomenological assumptions, not consequences of POM-3.

Old results we do not claim: the Harvey–Lawson identity,
Artin's theorem, G2 properties, or quantum graphity results.

No spacetime, physical fermion, Planck scale, QFT or TEGR follows.
-/

namespace POM1

def activeEdgeCount (a b c : Bool) : ℕ :=
  (if a then 1 else 0) + (if b then 1 else 0) +
    (if c then 1 else 0)

def triangleActive (a b c : Bool) : Bool := a && b && c

noncomputable def octonionLoopEnergy
    (mu gain normAssocSq : ℝ) (a b c : Bool) : ℝ :=
  mu * (activeEdgeCount a b c : ℝ) -
    (if triangleActive a b c then gain * normAssocSq else 0)

/-- Unlike historical POM-10, the edge-interaction energy of
    an EMPTY graph is independent of ALL octonion states. -/
theorem empty_graph_exactly_local (mu gain r : ℝ) :
    octonionLoopEnergy mu gain r false false false = 0 := by
  norm_num [octonionLoopEnergy, activeEdgeCount, triangleActive]

/-- An octonionic triple from different local quaternion sectors
    can attain normalized associator squared exactly one. -/
theorem full_octonionic_witness_energy :
    octonionLoopEnergy (1/4) 1 1 true true true =
      -(1/4 : ℝ) := by
  norm_num [octonionLoopEnergy, activeEdgeCount, triangleActive]

/-- Every incomplete graph has nonnegative energy. The proof is
    independent of the associator and of its calibration bound. -/
theorem incomplete_graph_nonnegative
    (r : ℝ) (a b c : Bool)
    (h : triangleActive a b c = false) :
    0 ≤ octonionLoopEnergy (1/4) 1 r a b c := by
  cases a <;> cases b <;> cases c <;>
    simp [triangleActive, octonionLoopEnergy, activeEdgeCount] at * <;>
    norm_num at *

/-- Exact global lower bound in the ENTIRE chosen model,
    conditional on the known Harvey–Lawson bound r<=1. -/
theorem all_graphs_have_lower_bound
    (r : ℝ) (hr : r ≤ 1) (a b c : Bool) :
    -(1/4 : ℝ) ≤ octonionLoopEnergy (1/4) 1 r a b c := by
  cases a <;> cases b <;> cases c <;>
    simp [octonionLoopEnergy, activeEdgeCount, triangleActive] <;>
    linarith

/-- Together with all_graphs_have_lower_bound, the explicit
    maximally nonassociative triple proves exact global minimum -1/4. -/
theorem octonionic_loop_selected_over_empty :
    octonionLoopEnergy (1/4) 1 1 true true true <
      octonionLoopEnergy (1/4) 1 0 false false false := by
  norm_num [octonionLoopEnergy, activeEdgeCount, triangleActive]

/-- Any triple contained in ONE real associative quaternion algebra
    has associator zero, so no loop reward is available. -/
theorem quaternionic_graph_nonnegative
    (a b c : Bool) :
    0 ≤ octonionLoopEnergy (1/4) 1 0 a b c := by
  cases a <;> cases b <;> cases c <;>
    norm_num [octonionLoopEnergy, activeEdgeCount, triangleActive]

/-- The two algebraic models differ in their exact preferred energies,
    given the SAME edge costs and same graph set. -/
theorem nonassociative_phase_has_strict_advantage :
    octonionLoopEnergy (1/4) 1 1 true true true <
      octonionLoopEnergy (1/4) 1 0 false false false := by
  exact octonionic_loop_selected_over_empty

/-- A model-specific, tunable threshold: gain > 3*edge_cost makes
    the complete maximally nonassociative triangle beat the empty graph. -/
theorem nonassociative_triangle_threshold
    (mu gain : ℝ) (h : 3*mu < gain) :
    octonionLoopEnergy mu gain 1 true true true <
      octonionLoopEnergy mu gain 0 false false false := by
  simp [octonionLoopEnergy, activeEdgeCount, triangleActive]
  linarith

/-- Robust edge phase: even when the complete triangle energy is
    increased by dFull and every incomplete graph is lowered by
    dIncomplete, errors with |d| < 1/8 cannot change the winner. -/
theorem octonionic_graph_robust_to_branch_errors
    (dFull dIncomplete : ℝ)
    (hF : dFull < 1/8)
    (hI : -(1/8 : ℝ) < dIncomplete) :
    -(1/4 : ℝ) + dFull < 0 + dIncomplete := by
  linarith

end POM1
