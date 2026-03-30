import streamlit as st
import fitz  # PyMuPDF
from analysis_pdf import analyze_resume_gemini

# ----------- FUNCTION: Extract text from uploaded PDF -----------
def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


# ----------- STREAMLIT UI -----------

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job Description Input
job_description = st.text_area("Paste Job Description")

# Analyze Button
if st.button("Analyze Resume"):
    if uploaded_file is None:
        st.error("Please upload a resume.")
    elif job_description.strip() == "":
        st.error("Please enter a job description.")
    else:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            result = analyze_resume_gemini(resume_text, job_description)

        st.success("Analysis Complete ✅")
        st.text_area("Result", result, height=400)