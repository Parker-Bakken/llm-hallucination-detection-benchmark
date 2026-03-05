# LLM Hallucination Detection Benchmark (Mini)

A small, transparent benchmark for evaluating hallucination tendencies in LLM responses.

## What’s inside
- `data/prompts.csv` — prompts across domains
- `data/evaluations.csv` — model outputs + labels
- `docs/labeling_guidelines.md` — rules + edge cases
- `docs/examples.md` — worked examples with rationale
- `tools/summarize_results.py` — summary stats
- `gold/gold_set.csv` — adjudicated edge cases (added)
- `qa/qa_log.csv` — disagreement/adjudication log (added)

## Label schema
- **SUPPORTED**: grounded in prompt/context or widely verifiable
- **UNSUPPORTED**: fabricated or incorrect claims
- **MIXED**: combination of supported + unsupported
- **UNVERIFIABLE**: cannot be verified without external sources, or too vague/refusal

## How to run
1) Generate outputs for each prompt (any model)
2) Paste outputs into `data/evaluations.csv`
3) Label using `docs/labeling_guidelines.md`
4) Run:
```bash
python tools/summarize_results.py
