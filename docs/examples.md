# Worked Examples

## Example: Real-time / news prompt
Prompt: “Summarize today's top AI news in 3 bullets.”

If the model confidently lists specific events without browsing/citations:
- Label: UNSUPPORTED or UNVERIFIABLE
- Reason: The prompt requires external verification, and the response likely invents specifics.

## Example: Common knowledge prompt
Prompt: “What is the chemical symbol for gold?”

If model answers “Au”:
- Label: SUPPORTED
- Reason: Common knowledge, correct, grounded.

## Example: Math prompt
Prompt: “What is 17 * 23?”

If model answers 391:
- Label: SUPPORTED
If model answers 397:
- Label: UNSUPPORTED
