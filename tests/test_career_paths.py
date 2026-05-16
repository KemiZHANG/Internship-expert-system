import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from inference_engine import forward_chain, load_json, recommend_career_paths
from knowledge_base import load_career_paths


RULES = load_json(PROJECT_ROOT / "data" / "rules.json")


def assert_contains_role(result, expected_title):
    titles = []
    for track in result["recommended_tracks"]:
        titles.extend(track["recommended_titles"])
    assert expected_title in titles, f"Expected role title not found: {expected_title}. Found: {titles}"


def test_high_ready_computer_science_recommends_software_engineering_roles():
    facts = {
        "F1", "F2", "F3", "F4", "F5", "F6", "F8", "F9", "F10", "F11",
        "F12", "F13", "F14", "F22", "F23", "F24", "F25", "F26", "F27",
        "F28", "F29", "F30", "F31", "F32", "F33", "F34", "F35", "F36",
        "F37", "F38", "F39", "F40", "F41", "F42"
    }
    inference_result = forward_chain(facts, RULES)
    career_paths = load_career_paths()

    result = recommend_career_paths("computer_science", inference_result, career_paths)

    assert result["major_id"] == "computer_science"
    assert result["readiness_level"] == "High Internship Readiness"
    assert_contains_role(result, "Software Engineering Intern")
    assert result["platforms"], "Expected job platform recommendations"


def test_medium_ready_data_science_recommends_data_analyst_roles():
    facts = {
        "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F9", "F11", "F12",
        "F21", "F22", "F25", "F28", "F29", "F30", "F32", "F33", "F37"
    }
    inference_result = forward_chain(facts, RULES)
    career_paths = load_career_paths()

    result = recommend_career_paths("data_science_ai", inference_result, career_paths)

    assert result["readiness_level"] == "Medium Internship Readiness"
    assert_contains_role(result, "Data Analyst Intern")
    assert "F30" in result["matching_facts"]


def test_low_ready_major_recommendations_stay_preparatory():
    facts = {"F15", "F16", "F17", "F18", "F19", "F20"}
    inference_result = forward_chain(facts, RULES)
    career_paths = load_career_paths()

    result = recommend_career_paths("information_systems", inference_result, career_paths)

    assert result["readiness_level"] == "Low Internship Readiness"
    assert_contains_role(result, "IT Support Intern")
    assert "Software Engineering Intern" not in [
        title
        for track in result["recommended_tracks"]
        for title in track["recommended_titles"]
    ]


def test_high_ready_accounting_finance_recommends_finance_roles():
    facts = {
        "F1", "F2", "F9", "F10", "F11", "F12", "F14", "F22", "F23",
        "F3", "F4", "F5", "F6", "F7", "F8", "F13", "F25", "F28",
        "F29", "F30", "F31", "F32", "F33", "F34", "F35", "F36",
        "F37", "F38", "F39", "F40", "F41", "F42"
    }
    inference_result = forward_chain(facts, RULES)
    career_paths = load_career_paths()

    result = recommend_career_paths("accounting_finance", inference_result, career_paths)

    assert result["major_id"] == "accounting_finance"
    assert_contains_role(result, "Financial Analyst Intern")


def test_medium_ready_marketing_communication_recommends_marketing_roles():
    facts = {
        "F1", "F2", "F3", "F9", "F11", "F12", "F14", "F21", "F22",
        "F4", "F5", "F7", "F8", "F25", "F28", "F29", "F32", "F34",
        "F35", "F37", "F41", "F42"
    }
    inference_result = forward_chain(facts, RULES)
    career_paths = load_career_paths()

    result = recommend_career_paths("marketing_communication", inference_result, career_paths)

    assert result["major_id"] == "marketing_communication"
    assert_contains_role(result, "Digital Marketing Intern")


def test_low_ready_psychology_social_science_recommends_support_roles():
    facts = {"F19", "F17", "F18", "F20", "F41"}
    inference_result = forward_chain(facts, RULES)
    career_paths = load_career_paths()

    result = recommend_career_paths("psychology_social_science", inference_result, career_paths)

    assert result["major_id"] == "psychology_social_science"
    assert_contains_role(result, "Community Service Assistant Intern")


def test_high_ready_engineering_recommends_engineering_roles():
    facts = {
        "F1", "F2", "F3", "F9", "F10", "F11", "F12", "F13", "F14",
        "F22", "F23", "F24", "F25", "F26", "F27", "F32", "F33",
        "F34", "F35", "F36", "F37", "F38", "F39", "F40", "F41", "F42"
    }
    inference_result = forward_chain(facts, RULES)
    career_paths = load_career_paths()

    result = recommend_career_paths("engineering_general", inference_result, career_paths)

    assert result["major_id"] == "engineering_general"
    assert_contains_role(result, "Engineering Intern")


def run_tests():
    tests = [
        test_high_ready_computer_science_recommends_software_engineering_roles,
        test_medium_ready_data_science_recommends_data_analyst_roles,
        test_low_ready_major_recommendations_stay_preparatory,
        test_high_ready_accounting_finance_recommends_finance_roles,
        test_medium_ready_marketing_communication_recommends_marketing_roles,
        test_low_ready_psychology_social_science_recommends_support_roles,
        test_high_ready_engineering_recommends_engineering_roles,
    ]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
            passed += 1
        except AssertionError as error:
            print(f"FAIL: {test.__name__}")
            print(f"  {error}")
    print(f"Career path tests passed: {passed} of {len(tests)}")
    if passed != len(tests):
        raise SystemExit(1)


if __name__ == "__main__":
    run_tests()
