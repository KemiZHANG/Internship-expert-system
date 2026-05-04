# Requirement Checklist

This checklist audits the current prototype against the WID2001 group project expectations.

## Summary Table

| Requirement | Status | Evidence in Project | Still Need to Do |
|---|---|---|---|
| Introduction | Completed | `README.md`, `docs/PROJECT_SUMMARY.md` | Refine wording for final report if needed. |
| Objectives | Completed | `README.md`, `docs/PROJECT_SUMMARY.md` | Align the final written report wording across group materials. |
| Human Expert & References / Literature Review | Partially Completed | `docs/INITIAL_KNOWLEDGE_SOURCES.md`, `data/references.json`, `docs/HUMAN_EXPERT_PLACEHOLDER.md`, support letter files outside repo | Add real Human Expert details, interview notes, validation comments, and formal literature review text in the group report. |
| ES Architecture | Completed | `app.py` Knowledge Base / Testing Guide architecture flow, `README.md`, `docs/PROJECT_SUMMARY.md` | Prepare one clean architecture figure for slides/report. |
| Knowledge Base / Knowledge Engineering / Decision Tree | Completed | `data/facts.json`, `data/rules.json`, `data/recommendations.json`, `docs/KNOWLEDGE_BASE_EXPLANATION.md`, Knowledge Base page | Optionally convert current rule layers into a polished decision-tree style diagram for slides. |
| Inference Engine / Reasoning Method | Completed | `inference_engine.py`, `docs/INFERENCE_ENGINE_EXPLANATION.md`, Explanation page | Add short pseudocode or flowchart to slides if desired. |
| User Interface | Completed | `app.py`, Streamlit tabs, multilingual UI, Results / Explanation / Knowledge Base / Testing Guide pages | Capture screenshots for the final presentation deck. |
| Implementation / Tool Selection | Completed | `README.md`, Python + Streamlit project structure, JSON KB files | Explain briefly in report why Streamlit + JSON were chosen for a local prototype. |
| Testing with Human Expert and End Users | Partially Completed | `tests/test_cases.py`, `docs/TESTING_GUIDE.md`, `docs/TESTING_REPORT_TEMPLATE.md` | Conduct and record real Human Expert testing and end-user testing. |
| Discussion / Results | Partially Completed | Results page, Explanation page, `README.md`, automated test output | Write group discussion of findings, limitations, and observations in report/slides. |
| Future and Conclusion | Partially Completed | `docs/FUTURE_OPTIMIZATION_GUIDE.md`, `docs/PROJECT_SUMMARY.md` | Add final report conclusion section after group testing and expert feedback. |
| Report Format / Tables / Figures / Gantt Chart / References | Missing | Partial source material exists in docs and external PDFs | Needs to be completed by group members. |
| Demonstration | Partially Completed | Streamlit app, demo cases, Explanation page, Knowledge Base Viewer, Testing Guide | Record final video demo and polish speaking flow. |
| Soft Skills / Group roles / Q&A / recorded presentation | Missing | Not evidenced in codebase | Needs to be completed by group members. |

## Why This Is an Expert System

1. Knowledge Base contains facts, IF-THEN rules, recommendations, and reference notes.
2. Inference Engine uses forward chaining to fire rules when conditions match.
3. User input becomes facts before reasoning starts.
4. Rules fire only when `all`, `any`, and `not` conditions are satisfied.
5. Intermediate decisions and final decisions are inferred from the rule chain.
6. Explanation Facility shows selected facts, triggered rules, inferred decisions, and recommendations.
7. Score is only supportive; rule-based reasoning is the core logic of the prototype.

## Requirement Notes

### What the Programmer Part Already Covers

- Local working prototype with `KB`, `IE`, and `UI`
- forward chaining implementation
- explanation facility
- recommendations and next action plan
- testing script with pass/fail output
- multilingual interface for demo clarity
- Knowledge Base viewer for facts, rules, and recommendations

### What Still Depends on Group Members

- real Human Expert consultation and evidence
- end-user testing evidence
- literature review writing
- Gantt chart
- roles and contribution table
- report formatting, tables, figures, and references
- recorded presentation, demo narration, and Q&A preparation

### Evidence Pointers

- Main UI: `app.py`
- Inference engine: `inference_engine.py`
- Knowledge base: `data/facts.json`, `data/rules.json`, `data/recommendations.json`
- Translation support: `data/translations.json`
- Automated tests: `tests/test_cases.py`
- Testing instructions: `docs/TESTING_GUIDE.md`
- Expert placeholder: `docs/HUMAN_EXPERT_PLACEHOLDER.md`

This initial prototype uses general internship preparation knowledge and public reference ideas to create a starting knowledge base. The rules and recommendations should be refined and validated through consultation with a real Human Expert.
