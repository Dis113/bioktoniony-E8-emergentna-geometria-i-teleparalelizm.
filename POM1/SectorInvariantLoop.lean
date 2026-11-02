import Mathlib
import POM1.HarveyLawsonLoopSelection

/-!
POM-12b: a FRAME-INVARIANT candidate for the earlier edge-gated
nonassociative loop model.

For quaternionic sectors H_i subset O chosen by POM-3, define
I(H1,H2,H3) as 1/108 times sum of 27 squared associator norms for
orthonormal bases of Im H_i. The contraction is invariant under O(3)
basis changes at each of the three FIXED sectors, and under central
POM-3 U(1) mixing of the two generators at each node.

This known multilinear-algebra frame invariance is explained in the
theory note. The EXACT octonion Cayley-Dickson witness I=4/9 is
checked in Python by integer multiplication (sum=48); it is a GIVEN
numerical parameter in this Lean file. This module proves the
model-specific energy consequences, not octonion composition laws.

The interaction is NOT yet invariant under arbitrary INDEPENDENT G2
transformations of octonion fibers at different vertices. Such
local covariance would require separately defined link transport.
-/

namespace POM1

/-- Exact POM-12b rational witness, given as an input derived by
    independent Cayley-Dickson integer arithmetic in Python. -/
def threeSectorAssociatorWitness : ℚ := 4/9

theorem three_sector_witness_above_threshold :
    (3/8 : ℚ) < threeSectorAssociatorWitness := by
  norm_num [threeSectorAssociatorWitness]

/-- The three-sector witness and the assumed loop energy with edge
    cost 1/4 and loop gain 2 give a STRICTLY negative energy. -/
theorem frame_invariant_witness_energy :
    octonionLoopEnergy (1/4) 2
      (threeSectorAssociatorWitness : ℝ) true true true =
      -(5/36 : ℝ) := by
  norm_num [octonionLoopEnergy, activeEdgeCount,
    triangleActive, threeSectorAssociatorWitness]

/-- A single shared associative quaternion subalgebra has associator
    zero, so for the SAME gain 2 its edge costs are nonnegative. -/
theorem frame_invariant_quaternion_control (a b c : Bool) :
    0 ≤ octonionLoopEnergy (1/4) 2 0 a b c := by
  cases a <;> cases b <;> cases c <;>
    norm_num [octonionLoopEnergy, activeEdgeCount, triangleActive]

/-- Under our exact integer Cayley-Dickson witness there exists an
    octonionic graph energy below every same-H quaternion graph energy.
    We do NOT claim that -5/36 is the GLOBAL O minimum. -/
theorem frame_invariant_strict_sep (a b c : Bool) :
    octonionLoopEnergy (1/4) 2
        (threeSectorAssociatorWitness : ℝ) true true true <
      octonionLoopEnergy (1/4) 2 0 a b c := by
  rw [frame_invariant_witness_energy]
  have h := frame_invariant_quaternion_control a b c
  linarith

/-- Any three-sector invariant q>3/8 selects a closed loop over an
    otherwise empty graph for mu=1/4 and gain=2. -/
theorem frame_invariant_loop_threshold (q : ℝ)
    (hq : 3/8 < q) :
    octonionLoopEnergy (1/4) 2 q true true true <
      octonionLoopEnergy (1/4) 2 0 false false false := by
  norm_num [octonionLoopEnergy, activeEdgeCount, triangleActive] at *
  linarith

/-- Explicit finite perturbation margin, model-specific; the
    operator norm or full-field stability of real particles is NOT
    proved here. -/
theorem frame_invariant_branch_robust
    (dTriangle dOpen : ℝ)
    (ht : dTriangle < 5/72)
    (ho : -(5/72 : ℝ) < dOpen) :
    -(5/36 : ℝ) + dTriangle < dOpen := by
  linarith

end POM1
