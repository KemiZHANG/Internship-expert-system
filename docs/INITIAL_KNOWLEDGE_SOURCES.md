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
- Technical and field-specific interview preparation for software, AI, data, business, engineering, communication, social science, and other internships
- Behavioral interview and STAR method
- Job description matching
- Application tracking and follow-up
- Rule-based expert system examples
- Python forward chaining expert system examples
- Streamlit decision support system examples
- Major-to-internship role mapping
- Entry-level technology role families
- Broad university major-to-career mapping
- Non-IT internship role families, including business, accounting, finance, HR, marketing, law, psychology, education, media, design, engineering, healthcare, science, hospitality, tourism, logistics, agriculture, language, and sports science
- Malaysia and student internship search platforms

## Sources Found

The real links are recorded in `data/references.json`. The reference set includes university career preparation guides, NACE career readiness competencies, STAR interview materials, application follow-up guides, GitHub portfolio guidance, and public rule-engine / Streamlit repositories.

For the career-path recommendation feature, public sources were searched for:

- BLS and O\*NET role descriptions for software development, QA, web development, data science, cybersecurity, systems analysis, and database roles.
- University career center pages that map majors such as Computer Science, Information Systems, Management Information Systems, and Data Science to possible entry-level roles.
- BLS occupation groups and university career exploration pages that map broad university majors to possible career families.
- Psychology, business, engineering, media/communication, education, legal, healthcare, science, hospitality, logistics, agriculture, language, and sports-related role ideas from public career resources.
- Public internship/job platforms such as LinkedIn Jobs, JobStreet Malaysia, Hiredly, MyNext by TalentCorp Malaysia, Prosple Malaysia, and Handshake guidance.

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
- selected major or study field
- role-track matching facts, such as programming, Git, SQL/database basics, project evidence, communication, and job-description comparison
- readiness-level role title recommendations, such as IT Support Intern for lower readiness or Software Engineering Intern/Data Science Intern for higher readiness
- broader readiness-level role title recommendations, such as Accounting Assistant Intern, Digital Marketing Intern, Legal Intern, Teaching Assistant Intern, Engineering Intern, Lab Assistant Intern, Hotel Operations Intern, Supply Chain Intern, or Community Service Assistant Intern

These facts were converted into IF-THEN rules. For example:

- If resume, tailored resume, professional profile, and supporting documents are present, infer high application material readiness.
- If a project exists but the student cannot explain the project goal or implementation, infer that project explanation needs improvement.
- If the student has not applied to companies yet, infer that application progress needs improvement.
- If no rule produces a final decision, use the score-based fallback to produce FD1, FD2, or FD3.

The career-path feature was added as a separate knowledge base file, `data/career_paths.json`. It maps:

- major -> suitable role tracks
- role track -> matching facts and suggested internship titles by readiness level
- readiness level -> suitable role-title difficulty
- platform -> job search use case and region

This is still an initial public-reference mapping, not expert-validated advice.

## Academic Honesty Note

This initial prototype uses general internship preparation knowledge and public reference ideas to create a starting knowledge base. The rules and recommendations should be refined and validated through consultation with a real Human Expert.

No Human Expert validation has been completed at this stage. No expert names, interview records, or validation comments are fabricated.
