# Knowledge Base Explanation

The Knowledge Base is stored in `data/`.

## Files

- `facts.json`: 42 facts with stable IDs and multilingual display text
- `rules.json`: IF-THEN rules for intermediate decisions, final readiness decisions, and recommendation rules
- `recommendations.json`: recommendation content for final decisions
- `career_paths.json`: major-to-role-track knowledge, readiness-level role titles, and job search platforms
- `references.json`: public sources used for initial knowledge ideas
- `translations.json`: UI translations for English, 中文, and Bahasa Melayu

## Knowledge Engineering Evidence

The latest version also includes Knowledge Engineering metadata supplied by the group:

- `01_Facts_List.csv` was used to add `evidence_status`, `input_or_condition_meaning`, `used_by_rule_ids`, and `knowledge_engineering_note` to facts.
- `02_Rule_Base.csv` was used to add `related_dimension`, `expert_alignment_status`, and `knowledge_engineering_note` to rules.
- `Interview Q&A.docx` supports several readiness factors, especially technical foundation, project explanation, problem-solving, portfolio evidence, interview communication, and soft skills.

This strengthens the project because the KB is no longer only a generic initial rule list; it now records which parts are supported by the interview, which parts are indirectly supported, and which parts still need Human Expert validation.

Important limitation: application-volume thresholds, application tracking, and follow-up rules are still marked as needing rule-level expert validation because the provided interview did not directly discuss those details.

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

## Career Path Knowledge

`data/career_paths.json` adds a career-path knowledge layer without replacing the rule base. It contains:

- majors, such as Computer Science, Software Engineering, Information Systems, Data Science / AI, Cybersecurity, Business Analytics, Accounting / Finance, Business Management / HR, Marketing / Communication, Law / Public Policy, Psychology / Social Science, Education, Mass Communication, Design, Engineering, Health Science, Environmental Science, Hospitality / Tourism, Logistics / Supply Chain, Agriculture / Food Science, Language / Linguistics, and Sports Science
- role tracks, such as Software Engineering, Data Analysis, Cybersecurity, Accounting, Finance, Marketing, HR, Legal, Policy Research, Human Services, Education, Journalism, Graphic Design, Engineering, Healthcare Administration, Laboratory Research, Sustainability, Hospitality, Events, Logistics, Procurement, Agriculture/Food, Translation, and Sports/Fitness
- matching facts for each role track, for example programming skill, Git, SQL/database basics, project evidence, communication, and job-description comparison
- suggested internship role titles for Low, Medium, and High readiness levels
- job search platforms such as LinkedIn Jobs, JobStreet Malaysia, Hiredly, MyNext, Prosple Malaysia, and Handshake

This career-path mapping is based on public references and must still be reviewed by a real Human Expert.

## Multilingual Display

Internal IDs remain unchanged. Display text is translated for the UI where appropriate. If a translation is missing, the app falls back to English.

## Knowledge Base Viewer

The Streamlit app includes a Knowledge Base Viewer with:

- object type filtering for Facts, Rules, Recommendations, and Career Paths
- category filtering
- rule-type filtering for intermediate, final, and recommendation rules
- evidence-status and KE-note columns for facts
- expert-alignment and KE-note columns for rules
- a simple system architecture flow for presentation
- a Decision Tree / Rule Diagram showing FACTS -> AND/OR/NOT -> DECISIONS

This helps demonstrate that the prototype is a structured rule-based Expert System rather than a simple form.

The Knowledge Base therefore supports the course requirement for knowledge engineering: domain knowledge is represented as facts, IF-THEN rules, decision layers, and recommendation objects that can be reviewed and updated later after Human Expert consultation.
