# KE Deliverables Audit

This audit checks the group-provided Human Expert interview and Knowledge Engineer deliverables against the WID2001 Expert System project requirements.

## Files Reviewed

| File | Usefulness for Project | Status |
|---|---|---|
| `Interview Q&A.docx` | Provides expert-informed domain knowledge about intern readiness, technical skills, project explanation, portfolio evidence, interview weaknesses, and soft skills. | Useful for KB refinement; full evidence belongs in report/appendix |
| `01_Facts_List.csv` | Maps fact IDs to dimensions, UI meanings, rule usage, evidence status, and notes. | Used to enrich `data/facts.json` |
| `02_Rule_Base.csv` | Documents rule IDs, conditions, conclusions, explanations, dimensions, and expert-alignment status. | Used to enrich `data/rules.json` |
| `03_Knowledge_Representation_and_Inference_Diagrams.md` | Provides diagrams for fact extraction, dimension-level inference, final decision/advice flow, and simplified decision tree. | Suitable for report/slides |
| `04_Inference_Trace.md` | Provides runtime traces for High, Medium, and Low readiness cases. | Suitable for report/testing discussion |
| `05_Explanation_Facility_Description.md` | Explains the explanation facility and traceable reasoning chain. | Suitable for report implementation/explanation section |

## Does This Satisfy the Teacher's Requirements?

| Requirement | Current Status | Notes |
|---|---|---|
| Knowledge Base | Completed | Facts and rules exist, and now include KE evidence metadata. |
| Inference Engine | Completed | The system uses forward chaining and returns triggered rules, decisions, recommendations, and explanation chain. |
| User Interface | Completed | Streamlit UI includes Assessment, Results, Explanation, Knowledge Base, and Testing Guide. |
| Knowledge Engineering | Stronger now | Facts/rules are mapped to dimensions and evidence status through KE CSV files. |
| Decision Tree / Rule Diagram | Partially completed | The KE diagram markdown is suitable for report/slides; it should be rendered as figures in the final report. |
| Human Expert | Completed for group report records | Interview content is integrated into the KB. Private expert details and evidence should be documented in the report/appendix, not displayed in the app. |
| Testing | Completed for automated tests; report evidence required | Automated tests exist. Human Expert validation evidence belongs in the report/appendix; end-user testing records should also be collected. |
| Explanation Facility | Completed | Explanation page and KE explanation document support this requirement. |

## Program Updates Made From KE Deliverables

- Added `evidence_status`, `input_or_condition_meaning`, `used_by_rule_ids`, and `knowledge_engineering_note` to `data/facts.json`.
- Added `related_dimension`, `expert_alignment_status`, and `knowledge_engineering_note` to `data/rules.json`.
- Updated the Knowledge Base Viewer to show evidence and expert-alignment columns.
- Added `docs/HUMAN_EXPERT_INTERVIEW_SUMMARY.md`.
- Updated `docs/HUMAN_EXPERT_PLACEHOLDER.md` as a report/appendix evidence template without exposing private details in the app.
- Updated requirement and knowledge-base documentation.

## What Should Go Into the Final Report / Appendix

- Human Expert name, role, organization, interview date, and interview method.
- Evidence such as screenshot, email, signed support letter, or meeting note.
- Final expert validation comments.
- Notes on whether the expert agrees with application-progress rules, especially applying to at least 5 companies, tracking applications, and sending follow-up emails.
- End-user testing feedback from students.
- KE diagrams and inference traces converted into final report/slides.

## Academic Honesty Note

The provided materials improve the system and support the knowledge engineering requirement. Private Human Expert evidence should be kept in the final project report or appendix. Do not publish private evidence in the app or repository unless permission is granted.
