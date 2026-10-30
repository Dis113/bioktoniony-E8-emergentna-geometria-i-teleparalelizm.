# POM-1: minimalna specyfikacja hipotezy (2026-10-30)

## 1. Status i zasada metodologiczna

POM-1 to projekt spekulatywnej teorii emergentnej geometrii. Oddzielamy:
1. **twierdzenia matematyczne** o zdefiniowanych układach;
2. **postulaty modelu**, np. komórki bioktonionowe i interakcje sieci;
3. **hipotezy identyfikacji fizycznych**, które wymagają wyprowadzenia i konfrontacji z danymi.

Powiązanie `E₈ → próżnia → Model Standardowy` NIE jest dowiedzione.

## 2. Algebra i E₈

Algebra bioktonionów: `B = ℂ ⊗_ℝ 𝕆`; wymiar rzeczywisty = 16.
Nie jest łączna. Wybranie rzeczywistego iloczynu skalarnego na jej składowych
jest dodatkową strukturą modelu (nie „macierzą gęstości” z definicji).

Dla 240 pierwiastków `α ∈ Φ(E₈) ⊂ ℝ⁸`, `‖α‖² = 2`:

```math
∑_α α_i α_j = 60 δ_ij.
```

Wybór: `Ψ_i = x_i + i y_i`, gdzie `x_i,y_i ∈ 𝕆 ≅ ℝ⁸`.
Wprowadzenie `i` oznacza zespolenie, nie jednostkę konkretnego oktonionu.

Potencjał orientacyjny:

```math
U_{E8}(x,y) = ε ∑_{α∈Φ(E8)}
  [2 - cos((α·x)/f) - cos((α·y)/f)]
```

`ε ≥ 0, f ≠ 0`; wówczas `U ≥ 0` i `U(0,0)=0`.
W pobliżu zera:

```math
U_{E8} = (30 ε/f²)(‖x‖²+‖y‖²) + O(‖(x,y)‖⁴).
```

Zatem izotropowy wkład do kwadratu masy:
`Δm² = 60 ε/f²` (przy kanonicznej normalizacji pól).
**Wszystkie 16 realnych modów ma na tym etapie ten sam wkład masowy.**
Wybór jednego lekkiego modu nie wynika sam z `E₈`.

## 3. Hipotetyczny hamiltonian sieci

Stan `Ψ_i` jest przypisany wierzchołkowi grafu przyczynowego `G`.
Jako klasyczne przybliżenie dynamiczne proponujemy

```math
H_micro =
 Σ_i [ (1/2)‖p_i‖² + (μ²/2)‖Ψ_i‖²
       + (λ_Ψ/4)‖Ψ_i‖⁴ + U_E8(Ψ_i) ]
 + (K/2) Σ_(i,j)‖Ψ_i−Ψ_j‖²
 + γ Σ_(i,j,k)‖(Ψ_iΨ_j)Ψ_k−Ψ_i(Ψ_jΨ_k)‖².
```

Aby energia była ograniczona od dołu w tej przykładowej wersji,
wystarczy `μ², λ_Ψ, K, γ, ε ≥ 0` (po ustaleniu konwencji normy).
Dla `γ>0` koszt energetyczny asocjatora nie jest automatycznie
mechanizmem uwięzienia koloru QCD.

Zdefiniowanie składowych pędu, Poissona lub unitarnej kwantyzacji, wyboru
grafu i dynamicznego porządku przyczynowego pozostaje otwartym zadaniem.

## 4. Teoria efektywna: oddzielny postulat

Po wyborze tetrady `e^a_μ` i płaskiej koneksji spinowej `ω^a_{bμ}`
przyjmujemy przykładowe działanie skalar–torzja w czterech wymiarach:

```math
S_eff = ∫ d⁴x e [
 -(M_P²+ξφ²) T/2
 -(1/2) g^{μν}∂_μφ∂_νφ
 - V₀ - m²φ²/2 - λφ⁴/4
 + L_SM
].
```

Zakładamy sygnaturę `(-+++)`, jednostki `ℏ=c=1` oraz konwencję
`R=-T+B`. Dla `ξ=0` część grawitacyjna odpowiada TEGR.
Nie ma jeszcze wyprowadzenia `φ, e^a_μ, ω^a_{bμ}, ξ` z `H_micro`.
Dopisanie `L_SM` nie jest unifikacją oddziaływań.

Przy `ξ=λ=0` i potencjale `V(φ)=V₀+m²φ²/2`:
- oscylacje pola z `m≫H` mają uśrednione `w≈0`, `ρ∝a⁻³`;
- dodatni `V₀` zachowuje się jak energia próżni `w=-1`.

To znany mechanizm skalarnej ciemnej materii plus stałej kosmologicznej,
a nie nowe obserwacyjne przewidywanie samej algebraicznej struktury E₈.

## 5. Czas, odległość i c

Relacje przyczynowe można badać bez zadanej metryki, lecz obecnie
w hamiltonianie używa się parametru ewolucji. Zatem *emergentny czas*
nie został jeszcze wyprowadzony.
Stosunek `ℓ_P/t_P=c` jest tożsamością definicyjną jednostek Plancka.

Aby móc mówić o wyprowadzeniu szczególnej względności i grawitacji,
potrzebne jest zdefiniowanie efektywnego stożka przyczynowego,
lokalnej izotropii, transformacji Lorentza, 3+1 wymiarów i tetrad.

## 6. Kryteria sukcesu

Minimalne kryteria:
- energia i ewolucja są dobrze określone; brak niestabilności od dołu;
- wyprowadzone, nie postulowane, stożki przyczynowe i metryka Lorentza;
- limit niskoenergetyczny odtwarza TEGR i testy grawitacyjne;
- odpowiednie sektory reprezentacji Modelu Standardowego (w tym chiralność);
- nowe przewidywania dają się ograniczyć obserwacyjnie;
- jawne odróżnienie dokładnych dowodów Lean od symulacji i hipotez.
