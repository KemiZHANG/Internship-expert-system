# Internship Preparation Advisory Expert System

Course: WID2001 Knowledge Representation and Reasoning

## English Overview

This project is a local rule-based Expert System prototype built with Python and Streamlit. It helps university students evaluate their internship preparation readiness and identify what they should improve before applying for internships.

The system is not a chatbot and not a normal survey form. User inputs are converted into facts, IF-THEN rules are stored in a Knowledge Base, and an Inference Engine applies forward chaining to infer intermediate decisions, final readiness levels, specific advice, and recommendations.

Academic honesty note:

> This initial prototype uses general internship preparation knowledge and public reference ideas to create a starting knowledge base. The rules and recommendations should be refined and validated through consultation with a real Human Expert.

## 中文简介

本项目是一个使用 Python 和 Streamlit 开发的本地规则型专家系统原型。系统主题是实习准备咨询，主要帮助大学生评估自己目前的实习申请准备程度，并指出下一步应该优先改进的方向。

这个系统不是聊天机器人，也不是普通问卷。用户在界面中的选择会先被转换成 facts，然后系统根据 Knowledge Base 中的 IF-THEN rules，通过 Inference Engine 的 forward chaining 前向推理，推导出中间决策、最终实习准备等级、具体建议和行动计划。

学术诚信说明：

> 当前原型使用一般实习准备知识和公开资料作为初始知识库来源。规则和建议之后仍需要通过真实 Human Expert 咨询进行改进和验证。

## What the System Does

The system evaluates internship readiness across these areas:

- Application Materials
- Project and Portfolio
- Technical Skills
- Interview Preparation
- Career Direction
- Application Progress
- Soft Skills and Work Readiness

It outputs:

- Overall Readiness Level: Low, Medium, or High
- Readiness Score out of 100
- Main Priority Area
- Rule-Based Specific Advice
- Recommendations and Next Action Plan
- Explanation Chain showing facts, rules, decisions, and recommendations

## 系统有什么作用

系统可以帮助学生快速判断自己是否已经适合开始申请实习，并明确当前最需要补强的部分。例如：

- 简历和作品集是否足够完整
- 技术基础是否需要加强
- 是否需要先练习面试
- 是否需要明确目标岗位
- 是否应该开始投递、记录申请状态和 follow-up

对于课程展示来说，本项目可以清楚体现 Knowledge Base、Inference Engine、User Interface、Explanation Facility 和 Testing。

## Expert System Components

| Component | Implementation |
|---|---|
| Knowledge Base, KB | `data/facts.json`, `data/rules.json`, `data/recommendations.json`, `data/references.json` |
| Inference Engine, IE | `inference_engine.py` |
| User Interface, UI | `app.py` with Streamlit |
| Explanation Facility | Explanation tab in the Streamlit app |
| Testing | `tests/test_cases.py` |
| Documentation | `README.md` and files in `docs/` |

## Internal Reasoning Flow

The reasoning flow is:

```text
User Interface
↓
User inputs become Facts
↓
Knowledge Base stores IF-THEN Rules
↓
Inference Engine applies Forward Chaining
↓
Intermediate Decisions
↓
Final Readiness Level and Specific Advice
↓
Recommendations and Next Action Plan
```

中文说明：

```text
用户界面
↓
用户输入转换成事实
↓
知识库存储 IF-THEN 规则
↓
推理引擎使用前向推理
↓
推导中间决策
↓
推导最终准备等级和具体建议
↓
输出推荐和下一步行动计划
```

## Why This Is an Expert System

- User inputs are represented as facts.
- The Knowledge Base stores IF-THEN rules.
- The Inference Engine applies forward chaining.
- Rules can infer intermediate decisions before final decisions.
- The Explanation Facility shows which facts and rules produced the result.
- The readiness score is supportive; rule-based reasoning remains the core.

## 为什么这不是普通问卷

普通问卷通常只是把选项加分后直接给结果。本系统的重点是规则推理：

- 用户输入会被转换成 facts
- 系统根据 Knowledge Base 中的 IF-THEN rules 推理
- 规则会先推出 intermediate decisions
- 再推出 final readiness decisions 和 advice decisions
- Explanation 页面会展示 triggered rules 和 reasoning chain

因此，本项目符合 WID2001 中 Expert System prototype 的核心要求。

## Project Structure

```text
Internship_ES_Project/
├── app.py
├── inference_engine.py
├── knowledge_base.py
├── requirements.txt
├── README.md
├── data/
│   ├── facts.json
│   ├── rules.json
│   ├── recommendations.json
│   ├── references.json
│   └── translations.json
├── tests/
│   └── test_cases.py
└── docs/
    ├── PROJECT_SUMMARY.md
    ├── INITIAL_KNOWLEDGE_SOURCES.md
    ├── KNOWLEDGE_BASE_EXPLANATION.md
    ├── INFERENCE_ENGINE_EXPLANATION.md
    ├── TESTING_GUIDE.md
    ├── TESTING_REPORT_TEMPLATE.md
    ├── HUMAN_EXPERT_PLACEHOLDER.md
    ├── FUTURE_OPTIMIZATION_GUIDE.md
    ├── REQUIREMENT_CHECKLIST.md
    └── SUBMISSION_READINESS.md
```

## How to Run on Your Computer

### 1. Clone the repository

```bash
git clone https://github.com/KemiZHANG/Internship-expert-system.git
cd Internship-expert-system
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## 如何在自己的电脑运行

1. 下载项目：

```bash
git clone https://github.com/KemiZHANG/Internship-expert-system.git
cd Internship-expert-system
```

2. 创建并开启虚拟环境：

```powershell
python -m venv .venv
.venv\Scripts\Activate
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

4. 运行网页：

```bash
streamlit run app.py
```

5. 在浏览器打开：

```text
http://localhost:8501
```

## How to Run Tests

```bash
python tests/test_cases.py
```

The test suite includes 10 cases covering high, medium, low readiness, weak interview preparation, unclear career direction, weak application materials, weak project explanation, weak application progress, and boundary cases.

## Demo Flow

For a short presentation, use this flow:

1. Open the Assessment tab and choose a demo case.
2. Show the Results tab with Level, Score, Priority, and Advice.
3. Open the Explanation tab to show facts, triggered rules, and inferred decisions.
4. Open the Knowledge Base tab to show facts, rules, recommendations, and filters.
5. Open the Testing Guide tab and explain the automated tests.

## Languages

The UI supports:

- English
- 中文
- Bahasa Melayu

Translations are stored in `data/translations.json`. Internal IDs such as `F1`, `R1`, `D1`, and `FD1` remain stable and are not translated.

## Future Human Expert Validation

Human Expert validation has not been completed in this initial prototype. After the group consults a real Human Expert, update:

- `data/facts.json`
- `data/rules.json`
- `data/recommendations.json`
- `data/references.json`
- `docs/HUMAN_EXPERT_PLACEHOLDER.md`

Do not claim Human Expert validation until real expert information and evidence are added.
