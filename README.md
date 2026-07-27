# 🤖 AI Helpdesk Agent Pro

<!-- Banner -->
![AI Helpdesk Agent Pro Banner](assets/banner.png)

> AI-powered IT Helpdesk system built with Flask, Ollama (Llama 3.2), SQLite, and n8n.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-green?style=for-the-badge)
![n8n](https://img.shields.io/badge/n8n-Automation-orange?style=for-the-badge)
🤖 AI Helpdesk Agent Pro
<div align="center">
🚀 Intelligent AI-Powered IT Helpdesk System

Built with Flask • Ollama (Llama 3.2) • SQLite • n8n Automation

</div>
📌 Project Overview

AI Helpdesk Agent Pro is an intelligent IT support platform that combines Artificial Intelligence, Workflow Automation, and Ticket Management into a single application.

Instead of manually classifying every support request, the system uses a local Ollama Llama 3.2 model to automatically analyze user tickets, predict the issue category, assign a priority level, generate a concise summary, and provide AI-powered responses. The application also supports secure user authentication, dashboard analytics, and automation through n8n webhooks.

✨ Features
👤 User Authentication
Secure Login
User Registration
Logout
Password Hashing
Admin & User Roles
🎫 Smart Ticket Management
Create Support Tickets
Automatic Ticket Classification
AI-generated Summary
AI-generated Priority
Ticket Status Tracking
Close Tickets
🤖 AI Assistant
AI Chat Support
IT Troubleshooting
Technical Guidance
Local AI using Ollama
Fast AI Responses
📊 Dashboard
Total Tickets
Pending Tickets
Closed Tickets
High Priority Tickets
Ticket History
🔄 Automation
n8n Integration
Webhook Support
API Communication
AI Workflow Automation
🧠 AI Capabilities

The system uses Llama 3.2 running locally through Ollama to perform:

AI Chat Assistant
Ticket Classification
Priority Prediction
Issue Summarization
IT Support Recommendations

Unlike cloud AI services, the model runs locally, helping keep project data on the user's machine while avoiding external API dependency.

🛠 Tech Stack
Technology	Purpose
Python	Backend
Flask	Web Framework
SQLite	Database
Ollama	Local AI Model
Llama 3.2	Large Language Model
HTML5	Frontend
CSS3	Styling
JavaScript	Client-side
n8n	Workflow Automation
Requests	API Communication
📂 Project Structure
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
⚙ Installation
Clone Repository
git clone https://github.com/yourusername/AI_HELPDESK_AGENT_PRO.git

cd AI_HELPDESK_AGENT_PRO
Create Virtual Environment
python -m venv venv

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt

The project depends on Flask, Werkzeug, and Requests.

🤖 Install Ollama

Download Ollama

https://ollama.com

Download the model

ollama pull llama3.2

Start Ollama

ollama serve
🗄 Create Database
python database.py

This creates the SQLite database and a default admin account.

▶ Run the Project
python app.py

Open

http://localhost:5000

The Flask application starts on port 5000 and expects the database to be initialized first.

🔄 AI Workflow
User Login
      │
      ▼
Create Ticket
      │
      ▼
Flask Backend
      │
      ▼
Ollama AI
      │
      ▼
Category Prediction
Priority Prediction
Summary Generation
      │
      ▼
SQLite Database
      │
      ▼
Dashboard
🔄 n8n Workflow
Webhook
      │
      ▼
Flask API
      │
      ▼
Ollama AI
      │
      ▼
AI Response
      │
      ▼
Return Result

The project also includes a dedicated webhook endpoint protected by an API key for automation tools like n8n

🚀 Future Improvements
Email Notifications
File Attachments
PDF Report Export
Charts & Analytics
Voice Support
Dark Mode
RAG Knowledge Base
Multi-language Support
Docker Deployment
PostgreSQL Support
👨‍💻 Author

Hadia Awan

Artificial Intelligence Student

GitHub: https://github.com/hadiaamjad07

⭐ Support

If you like this project,

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

📄 License

This project is developed for educational and internship purposes under the MIT License.
