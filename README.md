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

resume-screener/
├── backend/ # Python backend API
├── frontend/ # React/Next.js frontend
├── notebooks/ # ML/NLP experiments
├── examples/ # Sample resumes & JDs


---

## ⚡ Installation & Usage  

### 🔹 Backend (Flask/FastAPI)  
```bash
cd backend
pip install -r requirements.txt
python app.py
Runs on http://127.0.0.1:5000/

🔹 Frontend (Next.js)
bash
Copy code
cd frontend
npm install
npm run dev
Runs on http://localhost:3000/

🌐 Live Demo
🔗 Click here to view deployed app

📊 Example
Input: Job description (Software Engineer), Resume (John Doe).

Output:

Match Score: 78%

Skills Matched: Python, SQL, Machine Learning

Missing Skills: Docker, AWS

Visualization:


🔮 Future Improvements
Add multi-language resume parsing.

Integrate LinkedIn API for job descriptions.

Provide ATS-friendly resume improvement tips.

👤 Author
Alfeen K Afsal

🌐 Portfolio: [your-link-here]

💼 LinkedIn: [linkedin.com/in/yourprofile]

🐙 GitHub: [github.com/yourusername]

yaml
Copy code

---

✅ This structure + README makes your repo **portfolio-ready**.  
Next step: we’ll prepare your **backend `requirements.txt` + frontend `package.json` boilerplate**, so you can deploy right away.  

👉 Do you want me to generate the **starter code (backend + frontend skeleton)** for your Resume Screener, so you just need to plug in your existing logic?







Ask ChatGPT
You
