from typing import List, Dict

# Simulated drug interaction database
INTERACTIONS = {
    ("aspirin", "warfarin"): {
        "severity": "High",
        "risk": "Increased bleeding risk",
        "suggestion": "Use acetaminophen instead"
    },
    ("lipitor", "warfarin"): {
        "severity": "Moderate",
        "risk": "Increased INR",
        "suggestion": "Monitor INR levels"
    },
    ("metformin", "furosemide"): {
        "severity": "Moderate",
        "risk": "Risk of lactic acidosis",
        "suggestion": "Monitor kidney function"
    }
}

def check_interactions(data: Dict) -> List[Dict]:
    meds = [m.lower() for m in data.get("medications", [])]
    age = data.get("age", 40)
    conditions = [c.lower() for c in data.get("conditions", [])]

    results = []

    for i in range(len(meds)):
        for j in range(i + 1, len(meds)):
            pair = tuple(sorted((meds[i], meds[j])))
            if pair in INTERACTIONS:
                interaction = INTERACTIONS[pair].copy()
                interaction["interaction"] = list(pair)

                # Adjust severity if age is above 65
                if age > 65 and interaction["severity"] == "Moderate":
                    interaction["severity"] = "High"
                    interaction["risk"] += " (Elevated due to age)"

                # Adjust for medical conditions (example: stroke)
                if "stroke" in conditions and "bleeding" in interaction["risk"].lower():
                    interaction["severity"] = "High"
                    interaction["risk"] += " (Critical due to stroke history)"

                results.append(interaction)

    return results
