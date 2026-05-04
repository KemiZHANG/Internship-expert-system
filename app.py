from pathlib import Path

import streamlit as st

from inference_engine import forward_chain, load_json, readable_conditions
from knowledge_base import load_facts, load_recommendations, load_references, load_rules


BASE_DIR = Path(__file__).resolve().parent
ACADEMIC_NOTE = (
    "This initial prototype uses general internship preparation knowledge and public "
    "reference ideas to create a starting knowledge base. The rules and recommendations "
    "should be refined and validated through consultation with a real Human Expert."
)

LANGUAGE_OPTIONS = {
    "English": "en",
    "中文": "zh",
    "Bahasa Melayu": "ms",
}

LEGACY_DEMO_CASES = {
    "Custom assessment": "custom",
    "Very prepared student": "very_prepared",
    "Medium prepared student": "medium_prepared",
    "Low prepared student": "low_prepared",
    "Strong technical but weak interview": "strong_technical_weak_interview",
    "Good materials but unclear career direction": "good_materials_unclear_direction",
}

LEGACY_FIELD_VALUES = {
    "resume_status": {
        "No resume": "no_resume",
        "Resume completed but not tailored": "resume_not_tailored",
        "Resume completed and tailored": "resume_tailored",
    },
    "project_status": {
        "No related project": "no_project",
        "Has related project only": "one_project",
        "Has related project and GitHub / portfolio": "github_readme",
    },
    "technical_foundation": {
        "Weak": "weak",
        "Basic": "basic",
        "Good": "good",
    },
    "interview_preparation": {
        "Not prepared": "none",
        "Practiced basic interview questions": "basic",
        "Practiced interview and can explain projects clearly": "mock_ready",
    },
    "career_direction": {
        "Unclear": "unclear",
        "Has a general direction": "general",
        "Knows target internship role clearly and researched job requirements": "matched",
    },
    "application_progress": {
        "Has not applied yet": "none",
        "Applied to fewer than 5 companies": "lt5",
        "Applied to at least 5 companies": "gte5",
    },
}


ASSESSMENT_DEFAULTS = {
    "resume_status": "resume_not_tailored",
    "project_status": "one_project",
    "technical_foundation": "basic",
    "interview_preparation": "basic",
    "career_direction": "general",
    "application_progress": "lt5",
    "professional_profile": False,
    "cover_letter": False,
    "academic_documents": False,
    "experience": True,
    "communication_skill": False,
    "teamwork_time": False,
}


DEMO_CASES = {
    "custom": ASSESSMENT_DEFAULTS,
    "very_prepared": {
        "resume_status": "resume_tailored",
        "project_status": "strong_portfolio",
        "technical_foundation": "strong",
        "interview_preparation": "mock_ready",
        "career_direction": "matched",
        "application_progress": "tracked",
        "professional_profile": True,
        "cover_letter": True,
        "academic_documents": True,
        "experience": True,
        "communication_skill": True,
        "teamwork_time": True,
    },
    "medium_prepared": {
        "resume_status": "resume_tailored",
        "project_status": "github_readme",
        "technical_foundation": "good",
        "interview_preparation": "technical",
        "career_direction": "researched",
        "application_progress": "lt5",
        "professional_profile": True,
        "cover_letter": True,
        "academic_documents": False,
        "experience": True,
        "communication_skill": True,
        "teamwork_time": False,
    },
    "low_prepared": {
        "resume_status": "no_resume",
        "project_status": "no_project",
        "technical_foundation": "weak",
        "interview_preparation": "none",
        "career_direction": "unclear",
        "application_progress": "none",
        "professional_profile": False,
        "cover_letter": False,
        "academic_documents": False,
        "experience": False,
        "communication_skill": False,
        "teamwork_time": False,
    },
    "strong_technical_weak_interview": {
        "resume_status": "resume_tailored",
        "project_status": "strong_portfolio",
        "technical_foundation": "strong",
        "interview_preparation": "none",
        "career_direction": "matched",
        "application_progress": "lt5",
        "professional_profile": True,
        "cover_letter": True,
        "academic_documents": True,
        "experience": True,
        "communication_skill": True,
        "teamwork_time": True,
    },
    "good_materials_unclear_direction": {
        "resume_status": "resume_tailored",
        "project_status": "strong_portfolio",
        "technical_foundation": "good",
        "interview_preparation": "technical_behavioral",
        "career_direction": "unclear",
        "application_progress": "lt5",
        "professional_profile": True,
        "cover_letter": True,
        "academic_documents": True,
        "experience": True,
        "communication_skill": True,
        "teamwork_time": True,
    },
}


FIELD_OPTIONS = {
    "resume_status": ["no_resume", "resume_not_tailored", "resume_tailored"],
    "project_status": ["no_project", "one_project", "github_readme", "strong_portfolio"],
    "technical_foundation": ["weak", "basic", "good", "strong"],
    "interview_preparation": ["none", "basic", "technical", "technical_behavioral", "mock_ready"],
    "career_direction": ["unclear", "general", "researched", "matched"],
    "application_progress": ["none", "lt5", "gte5", "tracked"],
}

READINESS_DECISION_IDS = {"FD1", "FD2", "FD3"}
RULE_TYPE_OPTIONS = ["all", "intermediate", "final", "recommendation"]
OBJECT_TYPE_OPTIONS = ["all", "facts", "rules", "recommendations"]


def load_translations():
    return load_json(BASE_DIR / "data" / "translations.json")


def t(translations, lang, key, default=None):
    value = translations.get(lang, {}).get(key)
    if value is None:
        value = translations.get("en", {}).get(key)
    if value is None:
        value = default if default is not None else key
    return value


def localized_fact_text(fact, lang):
    return fact.get("display_text", {}).get(lang) or fact.get("display_text", {}).get("en") or fact["text"]


def localized_recommendation(item, lang, field):
    if lang == "en":
        return item.get(field)
    return item.get("display", {}).get(lang, {}).get(field) or item.get(field)


def option_label(translations, lang, field, option_id):
    return t(translations, lang, f"option.{field}.{option_id}", t(translations, lang, f"option.{option_id}", option_id))


def demo_label(translations, lang, demo_id):
    return t(translations, lang, f"demo.{demo_id}", demo_id)


def apply_demo_case():
    selected_case = normalize_demo_case(st.session_state.get("demo_case", "custom"))
    for field, value in DEMO_CASES[selected_case].items():
        st.session_state[field] = value


def normalize_demo_case(value):
    return LEGACY_DEMO_CASES.get(value, value if value in DEMO_CASES else "custom")


def normalize_field_value(field, value):
    value = LEGACY_FIELD_VALUES.get(field, {}).get(value, value)
    return value if value in FIELD_OPTIONS[field] else ASSESSMENT_DEFAULTS[field]


def initialize_assessment_state():
    st.session_state.setdefault("language", "English")
    st.session_state.setdefault("demo_case", "custom")
    if st.session_state.language not in LANGUAGE_OPTIONS:
        st.session_state.language = "English"
    st.session_state.demo_case = normalize_demo_case(st.session_state.demo_case)
    st.session_state.setdefault("analysis_requested", False)
    for field, value in ASSESSMENT_DEFAULTS.items():
        st.session_state.setdefault(field, value)
        if field in FIELD_OPTIONS:
            st.session_state[field] = normalize_field_value(field, st.session_state[field])


def assessment_to_facts(assessment):
    facts = set()

    if assessment["resume_status"] == "no_resume":
        facts.add("F19")
    elif assessment["resume_status"] == "resume_not_tailored":
        facts.add("F1")
    elif assessment["resume_status"] == "resume_tailored":
        facts.update(["F1", "F2"])

    if assessment["project_status"] == "no_project":
        facts.add("F16")
    elif assessment["project_status"] == "one_project":
        facts.add("F3")
    elif assessment["project_status"] == "github_readme":
        facts.update(["F3", "F4", "F25", "F28"])
    elif assessment["project_status"] == "strong_portfolio":
        facts.update(["F3", "F4", "F13", "F24", "F25", "F26", "F27", "F28"])

    if assessment["technical_foundation"] == "weak":
        facts.add("F15")
    elif assessment["technical_foundation"] == "basic":
        facts.update(["F5", "F29"])
    elif assessment["technical_foundation"] == "good":
        facts.update(["F5", "F6", "F29", "F30", "F32"])
    elif assessment["technical_foundation"] == "strong":
        facts.update(["F5", "F6", "F29", "F30", "F31", "F32"])

    if assessment["interview_preparation"] == "none":
        facts.add("F17")
    elif assessment["interview_preparation"] == "basic":
        facts.add("F7")
    elif assessment["interview_preparation"] == "technical":
        facts.update(["F7", "F33", "F8"])
    elif assessment["interview_preparation"] == "technical_behavioral":
        facts.update(["F7", "F8", "F33", "F34", "F35"])
    elif assessment["interview_preparation"] == "mock_ready":
        facts.update(["F7", "F8", "F13", "F33", "F34", "F35", "F36"])

    if assessment["career_direction"] == "unclear":
        facts.add("F18")
    elif assessment["career_direction"] == "general":
        facts.add("F9")
    elif assessment["career_direction"] == "researched":
        facts.update(["F9", "F14", "F37"])
    elif assessment["career_direction"] == "matched":
        facts.update(["F9", "F14", "F37", "F38"])

    if assessment["application_progress"] == "none":
        facts.add("F20")
    elif assessment["application_progress"] == "lt5":
        facts.add("F21")
    elif assessment["application_progress"] == "gte5":
        facts.add("F10")
    elif assessment["application_progress"] == "tracked":
        facts.update(["F10", "F39", "F40"])

    optional_fact_map = {
        "professional_profile": "F12",
        "cover_letter": "F22",
        "academic_documents": "F23",
        "experience": "F11",
        "communication_skill": "F41",
        "teamwork_time": "F42",
    }
    for field, fact_id in optional_fact_map.items():
        if assessment[field]:
            facts.add(fact_id)

    return facts


def build_triggered_rules_table(triggered_rules):
    return [
        {
            "Rule ID": rule["id"],
            "Rule Name": rule["name"],
            "Type": rule["type"],
            "Conditions": readable_conditions(rule.get("conditions", {})),
            "Conclusion": f"{rule['conclusion']} - {rule['conclusion_text']}",
            "Explanation": rule["explanation"],
        }
        for rule in triggered_rules
    ]


def split_final_decisions(result):
    final_decisions = result.get("final_decisions", [])
    readiness_decisions = [
        decision for decision in final_decisions if decision.get("id") in READINESS_DECISION_IDS
    ]
    advice_decisions = [
        decision for decision in final_decisions if decision.get("id") not in READINESS_DECISION_IDS
    ]
    return readiness_decisions, advice_decisions


def recommendation_category(decision_id):
    category_map = {
        "FD1": "Application Progress and Work Readiness",
        "FD2": "Application Progress and Work Readiness",
        "FD3": "Technical Skills",
        "FD4": "Application Progress and Work Readiness",
        "FD5": "Technical Skills",
        "FD6": "Application Materials",
        "FD7": "Interview Preparation",
        "FD8": "Career Direction",
        "FD9": "Project and Portfolio",
        "FD10": "Application Progress and Work Readiness",
    }
    return category_map.get(decision_id, "Application Materials")


def rule_categories(rule, fact_by_id):
    categories = set()
    for group in ("all", "any", "not"):
        for item in rule.get("conditions", {}).get(group, []):
            if item.startswith("F") and item in fact_by_id:
                categories.add(fact_by_id[item]["category"])
    conclusion = rule.get("conclusion", "")
    if conclusion == "FD5":
        categories.add("Technical Skills")
    elif conclusion == "FD6":
        categories.add("Application Materials")
    elif conclusion == "FD7":
        categories.add("Interview Preparation")
    elif conclusion == "FD8":
        categories.add("Career Direction")
    elif conclusion == "FD9":
        categories.add("Project and Portfolio")
    elif conclusion == "FD10":
        categories.add("Application Progress")
    return sorted(categories)


def architecture_flow_markdown(translations, lang):
    return (
        f"{t(translations, lang, 'arch.ui')}\n"
        f"↓\n"
        f"{t(translations, lang, 'arch.inputs')}\n"
        f"↓\n"
        f"{t(translations, lang, 'arch.kb')}\n"
        f"↓\n"
        f"{t(translations, lang, 'arch.ie')}\n"
        f"↓\n"
        f"{t(translations, lang, 'arch.intermediate')}\n"
        f"↓\n"
        f"{t(translations, lang, 'arch.final')}"
    )


def level_short(level):
    if level.startswith("High"):
        return "High"
    if level.startswith("Medium"):
        return "Medium"
    if level.startswith("Low"):
        return "Low"
    return level


def render_card(label, value):
    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-label">{label}</div>
            <div class="summary-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_summary_cards(result, translations, lang):
    readiness = result.get("readiness", {})
    level = readiness.get("level", result.get("score_based_level", "Medium Internship Readiness"))
    score = readiness.get("score", result.get("readiness_score", 0))
    priority = readiness.get("main_priority_area", result.get("main_priority_area", "Application Materials"))
    advice = readiness.get("main_advice", "Keep applying while improving the lowest-scoring preparation area.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_card(t(translations, lang, "results.level"), t(translations, lang, f"level.{level_short(level).lower()}"))
    with col2:
        render_card(t(translations, lang, "results.score"), f"{score} / 100")
    with col3:
        render_card(t(translations, lang, "results.priority"), t(translations, lang, f"area.{priority}", priority))
    with col4:
        render_card(t(translations, lang, "results.advice"), t(translations, lang, f"advice.{advice}", advice))

    st.subheader(t(translations, lang, f"readiness.{level}", level))


def render_component_scores(result, translations, lang):
    rows = []
    for area, detail in result.get("readiness", {}).get("component_scores", {}).items():
        rows.append(
            {
                t(translations, lang, "table.area"): t(translations, lang, f"area.{area}", area),
                t(translations, lang, "table.score"): detail["score"],
                t(translations, lang, "table.maximum"): detail["max"],
                t(translations, lang, "table.percent"): f"{round((detail['score'] / detail['max']) * 100)}%",
            }
        )
    st.dataframe(rows, use_container_width=True, hide_index=True)


def render_readiness_decisions(result, translations, lang):
    readiness_decisions, _ = split_final_decisions(result)
    for decision in readiness_decisions:
        source = t(translations, lang, f"source.{decision.get('source', 'rule_based')}")
        text = t(translations, lang, f"decision.{decision['id']}", decision["text"])
        st.write(f"- **{decision['id']} - {text}** ({source}): {decision['explanation']}")


def render_advice_decisions(result, translations, lang):
    _, advice_decisions = split_final_decisions(result)
    if not advice_decisions:
        st.write(t(translations, lang, "results.no_advice"))
        return

    for decision in advice_decisions:
        source = t(translations, lang, f"source.{decision.get('source', 'rule_based')}")
        text = t(translations, lang, f"decision.{decision['id']}", decision["text"])
        st.write(f"- **{decision['id']} - {text}** ({source}, {decision.get('rule_id', 'N/A')}): {decision['explanation']}")


def render_recommendations(result, recommendations, translations, lang):
    shown = set()
    for final_decision in result.get("final_decisions", []):
        rec = recommendations.get(final_decision["id"])
        if not rec or final_decision["id"] in shown:
            continue
        shown.add(final_decision["id"])
        st.markdown(f"**{localized_recommendation(rec, lang, 'title')}**")
        st.write(localized_recommendation(rec, lang, "summary"))
        st.write(localized_recommendation(rec, lang, "recommendation"))
        st.write(f"{t(translations, lang, 'results.priority')}: {localized_recommendation(rec, lang, 'priority')}")
        for step in localized_recommendation(rec, lang, "next_steps"):
            st.write(f"- {step}")

    extra_recs = [rule for rule in result.get("triggered_rules", []) if rule.get("type") == "recommendation"]
    if extra_recs:
        st.markdown(f"**{t(translations, lang, 'results.additional_recommendations')}**")
        for rule in extra_recs:
            st.write(f"- {rule['conclusion_text']}: {rule['explanation']}")


def render_explanation(result, fact_by_id, recommendations, translations, lang):
    st.subheader(t(translations, lang, "explain.selected_facts"))
    for fact_id in result.get("selected_facts", []):
        fact = fact_by_id.get(fact_id, {"text": fact_id})
        st.write(f"- {fact_id}: {localized_fact_text(fact, lang)}")

    st.markdown("### ↓")
    st.subheader(t(translations, lang, "explain.triggered_rules"))
    st.dataframe(build_triggered_rules_table(result.get("triggered_rules", [])), use_container_width=True, hide_index=True)

    st.markdown("### ↓")
    st.subheader(t(translations, lang, "explain.intermediate_decisions"))
    if result.get("inferred_decisions", []):
        for decision_id in result.get("inferred_decisions", []):
            rule = next((r for r in result.get("triggered_rules", []) if r["conclusion"] == decision_id), None)
            st.write(
                f"- `{t(translations, lang, 'label.rule_based_intermediate')}`: "
                f"{decision_id} - {rule['conclusion_text'] if rule else decision_id}"
            )
    else:
        st.write(t(translations, lang, "explain.no_intermediate"))

    st.markdown("### ↓")
    st.subheader(t(translations, lang, "explain.final_readiness_decision"))
    readiness = result.get("readiness", {})
    st.write(f"{t(translations, lang, 'explain.combined_level')}: **{readiness.get('level', result.get('score_based_level', ''))}**")
    st.write(f"{t(translations, lang, 'explain.score_level')}: **{readiness.get('score_level', result.get('score_based_level', ''))}**")
    for decision in result.get("final_decisions", []):
        if decision.get("id") in READINESS_DECISION_IDS:
            source = t(translations, lang, f"source.{decision.get('source', 'rule_based')}")
            text = t(translations, lang, f"decision.{decision['id']}", decision["text"])
            label = (
                t(translations, lang, "label.score_based_fallback")
                if decision.get("source") == "score_fallback"
                else t(translations, lang, "label.rule_based_final")
            )
            st.write(f"- `{label}`: **{decision['id']} - {text}** ({source}): {decision['explanation']}")
    if result.get("score_fallback_decisions", []):
        st.warning(t(translations, lang, "explain.fallback_note"))

    st.markdown("### ↓")
    st.subheader(t(translations, lang, "explain.specific_advice"))
    for decision in result.get("final_decisions", []):
        if decision.get("id") not in READINESS_DECISION_IDS:
            text = t(translations, lang, f"decision.{decision['id']}", decision["text"])
            st.write(
                f"- `{t(translations, lang, 'label.rule_based_advice')}`: "
                f"**{decision['id']} - {text}** (Rule ID: {decision.get('rule_id', 'N/A')}): "
                f"{decision['explanation']}"
            )

    st.markdown("### ↓")
    st.subheader(t(translations, lang, "explain.recommendations"))
    render_recommendations(result, recommendations, translations, lang)

    with st.expander(t(translations, lang, "explain.detailed_chain"), expanded=False):
        explanation_chain = result.get("explanation_chain", {"start": "", "steps": [], "end": ""})
        st.write(explanation_chain.get("start", ""))
        for step_number, step in enumerate(explanation_chain.get("steps", []), start=1):
            st.markdown(f"**Step {step_number}: {step['rule_id']} - {step['rule_name']}**")
            st.write(f"Conditions: {readable_conditions(step['conditions'])}")
            st.write(f"Conclusion added: {step['conclusion']} - {step['conclusion_text']}")
            st.write(step["explanation"])
        st.write(explanation_chain.get("end", ""))

def render_kb_viewer(facts, rules, recommendations, references, translations, lang, fact_by_id):
    st.markdown(f"**{t(translations, lang, 'kb.filters')}**")
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    with filter_col1:
        object_filter = st.selectbox(
            t(translations, lang, "kb.filter_object_type"),
            OBJECT_TYPE_OPTIONS,
            format_func=lambda item: t(translations, lang, f"kb.object_type.{item}", item.title()),
            key="kb_object_filter",
        )
    with filter_col2:
        category_options = ["all"] + sorted({fact["category"] for fact in facts})
        category_filter = st.selectbox(
            t(translations, lang, "kb.filter_category"),
            category_options,
            format_func=lambda item: t(translations, lang, f"area.{item}", t(translations, lang, "kb.all_categories") if item == "all" else item),
            key="kb_category_filter",
        )
    with filter_col3:
        rule_type_filter = st.selectbox(
            t(translations, lang, "kb.filter_rule_type"),
            RULE_TYPE_OPTIONS,
            format_func=lambda item: t(translations, lang, f"kb.rule_type.{item}", item.title()),
            key="kb_rule_type_filter",
        )

    st.markdown(f"**{t(translations, lang, 'kb.architecture')}**")
    st.code(architecture_flow_markdown(translations, lang), language="text")

    filtered_facts = [
        fact for fact in facts
        if category_filter == "all" or fact["category"] == category_filter
    ]
    filtered_rules = []
    for rule in rules:
        if rule_type_filter != "all" and rule["type"] != rule_type_filter:
            continue
        if category_filter != "all":
            categories = rule_categories(rule, fact_by_id)
            if category_filter not in categories:
                continue
        filtered_rules.append(rule)

    filtered_recommendations = {
        decision_id: item
        for decision_id, item in recommendations.items()
        if category_filter == "all" or recommendation_category(decision_id) == category_filter
    }

    if object_filter in {"all", "facts"}:
        with st.expander(t(translations, lang, "kb.view_facts"), expanded=True):
            fact_rows = [
                {
                    "ID": fact["id"],
                    t(translations, lang, "table.category"): t(translations, lang, f"area.{fact['category']}", fact["category"]),
                    t(translations, lang, "table.text"): localized_fact_text(fact, lang),
                }
                for fact in filtered_facts
            ]
            st.dataframe(fact_rows, use_container_width=True, hide_index=True)

    if object_filter in {"all", "rules"}:
        with st.expander(t(translations, lang, "kb.view_rules"), expanded=False):
            rule_rows = [
                {
                    "Rule ID": rule["id"],
                    "Name": rule["name"],
                    "Type": rule["type"],
                    "Categories": ", ".join(rule_categories(rule, fact_by_id)) or "-",
                    "Conditions": readable_conditions(rule.get("conditions", {})),
                    "Conclusion": rule["conclusion"],
                    "Conclusion Text": rule["conclusion_text"],
                    "Explanation": rule["explanation"],
                }
                for rule in filtered_rules
            ]
            st.dataframe(rule_rows, use_container_width=True, hide_index=True)

    if object_filter in {"all", "recommendations"}:
        with st.expander(t(translations, lang, "kb.view_recommendations"), expanded=False):
            recommendation_rows = [
                {
                    "Decision ID": decision_id,
                    "Category": t(translations, lang, f"area.{recommendation_category(decision_id)}", recommendation_category(decision_id)),
                    "Title": localized_recommendation(item, lang, "title"),
                    "Priority": localized_recommendation(item, lang, "priority"),
                    "Recommendation": localized_recommendation(item, lang, "recommendation"),
                    "Next Steps": "; ".join(localized_recommendation(item, lang, "next_steps")),
                }
                for decision_id, item in filtered_recommendations.items()
            ]
            st.dataframe(recommendation_rows, use_container_width=True, hide_index=True)

    with st.expander(t(translations, lang, "kb.source_note"), expanded=False):
        st.info(ACADEMIC_NOTE)
        for ref in references:
            st.write(f"- [{ref['title']}]({ref['url']})")


def main():
    st.set_page_config(page_title="Internship Preparation Advisory Expert System", layout="wide")
    initialize_assessment_state()

    facts = load_facts()
    rules = load_rules()
    recommendations = load_recommendations()
    references = load_references()
    translations = load_translations()
    fact_by_id = {fact["id"]: fact for fact in facts}

    st.markdown(
        """
        <style>
        .summary-card {
            border: 1px solid #d9dee7;
            border-radius: 8px;
            padding: 12px 14px;
            min-height: 112px;
            background: #ffffff;
        }
        .summary-label {
            font-size: 0.82rem;
            color: #536171;
            margin-bottom: 8px;
        }
        .summary-value {
            font-size: 1.2rem;
            font-weight: 700;
            line-height: 1.25;
            color: #142033;
            overflow-wrap: anywhere;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.selectbox(
            "Language / 语言 / Bahasa",
            list(LANGUAGE_OPTIONS.keys()),
            key="language",
        )
        lang = LANGUAGE_OPTIONS[st.session_state.language]
        st.header(t(translations, lang, "sidebar.project"))
        st.write("Internship Preparation Advisory Expert System")
        st.write("WID2001 Knowledge Representation and Reasoning")
        st.markdown(f"**{t(translations, lang, 'sidebar.components')}**")
        st.write("- KB: JSON facts, rules, recommendations")
        st.write("- IE: forward chaining + readiness score")
        st.write("- UI: Streamlit")
        st.markdown(f"**{t(translations, lang, 'sidebar.run_mode')}**")
        st.write(t(translations, lang, "sidebar.local"))

    st.title(t(translations, lang, "app.title"))
    st.caption(t(translations, lang, "app.subtitle"))

    assessment_tab, results_tab, explanation_tab, kb_tab, testing_tab = st.tabs(
        [
            t(translations, lang, "tab.assessment"),
            t(translations, lang, "tab.results"),
            t(translations, lang, "tab.explanation"),
            t(translations, lang, "tab.kb"),
            t(translations, lang, "tab.testing"),
        ]
    )

    with assessment_tab:
        st.header(t(translations, lang, "tab.assessment"))
        st.selectbox(
            t(translations, lang, "assessment.demo_case"),
            list(DEMO_CASES.keys()),
            key="demo_case",
            format_func=lambda item: demo_label(translations, lang, item),
            on_change=apply_demo_case,
        )

        col1, col2 = st.columns(2)
        with col1:
            resume_status = st.radio(
                t(translations, lang, "assessment.resume_status"),
                FIELD_OPTIONS["resume_status"],
                key="resume_status",
                format_func=lambda item: option_label(translations, lang, "resume_status", item),
            )
            project_status = st.radio(
                t(translations, lang, "assessment.project_status"),
                FIELD_OPTIONS["project_status"],
                key="project_status",
                format_func=lambda item: option_label(translations, lang, "project_status", item),
            )
            technical_foundation = st.radio(
                t(translations, lang, "assessment.technical_foundation"),
                FIELD_OPTIONS["technical_foundation"],
                key="technical_foundation",
                format_func=lambda item: option_label(translations, lang, "technical_foundation", item),
            )
            professional_profile = st.checkbox(t(translations, lang, "assessment.professional_profile"), key="professional_profile")
            cover_letter = st.checkbox(t(translations, lang, "assessment.cover_letter"), key="cover_letter")
            academic_documents = st.checkbox(t(translations, lang, "assessment.academic_documents"), key="academic_documents")

        with col2:
            interview_preparation = st.radio(
                t(translations, lang, "assessment.interview_preparation"),
                FIELD_OPTIONS["interview_preparation"],
                key="interview_preparation",
                format_func=lambda item: option_label(translations, lang, "interview_preparation", item),
            )
            career_direction = st.radio(
                t(translations, lang, "assessment.career_direction"),
                FIELD_OPTIONS["career_direction"],
                key="career_direction",
                format_func=lambda item: option_label(translations, lang, "career_direction", item),
            )
            application_progress = st.radio(
                t(translations, lang, "assessment.application_progress"),
                FIELD_OPTIONS["application_progress"],
                key="application_progress",
                format_func=lambda item: option_label(translations, lang, "application_progress", item),
            )
            experience = st.checkbox(t(translations, lang, "assessment.experience"), key="experience")
            communication_skill = st.checkbox(t(translations, lang, "assessment.communication_skill"), key="communication_skill")
            teamwork_time = st.checkbox(t(translations, lang, "assessment.teamwork_time"), key="teamwork_time")

        if st.button(t(translations, lang, "assessment.analyze"), type="primary"):
            st.session_state.analysis_requested = True
        st.success(t(translations, lang, "assessment.mapping_note"))

    assessment = {
        "resume_status": resume_status,
        "project_status": project_status,
        "technical_foundation": technical_foundation,
        "interview_preparation": interview_preparation,
        "career_direction": career_direction,
        "application_progress": application_progress,
        "professional_profile": professional_profile,
        "cover_letter": cover_letter,
        "academic_documents": academic_documents,
        "experience": experience,
        "communication_skill": communication_skill,
        "teamwork_time": teamwork_time,
    }
    selected_facts = assessment_to_facts(assessment)
    result = forward_chain(selected_facts, rules)

    with results_tab:
        st.header(t(translations, lang, "tab.results"))
        st.subheader(t(translations, lang, "results.overall_readiness"))
        render_summary_cards(result, translations, lang)
        st.caption(t(translations, lang, "results.overall_note"))
        st.subheader(t(translations, lang, "results.component_scores"))
        render_component_scores(result, translations, lang)
        st.subheader(t(translations, lang, "results.rule_based_specific_advice"))
        render_advice_decisions(result, translations, lang)
        st.subheader(t(translations, lang, "results.recommendations"))
        render_recommendations(result, recommendations, translations, lang)
        with st.expander(t(translations, lang, "results.view_readiness_details"), expanded=False):
            render_readiness_decisions(result, translations, lang)

    with explanation_tab:
        st.header(t(translations, lang, "tab.explanation"))
        render_explanation(result, fact_by_id, recommendations, translations, lang)

    with kb_tab:
        st.header(t(translations, lang, "tab.kb"))
        render_kb_viewer(facts, rules, recommendations, references, translations, lang, fact_by_id)

    with testing_tab:
        st.header(t(translations, lang, "tab.testing"))
        st.write(t(translations, lang, "testing.run_text"))
        st.code("python tests/test_cases.py", language="bash")
        st.subheader(t(translations, lang, "testing.why_expert_system"))
        for key in (
            "testing.expert_point_1",
            "testing.expert_point_2",
            "testing.expert_point_3",
            "testing.expert_point_4",
            "testing.expert_point_5",
        ):
            st.write(f"- {t(translations, lang, key)}")
        st.subheader(t(translations, lang, "testing.architecture"))
        st.code(architecture_flow_markdown(translations, lang), language="text")
        st.write(t(translations, lang, "testing.demo_text"))
        st.write("- Very prepared student -> High readiness")
        st.write("- Medium prepared student -> Medium readiness")
        st.write("- Low prepared student -> Low readiness")
        st.write("- Strong technical but weak interview -> Need interview preparation")
        st.write("- Good materials but unclear career direction -> Clarify target role")


if __name__ == "__main__":
    main()
