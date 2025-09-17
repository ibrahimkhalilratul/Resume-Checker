from sentence_transformers import SentenceTransformer, util
import json
from fuzzywuzzy import process  # For approximate skill matching

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load predefined skills
with open("model/skills.json", "r") as f:
    skill_db = json.load(f)

def extract_job_skills(job_desc):
    job_skills = []
    for skill in skill_db:
        match, score = process.extractOne(skill, [job_desc])
        if score > 80:  # Fuzzy match threshold
            job_skills.append(skill)
    return list(set(job_skills))

def match_resume_to_job(resume_text, job_desc):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_desc, convert_to_tensor=True)
    
    similarity = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
    return round(similarity * 100, 2)  # Return percentage match

def suggest_missing_skills(resume_skills, job_desc):
    job_required_skills = extract_job_skills(job_desc)
    missing_skills = list(set(job_required_skills) - set(resume_skills))
    return missing_skills