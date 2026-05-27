import gradio as gr

from agents.ag2_agents import (
    symptom_analyzer,
    safety_checker,
    medical_knowledge_agent,
    health_guidance,
    final_response_agent,
)

from agents.report_agent import extract_report_text, summarize_report_agent
from agents.doctor_agent import recommend_doctor_agent


EMERGENCY_KEYWORDS = [
    "chest pain",
    "difficulty breathing",
    "shortness of breath",
    "severe bleeding",
    "unconscious",
    "seizure",
    "stroke",
    "heart attack",
    "suicide",
    "fainting",
    "severe allergic reaction",
]


def has_emergency_symptom(symptoms):
    symptoms_lower = symptoms.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in symptoms_lower:
            return True
    return False


def ask_agent(agent, message):
    reply = agent.generate_reply(
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    if isinstance(reply, dict):
        return reply.get("content", "")

    return str(reply)


def automed_response(symptoms, report_file):
    symptoms = symptoms.strip()

    if not symptoms and report_file is None:
        return (
            "Please enter symptoms or upload a medical report.",
            "",
            "",
            "",
            "",
            "",
            ""
        )

    report_summary = "No medical report uploaded."

    if report_file is not None:
        report_text = extract_report_text(report_file.name)
        report_summary = summarize_report_agent(report_text)

    if symptoms and has_emergency_symptom(symptoms):
        emergency_message = """
Emergency Warning:
Your symptoms may require urgent medical attention.

Please contact emergency services or visit the nearest hospital immediately.

AutoMed is not a substitute for professional medical diagnosis or treatment.
"""

        doctor_recommendation = recommend_doctor_agent(symptoms)

        return (
            "Emergency symptoms detected.",
            emergency_message,
            "Medical knowledge skipped due to emergency warning.",
            "General guidance skipped due to emergency warning.",
            report_summary,
            doctor_recommendation,
            emergency_message
        )

    if symptoms:
        symptom_result = ask_agent(
            symptom_analyzer,
            f"Analyze these symptoms without diagnosis: {symptoms}"
        )

        safety_result = ask_agent(
            safety_checker,
            f"Check if these symptoms contain emergency warning signs: {symptoms}"
        )

        knowledge_result = ask_agent(
            medical_knowledge_agent,
            f"Give safe general medical background for these symptoms: {symptoms}"
        )

        guidance_result = ask_agent(
            health_guidance,
            f"Give safe general health guidance for these symptoms: {symptoms}"
        )

        doctor_recommendation = recommend_doctor_agent(symptoms)

    else:
        symptom_result = "No symptoms entered."
        safety_result = "No emergency symptom check performed because no symptoms were entered."
        knowledge_result = "Medical knowledge generated only from symptoms, so no symptom-based knowledge is available."
        guidance_result = "Please consult a qualified doctor for report interpretation."
        doctor_recommendation = "Please enter symptoms to recommend a suitable specialist."

    final_result = ask_agent(
        final_response_agent,
        f"""
Create final patient-friendly response using these agent outputs.

User Symptoms:
{symptoms}

Symptom Agent Output:
{symptom_result}

Safety Agent Output:
{safety_result}

Medical Knowledge Agent Output:
{knowledge_result}

Health Guidance Agent Output:
{guidance_result}

Medical Report Agent Output:
{report_summary}

Doctor Recommendation Agent Output:
{doctor_recommendation}

Rules:
Do not diagnose.
Do not prescribe medicines.
Do not give dosage.
Use report content only as informational summary.
Always advise professional consultation.
"""
    )

    return (
        symptom_result,
        safety_result,
        knowledge_result,
        guidance_result,
        report_summary,
        doctor_recommendation,
        final_result
    )


with gr.Blocks(title="AutoMed Multi-Agent Healthcare Assistant") as demo:

    gr.Markdown(
        """
# AutoMed Multi-Agent Healthcare Assistant

AI-powered healthcare information assistant using AG2-style multi-agent collaboration.

### Multi-Agent Workflow

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

**Note:** This tool provides general health information only. It does not diagnose, prescribe medicines, or replace professional medical care.
"""
    )

    symptoms_input = gr.Textbox(
        label="Enter Symptoms",
        lines=5,
        placeholder="Example: fever, headache, body pain"
    )

    report_input = gr.File(
        label="Upload Medical Report PDF / DOCX / TXT",
        file_types=[".pdf", ".docx", ".txt"]
    )

    analyze_button = gr.Button("Analyze")

    gr.Markdown("## Agent Outputs")

    with gr.Row():
        symptom_output = gr.Textbox(
            label="Symptom Analyzer Agent",
            lines=8
        )

        safety_output = gr.Textbox(
            label="Safety Checker Agent",
            lines=8
        )

    knowledge_output = gr.Textbox(
        label="Medical Knowledge Agent",
        lines=10
    )

    guidance_output = gr.Textbox(
        label="Health Guidance Agent",
        lines=10
    )

    report_output = gr.Textbox(
        label="Medical Report Upload Agent",
        lines=10
    )

    doctor_output = gr.Textbox(
        label="Doctor Recommendation Agent",
        lines=8
    )

    final_output = gr.Textbox(
        label="Final Response Agent",
        lines=15
    )

    analyze_button.click(
        automed_response,
        inputs=[
            symptoms_input,
            report_input
        ],
        outputs=[
            symptom_output,
            safety_output,
            knowledge_output,
            guidance_output,
            report_output,
            doctor_output,
            final_output
        ]
    )


demo.launch()