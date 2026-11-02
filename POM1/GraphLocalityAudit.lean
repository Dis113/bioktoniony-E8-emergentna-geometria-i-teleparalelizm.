import Mathlib
import POM1.SelfGeneratedFlux

/-!
Critical audit of a previously overstated physical claim in POM-10.

The closed-loop trial energy is correctly minimized under its assumed
polynomial. HOWEVER the 'open' energy already couples spins when the
graph has ZERO active edges. Thus choosing 3 Boolean edges does not
demonstrate that a network of local interactions emerged from an
initially disconnected system. The global spin background is an input.

This is a POM-specific model diagnostic. It does not re-prove known
theorems about graph locality, octonions, or Weyl eigenvalue bounds.
-/

namespace POM1

/-- Valid open-graph spin data with u1=e1,u2=e2,u3=e1:
a=b=chi=0, c=1. With NO edges, energy is -5. -/
theorem empty_graph_parallel_background :
    openTriangleEnergy 1 0 0 = (-5 : ℝ) := by
  norm_num [openTriangleEnergy]

/-- Valid open-graph spin data with u3=-e1:
a=b=chi=0, c=-1. With NO edges, energy is +7. -/
theorem empty_graph_antiparallel_background :
    openTriangleEnergy (-1) 0 0 = (7 : ℝ) := by
  norm_num [openTriangleEnergy]

/-- At zero edges the POM-10 energy remains sensitive to remote
orientations (12 energy units), a concrete failure of strict edge locality. -/
theorem empty_graph_has_residual_interaction :
    openTriangleEnergy (-1) 0 0 -
      openTriangleEnergy 1 0 0 = (12 : ℝ) := by
  norm_num [openTriangleEnergy]

/-- The no-edge background cannot be an edge-local energy functional
with zero spin interaction. Any interpretation of the closed-loop
selection must explicitly retain this nonlocal prerequisite. -/
theorem empty_graph_not_spin_independent :
    openTriangleEnergy 1 0 0 ≠
      openTriangleEnergy (-1) 0 0 := by
  norm_num [openTriangleEnergy]

end POM1
