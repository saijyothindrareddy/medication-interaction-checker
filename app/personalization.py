def personalize_risk(interactions, patient_data):
    # Example: Increase severity for elderly
    age = patient_data.get("age", 50)
    for inter in interactions:
        if age > 70 and inter["severity"] == "Moderate":
            inter["severity"] = "High"
            inter["risk"] += " (elevated for elderly)"
    return interactions
