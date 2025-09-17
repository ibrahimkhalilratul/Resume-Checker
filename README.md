# Resume-Checker
NLP based project to check you resume is perfectly going or not with your applying job!!

🔹 Overview

This project is an AI-based resume analysis tool that evaluates how well a candidate’s resume matches a given job description. It extracts text from PDF resumes, processes the job description, and calculates a match score along with skill gap analysis.

The system leverages NLP and ML techniques to highlight missing skills and provide actionable suggestions for resume improvement.



🔹 **Features**

📂 Resume Parsing: Extracts text from resumes using pdfplumber.

🧠 NLP Processing: Uses spaCy and NLTK for tokenization, named entity recognition, and keyword extraction.

🔎 Semantic Similarity: Employs sentence-transformers to measure similarity between resume content and job requirements.

📊 Machine Learning: scikit-learn used for feature extraction (TF-IDF, cosine similarity) and match scoring.

📈 Skill Gap Analysis: Identifies missing or weak skills in the resume compared to job description.

⚡ Easy Integration: Can be extended for ATS (Applicant Tracking System) or HR platforms.



🔹 **Tech Stack**

_Python 3.x

spaCy – Named Entity Recognition, NLP preprocessing

NLTK – Text preprocessing, stopword removal, stemming

pdfplumber – PDF resume text extraction

scikit-learn – TF-IDF, cosine similarity, ML models

sentence-transformers – Semantic similarity (BERT-based embeddings)_
