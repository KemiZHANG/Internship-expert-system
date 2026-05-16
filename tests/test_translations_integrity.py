import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


TRANSLATIONS = json.loads((PROJECT_ROOT / "data" / "translations.json").read_text(encoding="utf-8"))
CAREER_PATHS = json.loads((PROJECT_ROOT / "data" / "career_paths.json").read_text(encoding="utf-8"))

SUSPICIOUS_TOKENS = ["??", "\ufffd", "涓", "鈫", "鍩", "瀹", "绯", "鐭", "锛", "銆"]


def walk_strings(value, path=""):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk_strings(item, f"{path}.{key}" if path else str(key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk_strings(item, f"{path}[{index}]")
    elif isinstance(value, str):
        yield path, value


def test_no_mojibake_tokens_in_translation_and_career_knowledge():
    checked = {
        "translations": TRANSLATIONS,
        "career_paths": CAREER_PATHS,
    }
    failures = []
    for name, data in checked.items():
        for path, value in walk_strings(data):
            for token in SUSPICIOUS_TOKENS:
                if token in value:
                    failures.append(f"{name}:{path} contains {token!r}: {value!r}")
    assert not failures, "\n".join(failures)


def test_all_major_options_have_three_language_labels():
    missing = []
    for major_id in CAREER_PATHS["majors"]:
        key = f"option.major.{major_id}"
        for lang in ("en", "zh", "ms"):
            if not TRANSLATIONS.get(lang, {}).get(key):
                missing.append(f"{lang}.{key}")
    assert not missing, "Missing translation keys: " + ", ".join(missing)


def run_tests():
    tests = [
        test_no_mojibake_tokens_in_translation_and_career_knowledge,
        test_all_major_options_have_three_language_labels,
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
    print(f"Translation integrity tests passed: {passed} of {len(tests)}")
    if passed != len(tests):
        raise SystemExit(1)


if __name__ == "__main__":
    run_tests()
