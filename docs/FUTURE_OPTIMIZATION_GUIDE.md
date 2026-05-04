# Future Optimization Guide

Use this guide after the group receives Human Expert feedback, better rules, more references, testing feedback, or new recommendations.

## Human Expert Feedback

1. Record real expert details in `docs/HUMAN_EXPERT_PLACEHOLDER.md`.
2. Extract expert comments into possible facts, rules, weights, and recommendations.
3. Update only the relevant KB files.
4. Re-run tests.
5. Document what changed and why.

Do not fabricate expert names, interviews, or validation.

## Update Facts

Edit `data/facts.json`.

- Keep IDs stable if possible.
- Add multilingual `display_text`.
- Avoid contradictory facts in the UI mapping.

## Update Rules

Edit `data/rules.json`.

- Keep rule IDs unique.
- Use `all`, `any`, and `not`.
- Keep explanations short and presentation-friendly.
- Re-run `python tests/test_cases.py`.

## Update Recommendations

Edit `data/recommendations.json`.

- Update title, summary, recommendation, next steps, and priority.
- Add multilingual display content if the UI should show translated advice.

## Update Translations

Edit `data/translations.json`.

- Use UTF-8.
- Keep internal IDs untranslated.
- If a translation is missing, the app falls back to English.

## Update Scoring

Edit `calculate_readiness_score` and `build_readiness_summary` in `inference_engine.py`.

If expert feedback changes weights, update README and docs too.

## Update References

Edit `data/references.json` with real links only.
