import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from inference_engine import forward_chain, load_json


RULES = load_json(PROJECT_ROOT / "data" / "rules.json")
FACTS = {fact["id"]: fact["text"] for fact in load_json(PROJECT_ROOT / "data" / "facts.json")}


TEST_CASES = [
    {
        "name": "Case 1: Very prepared student",
        "facts": [
            "F1", "F2", "F3", "F4", "F5", "F6", "F8", "F9", "F10", "F11",
            "F12", "F13", "F14", "F22", "F23", "F24", "F25", "F26", "F27",
            "F28", "F29", "F30", "F31", "F32", "F33", "F34", "F35", "F36",
            "F37", "F38", "F39", "F40", "F41", "F42"
        ],
        "expected_level": "High Internship Readiness",
        "expected_decision": "FD1",
    },
    {
        "name": "Case 2: Medium prepared student",
        "facts": ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F9", "F11", "F12", "F21", "F22", "F25", "F28", "F29", "F30", "F32", "F33", "F37"],
        "expected_level": "Medium Internship Readiness",
        "expected_decision": "FD2",
    },
    {
        "name": "Case 3: Low prepared student",
        "facts": ["F15", "F16", "F17", "F18", "F19", "F20"],
        "expected_level": "Low Internship Readiness",
        "expected_decision": "FD3",
    },
    {
        "name": "Case 4: Strong technical but weak interview",
        "facts": ["F1", "F2", "F3", "F4", "F5", "F6", "F9", "F11", "F12", "F13", "F14", "F17", "F21", "F22", "F23", "F24", "F25", "F26", "F27", "F28", "F29", "F30", "F31", "F32", "F37", "F38", "F41", "F42"],
        "expected_level": "High Internship Readiness",
        "expected_decision": "FD7",
    },
    {
        "name": "Case 5: Good materials but unclear career direction",
        "facts": ["F1", "F2", "F3", "F4", "F5", "F6", "F8", "F11", "F12", "F13", "F18", "F21", "F22", "F23", "F24", "F25", "F26", "F27", "F28", "F29", "F30", "F32", "F33", "F34", "F35", "F41", "F42"],
        "expected_level": "Medium Internship Readiness",
        "expected_decision": "FD8",
    },
    {
        "name": "Case 6: Has resume but no project or portfolio",
        "facts": ["F1", "F2", "F5", "F6", "F9", "F12", "F14", "F16", "F21", "F22", "F29"],
        "expected_level": "Low Internship Readiness",
        "expected_decision": "FD6",
    },
    {
        "name": "Case 7: Has project but cannot explain it",
        "facts": ["F1", "F2", "F3", "F5", "F6", "F9", "F12", "F14", "F21", "F22", "F29"],
        "expected_level": "Medium Internship Readiness",
        "expected_decision": "FD9",
    },
    {
        "name": "Case 8: Has not applied to any company",
        "facts": ["F1", "F2", "F3", "F4", "F5", "F6", "F8", "F9", "F11", "F12", "F13", "F14", "F20", "F22", "F25", "F26", "F28", "F29", "F30", "F32", "F33", "F34", "F35", "F37", "F38", "F41"],
        "expected_level": "Medium Internship Readiness",
        "expected_decision": "FD10",
    },
    {
        "name": "Case 9: High score but unclear career direction",
        "facts": ["F1", "F2", "F3", "F4", "F5", "F6", "F8", "F11", "F12", "F13", "F18", "F21", "F22", "F23", "F24", "F25", "F26", "F27", "F28", "F29", "F30", "F31", "F32", "F33", "F34", "F35", "F36", "F41", "F42"],
        "expected_levels": ["Medium Internship Readiness", "High Internship Readiness"],
        "expected_decision": "FD8",
    },
    {
        "name": "Case 10: Low score but strong application materials only",
        "facts": ["F1", "F2", "F12", "F15", "F17", "F22", "F23"],
        "expected_level": "Low Internship Readiness",
        "expected_decisions_any": ["FD5", "FD7"],
    },
]


def describe_facts(fact_ids):
    return [f"{fact_id}: {FACTS.get(fact_id, fact_id)}" for fact_id in fact_ids]


def expected_score_level(score):
    if score <= 39:
        return "Low Internship Readiness"
    if score <= 69:
        return "Medium Internship Readiness"
    return "High Internship Readiness"


def run_tests():
    full_pass = 0
    partial_pass = 0

    for case in TEST_CASES:
        result = forward_chain(set(case["facts"]), RULES)
        score = result.get("readiness_score", result.get("readiness", {}).get("score", 0))
        score_based_level = result.get("score_based_level", expected_score_level(score))
        displayed_level = result.get("readiness", {}).get("level", score_based_level)
        final_ids = [decision["id"] for decision in result.get("final_decisions", [])]
        rule_based_final_ids = [decision["id"] for decision in result.get("rule_based_final_decisions", [])]
        fallback_ids = [decision["id"] for decision in result.get("score_fallback_decisions", [])]
        triggered_rule_ids = [rule["id"] for rule in result.get("triggered_rules", [])]

        score_level_check = score_based_level == expected_score_level(score)
        allowed_levels = case.get("expected_levels")
        if allowed_levels:
            level_check = displayed_level in allowed_levels
            expected_level_display = " / ".join(allowed_levels)
        else:
            level_check = displayed_level == case["expected_level"]
            expected_level_display = case["expected_level"]

        if "expected_decisions_any" in case:
            decision_check = any(decision in final_ids for decision in case["expected_decisions_any"])
            expected_decision_display = " or ".join(case["expected_decisions_any"])
        else:
            decision_check = case["expected_decision"] in final_ids
            expected_decision_display = case["expected_decision"]
        overall_pass = level_check and decision_check and score_level_check
        partial = decision_check and not overall_pass

        if overall_pass:
            full_pass += 1
        elif partial:
            partial_pass += 1

        if overall_pass:
            status = "PASS"
        elif partial:
            status = "PARTIAL PASS"
        else:
            status = "FAIL"

        print("=" * 88)
        print(case["name"])
        print("Selected facts:")
        for fact in describe_facts(case["facts"]):
            print(f"  - {fact}")
        print(f"Readiness score: {score} / 100")
        print("Score-based level:", score_based_level)
        print("Final displayed readiness level:", displayed_level)
        print("Triggered rules:", ", ".join(triggered_rule_ids) or "None")
        print("Rule-based final decisions:", ", ".join(rule_based_final_ids) or "None")
        print("Score fallback decisions:", ", ".join(fallback_ids) or "None")
        print("Final decisions:", ", ".join(final_ids) or "None")
        print("Expected readiness level:", expected_level_display)
        print("Expected decision:", expected_decision_display)
        print("Score level check:", "PASS" if score_level_check else "FAIL")
        print("Level check:", "PASS" if level_check else "FAIL")
        print("Decision check:", "PASS" if decision_check else "FAIL")
        print("Overall:", status)

    print("=" * 88)
    print(f"Full PASS: {full_pass} of {len(TEST_CASES)} test cases.")
    print(f"PARTIAL PASS: {partial_pass} of {len(TEST_CASES)} test cases.")


if __name__ == "__main__":
    run_tests()
