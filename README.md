# 🤖 AI Helpdesk Agent Pro
> AI-powered IT Helpdesk system built with Flask, Ollama (Llama 3.2), SQLite, and n8n.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-green?style=for-the-badge)
![n8n](https://img.shields.io/badge/n8n-Automation-orange?style=for-the-badge)
🤖 AI Helpdesk Agent Pro
# 🤖 AI Helpdesk Agent Pro

<p align="center">
  <img src="assets/banner.png" alt="AI Helpdesk Agent Pro Banner" width="100%">
</p>

<h3 align="center">🚀 Intelligent AI-Powered IT Helpdesk System</h3>

<p align="center">
Built with <b>Flask</b> • <b>Ollama (Llama 3.2)</b> • <b>SQLite</b> • <b>n8n Automation</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_AI-success?style=for-the-badge)
![n8n](https://img.shields.io/badge/n8n-Automation-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)

</p>

---

# 📌 Project Overview

AI Helpdesk Agent Pro is an intelligent IT support platform that combines **Artificial Intelligence**, **Workflow Automation**, and **Ticket Management** into a single application.

Instead of manually classifying every support request, the system uses a **local Ollama Llama 3.2 model** to automatically analyze user tickets, predict the issue category, assign a priority level, generate a concise summary, and provide AI-powered responses.

The application also supports secure user authentication, dashboard analytics, and automation through **n8n webhooks**.

---

# ✨ Features

## 👤 User Authentication

- Secure Login
- User Registration
- Logout
- Password Hashing
- Admin & User Roles

---

## 🎫 Smart Ticket Management

- Create Support Tickets
- Automatic Ticket Classification
- AI-generated Summary
- AI-generated Priority
- Ticket Status Tracking
- Close Tickets

---

## 🤖 AI Assistant

- AI Chat Support
- IT Troubleshooting
- Technical Guidance
- Local AI using Ollama
- Fast AI Responses

---

## 📊 Dashboard

- Total Tickets
- Pending Tickets
- Closed Tickets
- High Priority Tickets
- Ticket History

---

## 🔄 Automation

- n8n Integration
- Webhook Support
- API Communication
- AI Workflow Automation

---

# 🧠 AI Capabilities

The system uses **Llama 3.2** running locally through **Ollama** to perform:

- 🤖 AI Chat Assistant
- 🎫 Ticket Classification
- ⚡ Priority Prediction
- 📝 Issue Summarization
- 💡 IT Support Recommendations

Unlike cloud AI services, the model runs locally, helping keep project data on the user's machine while avoiding external API dependency.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| SQLite | Database |
| Ollama | Local AI Model |
| Llama 3.2 | Large Language Model |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Client-side |
| n8n | Workflow Automation |
| Requests | API Communication |

---

# 📸 Screenshots

## 🔐 Login Page

![Login](assets/login.png)

---

## 📊 Dashboard

![Dashboard](assets/dashboard.png)

---

## 🎫 Create Ticket

![Create Ticket](assets/create-ticket.png)

---

## 🤖 AI Chat

![AI Chat](assets/chat.png)

---

# 🎥 Demo

> Replace the link below with your YouTube demo video.

**🎬 Watch Demo:**  
https://youtu.be/your-demo-video

---

# 📂 Project Structure

```text
AI_HELPDESK_AGENT_PRO/

│── app.py
│── database.py
│── requirements.txt
│── database.db
│
├── ai/
│     └── ollama.py
│
├── routes/
│     ├── login.py
│     ├── ticket.py
│     └── chat.py
│
├── templates/
│     ├── login.html
│     ├── dashboard.html
│     ├── create_ticket.html
│     └── chat.html
│
├── static/
│     ├── css/
│     ├── js/
│     └── images/
│
└── workflows/
      └── helpdesk.json

This project is developed for educational and internship purposes under the MIT License.
