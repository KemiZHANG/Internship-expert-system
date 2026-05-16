# Testing Guide

## Run App

```bash
streamlit run app.py
```

## Manual UI Test

Use this presentation flow:

1. Assessment: choose a demo case or custom inputs.
2. Results: show Level, Score, Priority, Advice, final decisions, and recommendations.
3. Results: show recommended internship role titles and job search platforms based on the selected major.
4. Explanation: show facts -> rules -> intermediate decisions -> final readiness decision -> specific advice decisions -> recommendations -> career role matching.
5. Knowledge Base: open the filtered Facts, Rules, Recommendations, and Career Paths viewers.
6. Testing Guide: show how automated tests are executed.

## Run Automated Tests

```bash
python tests/test_cases.py
```

Career-path recommendation tests:

```bash
python tests/test_career_paths.py
```

Translation integrity tests:

```bash
python tests/test_translations_integrity.py
```

## Test Cases

The test file includes:

1. Very prepared student -> High readiness
2. Medium prepared student -> Medium readiness
3. Low prepared student -> Low readiness
4. Strong technical but weak interview -> Need interview preparation
5. Good materials but unclear career direction -> Need to clarify target role
6. Has resume but no project/portfolio -> Improve application materials
7. Has project but cannot explain it -> Improve project explanation
8. Has not applied to any company -> Improve application progress
9. High score but unclear career direction -> Must include FD8
10. Low score but strong application materials only -> Must recommend technical or interview improvement

Each test prints:

- selected facts
- readiness score
- score-based level
- final displayed readiness level
- rule-based final decisions
- score fallback decisions
- expected readiness level
- expected decision
- level check PASS / FAIL
- decision check PASS / FAIL
- overall PASS / PARTIAL PASS / FAIL

`PARTIAL PASS` means the expected decision was found but the readiness level did not match the expected level.

`tests/test_career_paths.py` checks that:

- a high-readiness Computer Science student receives software engineering role suggestions
- a medium-readiness Data Science / AI student receives data analyst role suggestions
- a low-readiness Information Systems student receives preparatory role suggestions such as IT Support Intern rather than advanced software engineering roles
- a high-readiness Accounting / Finance student receives finance-related role suggestions
- a medium-readiness Marketing / Communication student receives marketing-related role suggestions
- a low-readiness Psychology / Social Science student receives supervised support role suggestions
- a high-readiness Engineering student receives engineering role suggestions

`tests/test_translations_integrity.py` checks that:

- translation and career-path JSON files do not contain common mojibake strings such as `??` or replacement characters
- every major option has English, Chinese, and Bahasa Melayu labels

## Why This Is an Expert System, Not a Normal Survey

- User inputs are converted into facts.
- IF-THEN rules are stored in the Knowledge Base.
- The Inference Engine applies forward chaining.
- Intermediate decisions and final decisions are inferred.
- The Explanation Facility shows which rules were triggered.

Testing therefore supports both functionality and reasoning accuracy, not only page interaction.

## Human Expert and End-User Testing Still Needed

Automated tests confirm that the current prototype runs and that the reasoning output is consistent with the current rule base. However, the full group project still needs:

- Human Expert validation of facts, rules, and recommendations
- end-user testing feedback from students or intended users
- recorded notes in `docs/TESTING_REPORT_TEMPLATE.md`
- evidence such as screenshots, meeting notes, or email confirmation where appropriate

Do not claim that Human Expert validation has been completed until real evidence has been added.
