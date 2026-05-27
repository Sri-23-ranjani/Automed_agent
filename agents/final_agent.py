import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def final_agent(symptom_summary, treatment_info):
    prompt = f"""
You are AutoMed, a safe multi-agent AI health information assistant.

Inputs from agents:

{symptom_summary}

{treatment_info}

Rules:
1. Do not diagnose.
2. Do not prescribe medicines.
3. Do not give dosage.
4. Give possible general causes only.
5. Give safe self-care tips.
6. Mention when to consult a doctor.
7. Include a medical disclaimer.
8. Keep it simple and clear.

Output format:

Symptom Summary:
...

Possible General Causes:
...

Safe Self-Care:
...

When to See a Doctor:
...

Medical Disclaimer:
...
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content