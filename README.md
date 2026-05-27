# AutoMed Multi-Agent Healthcare Assistant

## AI-Powered Healthcare Information Assistant using AG2 Multi-Agent Framework

AutoMed is a multi-agent AI healthcare information assistant built using AG2 (AutoGen), Groq LLMs, and Gradio.

The system simulates collaborative healthcare assistance using multiple specialized AI agents that analyze symptoms, perform safety checks, summarize uploaded medical reports, recommend suitable specialists, and generate safe health-information guidance.

---

# Features

- Multi-Agent AI Architecture
- Symptom Analysis Agent
- Emergency Safety Detection
- Medical Knowledge Agent
- Health Guidance Agent
- Medical Report Upload Support
- Doctor Recommendation System
- Final Response Aggregation Agent
- PDF / DOCX / TXT Report Parsing
- Groq LLM Integration
- Gradio Web Interface
- Safe AI Prompting
- Modular Agent-Based Design

---

# Multi-Agent Workflow

```text
User Symptoms / Medical Report
            ↓
Symptom Analyzer Agent
            ↓
Safety Checker Agent
            ↓
Medical Knowledge Agent
            ↓
Health Guidance Agent
            ↓
Medical Report Upload Agent
            ↓
Doctor Recommendation Agent
            ↓
Final Response Agent
```

---

# Technologies Used

- Python
- AG2 (AutoGen)
- Groq API
- Gradio
- python-dotenv
- pypdf
- python-docx

---

# Project Structure

```text
automed-agent/
│
├── app.py
├── .env
├── requirements.txt
│
├── agents/
│   ├── __init__.py
│   ├── ag2_agents.py
│   ├── report_agent.py
│   ├── doctor_agent.py
│   ├── symptom_agent.py
│   ├── safety_agent.py
│   ├── treatment_agent.py
│   └── final_agent.py
│
└── venv/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AutoMed-Agent.git
```

---

## Navigate to Project

```bash
cd AutoMed-Agent
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run Application

```bash
python app.py
```

---

# Example Symptoms

- fever and headache
- cough and cold
- stomach pain
- chest pain and breathing difficulty
- skin allergy and itching

---

# Medical Report Upload

Users can upload:

- PDF medical reports
- DOCX reports
- TXT medical notes

The system extracts and summarizes report content safely.

---

# Doctor Recommendation System

Based on symptoms, AutoMed can recommend:

- General Physician
- Cardiologist
- Dermatologist
- Gastroenterologist
- ENT Specialist
- Orthopedic Doctor
- Ophthalmologist
- Psychiatrist

---

# Safety Features

- Emergency symptom detection
- No medicine prescriptions
- No dosage recommendations
- No direct diagnosis
- Professional medical disclaimer
- Safe AI prompting

---

# Important Disclaimer

AutoMed is designed only for general healthcare information and educational purposes.

It does NOT:
- replace doctors
- provide medical diagnosis
- prescribe medicines
- provide emergency treatment

Always consult a qualified healthcare professional for medical advice.

---

# Future Improvements

- Voice-based symptom input
- Chat history memory
- Real medical database integration
- Hospital recommendation system
- LangGraph orchestration
- Authentication system
- Cloud deployment
- Multilingual support

---

# Author

Sri Ranjani V

---

# License

This project is for educational and research purposes only.