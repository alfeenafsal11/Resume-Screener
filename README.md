# Resume Screener 🔍  

An AI-powered web application that matches resumes to job descriptions using NLP.  
Deployed on **Vercel** with a clean, interactive frontend and a Python backend.  

---

## 📌 Overview  
Recruiters spend hours manually filtering resumes. This tool automates the process by:  
- Parsing resumes and job descriptions.  
- Calculating a **match score** using NLP.  
- Highlighting **missing skills**.  
- Ranking multiple resumes against a single job description.  

---

## 🚀 Features  
- 📂 Upload **Job Description (PDF/Text)** and **Resume(s) (PDF)**  
- 📊 Match Score (%) with detailed breakdown  
- 🧠 **Skill Gap Analysis** – missing & matched keywords  
- 📈 Visualization (bar & pie charts)  
- 🏆 Multi-resume ranking  
- 📑 Export results as a **PDF report**  

---

## 🛠️ Tech Stack  
- **Frontend**: Next.js + TailwindCSS (hosted on Vercel)  
- **Backend**: Python (Flask/FastAPI) + Hugging Face Transformers  
- **NLP Models**: Sentence Transformers (`all-MiniLM-L6-v2`)  
- **Data Handling**: PyPDF2, Pandas, NumPy, Matplotlib  
- **Deployment**: Vercel (Frontend) + Render (Backend)  

---

## 📂 Project Structure  
