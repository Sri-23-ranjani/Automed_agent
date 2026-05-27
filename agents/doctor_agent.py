def recommend_doctor_agent(symptoms):
    symptoms = symptoms.lower()

    if any(word in symptoms for word in ["fever", "cold", "cough", "headache", "body pain"]):
        specialist = "General Physician"

    elif any(word in symptoms for word in ["chest pain", "heart", "palpitation"]):
        specialist = "Cardiologist"

    elif any(word in symptoms for word in ["skin", "rash", "itching", "allergy"]):
        specialist = "Dermatologist"

    elif any(word in symptoms for word in ["stomach", "vomiting", "diarrhea", "digestion"]):
        specialist = "Gastroenterologist"

    elif any(word in symptoms for word in ["eye", "vision", "blurred"]):
        specialist = "Ophthalmologist"

    elif any(word in symptoms for word in ["ear", "nose", "throat", "sinus"]):
        specialist = "ENT Specialist"

    elif any(word in symptoms for word in ["bone", "joint", "fracture", "back pain"]):
        specialist = "Orthopedic Doctor"

    elif any(word in symptoms for word in ["anxiety", "depression", "stress", "sleep"]):
        specialist = "Psychiatrist / Mental Health Professional"

    else:
        specialist = "General Physician"

    return f"""
Doctor Recommendation Agent:

Suggested specialist:
{specialist}

Reason:
Based on the symptoms entered, this specialist may be suitable for further consultation.

Note:
This is only a general recommendation. Please consult a hospital or qualified healthcare provider.
"""