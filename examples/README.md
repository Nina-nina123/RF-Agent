# RF-Agent — Worked Examples

This folder collects two human-readable examples that illustrate the core
mechanics of RF-Agent:

1. a single **mcQTSA reasoning sample** (the Question–Thinking–Solution–Answer
   format used for both training and evaluation), and
2. a **RAG hit-vs-miss retrieval case** showing how retrieval quality drives
   answer correctness.

Both correspond to illustrative figures in the paper and are linked to the
released data they were drawn from, so they can be inspected, reproduced, or
extended directly from the repository.

---

## 1. Representative mcQTSA Sample — SSB Mixer Spur Analysis

<!-- Optional: export Fig. 2 from the LaTeX source and place it here as
     mcQTSA_example_mixer.png to show the rendered figure. -->
<!-- ![mcQTSA example](mcQTSA_example_mixer.png) -->

**Source dataset:** `QAs from textbooks/dataset&benchmark/mcQTSA_new4/`
**Benchmark partition:** `SFT/Qwen3-0.6B/testbench/mcQTSA_test_final.jsonl`
**Reasoning perspective:** circuit-level behavior / performance analysis

### Question

In a direct-conversion transmitter using an SSB mixer with input frequencies
ω1 and ω2 = ω1/2, the output contains the desired component at ω1 + ω2 = 3ω1/2
and spurs at frequencies 3ω1 − ω2 and 3ω2 − ω1. If the port sensing ω2 is
linearized to suppress its associated spur, which spur frequency remains
problematic, and why does this require substantial filtering?

- **A.** The spur at ω1/2 remains problematic because it is too close to the
  desired carrier, causing insufficient attenuation by typical LC filtering.
- **B.** The spur at 5ω1/2 remains problematic because it arises from the
  nonlinearity at the ω1 port and lies outside the easily filterable band.
- **C.** The spur at 5ω1/2 remains problematic because the LC filter cannot
  distinguish it from the fundamental carrier frequency at 3ω1/2.
- **D.** The spur at 3ω1/2 remains problematic since it coincides with the
  desired signal, thereby causing interference that filtering cannot resolve.

### Thinking  `<think> … </think>`

The transmitter uses an SSB mixer with inputs ω1 and ω2 = ω1/2. The desired
output is at ω1 + ω2 = 3ω1/2. Third-order nonlinearity generates spurs at
3ω1 − ω2 and 3ω2 − ω1; substituting ω2 = ω1/2:

- 3ω1 − ω2 = 3ω1 − (ω1/2) = 5ω1/2
- 3ω2 − ω1 = 3(ω1/2) − ω1 = ω1/2

Linearizing the port that senses ω2 suppresses the spur at 3ω2 − ω1 (= ω1/2).
The spur at 3ω1 − ω2 (= 5ω1/2) is not suppressed by that linearization and
therefore remains, requiring substantial filtering. Option B states the 5ω1/2
spur remains and arises from the nonlinearity at the ω1 port — this matches.
The correct choice is B.

### Solution

- **Problem setup** — Inputs: ω1 and ω2 = ω1/2. Desired SSB output: ω1 + ω2 = 3ω1/2.
- **Spur frequencies** — 3ω1 − ω2 = 5ω1/2; 3ω2 − ω1 = ω1/2.
- **Effect of port linearization** — Linearizing the ω2-sensing port suppresses
  the spur at 3ω2 − ω1 (= ω1/2). The remaining spur, 3ω1 − ω2 (= 5ω1/2),
  originates from the nonlinearity of the ω1 port and cannot be simultaneously
  linearized, so it persists and requires substantial filtering.
- **Map to choices** — B is correct: the 5ω1/2 spur remains and requires
  substantial filtering because it arises from the nonlinearity at the ω1 port.

### Answer  `<answer> … </answer>`

**B**

---

## 2. Representative RAG Hit-vs-Miss Case — Single-Turn Inductor Self-Inductance

<!-- Optional: export Fig. 4 from the LaTeX source and place it here as
     hit_miss_example_inductor.png to show the rendered figure. -->
<!-- ![hit-miss example](hit_miss_example_inductor.png) -->

This example illustrates the hit/miss validation used to confirm that accuracy
gains stem from retrieval quality rather than incidental context injection. For
the same question, the **hit** condition uses the top-3 retrieved chunks as
context, while the **miss** condition uses the next three chunks (ranks 4–6)
from the same retrieval run.

### Question

For a single-turn planar round inductor with mean radius *a* and strip width
*w*, assuming *w ≪ a*, which expression correctly approximates its
self-inductance *L*?

- **A.** L ≈ μa [ ln(8a / w) − 2 ], valid for a ≫ w
- **B.** L ≈ (μl / 2π) [ ln(4a / w) − 1 ], where l = 2πa
- **C.** L ≈ μ₀l [ arcsinh(l / 2w) − 1 ], valid only for square planar inductors
- **D.** L ≈ μ√(ab) [ (2/k − k) K(k) − (2/k) E(k) ], where k = w / 2a and
  K(k), E(k) are elliptic integrals

### Outcome

| Condition | Retrieved context (source) | Why | Model answer | Correct? |
|-----------|----------------------------|-----|--------------|----------|
| **Hit**  | top-3 chunks — *RF Power Amplifiers* (Kazimierczuk), p. 475 | Contains the exact single-turn self-inductance derivation | **A** | ✅ |
| **Miss** | ranks 4–6 — *RF Power Amplifiers* (Kazimierczuk), p. 480 | Related passage (square-spiral / Wheeler's formula) but not the needed derivation | **B** | ❌ |

The hit chunk surfaces the precise derivation required to answer the question;
the miss chunk retrieves a topically related but insufficient passage from the
same document, leading the model to an incorrect choice.

### Full retrieved chunks (released data)

The actual hit and miss context passages for every benchmark question are
released here (example shown is from the Qwen3-4B-Thinking, semantic/basic
configuration):

- **Hit contexts:** `RAG/hit_miss_qwen3/results/100_Qwen3_4B_thinking_contexts_Basic_hit.jsonl`
- **Miss contexts:** `RAG/hit_miss_qwen3/results/100_Qwen3_4B_thinking_contexts_Basic_miss.jsonl`
- **Model answers:** `RAG/hit_miss_qwen3/results/100_Qwen3_4B_thinking_RAG_Basic_hit.jsonl`
  and `…_miss.jsonl`

Equivalent files for the 0.6B and 1.7B models and for the keyword/hybrid
configurations are in the same `RAG/hit_miss_qwen3/results/` directory.

---

## Notes

- **Adding the figure images (optional).** The two commented-out image links
  above reference the worked-example figures from the paper. To include them,
  export the figures from the LaTeX source as `mcQTSA_example_mixer.png` and
  `hit_miss_example_inductor.png`, place them in this folder, and uncomment the
  corresponding `![…]` lines.
- The mcQTSA sample reproduces a representative item in the released dataset;
  the math notation is transcribed from the paper figure for readability.
