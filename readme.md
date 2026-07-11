# 🚀 AI Career Copilot

An AI-powered web application that analyzes resumes, identifies skill gaps, provides personalized learning roadmaps, generates interview questions, and estimates an ATS score based on the user's target job role.

## ✨ Features

- 🔐 Secure User Authentication (Signup/Login with Password Hashing)
- 📄 Resume Upload (PDF & DOCX) or Paste Resume Text
- 🤖 AI-Powered Resume Analysis using Groq Llama 3.3
- 💡 Extracts Relevant Skills
- 📉 Identifies Missing Skills
- 🎯 Calculates ATS Score
- 🗺️ Generates Personalized Learning Roadmap
- 💬 Generates Role-Specific Interview Questions
- 📚 Stores Resume Analysis History
- 🚪 Logout Functionality

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- SQLAlchemy
- Groq API (Llama 3.3-70B)
- PyPDF2
- python-docx

### Database
- MySQL / TiDB Cloud

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

---

## 📂 Project Structure

```text
AI-Career-Copilot/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── history.html
│   ├── login.html
│   ├── signup.html
│   └── forget_password.html
│
└── .env
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Career-Copilot.git
cd AI-Career-Copilot
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Configure Database

Update your database connection inside `db.py`.

### 6. Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---


## 🎯 Future Improvements

- Email-based Password Reset
- Resume PDF Report Download
- AI Resume Improvement Suggestions
- Dark Mode
- Role Recommendation
- Resume Keyword Optimization
- Admin Dashboard

---

## 🔒 Security

- Password Hashing using Werkzeug
- Environment Variables for API Keys
- Session-Based Authentication

---

## 👩‍💻 Author

**Vanshika Jain**

- GitHub: https://github.com/YOUR_USERNAME
- LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.