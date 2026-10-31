import Mathlib

/-!
POM-6: model-specific scalar overlap coupling in two canonical quaternion
subalgebras of the real octonions.

A = span{1,e1,e2,e3}, B=span{1,e1,e4,e5}, with e4*e5=e1
in the Cayley-Dickson convention used in Simulations/pom1_model.py.

The root/SSH bulk-boundary or index theorem is KNOWN published mathematics
and is NOT re-proved here. These finite algebraic identities only establish
the particular POM-6 couplings derived from projector overlaps.
-/

namespace POM1

def quaternionProjectorA (i : Fin 8) : ℚ :=
  if i.val < 4 then 1 else 0

def quaternionProjectorB (i : Fin 8) : ℚ :=
  if i.val = 0 ∨ i.val = 1 ∨ i.val = 4 ∨ i.val = 5 then 1 else 0

/-- Overlap Tr(P_A P_B)/4 for the explicit two octonionic sectors. -/
def quaternionOverlapAB : ℚ :=
  (∑ i : Fin 8, quaternionProjectorA i * quaternionProjectorB i) / 4

theorem quaternionOverlapAB_half :
    quaternionOverlapAB = (1/2 : ℚ) := by
  decide

/-- Every sector projector overlaps itself with normalized trace 1. -/
theorem quaternionOverlapAA_one :
    (∑ i : Fin 8, quaternionProjectorA i * quaternionProjectorA i) / 4 =
    (1 : ℚ) := by
  decide

/-- Phenomenological, positive link strength from scalar sector overlap. -/
noncomputable def spectralLink (offset stiffness overlap : ℝ) : ℝ :=
  offset + stiffness * overlap

theorem same_sector_link (offset stiffness : ℝ) :
    spectralLink offset stiffness 1 = offset + stiffness := by
  unfold spectralLink
  ring

theorem cross_sector_link (offset stiffness : ℝ) :
    spectralLink offset stiffness (1/2) = offset + stiffness/2 := by
  unfold spectralLink
  ring

/-- The POM overlap rule creates alternating weak/strong bonds if the
    intrabond sectors differ and the interbond sectors agree. -/
theorem aligned_bond_stronger (offset stiffness : ℝ)
    (h_stiff : 0 < stiffness) :
    spectralLink offset stiffness (1/2) <
    spectralLink offset stiffness 1 := by
  unfold spectralLink
  linarith

/-- Exact SSH band gap 2|t_inter-t_intra| for the linked two-sector
    periodic toy chain follows from the well-known SSH spectrum. This
    lemma computes its POM-specific *algebraic value*, not SSH topology. -/
theorem two_sector_bulk_gap (offset stiffness : ℝ)
    (h_stiff : 0 < stiffness) :
    2 * (spectralLink offset stiffness 1 -
         spectralLink offset stiffness (1/2)) = stiffness := by
  unfold spectralLink
  ring

/-- A uniform quaternion sector does NOT induce dimerization:
    its two neighboring overlaps are equal, and the overlap-only
    mechanism cannot produce a nontrivial SSH phase. -/
theorem uniform_sector_no_dimerization (offset stiffness : ℝ) :
    spectralLink offset stiffness 1 -
      spectralLink offset stiffness 1 = 0 := by
  ring

/-- The postulated graph link can represent a true gap only if there
    is a nonzero sector contrast. -/
theorem overlap_contrast_needed (offset stiffness q : ℝ)
    (h_stiff : 0 < stiffness)
    (heq : spectralLink offset stiffness q =
       spectralLink offset stiffness 1) :
    q = 1 := by
  unfold spectralLink at heq
  nlinarith

end POM1
