# Programmer Handoff Requirements

This file summarizes what the programmer still needs from the group to improve the Internship Preparation Advisory Expert System and to satisfy the WID2001 group project requirements.

## Current Programmer Deliverables

The current prototype already provides:

| Course Component | Evidence |
|---|---|
| Knowledge Base, KB | `data/facts.json`, `data/rules.json`, `data/recommendations.json`, `data/references.json` |
| Inference Engine, IE | `inference_engine.py`, forward chaining with rule firing and score fallback |
| User Interface, UI | `app.py`, Streamlit tabs, multilingual interface |
| Explanation Facility | Explanation page showing facts, triggered rules, intermediate decisions, final decisions, and recommendations |
| Testing | `tests/test_cases.py`, Testing Guide page, `docs/TESTING_GUIDE.md` |
| Documentation | `README.md`, `docs/PROJECT_SUMMARY.md`, `docs/REQUIREMENT_CHECKLIST.md`, and related docs |

## What Each Role Should Provide

| Role | What the Programmer Needs | Where It Will Be Used |
|---|---|---|
| Project Manager | Gantt chart, final roles table, submission schedule, presentation flow, slide/report coordination | `docs/SUBMISSION_READINESS.md`, final slides/report |
| Domain Expert | Internship readiness factors, SDG 4/SDG 8 justification, domain assumptions, reliable public references | `data/references.json`, `docs/INITIAL_KNOWLEDGE_SOURCES.md`, report literature/domain sections |
| Knowledge Engineer | Human Expert interview questions, interview notes, knowledge acquisition summary, corrected rules, decision tree or rule diagram | `data/facts.json`, `data/rules.json`, `docs/KNOWLEDGE_BASE_EXPLANATION.md`, final report |
| Programmer | Implement rule changes, maintain UI/IE/KB integration, run tests, prepare demo flow | `app.py`, `inference_engine.py`, `tests/test_cases.py` |
| End User | Student testing feedback, usability comments, expected results for sample cases, screenshots or notes | `docs/TESTING_REPORT_TEMPLATE.md`, `docs/TESTING_GUIDE.md`, discussion/results section |
| Human Expert / SME | Real name, role, organization, interview date/method, evidence, validation comments, rule corrections | `docs/HUMAN_EXPERT_PLACEHOLDER.md`, KB update, final validation section |

## Still Missing for Full Group Submission

These items cannot be completed by code alone and need real group evidence:

- real Human Expert validation and evidence
- knowledge acquisition notes from the expert interview
- end-user testing records
- final literature review text
- final Gantt chart
- contribution table and group roles
- recorded presentation and prototype demo
- final discussion, conclusion, and future work based on testing feedback

## How Group Feedback Should Update the System

| New Material From Group | File to Update |
|---|---|
| New preparation factors | `data/facts.json` |
| New IF-THEN rules or decision-tree corrections | `data/rules.json` |
| New advice or next action plan | `data/recommendations.json` |
| New literature or online sources | `data/references.json`, `docs/INITIAL_KNOWLEDGE_SOURCES.md` |
| Human Expert details and validation comments | `docs/HUMAN_EXPERT_PLACEHOLDER.md` |
| End-user feedback | `docs/TESTING_REPORT_TEMPLATE.md`, final report testing section |
| UI wording corrections | `data/translations.json` |

## Important Academic Honesty Note

Human Expert validation has not been completed unless real expert information and evidence are added by the group.

This initial prototype uses general internship preparation knowledge and public reference ideas to create a starting knowledge base. The rules and recommendations should be refined and validated through consultation with a real Human Expert.
