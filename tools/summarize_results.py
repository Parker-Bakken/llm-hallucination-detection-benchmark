import csv
from collections import Counter, defaultdict
from pathlib import Path

EVAL_PATH = Path(__file__).resolve().parents[1] / "data" / "evaluations.csv"

def main():
    if not EVAL_PATH.exists():
        raise FileNotFoundError(f"Missing {EVAL_PATH}")

    rows = []
    with EVAL_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r.get("label"):
                rows.append(r)

    if not rows:
        print("No labeled rows found yet.")
        return

    overall = Counter(r["label"].strip().upper() for r in rows)
    by_model = defaultdict(Counter)
    for r in rows:
        by_model[r["model_name"]][r["label"].strip().upper()] += 1

    print("Overall label counts:")
    for k, v in overall.most_common():
        print(f"  {k}: {v}")

    print("\nBy model:")
    for model, counts in by_model.items():
        total = sum(counts.values())
        print(f"  {model} (n={total})")
        for k, v in counts.most_common():
            print(f"    {k}: {v}")

if __name__ == "__main__":
    main()
