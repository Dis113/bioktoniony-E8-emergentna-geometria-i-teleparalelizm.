import Mathlib

/-!
# POM-8: exact rational full-sector trial counterexample

The model-specific ring energy is E=(16/3)*sum_i(q_(i,i+2)-q_(i,i+1)),
where q=Tr(P_i P_j)/4 for quaternion projectors selected by POM-3.
This eight-site witness is a finite rational certificate, NOT a global
minimum theorem, physical fermion proof, or rediscovery of ANNNI/SSH.

Two integer Householder reflection vectors per site give exact rational
orthonormal imaginary vectors u_i,v_i in R^7. Their octonionic product
w_i=u_i*v_i supplies the third imaginary quaternion basis direction.
The Cayley-Dickson structure constants below agree with the Python
implementation in Simulations/pom1_model.py.

WARNING: finite rational computation uses native_decide/compiler trust.
The known quaternion composition-algebra results are not re-proved.
-/

namespace POM1

def witnessZ1 (s : Fin 8) : Fin 7 → ℤ :=
  match s.val with
  | 0 => ![6, 0, -1, 0, 3, 1, -2]
  | 1 => ![2, 2, 1, -1, 0, 0, 2]
  | 2 => ![4, -1, 1, 1, 3, -3, 0]
  | 3 => ![3, 1, -1, 1, -2, 2, -2]
  | 4 => ![2, 1, -1, 1, 0, 3, -2]
  | 5 => ![6, -1, 0, 0, -1, -3, 2]
  | 6 => ![4, 1, -1, 0, -2, -2, 2]
  | 7 => ![5, -2, 2, -1, -2, 0, 0]
  | _ => ![1, 0, 0, 0, 0, 0, 0]

def witnessZ2 (s : Fin 8) : Fin 7 → ℤ :=
  match s.val with
  | 0 => ![0, 1, -1, 0, -2, 1, 1]
  | 1 => ![0, 3, 0, -1, 0, 1, -3]
  | 2 => ![0, 4, 0, 1, -2, 0, -3]
  | 3 => ![0, 3, -2, 0, 0, 3, 2]
  | 4 => ![0, 7, 2, -1, -1, -1, -1]
  | 5 => ![0, 8, -1, -1, -1, 0, 0]
  | 6 => ![0, 1, 2, 0, -1, -1, 0]
  | 7 => ![0, 5, 1, 1, -2, -3, 1]
  | _ => ![1, 0, 0, 0, 0, 0, 0]


def householderEntry (z : Fin 7 → ℤ) (i j : Fin 7) : ℚ :=
  (if i = j then (1 : ℚ) else 0) -
    2 * (z i : ℚ) * (z j : ℚ) /
    (∑ k : Fin 7, (z k : ℚ)^2)

def trialU (s : Fin 8) (k : Fin 7) : ℚ :=
  householderEntry (witnessZ1 s) k 0

def trialV (s : Fin 8) (k : Fin 7) : ℚ :=
  ∑ l : Fin 7, householderEntry (witnessZ1 s) k l *
    householderEntry (witnessZ2 s) l 1

/-- Integer multiplication structure on the seven imaginary Cayley-Dickson
octonion basis vectors, only for i < j; reverse products are negative. -/
def basisCrossUpper (i j : Nat) : Nat × ℤ :=
  match i, j with
  | 0, 1 => (2, 1)
  | 0, 2 => (1, -1)
  | 0, 3 => (4, 1)
  | 0, 4 => (3, -1)
  | 0, 5 => (6, -1)
  | 0, 6 => (5, 1)
  | 1, 2 => (0, 1)
  | 1, 3 => (5, 1)
  | 1, 4 => (6, 1)
  | 1, 5 => (3, -1)
  | 1, 6 => (4, -1)
  | 2, 3 => (6, 1)
  | 2, 4 => (5, -1)
  | 2, 5 => (4, 1)
  | 2, 6 => (3, -1)
  | 3, 4 => (0, 1)
  | 3, 5 => (1, 1)
  | 3, 6 => (2, 1)
  | 4, 5 => (2, -1)
  | 4, 6 => (1, 1)
  | 5, 6 => (0, -1)
  | _, _ => (0, 0)

def basisCrossCoefficient (i j k : Fin 7) : ℤ :=
  if i = j then 0
  else if i.val < j.val then
    if (basisCrossUpper i.val j.val).1 = k.val then
      (basisCrossUpper i.val j.val).2 else 0
  else
    if (basisCrossUpper j.val i.val).1 = k.val then
      -(basisCrossUpper j.val i.val).2 else 0

def trialW (s : Fin 8) (k : Fin 7) : ℚ :=
  ∑ i : Fin 7, ∑ j : Fin 7,
    trialU s i * trialV s j * (basisCrossCoefficient i j k : ℚ)

def trialImaginaryFrame (s : Fin 8) (a : Fin 3) (k : Fin 7) : ℚ :=
  if a.val = 0 then trialU s k
  else if a.val = 1 then trialV s k
  else trialW s k

/-- Orthogonal projector trace for the 4-real-dimensional quaternion sectors.
Each basis shares the scalar 1 and three orthonormal imaginary vectors. -/
def trialOverlap (i j : Fin 8) : ℚ :=
  (1 + ∑ a : Fin 3, ∑ b : Fin 3,
    (∑ k : Fin 7,
      trialImaginaryFrame i a k * trialImaginaryFrame j b k)^2) / 4

def trialFrustrationEnergy : ℚ :=
  (16/3 : ℚ) * (∑ i : Fin 8,
    (trialOverlap i (i + 2) - trialOverlap i (i + 1)))

/-- The explicit rational eight-site orientation has lower energy than -12,
the energy of the previously studied optimized period-4 binary trial.
This is a COUNTEREXAMPLE to the assertion that that binary trial is a
global energy minimum on the full quaternion-sector configuration space. -/
theorem trial_full_vacuum_beats_binary_period_four :
    trialFrustrationEnergy < (-12 : ℚ) := by
  native_decide

end POM1
