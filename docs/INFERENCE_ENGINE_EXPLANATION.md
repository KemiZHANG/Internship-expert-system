# Inference Engine Explanation

The Inference Engine is implemented in `inference_engine.py`.

This component corresponds directly to the course requirement for the Inference Engine (IE). It is the part of the prototype that applies reasoning to the facts selected in the UI and produces inferred decisions.

## Forward Chaining

The engine follows this process:

1. User input is mapped to facts.
2. Facts are added to working memory.
3. Rules are checked one by one.
4. If a rule condition is satisfied, the rule fires.
5. The rule conclusion is added to working memory.
6. The process repeats until no new conclusion can be added.

## Condition Evaluation

The engine supports:

- `all`: all listed items must be in working memory
- `any`: at least one listed item must be in working memory
- `not`: none of the listed items may be in working memory

## Score-Based Fallback

The rule-based system remains the main reasoning mechanism. The score is used to make final readiness more robust.

Score structure:

- Application Materials: 25
- Project and Portfolio: 15
- Technical Skills: 25
- Interview Preparation: 15
- Career Direction: 10
- Application Progress and Work Readiness: 10

If no rule-based readiness decision (`FD1`, `FD2`, or `FD3`) is produced by rules, the system creates one fallback readiness decision:

- `FD3`: 0-39
- `FD2`: 40-69
- `FD1`: 70-100

The Explanation tab marks fallback decisions as score-based fallback decisions.

Specific advice decisions such as `FD5`, `FD6`, `FD7`, `FD8`, `FD9`, and `FD10` are still produced by rule-based final rules. The UI separates readiness level from specific advice so advice is not treated as the readiness level.

This means the displayed output always has:

- one readiness level
- zero or more rule-based specific advice decisions
- recommendations and next actions

## Output

The engine returns:

- selected facts
- working memory
- inferred intermediate decisions
- rule-based final decisions
- score fallback final decisions
- recommendations
- readiness score
- score-based level
- main priority area
- triggered rules
- component scores
- explanation chain

The current UI explains the chain as:

Selected Facts -> Triggered Rules -> Intermediate Decisions -> Final Readiness Decision -> Specific Advice Decisions -> Recommendations

Because the system performs explicit rule matching and inference, it functions as an Expert System rather than a normal survey form. The score is supportive, but the rule-based forward chaining process remains the core reasoning method.
