import json
import re

def score_difficulty(obj):
    q = obj["question"]
    t = obj.get("type", "")

    base = 2.5

    q_len = len(q)
    if q_len < 350:
        base -= 1.3
    elif q_len < 550:
        base -= 0.7
    elif q_len < 900:
        base += 0.0
    elif q_len < 1300:
        base += 0.6
    elif q_len < 1800:
        base += 1.1
    else:
        base += 1.5

    inline_eq = q.count("\\(") + q.count("\\)")
    block_eq = q.count("\\[") + q.count("\\]")
    formula_units = inline_eq // 2 + block_eq // 2
    if formula_units >= 25:
        base += 1.5
    elif formula_units >= 15:
        base += 1.0
    elif formula_units >= 8:
        base += 0.6
    elif formula_units >= 3:
        base += 0.2

    complex_symbols = sum(q.count(s) for s in ["\\sqrt", "\\frac", "\\sum", "\\int",
                                                "\\partial", "\\omega", "\\beta",
                                                "\\Gamma", "\\eta", "\\mu", "\\epsilon"])
    if complex_symbols >= 15:
        base += 0.5
    elif complex_symbols >= 8:
        base += 0.3
    elif complex_symbols >= 3:
        base += 0.1

    if t == "Methematical Derivation":
        base += 0.5
    elif t == "Performance Analysis":
        base += 0.3
    elif t == "Design Implementation":
        base += 0.2
    elif t == "Application & Limitations":
        base -= 0.1
    elif t == "Conceptual Understanding":
        base -= 0.2

    qlow = q.lower()
    multi_indicators = ["derive", "implication", "and how", "and what",
                        "considering", "what condition", "under which",
                        "given that", "based on"]
    if any(ind in qlow for ind in multi_indicators):
        base += 0.2

    advanced_topics = ["class e", "class f", "doherty", "outphasing",
                       "feedforward", "predistortion", "envelope tracking",
                       "kahn", "eer", "polar modulation", "harmonic balance",
                       "manley-rowe", "ferrite", "gyromagnetic", "smith chart",
                       "stability circle", "rollett", "load-pull",
                       "intermodulation", "memory effect"]
    if any(topic in qlow for topic in advanced_topics):
        base += 0.2

    basic_markers = ["which of the following statements correctly describes",
                     "what is the primary",
                     "why is", "why does", "why are"]
    if q_len < 700 and any(m in qlow for m in basic_markers):
        base -= 0.1

    score = max(1, min(5, round(base)))
    return score

input_path = "/home/xy67/RFIC Chatbot/QAs from textbooks/Claude_rating/testbench_type.jsonl"
output_path = "/home/xy67/RFIC Chatbot/QAs from textbooks/Claude_rating/testbench_score_Claude.jsonl"

distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

with open(input_path, "r", encoding="utf-8") as fin, open(output_path, "w", encoding="utf-8") as fout:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        s = score_difficulty(obj)
        obj["score"] = s
        distribution[s] += 1
        fout.write(json.dumps(obj, ensure_ascii=False) + "\n")

total = sum(distribution.values())
print(f"Total: {total}")
for k in sorted(distribution):
    print(f"Score {k}: {distribution[k]} ({distribution[k]/total*100:.1f}%)")
