# Project Outline

## Project Title

Interview Question Generator & Skill Assessor

## Problem Statement

Recruiters spend significant time reviewing resumes, creating interview questions, and evaluating candidates.

This project aims to automate parts of the hiring process using AI and Machine Learning.

---

## Proposed Solution

The system will:

1. Accept a candidate resume.
2. Accept a job description.
3. Extract candidate skills.
4. Match candidate skills with job requirements.
5. Generate interview questions.
6. Assess candidate responses.
7. Display results through a dashboard.

---

## Workflow

Resume Upload (PDF/DOCX)
        ↓
Resume Classifier (ML)  ← TF-IDF + Logistic Regression, trained on 8,167 real resumes
        ↓
Predicted Role  (10 IT job categories)
        ↓
Skill Extraction  ← matched against a real skill vocabulary
        ↓
Job Description Analysis
        ↓
Required Skills Extraction
        ↓
Skill Matching Engine  (weighted: 70% required / 30% preferred)
        ↓
Match Score
        ↓
Question Generation  ← Google Gemini API (+ local fallback bank)
        ↓
Answer Evaluation  ← Google Gemini (0–10 score, grade, feedback)
        ↓
Dashboard
---

## Inputs

- Resume (PDF)
- Job Description
- Candidate Answers

---

## Outputs

- Extracted Skills
- Skill Match Percentage
- Generated Questions
- Skill Assessment Score
- Dashboard Summary

---

## Technology Stack

Frontend:
- Streamlit

Backend:
- Python

Libraries:
- Pandas
- NumPy
- Scikit-learn

Version Control:
- Git
- GitHub

---

## MVP (Minimum Viable Product)

Phase 1:
- Resume Upload
- Skill Extraction

Phase 2:
- Skill Matching
- Question Generation

Phase 3:
- Skill Assessment
- Dashboard

---

## Expected Outcome

A web-based application that helps recruiters generate interview questions and perform basic candidate skill assessment.