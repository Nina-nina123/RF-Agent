# Supervised Fine-Tuning (SFT)

We perform Supervised Fine-Tuning (SFT) on the RF QTSA dataset to adapt general-purpose LLMs to RF circuit reasoning tasks.

The QTSA dataset contains structured RF reasoning supervision in Question–Thinking–Solution–Answer (QTSA) format.

## File Description

| File / Folder | Description |
|----------------|-------------|
| `README.md` | Documentation for SFT experiments |
| `Qwen3-0.6B/` | Final dataset & testbench generation<br>Fine-tuning experiments and saved models for Qwen3-0.6B<br>Generation and calculation of final accuracy of Qwen series |
| `Qwen3-1.7B/` | Fine-tuning experiments for Qwen3-1.7B |
| `Qwen3-4B/` | Fine-tuning experiments for Qwen3-4B |
| `Llama3.2-1B/` | Fine-tuning experiments for Llama3.2-1B<br>Generation and calculation of final accuracy of Llama series |
| `Llama3.2-1B-Instruct/` | Fine-tuning experiments for Llama3.2-1B-Instruct |
| `Llama3.2-3B/` | Fine-tuning experiments for Llama3.2-3B |
| `Llama3.2-3B-Instruct/` | Fine-tuning experiments for Llama3.2-3B-Instruct |


## Results

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

*T: Thinking mode; NT: Non-thinking mode.*

## Summary

- Domain-specific SFT consistently improves RF reasoning performance.
- Small and medium-sized models benefit the most.
- Thinking-mode models achieve stronger RF reasoning capability.
- Larger models show smaller gains due to stronger baseline performance.

