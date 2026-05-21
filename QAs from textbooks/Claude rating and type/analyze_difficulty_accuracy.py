import json
from collections import defaultdict

# Load difficulty scores by line number (1-indexed)
difficulty = {}
with open("testbench_score_Claude.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        obj = json.loads(line)
        difficulty[i] = obj["score"]

# Load Llama outcomes; ID field corresponds to line number 1..1000
records = []
with open("LLama_Outcome_1000.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        records.append(obj)

# Identify model columns (exclude ID and Correct Answer)
sample = records[0]
model_cols = [k for k in sample.keys() if k not in ("ID", "Correct Answer")]

# Compute accuracy per model per difficulty level
# An answer is correct if it exactly matches the correct answer string
acc_by_diff = {m: defaultdict(lambda: [0, 0]) for m in model_cols}  # [correct, total]
overall_by_diff = defaultdict(lambda: [0, 0])

for rec in records:
    rid = int(rec["ID"])
    diff = difficulty.get(rid)
    if diff is None:
        continue
    correct = rec["Correct Answer"]
    for m in model_cols:
        ans = rec.get(m)
        if ans is None:
            continue  # skip null answers
        acc_by_diff[m][diff][1] += 1
        if ans == correct:
            acc_by_diff[m][diff][0] += 1
        overall_by_diff[diff][1] += 1
        if ans == correct:
            overall_by_diff[diff][0] += 1

print("=" * 100)
print("Accuracy by difficulty (excluding null answers)")
print("=" * 100)
print(f"{'Model':<50} " + " ".join(f"Diff{d}" for d in [1,2,3,4,5]))
print("-" * 100)
for m in model_cols:
    row = [m]
    parts = []
    for d in [1, 2, 3, 4, 5]:
        c, t = acc_by_diff[m][d]
        if t == 0:
            parts.append("  N/A")
        else:
            parts.append(f"{c/t*100:5.1f}")
    print(f"{m:<50} " + " ".join(parts))

print()
print("Overall accuracy (averaged across all model variants) by difficulty:")
print(f"{'Difficulty':<12} {'Accuracy':<12} {'N':<10}")
for d in [1, 2, 3, 4, 5]:
    c, t = overall_by_diff[d]
    if t == 0:
        print(f"{d:<12} {'N/A':<12} {t}")
    else:
        print(f"{d:<12} {c/t*100:5.1f}%       {t}")

# Spearman-like rank check: compute average accuracy per difficulty
print()
print("Difficulty distribution in test bank:")
diff_dist = defaultdict(int)
for d in difficulty.values():
    diff_dist[d] += 1
for d in [1, 2, 3, 4, 5]:
    print(f"  Score {d}: {diff_dist[d]} questions")
