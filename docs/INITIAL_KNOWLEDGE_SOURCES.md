# Initial Knowledge Sources

## Purpose

This file records public sources searched for the initial and optimized knowledge base. These sources are used only as public reference ideas. They are not Human Expert interview results.

## Search Directions

The following directions were searched:

- Internship preparation checklist
- Career readiness assessment
- Student internship readiness factors
- Resume and cover letter preparation
- Portfolio, GitHub, and LinkedIn preparation for CS or AI students
- Technical interview preparation for software, AI, and data internships
- Behavioral interview and STAR method
- Job description matching
- Application tracking and follow-up
- Rule-based expert system examples
- Python forward chaining expert system examples
- Streamlit decision support system examples

## Sources Found

The real links are recorded in `data/references.json`. The reference set includes university career preparation guides, NACE career readiness competencies, STAR interview materials, application follow-up guides, GitHub portfolio guidance, and public rule-engine / Streamlit repositories.

## Conversion Into Facts and Rules

Public reference ideas were converted into prototype facts such as:

- resume completed
- tailored resume
- cover letter prepared
- professional profile prepared
- GitHub or project portfolio available
- project README or demo available
- programming and technical foundations
- technical and behavioral interview practice
- STAR method
- target role clarity
- job description comparison
- application tracking and follow-up
- communication, teamwork, and time management

These facts were converted into IF-THEN rules. For example:

- If resume, tailored resume, professional profile, and supporting documents are present, infer high application material readiness.
- If a project exists but the student cannot explain the project goal or implementation, infer that project explanation needs improvement.
- If the student has not applied to companies yet, infer that application progress needs improvement.
- If no rule produces a final decision, use the score-based fallback to produce FD1, FD2, or FD3.

## Academic Honesty Note

This initial prototype uses general internship preparation knowledge and public reference ideas to create a starting knowledge base. The rules and recommendations should be refined and validated through consultation with a real Human Expert.

No Human Expert validation has been completed at this stage. No expert names, interview records, or validation comments are fabricated.
