import Mathlib
import POM1.SectorVacuum
import POM1.HarveyLawsonLoopSelection

/-!
# POM-13: a smooth, bounded, full-amplitude octonionic graph potential

Published input, NOT re-proved:
* Harvey--Lawson's octonion associative-calibration theorem bounds
  ||[u,v,w]||²/4 by ||u||²||v||²||w||².
* Standard spectral decomposition for PSD matrices and the
  finite-dimensional Weierstrass/coercivity theorem.
* The POM-3 vacuum lower bound (already proved in SectorVacuum.lean).

The new POM-13 model uses a smooth normalized PSD matrix R(psi)
constructed from each pair of imaginary real-octonion components.
Its trace is <=3 for ALL field amplitudes, even at degenerate or zero
states; on an ordered POM-3 vacuum R equals the exact imaginary
quaternion projector. The triple associator contraction satisfies
0 <= Q(R1,R2,R3) <= 1 by published Harvey--Lawson mathematics.
That tensor inequality is assumed, not re-proved, in the graph
comparison theorems below.

The THREE VERTICES, discrete graph, negative energy reward, and
overall microscopic coupling remain POSTULATES. The scalar
regularizer and exact model-specific graph consequences are PROVED.

This is not a proof of physical photons, fermions, spacetime, G2
gauge covariance on independent fibers, hbar or TEGR.
-/

namespace POM1

/-- If M is a PSD matrix with trace t, the smooth soft-sector tensor
    R = 36a M/(t+3a)^2 has trace softTrace a t. -/
noncomputable def softTrace (a t : ℝ) : ℝ :=
  36*a*t/(t+3*a)^2

/-- Core new stabilization inequality, valid at arbitrary amplitudes.
    It is the elementary completion (t-3a)^2 >= 0. -/
theorem soft_trace_bounded (a t : ℝ)
    (ha : 0 < a) (ht : 0 ≤ t) :
    0 ≤ softTrace a t ∧ softTrace a t ≤ 3 := by
  have hden : 0 < (t+3*a)^2 := sq_pos_of_pos (by linarith)
  constructor
  · unfold softTrace
    apply div_nonneg
    · exact mul_nonneg (by positivity) ht
    · exact le_of_lt hden
  · unfold softTrace
    apply (div_le_iff₀ hden).2
    nlinarith [sq_nonneg (t-3*a)]

/-- On the POM-3 ordered vacuum, tr(M)=3a and R=M/a:
    the soft matrix is exactly the imaginary quaternion projector. -/
theorem soft_trace_vacuum (a : ℝ) (ha : 0 < a) :
    softTrace a (3*a) = 3 := by
  have hne : a ≠ 0 := ne_of_gt ha
  unfold softTrace
  have h : (3*a+3*a) = 6*a := by ring
  rw [h]
  field_simp
  ring

/-- POM-3 onsite excess, with alpha=9/20, lambda=4/5,
    eta=1/5, r=3/4; its exact minimum is -27/320. -/
noncomputable def fullFieldOnsiteExcess (t p q c : ℝ) : ℝ :=
  sectorPotential (9/20) (4/5) (1/5)
    (t+p+q) (p*q-c^2) + (27/320 : ℝ)

/-- This positivity is NOT a duplicate proof of the POM-3 bound:
    it instantiates the already established SectorVacuum theorem. -/
theorem full_field_onsite_nonnegative
    (t p q c : ℝ) (ht : 0 ≤ t) (hp : 0 ≤ p) (hq : 0 ≤ q) :
    0 ≤ fullFieldOnsiteExcess t p q c := by
  have h := sector_potential_lower_bound
    (4/5 : ℝ) (1/5 : ℝ) (3/4 : ℝ)
    t p q c (by norm_num) (by norm_num) ht hp hq
  have he :
      -(27/320 : ℝ) ≤
        sectorPotential (9/20) (4/5) (1/5)
          (t+p+q) (p*q-c^2) := by
    convert h using 1 <;> norm_num
  unfold fullFieldOnsiteExcess
  linarith

/-- Three-site full-amplitude energy, where each onsite variable is
    an exact POM-3 excess and Q is the bounded octonionic reward. -/
noncomputable def fullAmplitudeLoopEnergy
    (v1 v2 v3 reward : ℝ) (a b c : Bool) : ℝ :=
  v1 + v2 + v3 + (1/4 : ℝ) * (activeEdgeCount a b c : ℝ) -
    if triangleActive a b c then 2*reward else 0

/-- All incomplete graphs are nonnegative, for any reward at all. -/
theorem full_amplitude_open_nonnegative
    (v1 v2 v3 reward : ℝ) (a b c : Bool)
    (hv1 : 0 ≤ v1) (hv2 : 0 ≤ v2) (hv3 : 0 ≤ v3)
    (hopen : triangleActive a b c = false) :
    0 ≤ fullAmplitudeLoopEnergy v1 v2 v3 reward a b c := by
  cases a <;> cases b <;> cases c <;>
    simp_all [triangleActive, fullAmplitudeLoopEnergy, activeEdgeCount] <;>
    linarith

/-- A uniform lower bound for every field and all 8 graph states,
    assuming the already established 0 <= Q <= 1 tensor bound. -/
theorem full_amplitude_global_lower_bound
    (v1 v2 v3 reward : ℝ) (a b c : Bool)
    (hv1 : 0 ≤ v1) (hv2 : 0 ≤ v2) (hv3 : 0 ≤ v3)
    (hQ : reward ≤ 1) :
    -(5/4 : ℝ) ≤ fullAmplitudeLoopEnergy v1 v2 v3 reward a b c := by
  cases a <;> cases b <;> cases c <;>
    simp [fullAmplitudeLoopEnergy, activeEdgeCount, triangleActive] <;>
    linarith

/-- The POM-12b exact quaternion-projector witness Q=4/9
    is still admitted by the NEW smooth full-amplitude model. -/
theorem full_amplitude_octonion_witness :
    fullAmplitudeLoopEnergy 0 0 0 (4/9) true true true =
      -(5/36 : ℝ) := by
  norm_num [fullAmplitudeLoopEnergy, activeEdgeCount, triangleActive]

/-- Every global minimum with negative energy must select a loop:
    there are NO hidden interactions when all links are OFF. -/
theorem negative_energy_forces_complete_loop
    (v1 v2 v3 reward : ℝ) (a b c : Bool)
    (hv1 : 0 ≤ v1) (hv2 : 0 ≤ v2) (hv3 : 0 ≤ v3)
    (hnegative : fullAmplitudeLoopEnergy v1 v2 v3 reward a b c < 0) :
    triangleActive a b c = true := by
  cases a <;> cases b <;> cases c <;>
    simp_all [fullAmplitudeLoopEnergy, activeEdgeCount, triangleActive] <;>
    linarith

/-- On a single common quaternion H, all associators vanish, hence
    Q=0 and no full-amplitude graph configuration has negative energy. -/
theorem full_amplitude_quaternion_nonnegative
    (v1 v2 v3 : ℝ) (a b c : Bool)
    (hv1 : 0 ≤ v1) (hv2 : 0 ≤ v2) (hv3 : 0 ≤ v3) :
    0 ≤ fullAmplitudeLoopEnergy v1 v2 v3 0 a b c := by
  cases a <;> cases b <;> cases c <;>
    norm_num [fullAmplitudeLoopEnergy, activeEdgeCount, triangleActive] <;>
    linarith

/-- The new model has a STRICT separation from EVERY shared-H state,
    but -5/36 is a witness, NOT a computed global minimum in O. -/
theorem full_amplitude_octonion_beats_every_shared_quaternion
    (v1 v2 v3 : ℝ) (a b c : Bool)
    (hv1 : 0 ≤ v1) (hv2 : 0 ≤ v2) (hv3 : 0 ≤ v3) :
    fullAmplitudeLoopEnergy 0 0 0 (4/9) true true true <
      fullAmplitudeLoopEnergy v1 v2 v3 0 a b c := by
  rw [full_amplitude_octonion_witness]
  have h := full_amplitude_quaternion_nonnegative
    v1 v2 v3 a b c hv1 hv2 hv3
  linarith

end POM1
