# LLM Hallucination Detection Benchmark (Mini)

A small, transparent benchmark to evaluate hallucination tendencies in LLM responses.

## What this repo contains
- `data/prompts.csv`: 30 test prompts across domains
- `data/evaluations.csv`: labeled outcomes using a simple rubric
- `docs/labeling_guidelines.md`: labeling rules and edge cases
- `docs/examples.md`: worked examples with rationale
- `tools/summarize_results.py`: quick summary stats

## Label schema
- **SUPPORTED**: Claims are grounded in prompt/context or widely verifiable facts
- **UNSUPPORTED**: Contains fabricated or incorrect claims
- **MIXED**: Combination of supported + unsupported claims
- **UNVERIFIABLE**: Cannot be verified without external sources or the model refuses / is too vague

## How to use
1) Run prompts through any model(s) you want to evaluate.
2) Paste model outputs into `data/evaluations.csv`.
3) Label each response using the rubric.
4) Run summary: `python tools/summarize_results.py`

## Why this matters
Rater work often involves judging whether outputs are grounded, faithful, and safe—this repo demonstrates that evaluation workflow in a reproducible format.
