# Project Summary

## Introduction

The Internship Preparation Advisory Expert System is a local rule-based prototype for WID2001 Knowledge Representation and Reasoning. It helps university students evaluate internship preparation and identify the next priority area.

## Objectives

- Represent internship preparation knowledge as facts and IF-THEN rules
- Use forward chaining to infer intermediate and final decisions
- Provide explanation of selected facts, triggered rules, decisions, and recommendations
- Add score-based fallback so the system always produces a final readiness decision
- Support English, Chinese, and Bahasa Melayu UI text
- Provide demo cases and automated tests for presentation

## Domain

The domain is internship preparation for university students, especially students preparing for software, AI, data, or CS-related internships.

## SDG Link

- SDG 4 Quality Education: supports student career learning and self-assessment
- SDG 8 Decent Work and Economic Growth: supports preparation for internship and employability opportunities

## System Architecture

- KB: JSON facts, rules, recommendations, references, and translations
- IE: Python forward chaining in `inference_engine.py`
- UI: Streamlit interface in `app.py`
- Explanation: reasoning chain shown in the Explanation tab
- Testing: `tests/test_cases.py`

## Current Limitation

This initial prototype uses general internship preparation knowledge and public reference ideas to create a starting knowledge base. The rules and recommendations should be refined and validated through consultation with a real Human Expert.
