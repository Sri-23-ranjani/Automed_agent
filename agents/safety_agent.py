def safety_agent(symptoms):
    emergency_keywords = [
        "chest pain",
        "difficulty breathing",
        "shortness of breath",
        "severe bleeding",
        "unconscious",
        "seizure",
        "stroke",
        "suicide",
        "severe allergic reaction"
    ]

    for keyword in emergency_keywords:
        if keyword in symptoms.lower():
            return True

    return False