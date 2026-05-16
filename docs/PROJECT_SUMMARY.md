# Project Summary

## Introduction

The Internship Preparation Advisory Expert System is a local rule-based prototype for WID2001 Knowledge Representation and Reasoning. It helps university students evaluate internship preparation and identify the next priority area.

## Objectives

- Represent internship preparation knowledge as facts and IF-THEN rules
- Use forward chaining to infer intermediate and final decisions
- Provide explanation of selected facts, triggered rules, decisions, and recommendations
- Recommend suitable internship role titles and job search platforms based on selected major and inferred readiness
- Add score-based fallback so the system always produces a final readiness decision
- Support English, Chinese, and Bahasa Melayu UI text
- Provide demo cases and automated tests for presentation

## Domain

The domain is internship preparation for university students. The original prototype focused mainly on software, AI, data, and CS-related internships; the optimized career-path knowledge base now also includes broader university study areas such as business, accounting, finance, HR, marketing, law, psychology, education, media, design, engineering, health science, environmental science, hospitality, logistics, agriculture, language, and sports science.

The optimized prototype also includes a career-path advisory layer for IT-related majors. It maps selected major and readiness level to suitable internship role titles and public job search platforms.

## SDG Link

- SDG 4 Quality Education: supports student career learning and self-assessment
- SDG 8 Decent Work and Economic Growth: supports preparation for internship and employability opportunities

## System Architecture

- KB: JSON facts, rules, recommendations, career paths, references, and translations
- IE: Python forward chaining in `inference_engine.py`, plus a deterministic career-path matching helper that uses the inferred readiness result
- UI: Streamlit interface in `app.py`
- Explanation: reasoning chain shown in the Explanation tab
- Testing: `tests/test_cases.py`

## Current Limitation

This initial prototype uses general internship preparation knowledge and public reference ideas to create a starting knowledge base. The rules and recommendations should be refined and validated through consultation with a real Human Expert.
