# RF-Agent: A Practical Framework for Building Language Agents for RFIC Design

This repository accompanies the paper **"RF-Agent: A Practical Framework
for Building Language Agents for RFIC Design"**. It releases the code,
datasets, and benchmarks used to construct the first reasoning-oriented
language-agent framework for radio-frequency integrated circuit (RFIC)
design.

RF-Agent addresses the lack of domain-specific resources for RFIC-oriented
language agents by combining:

- A **textbook-driven RF reasoning corpus** distilled from seven canonical
  RF textbooks.
- A **multi-agent QTSA (Question–Thinking–Solution–Answer) distillation
  pipeline** that converts the corpus into reasoning-oriented training
  data.
- The **first open-source RF-domain reasoning dataset** with over 11,000
  samples and a dedicated 1,000-question multiple-choice benchmark.
- Two complementary domain-adaptation strategies — **Supervised
  Fine-Tuning (SFT)** and **Retrieval-Augmented Generation (RAG)** — with
  a comparative study of three retrieval configurations (semantic,
  keyword, hybrid).
- A **cross-model evaluation** across multiple LLM families (Qwen3,
  Llama-3.2, GPT-4o, DeepSeek).

![Multi-agent QTSA distillation pipeline](./Multi-agent%20QTSA%20distillation%20pipeline.png)

---

## Repository Structure

| Folder | Description |
|---|---|
| [`QAs from textbooks/`](./QAs%20from%20textbooks) | RF corpus construction, multi-agent QTSA distillation pipeline, mcQTSA / ndQTSA generation, and release of the dataset & benchmark. |
| [`Question difficulty scoring & categorization/`](./Question%20difficulty%20scoring%20%26%20categorization) | Question difficulty scoring (1–5) and question-type categorization for the benchmark, plus accuracy-vs-difficulty / accuracy-vs-type validation across all evaluated models. |
| [`RAG/`](./RAG) | Retrieval-augmented generation pipelines and evaluation: basic, hybrid, hit-and-miss, and DeepSeek / GPT testing scripts on the RF knowledge base. |
| [`SFT/`](./SFT) | Supervised fine-tuning experiments on the QTSA dataset across the Qwen3 (0.6B / 1.7B / 4B & Thinking / NoThinking) and Llama-3.2 (1B / 3B, base & instruct) families. |
| `Hybrid RAG pipeline for RF knowledge retrieval.png` | Hybrid RAG pipeline figure (Fig. 3 in the paper), illustrates the BM25 + BGE-M3 + RRF + BGE-ReRanker-V2-M3 retrieval flow over the RF knowledge base. |
| `Multi-agent QTSA distillation pipeline.png` | Multi-agent QTSA distillation pipeline (Fig. 1 in the paper). |


---

## 1. RF-Domain Reasoning Dataset and Benchmark

We extract content from **seven canonical RF textbooks** and parse each
book at the subsection level into self-contained conceptual units. A
three-agent pipeline (Question Agent → Answer Agent → Process Agent)
then converts each subsection into structured Q–T–S–A quadruples.

| Dataset    | Samples           | Avg. Tokens | Total Tokens |
|------------|-------------------|-------------|--------------|
| Subsection | 1,108             | 1,974       | 2.2 M        |
| mcQTSA     | 5,540             | 1,136       | 7.4 M        |
| ndQTSA     | 5,529             | 2,480       | 13.7 M       |

Features:
- **Five-perspective question generation** — conceptual understanding,
  mathematical derivation, design implementation, performance analysis,
  and applications & limitations.
- **Chain-of-thought supervision** using `<think>…</think>` and
  `<answer>…</answer>` tags, directly compatible with thinking-mode SFT.
- A standardized **1,000-question RF multiple-choice benchmark** carved
  from the held-out mcQTSA subset.

See `QAs from textbooks/`for the construction
notebooks and the released `dataset&benchmark/` directory.

---

## 2. Domain Adaptation via Supervised Fine-Tuning

We fine-tune across two model families spanning 0.6B–4B parameters with
both base and instruction-tuned variants, in both thinking and
non-thinking inference modes.

| Model | Base Acc. | Base Time (s) | Fine-tuned Acc. | Fine-tuned Time (s) |
|--------|------------|----------------|-----------------|---------------------|
| Llama3.2-1B-Base | 24.7% | 1.34 | 54.4% | 18.80 |
| Llama3.2-1B-Instruct | 34.2% | 3.75 | 59.3% | 31.10 |
| Llama3.2-3B-Base | 37.1% | 42.64 | 70.5% | 45.64 |
| Llama3.2-3B-Instruct | 71.3% | 2.49 | 74.7% | 16.50 |
| Qwen3-0.6B-T | 63.6% | 62.98 | 70.2% | 35.87 |
| Qwen3-0.6B-NT | 62.9% | 4.57 | 67.7% | 16.22 |
| Qwen3-1.7B-T | 70.3% | 68.47 | 75.3% | 41.61 |
| Qwen3-1.7B-NT | 66.5% | 2.29 | 71.3% | 17.94 |
| Qwen3-4B-T | 82.6% | 112.78 | 83.5% | 53.14 |
| Qwen3-4B-NT | 78.2% | 5.06 | 80.5% | 32.59 |

*T: thinking mode; NT: non-thinking mode.*

Key findings:
- Domain-specific SFT consistently improves RF reasoning.
- **Small and medium-sized models benefit the most.**
- Thinking-mode models achieve stronger RF reasoning capability and
  faster post-tuning inference.
- Gains diminish for larger, already-strong models.

See `SFT/` for fine-tuning notebooks and per-model evaluation
scripts.

---

## 3. RF Retrieval-Augmented Generation

The RAG module grounds model responses in an authoritative external RF
knowledge base:

- **950** RF-related peer-reviewed papers
- **10** canonical RF textbooks
- Diagram-aware multimodal retrieval — schematics, Smith charts,
  S-parameter plots, and block diagrams are converted to structured
  textual descriptions and indexed alongside text chunks.

Three retrieval configurations are systematically compared:

- **Semantic retrieval** (BGE-M3 embeddings + ChromaDB)
- **Keyword retrieval** (BM25)
- **Hybrid retrieval** (Reciprocal Rank Fusion + BGE-ReRanker-V2-M3)

Experiments show that **semantic retrieval consistently outperforms
keyword and hybrid retrieval** for RF reasoning, e.g. raising GPT-4o from
89.6% → 93.0% and DeepSeek-V3.2-T from 89.1% → 93.7% on the RF
benchmark. See `RAG/`.


### **Evaluation of State-of-the-Art LLMs With and Without RAG**

| Model | No RAG | Semantic | Keyword | Hybrid |
|-------|--------|----------|---------|--------|
| GPT-4o | 89.6% | 93.0% | 92.1% | 91.2% |
| DeepSeek-V3.2-T | 89.1% | 93.7% | 93.0% | 91.6% |

### **Hit-and-Miss Retrieval Validation Across Model Sizes**

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th colspan="2">Semantic RAG</th>
      <th colspan="2">Keyword RAG</th>
      <th colspan="2">Hybrid RAG</th>
    </tr>
    <tr>
      <th></th>
      <th>Hit</th>
      <th>Miss</th>
      <th>Hit</th>
      <th>Miss</th>
      <th>Hit</th>
      <th>Miss</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Qwen3-0.6B-T</td>
      <td><strong>81%</strong></td>
      <td>65%</td>
      <td><strong>74%</strong></td>
      <td>73%</td>
      <td><strong>71%</strong></td>
      <td>65%</td>
    </tr>
    <tr>
      <td>Qwen3-1.7B-T</td>
      <td><strong>84%</strong></td>
      <td>75%</td>
      <td><strong>80%</strong></td>
      <td>75%</td>
      <td><strong>80%</strong></td>
      <td>75%</td>
    </tr>
    <tr>
      <td>Qwen3-4B-T</td>
      <td><strong>92%</strong></td>
      <td>83%</td>
      <td><strong>86%</strong></td>
      <td>82%</td>
      <td><strong>85%</strong></td>
      <td>80%</td>
    </tr>
    <tr>
      <td><strong>Avg. Δ</strong></td>
      <td colspan="2"><strong>+10.3%</strong></td>
      <td colspan="2"><strong>+3.3%</strong></td>
      <td colspan="2"><strong>+5.0%</strong></td>
    </tr>
  </tbody>
</table>

![Hybrid RAG pipeline for RF knowledge retrieval](./Hybrid%20RAG%20pipeline%20for%20RF%20knowledge%20retrieval.png)

---

## 4. Question Difficulty Scoring & Categorization

To validate the benchmark, we assign each multiple-choice question a
**difficulty score (1–5)** based on length, formula count, math
complexity, question type, reasoning markers, and advanced-topic
keywords. We further label each question by one of five **categories**
(Application & Limitations, Conceptual Understanding, Design
Implementation, Mathematical Derivation, Performance Analysis).

Across all evaluated models (small, medium, and frontier) accuracy
decreases **monotonically** as difficulty increases, and **mathematical
derivation (type 4)** is consistently the hardest category. RAG helps
most on knowledge-heavy types, while SFT helps most on conceptual and
design questions.

See `Question difficulty scoring & categorization/`
for the scoring methodology, the `testbench_type&score.jsonl` file, and
the analysis among difficulty, categorization and accuracy.


