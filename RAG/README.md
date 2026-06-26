# RAG Experiment Summary

This repository contains several RAG experiment notebooks organized into four main testing categories.

## 1. Basic RAG testing on lower-parameter Qwen models

Folder: `basic_rag_testing/`

Notebooks:
- `Qwen2.5_0.5B_RAG_Basic.ipynb`
- `Qwen2.5_0.5B_Instruct_RAG_Basic.ipynb`
- `Qwen2.5_1.5B_RAG_Basic.ipynb`
- `Qwen2.5_1.5B_Instruct_RAG_Basic.ipynb`
- `Qwen2.5_3B_RAG_Basic.ipynb`
- `Qwen2.5_3B_Instruct_RAG_Basic.ipynb`
- `Qwen3_0.6B_nothinking_RAG_Basic.ipynb`
- `Qwen3_0.6B_thinking_RAG_Basic.ipynb`
- `Qwen3_1.7B_nothinking_RAG.ipynb`
- `Qwen3_1.7B_thinking_RAG_Basic.ipynb`
- `Qwen3_4B_nothinking_RAG_Basic.ipynb`
- `Qwen3_4B_thinking_RAG_Basic.ipynb`

## 2. Hit/Miss experiments using low-parameter Qwen models for all RAG types

Folder: `hit_miss_qwen3/`

Notebooks:
- `Qwen3_0.6B_thinking_RAG_Basic_hit.ipynb`
- `Qwen3_0.6B_thinking_RAG_Basic_miss.ipynb`
- `Qwen3_0.6B_thinking_RAG_Hybrid_hit.ipynb`
- `Qwen3_0.6B_thinking_RAG_Hybrid_miss.ipynb`
- `Qwen3_0.6B_thinking_RAG_Keyword_hit.ipynb`
- `Qwen3_0.6B_thinking_RAG_Keyword_miss.ipynb`
- `Qwen3_1.7B_thinking_RAG_Basic_hit.ipynb`
- `Qwen3_1.7B_thinking_RAG_Basic_miss.ipynb`
- `Qwen3_1.7B_thinking_RAG_Hybrid_hit.ipynb`
- `Qwen3_1.7B_thinking_RAG_Hybrid_miss.ipynb`
- `Qwen3_1.7B_thinking_RAG_Keyword_hit.ipynb`
- `Qwen3_1.7B_thinking_RAG_Keyword_miss.ipynb`
- `Qwen3_4B_thinking_RAG_Basic_hit.ipynb`
- `Qwen3_4B_thinking_RAG_Basic_miss.ipynb`
- `Qwen3_4B_thinking_RAG_Hybrid_hit.ipynb`
- `Qwen3_4B_thinking_RAG_Hybrid_miss.ipynb`
- `Qwen3_4B_thinking_RAG_Keyword_hit.ipynb`
- `Qwen3_4B_thinking_RAG_Keyword_miss.ipynb`

## 3. Deepseek SOTA model testing on base, basic, hybrid, keyword RAG

Folder: `deepseek_testing/`

Notebooks:
- `Deepseek-V3.2-Thinking_Basic_RAG.ipynb`
- `Deepseek-V3.2-Thinking_Hybrid_RAG.ipynb`
- `Deepseek-V3.2-Thinking_Keyword_RAG.ipynb`
- `Deepseek-V3.2-Thinking_Testing.ipynb`

## 4. GPT-4o SOTA model testing on base, basic, hybrid, keyword RAG

Folder: `gpt_testing/`

Notebooks:
- `GPT_4o_Basic_RAG.ipynb`
- `GPT_4o_Hybrid_RAG.ipynb`
- `GPT_4o_keyword_RAG.ipynb`
- `GPT_4o_Testing.ipynb`

## Shared testbench

All experiment notebooks are intended to use the same testbench dataset:

- `testbench/mcQTSA_test_final.jsonl`

Replace the notebook's `INPUT_FILE` path with the above path corresponding to that file in the repository.
