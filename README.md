<!-- ----------------------------------------------------- -->
<!-- 🌈 NEUROQUIZ — AI-Powered Quiz App README (v2.0) 🌈 -->
<!-- --------------------------------------------------- -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,100:9333EA&height=200&section=header&text=🧠%20NeuroQuiz&fontSize=50&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35" />
</p>


---

> 🚀 **NeuroQuiz** is an **AI-powered quiz web app** that brings together intelligence, learning, and design.  
> Built with **Flask**, **OpenAI**, and **SQLite**, it allows users to **generate smart quizzes**, **receive instant feedback**, and **track performance** — all wrapped in a sleek, modern interface.

---

## 🌟 Features at a Glance

| 🔐 Authentication | 🤖 AI Quiz Generation | 🧠 Smart Feedback | 📊 History Tracking |
|-------------------|-----------------------|------------------|----------------------|
| Secure login/signup with password hashing | AI-generated questions (OpenAI) | Instant result evaluation | Stores quiz attempts, scores, and timestamps |

---

## 🎯 Core Highlights

### 🔐 Secure User Authentication
- Login & registration system using Flask + SQLite  
- Passwords hashed for data safety  
- Session management for persistent login  

### 🤖 AI Quiz Generator
- Uses **OpenAI API** to dynamically create questions  
- Multiple topics & difficulty levels  
- Every quiz is 100% unique  

### 🧠 Instant Feedback System
- Real-time answer validation  
- Instant correct/incorrect feedback  
- Auto-calculated score display  

### 📈 Quiz History Dashboard
- View past quizzes with score, time, and date  
- Simple, clean leaderboard-style layout  

### 🎨 TailwindCSS UI
- Fully responsive & minimal  
- Elegant gradient backgrounds  
- Smooth transitions & soft shadows  

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML, CSS, JavaScript, TailwindCSS |
| **Database** | SQLite |
| **AI Model** | Any LLM API |
| **Hosting** | Render / Localhost |
| **Version Control** | Git + GitHub |


---

## ⚙️ Setup Guide

### 🧰 Requirements
- Python 3.10+
- Git
- LLM API Key

---

## 🚀 Installation

• Clone repository :

>git clone https://github.com/Zyashx07/AI-QUIZ-APP.git
cd NeuroQuiz

• Create virtual environment:

>1.python -m venv venv

• Activation 

>For Windows :
venv\Scripts\activate

>For Mac/Linux :
source venv/bin/activate

• Install dependencies :

>pip install -r requirements.txt

• Add your LLM API key :

>Create a file named .env and paste:
LLM_API_KEY=your_api_key_here

Run the Flask app :
python app.py

Procfile :
web: gunicorn app:app

Now open your browser at 👉 http://127.0.0.1:5000


---

### 🧠 How It Works

1. 🧾 User logs in or signs up


2. 🎯 Selects quiz topic and difficulty


3. ⚙️ AI dynamically generates questions


4. 💡 User answers → gets instant feedback


5. 📊 Quiz data saved to history database




---


## 🌍 Deployment

You can host NeuroQuiz on:

🚀 Render

⚙️ Railway

💻 Localhost for testing



---

## 📜 License

Licensed under the MIT License
Feel free to fork, modify, and learn from it ✨


---


  <br>
  <em>“Knowledge becomes power when shared — NeuroQuiz helps you discover it.”</em>
</p>
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:9333EA,100:06B6D4&height=150&section=footer&fontColor=FFFFFF&animation=twinkling" />
</p><p align="center">
