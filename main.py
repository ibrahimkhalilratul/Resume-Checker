import streamlit as st
import time
import random
from resume_parser import parse_resume
from job_matcher import match_resume_to_job, suggest_missing_skills
from streamlit_extras.add_vertical_space import add_vertical_space

# --- Page Config ---
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")

# --- Custom Styles ---
st.markdown("""
    <style>
    body {background-color: #f4f4f4;}
    .big-title {font-size: 24px; font-weight: bold; text-align: center; color: #2c3e50;}
    .box-style {border-radius: 12px; padding: 20px; background-color: #ffffff; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);}
    .check-btn {background-color: #007bff; color: white; font-size: 18px; font-weight: bold; padding: 10px 20px; border-radius: 10px;}
    .check-btn:hover {background-color: #0056b3;}
    .blinking {animation: blink 1s infinite;}
    @keyframes blink {50% {opacity: 0.5;}}
    </style>
""", unsafe_allow_html=True)

# --- UI Layout ---
st.markdown('<p class="big-title">🔍 Give Your Job Description</p>', unsafe_allow_html=True)
job_desc = st.text_area("", height=150, placeholder="Paste the job description here...")

add_vertical_space(2)  # Adds space between elements

st.markdown('<p class="big-title">📂 Upload Your Resume (PDF)</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"])

add_vertical_space(2)

# --- Blinking "Check" Button ---
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
check_clicked = st.button("⚡ Check", key="check_btn")
st.markdown('</div>', unsafe_allow_html=True)

if check_clicked:
    if uploaded_file is None or job_desc.strip() == "":
        st.warning("⚠️ Please upload a resume and enter a job description before checking.")
    else:
        # --- Show Loading Animation ---
        with st.spinner("🛠️ Analyzing your resume... Please wait!"):
            time.sleep(random.uniform(2, 4))  # Simulating processing time

        # --- Process Resume ---
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        resume_data = parse_resume("temp.pdf")
        match_score = match_resume_to_job(resume_data["text"], job_desc)
        missing_skills = suggest_missing_skills(resume_data["skills"], job_desc)

        # --- Display Results ---
        st.success("✅ Analysis Complete!")
        st.subheader("📊 Resume Match Score:")
        st.write(f"🎯 **{match_score}% Match**")

        st.subheader("🛠️ Suggested Skills to Improve Your Resume:")
        if match_score < 70:  # Adjust threshold
         st.markdown(f"⚒️ **Suggested Skills to Improve Your Resume:**")
    if missing_skills:
        st.write(", ".join(missing_skills))
    else:
        st.write("Your resume covers most skills, but consider adding more details.")
else:
    st.markdown("✅ **Your resume covers all key skills!**")
