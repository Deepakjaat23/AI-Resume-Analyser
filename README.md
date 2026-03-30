🚀 AI Resume Analyzer (Streamlit + Gemini API)
📌 Overview

This project is an AI-powered Resume Analyzer that compares a candidate’s resume with a job description and provides:

✅ Match Score (out of 100)
❌ Missing Skills
💡 Improvement Suggestions
📊 Structured Feedback Summary

Built using Streamlit + Google Gemini API, this tool helps users understand how well their resume aligns with industry requirements.

🔥 Features
📄 Upload Resume (PDF)
🧠 AI-based Resume Analysis
🎯 Job Description Matching
📊 Match Score Generation
💡 Smart Suggestions for Improvement
⚡ Fast & Interactive UI using Streamlit

🛠️ Tech Stack
Frontend: Streamlit
Backend: Python
AI Model: Google Gemini API
PDF Processing: PyMuPDF
Environment Management: python-dotenv

📂 Project Structure
Resume_Analyser/
│── app.py                # Streamlit UI
│── analysis_pdf.py       # AI logic (Gemini API)
│── .env                  # API Key (not uploaded)
│── requirements.txt      # Dependencies
│── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables
Create a .env file:
GEMINI_API_KEY=your_api_key_here

▶️ Run the App
python -m streamlit run app.py

🚧 Future Improvements
📊 Visual charts for match score
📥 Downloadable report (PDF)
🎯 Multiple job role selection
🌐 Deployment (Streamlit Cloud / AWS)

💡 Why This Project?
Most resumes fail not because of lack of skills, but due to poor alignment with job descriptions.
This tool bridges that gap using AI.

🤝 Connect With Me
If you found this useful or have suggestions, feel free to connect on LinkedIn!

⭐ If you like this project
Give it a star ⭐ on GitHub — it helps!
GEMINI_API_KEY=your_api_key_here
▶️ Run the App
python -m streamlit run app.py
