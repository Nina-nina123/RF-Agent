###

# RF-Agent Dataset Collection & Benchmark Construction

This document describes the construction of the **RF-Agent reasoning dataset** and the accompanying **multiple-choice benchmark** for evaluating language models on RF circuit design tasks.

We release two complementary datasets:
- **mcQTSA**: Multiple-choice QTSA (Question–Thinking–Solution–Answer) for discriminative reasoning and evaluation.
- **ndQTSA**: Open-ended QTSA for generative reasoning and explanation depth.

Both datasets are distilled from authoritative RF textbooks using a **multi-agent pipeline**, forming the first open-source reasoning-oriented corpus for RFIC design.

### Human Quality Control

Although the QTSA generation pipeline is largely automated, we further introduced manual quality control procedures to improve dataset reliability and consistency.

Specifically:

- **Manual inspection of generated samples:** Thousands of QTSA samples were manually reviewed to identify formatting issues, invalid reasoning traces, and generation failures.

- **Semantic subdivision of overly long nodes:** Source textbook sections that were excessively long or contained multiple independent concepts were manually divided into semantically coherent units before QTSA generation, improving reasoning granularity and retrieval quality.

- **Format normalization and correction:** Parts of generated outputs were manually checked and corrected for formatting inconsistencies, including malformed JSON structures, incomplete QTSA fields, incorrect option formatting, and structural deviations from the target schema.

- **Spot-checking of theoretical validity in testbench:** 200 samples from testbench were randomly selected for detailed manual verification. The checking process, conducted by individuals with graduate-level domain knowledge, focused on the logical coherence of reasoning traces, the correctness of final answers, and the consistency of each QTSA with the source textbook content, helping to ensure that automated generation does not compromise theoretical reliability.

These human quality assurance steps complement the automated multi-agent distillation pipeline and help ensure higher dataset consistency, reasoning quality, and benchmark reliability.

## File Description

| File / Folder | Description |
|----------------|-------------|
| `dataset&benchmark/` | Collection of mcQTSA, ndQTSA and RF-benchmark |
| `get_nodes.ipynb` | Getting subsections through data distillation from RF textbooks |
| `mcQTSA_generation.ipynb` | Getting mcQTSA from subsections |
| `ndQTSA_generation.ipynb` | Getting ndQTSA from subsections |
| `node.jsonl` | File of subsections |

## 📚 Corpus Source

We extract content from **seven canonical RF textbooks**, covering:
- ***Microwave Engineering*** by David M. Pozar
- ***RF and Microwave Power Amplifier Design*** by Andrei Grebennikov
- ***RF Microelectronics*** by Behzad Razavi
- ***RF Power Amplifiers*** by Marian K. Kazimierczuk
- ***RF Power Amplifiers for Wireless Communications*** by Steve C. Cripps,
- ***Advanced Techniques in RF Power Amplifier Design*** by Steve C. Cripps
- ***RF Circuit Design: Theory & Applications*** by Reinhold Ludwig

Each book is parsed at the subsection level into self-contained conceptual units.  

## 🤖 Multi-Agent QTSA Distillation Pipeline

![Multi-agent QTSA distillation pipeline](../Multi-agent%20QTSA%20distillation%20pipeline.png)

## 📊 Dataset Statistics

| Dataset | Samples | Avg. Tokens | Total Tokens |
|---------|---------|--------------|----------------|
| Subsection | 1,108 | 1,974 | 2.2M |
| mcQTSA | 5,540 | 1,136 | 7.4M |
| ndQTSA | 5,529 | 2,480 | 13.7M |

