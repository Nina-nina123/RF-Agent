# RF_Agent
A Practical Framework for Building Language Agents for RFIC Design

## Overview

RF-Agent addresses the lack of domain-specific resources for RFIC-oriented language agents by introducing:

- A textbook-driven RF reasoning corpus constructed from canonical RF textbooks
- A multi-agent QTSA (Question–Thinking–Solution–Answer) distillation pipeline
- The first RF-domain reasoning dataset with over 11K samples
- A standardized RF multiple-choice benchmark
- Domain adaptation via:
  - Supervised Fine-Tuning (SFT)
  - Retrieval-Augmented Generation (RAG)
- Cross-model evaluation across multiple LLM families

## Key Contributions

### 1. RF-Domain Reasoning Dataset

We construct:

| Dataset | Samples | Description |
|----------|----------|-------------|
| mcQTSA | 5,540 | Multiple-choice RF reasoning dataset |
| ndQTSA | 5,529 | Normal dialog and open-ended RF reasoning dataset |
| RF Corpus | 1,108 subsections | Canonical RF textbook corpus |

Features:

- Five-perspective question generation
- Chain-of-thought supervision
- RF-domain benchmark construction
- Thinking-oriented training format

### 2. RF Retrieval-Augmented Generation

Three retrieval strategies are systematically evaluated:

- Semantic Retrieval
- Keyword Retrieval (BM25)
- Hybrid Retrieval

Knowledge base:

- 950 RF papers
- 10 canonical RF textbooks
- Diagram-aware multimodal retrieval

### 3. Domain Adaptation Study

We evaluate:

- Qwen3 series
- Llama3.2 series
- GPT models
- DeepSeek models

Results demonstrate:

- Significant RF reasoning improvement through domain adaptation
- Strong gains for small and medium-sized models
- Semantic retrieval consistently outperforms keyword and hybrid retrieval

