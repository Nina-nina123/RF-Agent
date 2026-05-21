import json
from collections import defaultdict

difficulty = {}
with open("testbench_score_Claude.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        obj = json.loads(line)
        difficulty[i] = obj["score"]

records = []
with open("LLama_Outcome_1000.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        records.append(obj)

sample = records[0]
model_cols = [k for k in sample.keys() if k not in ("ID", "Correct Answer")]

# Treat null as wrong (denominator = all questions)
acc_by_diff = {m: defaultdict(lambda: [0, 0]) for m in model_cols}
overall_by_diff = defaultdict(lambda: [0, 0])

for rec in records:
    rid = int(rec["ID"])
    diff = difficulty.get(rid)
    if diff is None:
        continue
    correct = rec["Correct Answer"]
    for m in model_cols:
        ans = rec.get(m)
        acc_by_diff[m][diff][1] += 1
        if ans == correct:
            acc_by_diff[m][diff][0] += 1
        overall_by_diff[diff][1] += 1
        if ans == correct:
            overall_by_diff[diff][0] += 1

print("Accuracy (null=wrong), per model per difficulty:")
print(f"{'Model':<50} " + " ".join(f"Diff{d}" for d in [2,3,4,5]))
print("-" * 100)
monotonic_decrease = 0
total_models = len(model_cols)
for m in model_cols:
    accs = []
    for d in [2, 3, 4, 5]:
        c, t = acc_by_diff[m][d]
        accs.append(c/t*100 if t else None)
    # Check if monotonically (weakly) decreasing 2->5
    valid = [a for a in accs if a is not None]
    if len(valid) >= 4 and all(valid[i] >= valid[i+1] - 2 for i in range(len(valid)-1)):
        monotonic_decrease += 1
    print(f"{m:<50} " + " ".join(f"{a:5.1f}" if a is not None else "  N/A" for a in accs))

print()
print(f"Models with (weakly) monotonic decreasing accuracy 2→5: {monotonic_decrease}/{total_models}")

print()
print("Overall (all-model-answers pooled) accuracy by difficulty (null=wrong):")
for d in [2, 3, 4, 5]:
    c, t = overall_by_diff[d]
    print(f"  Diff {d}: {c/t*100:5.1f}% ({c}/{t})")
