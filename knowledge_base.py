from pathlib import Path

from inference_engine import load_json


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def load_facts():
    return load_json(DATA_DIR / "facts.json")


def load_rules():
    return load_json(DATA_DIR / "rules.json")


def load_recommendations():
    return load_json(DATA_DIR / "recommendations.json")


def load_references():
    return load_json(DATA_DIR / "references.json")


def load_career_paths():
    return load_json(DATA_DIR / "career_paths.json")


def fact_lookup(facts):
    return {fact["id"]: fact for fact in facts}


def rule_lookup(rules):
    return {rule["id"]: rule for rule in rules}
