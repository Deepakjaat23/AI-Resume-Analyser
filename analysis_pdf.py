import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Use the VARIABLE NAME from your .env file
api_key = os.getenv("GEMINI_API_KEY") 

if not api_key:
    raise ValueError("API Key not found. Please check your .env file.")

genai.configure(api_key=api_key)

# --- NEW LOGIC: Automatically find a valid model ---
def get_available_model():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            return m.name
    return "gemini-1.5-flash"  # Fallback

working_model_name = get_available_model()
print(f"Using model: {working_model_name}")

configuration = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
    model_name=working_model_name,
    generation_config=configuration
)

def analyze_resume_gemini(resume_content, job_description):
    prompt = f"""
    You are a professional resume analyzer.

    Resume:
    {resume_content}

    Job Description:
    {job_description}

    Task:
    - Analyze the resume against the job description.
    - Give a match score out of 100.
    - Highlight missing skills or experiences.
    - Suggest improvements.

    Return the result in structured format:
    Match Score: XX/100
    Missing Skills:
    - ...
    Suggestions:
    - ...
    Summary:
    ...
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred during generation: {str(e)}"