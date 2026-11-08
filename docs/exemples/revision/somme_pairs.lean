import Mathlib

theorem somme_de_deux_pairs (a b : ℤ)
    (ha : Even a) (hb : Even b) : Even (a + b) := by
  rcases ha with ⟨k, hk⟩
  rcases hb with ⟨l, hl⟩
  refine ⟨k + l, ?_⟩
  rw [hk, hl]
  ring
