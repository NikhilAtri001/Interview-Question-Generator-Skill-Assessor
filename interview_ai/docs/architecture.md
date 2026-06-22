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