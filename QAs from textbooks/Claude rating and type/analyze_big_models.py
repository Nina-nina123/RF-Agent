import json
from collections import defaultdict

difficulty = {}
with open("testbench_score_Claude.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        obj = json.loads(line)
        difficulty[i] = obj["score"]

files = [
    ("DeepSeek", "/home/jw161/chatbot/deepseek_testing/results/Outcome_1000.jsonl"),
    ("GPT", "/home/jw161/chatbot/gpt_testing/results/Outcome_1000.jsonl"),
]

for source, path in files:
    print("=" * 90)
    print(f"{source}: {path}")
    print("=" * 90)

    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            records.append(obj)

    model_cols = [k for k in records[0].keys() if k not in ("ID", "Correct Answer")]

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

    print(f"{'Model':<55} " + " ".join(f"Diff{d}" for d in [2, 3, 4, 5]) + "   Overall")
    print("-" * 95)
    for m in model_cols:
        accs = []
        total_c, total_t = 0, 0
        for d in [2, 3, 4, 5]:
            c, t = acc_by_diff[m][d]
            accs.append(c / t * 100 if t else None)
            total_c += c
            total_t += t
        overall = total_c / total_t * 100 if total_t else 0
        acc_str = " ".join(f"{a:5.1f}" if a is not None else "  N/A" for a in accs)
        print(f"{m:<55} {acc_str}    {overall:5.1f}")

    print(f"\n  Pooled accuracy by difficulty (all variants together):")
    for d in [2, 3, 4, 5]:
        c, t = overall_by_diff[d]
        print(f"    Diff {d}: {c/t*100:5.1f}% ({c}/{t})")
    print()
