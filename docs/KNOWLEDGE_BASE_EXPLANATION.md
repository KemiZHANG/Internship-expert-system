# Knowledge Base Explanation

The Knowledge Base is stored in `data/`.

## Files

- `facts.json`: 42 facts with stable IDs and multilingual display text
- `rules.json`: IF-THEN rules for intermediate decisions, final readiness decisions, and recommendation rules
- `recommendations.json`: recommendation content for final decisions
- `references.json`: public sources used for initial knowledge ideas
- `translations.json`: UI translations for English, 中文, and Bahasa Melayu

## Fact Categories

- Application Materials
- Project and Portfolio
- Technical Skills
- Interview Preparation
- Career Direction
- Application Progress
- Soft Skills and Work Readiness

## Rule Format

Each rule contains:

- `id`
- `name`
- `type`
- `conditions`
- `conclusion`
- `conclusion_text`
- `explanation`

Conditions support:

- `all`
- `any`
- `not`

## Decisions

Intermediate decisions use `D` IDs, for example `D1`.

Final decisions use `FD` IDs, for example `FD1`.

Recommendation rule conclusions use `REC` IDs, for example `REC1`.

## Multilingual Display

Internal IDs remain unchanged. Display text is translated for the UI where appropriate. If a translation is missing, the app falls back to English.

## Knowledge Base Viewer

The Streamlit app includes a Knowledge Base Viewer with:

- object type filtering for Facts, Rules, and Recommendations
- category filtering
- rule-type filtering for intermediate, final, and recommendation rules
- a simple system architecture flow for presentation

This helps demonstrate that the prototype is a structured rule-based Expert System rather than a simple form.

The Knowledge Base therefore supports the course requirement for knowledge engineering: domain knowledge is represented as facts, IF-THEN rules, decision layers, and recommendation objects that can be reviewed and updated later after Human Expert consultation.
