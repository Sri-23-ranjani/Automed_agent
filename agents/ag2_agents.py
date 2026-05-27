import os
from dotenv import load_dotenv
from autogen import ConversableAgent

load_dotenv()

llm_config = {
    "config_list": [
        {
            "model": "llama-3.1-8b-instant",
            "api_key": os.getenv("GROQ_API_KEY"),
            "base_url": "https://api.groq.com/openai/v1",
            "api_type": "openai",
        }
    ],
    "temperature": 0.2,
}


symptom_analyzer = ConversableAgent(
    name="Symptom_Analyzer_Agent",
    system_message="""
You are a symptom intake agent.
Your job is to understand the user's symptoms clearly.
Do not diagnose.
Summarize symptoms in simple terms.
""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

safety_checker = ConversableAgent(
    name="Safety_Checker_Agent",
    system_message="""
You are a medical safety agent.
Your job is to identify emergency warning signs.
If symptoms suggest emergency, clearly say urgent medical care is needed.
Do not diagnose.
""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

medical_knowledge_agent = ConversableAgent(
    name="Medical_Knowledge_Agent",
    system_message="""
You are a medical knowledge information agent.

Your job:
Give safe, general medical background related to the symptoms.

Rules:
1. Do not diagnose.
2. Do not prescribe medicines.
3. Do not give dosage.
4. Explain only common general possibilities.
5. Mention that symptoms can have many causes.
6. Keep the information simple and safe.
""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

health_guidance = ConversableAgent(
    name="Health_Guidance_Agent",
    system_message="""
You are a safe health guidance agent.
Give general self-care advice only.
Do not prescribe medicines.
Do not give dosage.
Do not diagnose.
Give safe self-care tips and when to consult a doctor.
""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

final_response_agent = ConversableAgent(
    name="Final_Response_Agent",
    system_message="""
You are the final medical response formatter.
Combine all agent outputs into one clear answer.

Rules:
1. Do not diagnose.
2. Do not prescribe medicines.
3. Include emergency warning if needed.
4. Include doctor consultation advice.
5. Include disclaimer.
6. Keep the final answer patient-friendly.
""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)