import fitz   # pymupdf
import google.generativeai as genai
from analysis_pdf import analyze_resume_gemini
from dotenv import load_dotenv
import os



# function to text from the resume pdf
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


pdf_path = "DEEPAK.pdf"

resum_content = extract_text_from_pdf(pdf_path)

job_description = """
    We are hiring a Data Scientist with experience in:
    - Machine Learning
    - Deep Learning
    - Natural Language Processing
    - Python and R programming
    - Data Visualization
    - Statistical Analysis
    Responsibilities include:
    - Analyzing large datasets to extract insights
    - Building predictive models
    - Communicating findings to stakeholders
    - Collaborating with cross-functional teams
    - Staying updated with the latest research in data science
    """

result = analyze_resume_gemini(resum_content, job_description)
print(result)