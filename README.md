
---
title: Resume Screener
emoji: 📄
colorFrom: blue
colorTo: green
sdk: docker
app_file: streamlit_app.py
pinned: false
---


# AI Resume Screener

A web application that matches a resume against a job description using NLP and semantic similarity.

## What It Does
- Upload a resume PDF and paste a job description
- Get a match score showing how well the resume fits the JD
- See a list of missing keywords to improve the resume

## Tech Stack
- **Sentence Transformers** — semantic similarity between resume and JD
- **spaCy** — keyword extraction from job description
- **pdfplumber** — extract text from PDF resume
- **FastAPI** — backend REST API
- **Streamlit** — frontend web interface
- **Render** — deployment

## How It Works
1. Resume PDF is uploaded and text is extracted using pdfplumber
2. Both resume text and JD text are converted to vectors using sentence-transformers
3. Cosine similarity between the two vectors gives the match score
4. spaCy extracts keywords from JD and checks which ones are missing from resume

## How To Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Rohit2209Raj/resume-screener.git
cd resume-screener
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**4. Run FastAPI backend**
```bash
uvicorn main:app --reload
```

**5. Run Streamlit frontend**
```bash
streamlit run app.py
```

**6. Open browser at** `http://localhost:8501`

## Project Structure


resume-screener/
├── main.py          # FastAPI backend
├── matcher.py       # Match score + keyword extraction
├── utils.py         # PDF text extraction
├── app.py           # Streamlit frontend
├── requirements.txt
└── .gitignore


## Limitations
- Missing keywords uses NLP noun chunk extraction — works best with well structured JDs
- Scanned PDF resumes (image based) may not extract text correctly

## Author
- Rohit Raj — B.Tech CSE, Poornima College of Engineering
- GitHub: github.com/Rohit2209Raj