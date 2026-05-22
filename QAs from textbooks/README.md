###

# RF-Agent Dataset Collection & Benchmark Construction

This document describes the construction of the **RF-Agent reasoning dataset** and the accompanying **multiple-choice benchmark** for evaluating language models on RF circuit design tasks.

We release two complementary datasets:
- **mcQTSA**: Multiple-choice QTSA (Question–Thinking–Solution–Answer) for discriminative reasoning and evaluation.
- **ndQTSA**: Open-ended QTSA for generative reasoning and explanation depth.

Both datasets are distilled from authoritative RF textbooks using a **multi-agent pipeline**, forming the first open-source reasoning-oriented corpus for RFIC design.

### File Description

| File / Folder | Description |
|----------------|-------------|
| `train.py` | Main script for Supervised Fine-Tuning |
| `inference.py` | RF reasoning inference using trained checkpoints |
| `train.sh` | Training launcher script |
| `config.yaml` | Hyperparameter configuration |
| `dataset/` | RF QTSA training dataset |
| `outputs/` | Fine-tuned checkpoints and exported models |
| `logs/` | TensorBoard logs and training records |
| `merge_lora.py` | Merge LoRA weights into base model |

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

