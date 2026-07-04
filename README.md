# 🤖 AI-Powered Enterprise API Troubleshooting Assistant

> An AI-powered technical support application that helps developers and enterprise support teams diagnose REST API integration issues using Google's Gemini Large Language Model (LLM).
---
## 📌 Overview

Enterprise technical support engineers spend significant time investigating API failures, authentication errors, HTTP status codes, and application logs. This project demonstrates how Large Language Models (LLMs) can assist in accelerating that workflow.
The application accepts REST API details—including endpoints, HTTP status codes, request/response payloads, and application logs—and generates structured troubleshooting recommendations, root cause analysis, best practices, and customer-friendly explanations.
Built as a portfolio project inspired by real-world enterprise technical support workflows.
---
## ✨ Features

- 🔍 Analyze REST API integration issues
- 🤖 AI-powered root cause analysis using Google Gemini
- 📡 HTTP status code interpretation
- 📄 Application log analysis
- 🛠 Actionable troubleshooting recommendations
- 💡 Best practice suggestions
- 😊 Customer-friendly explanations
- 🧩 Modular Python architecture
- ⚡ Interactive Streamlit interface
---
## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| AI Integration | Google GenAI SDK |
| Configuration | python-dotenv |
| Version Control | Git |
| Repository | GitHub |
---

## 🏗 Project Architecture

```text
                User
                  │
                  ▼
         Streamlit Web Interface
                  │
                  ▼
          Prompt Generation
            (prompts.py)
                  │
                  ▼
      Google Gemini API (LLM)
          (ai_service.py)
                  │
                  ▼
     AI Troubleshooting Analysis
                  │
                  ▼
      Results Displayed to User
---

## 📂 Project Structure

```text
AI-Enterprise-Troubleshooting-Assistant
│
├── app.py                 # Streamlit user interface
├── ai_service.py          # Gemini API integration
├── prompts.py             # Prompt engineering
├── requirements.txt
├── .gitignore
└── README.md
```
## ⚙️ How It Works

1. Enter the API endpoint.
2. Provide the HTTP status code.
3. Paste the request payload.
4. Paste the response payload.
5. Add application logs.
6. Click **Analyze Issue**.
7. The application sends the information to Google Gemini.
8. Gemini generates:

- Root Cause
- Possible Reasons
- Troubleshooting Steps
- Best Practices
- Customer-Friendly Explanation
---
## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/RakshithaB17/AI-Enterprise-Troubleshooting-Assistant.git
```

### Navigate to the project

```bash
cd AI-Enterprise-Troubleshooting-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

---

## 💼 Skills Demonstrated

- Large Language Model (LLM) Integration
- Prompt Engineering
- REST API Troubleshooting
- Python Development
- Streamlit Application Development
- API Authentication
- Modular Software Architecture
- Enterprise Technical Support Workflows
- AI-Assisted Root Cause Analysis

---

## 🚧 Planned Enhancements

- Structured JSON responses from the LLM
- Knowledge Base article generation
- Customer response generator
- PDF troubleshooting reports
- Issue history
- ElevenLabs Text-to-Speech integration
- Streamlit Community Cloud deployment

---

## 📸 Screenshots

### Home Screen

_Add screenshot_

### Issue Analysis

_Add screenshot_

### AI Troubleshooting Report

_Add screenshot_

---

## 👩‍💻 Author

**Rakshitha B**

GitHub: https://github.com/RakshithaB17

---

⭐ If you found this project interesting, feel free to star the repository.
