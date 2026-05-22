# Question Difficulty Scoring & Validation

This module assigns a difficulty score (1–5) to each multiple-choice question in the RFIC textbook test bank and validates whether the score correlates with LLM accuracy across small, medium, and frontier models.

## File Description

| File / Folder | Description |
|----------------|-------------|
| `build_score.ipynb` | Using a scoring methodology to get difficulty of each question in testbench |
| `build_type.ipynb` | Getting ordered categorization of each question in testbench |
| `score_vs_accuracy.ipynb` | Comparison of accuracy and scores of testbench for Llama, Qwen and commercial models |
| `testbench_type&score.jsonl` | Testbench and corresponding type and score |
| `testbench_type.jsonl` | Testbench and corresponding type |
| `types_vs_accuracy.ipynb` | Comparison of accuracy and types of testbench for Llama, Qwen and commercial models |

## Scoring Methodology

Each question starts at **2.5**, then adjusted by six factors: length, formula count, complex math symbols, question type, presence of multi-step reasoning markers, and advanced-topic keywords. A basic‑template penalty may also apply. The final score is clamped to `[1, 5]` and rounded to an integer.

## Score Distribution of Testbench (1000 questions)


| Score | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Count | 1 | 232 | 423 | 271 | 73 |
| Ratio | 0.1% | 23.2% | 42.3% | 27.1% | 7.3% |

Most questions cluster at medium difficulty (3–4), with a meaningful tail of harder questions at 5. Score 1 is effectively unused given RFIC textbook content rarely contains trivial recall.

## Validation: Accuracy vs. Difficulty

The scoring is validated against model accuracy on the same test bank. **If the score is meaningful, accuracy should decrease monotonically as difficulty increases.**

### Qwen models 
| Variant | Diff2 | Diff3 | Diff4 | Diff5 | Overall |
|---------|-------|-------|-------|-------|---------|
| Qwen3-0.6B-T | 66.8% | 67.4% | 59.0% | 49.3% | 60.6% |
| Qwen3-0.6B-NT | 68.1% | 65.2% | 58.7% | 49.3% | 60.3% |
| Qwen3-1.7B-T | 72.0% | 75.7% | 63.5% | 58.9% | 67.5% |
| Qwen3-1.7B-NT | 72.4% | 69.0% | 62.0% | 50.7% | 63.5% |
| Qwen3-4B-T | 86.6% | 84.4% | 79.0% | 72.6% | 80.7% |
| Qwen3-4B-NT | 84.5% | 80.6% | 70.7% | 72.6% | 77.1% |
| finetuned-Qwen3-0.6B-T | 76.7% | 70.9% | 68.9% | 52.8% | 67.3% |
| finetuned-Qwen3-0.6B-NT | 72.1% | 72.6% | 63.9% | 52.8% | 65.4% |
| finetuned-Qwen3-1.7B-T | 81.7% | 77.3% | 74.3% | 58.9% | 73.1% |
| finetuned-Qwen3-1.7B-NT | 78.2% | 75.4% | 69.2% | 55.1% | 69.5% |
| finetuned-Qwen3-4B-T | 89.1% | 87.4% | 80.9% | 65.8% | 80.8% |
| finetuned-Qwen3-4B-NT | 86.5% | 84.8% | 80.0% | 62.5% | 78.5% |

### Llama models 
| Variant | Diff2 | Diff3 | Diff4 | Diff5 | Overall |
|---------|-------|-------|-------|-------|---------|
| Llama3.2-1B-Base | 31.5% | 23.9% | 22.1% | 16.4% | 24.6% |
| Llama3.2-1B-Instruct | 35.3% | 32.9% | 35.8% | 32.9% | 34.2% |
| Llama3.2-3B-Base | 47.8% | 37.8% | 27.3% | 31.5% | 36.8% |
| Llama3.2-3B-Instruct | 75.9% | 75.2% | 66.8% | 52.1% | 71.4% |
| finetuned-Llama3.2-1B-Base | 59.5% | 57.9% | 47.2% | 42.5% | 54.3% |
| finetuned-Llama3.2-1B-Instruct | 65.1% | 61.7% | 54.6% | 45.2% | 59.4% |
| finetuned-Llama3.2-3B-Base | 72.8% | 74.7% | 67.2% | 50.7% | 70.5% |
| finetuned-Llama3.2-3B-Instruct | 82.3% | 77.1% | 70.8% | 52.1% | 74.8% |


### Per-variant detail (big models)

| Variant | Diff2 | Diff3 | Diff4 | Diff5 | Overall |
|---|---|---|---|---|---|
| DeepSeek (no RAG) | 92.7% | 91.5% | 86.7% | 71.2% | 89.0% |
| DeepSeek + Basic RAG | 96.6% | 96.2% | 90.8% | 80.8% | 93.7% |
| DeepSeek + Hybrid RAG | 95.3% | 93.9% | 88.9% | 76.7% | 91.6% |
| GPT-4o (no RAG) | 91.8% | 91.5% | 86.3% | 83.6% | 89.6% |
| GPT-4o + Basic RAG | 95.3% | 95.0% | 89.3% | 87.7% | 93.0% |
| GPT-4o + Hybrid RAG | 95.3% | 93.9% | 87.5% | 76.7% | 91.2% |

All 6 big-model variants are **strictly monotonically decreasing** from Diff 2 → Diff 5.


## Validation: Accuracy vs. Categorization

For validation, we assigned a numeric label to each question type for easier reference in later analysis.

During the experiment, we find that: Mathematical derivation (type4) is the hardest type for all models. Scaling, fine-tuning, RAG, and thinking mode all help, with the largest improvements on type4. RAG excels at knowledge-heavy types, while fine-tuning works best for conceptual and design questions.

| Application & Limitations | Conceptual Understanding | Design Implementation | Mathematical Derivation | Performance Analysis |
|---|---|---|---|---|
| type1 | type2 | type3 | type4 | type5 |

### Qwen models 

| Variant | type1 | type2 | type3 | type4 | type5 | Overall |
|-------|-------|-------|-------|-------|-------|---------|
| Qwen3-0.6B-T | 67.0% | 62.9% | 68.6% | 57.1% | 62.1% | 63.5% |
| Qwen3-0.6B-NT | 67.5% | 65.0% | 68.1% | 51.8% | 61.6% | 62.8% |
| Qwen3-1.7B-T | 75.8% | 72.6% | 73.4% | 59.7% | 69.7% | 70.2% |
| Qwen3-1.7B-NT | 74.7% | 68.5% | 69.1% | 55.5% | 64.5% | 66.5% |
| Qwen3-4B-T | 86.6% | 85.3% | 83.6% | 75.9% | 81.5% | 82.6% |
| Qwen3-4B-NT | 83.0% | 81.6% | 83.1% | 68.1% | 75.4% | 78.2% |
| finetuned-Qwen3-0.6B-T | 75.3% | 72.6% | 73.9% | 56.8% | 72.4% | 70.2% |
| finetuned-Qwen3-0.6B-NT | 71.9% | 70.8% | 70.7% | 58.7% | 70.3% | 68.5% |
| finetuned-Qwen3-1.7B-T | 80.3% | 80.1% | 80.9% | 64.6% | 74.4% | 76.1% |
| finetuned-Qwen3-1.7B-NT | 74.0% | 75.5% | 76.1% | 64.6% | 73.6% | 72.8% |
| finetuned-Qwen3-4B-T | 90.1% | 88.2% | 85.5% | 74.7% | 82.9% | 84.3% |
| finetuned-Qwen3-4B-NT | 87.3% | 86.6% | 82.9% | 70.3% | 83.9% | 82.2% |

### Llama models 
| Variant | type1 | type2 | type3 | type4 | type5 | Overall |
|-------|-------|-------|-------|-------|-------|---------|
| Llama3.2-1B-Base | 23.5% | 33.3% | 33.0% | 25.3% | 26.2% | 28.3% |
| Llama3.2-1B-Instruct  | 34.6% | 34.2% | 36.6% | 39.4% | 30.7% | 35.1% |
| Llama3.2-3B-Base | 69.4% | 70.7% | 64.6% | 65.1% | 57.9% | 65.5% |
| Llama3.2-3B-Instruct | 74.7% | 76.1% | 77.8% | 59.3% | 68.7% | 71.3% |
| finetuned-Llama3.2-1B-Base | 62.0% | 56.9% | 53.9% | 45.3% | 55.0% | 54.6% |
| finetuned-Llama3.2-1B-Instruct | 66.0% | 59.4% | 56.0% | 53.9% | 61.1% | 59.3% |
| finetuned-Llama3.2-3B-Base  | 74.7% | 76.0% | 72.8% | 58.6% | 73.1% | 71.0% |
| finetuned-Llama3.2-3B-Instruct | 79.4% | 78.6% | 78.7% | 57.4% | 79.5% | 74.7% |

### Per-variant detail (big models)

| Variant | type1 | type2 | type3 | type4 | type5 | Overall |
|-------|-------|-------|-------|-------|-------|---------|
| DeepSeek (no RAG) | 90.7% | 92.4% | 88.9% | 83.2% | 89.6% | 89.0% |
| DeepSeek + Basic RAG | 99.0% | 95.9% | 94.2% | 87.4% | 91.9% | 93.7% |
| DeepSeek + Hybrid RAG | 94.3% | 93.4% | 93.7% | 85.9% | 90.5% | 91.6% |
| GPT-4o (no RAG) | 92.3% | 90.9% | 93.7% | 79.6% | 91.0% | 89.6% |
| GPT-4o + Basic RAG | 95.9% | 93.4% | 92.8% | 89.0% | 93.8% | 93.0% |
| GPT-4o + Hybrid RAG | 95.4% | 92.4% | 93.7% | 85.9% | 88.6% | 91.2% |
