import spacy
import json
import fitz  # PyMuPDF

nlp = spacy.load("en_core_web_sm")

# Load predefined skills
with open("model/skills.json", "r") as f:
    skill_db = json.load(f)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

def extract_skills(text):
    doc = nlp(text)
    resume_skills = []

    for token in doc:
        if token.text in skill_db:  # Check if token is in skill database
            resume_skills.append(token.text)

    return list(set(resume_skills))  # Remove duplicates

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    skills = extract_skills(text)
    return {"text": text, "skills": skills}