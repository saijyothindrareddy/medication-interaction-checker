known_interactions = {
    ("aspirin", "warfarin"): {
        "severity": "High",
        "risk": "Increased bleeding risk",
        "suggestion": "Use acetaminophen instead"
    },
    ("lipitor", "warfarin"): {
        "severity": "Moderate",
        "risk": "INR may increase",
        "suggestion": "Monitor INR"
    }
}

def get_interactions(meds):
    results = []
    for i in range(len(meds)):
        for j in range(i+1, len(meds)):
            pair = tuple(sorted((meds[i], meds[j])))
            if pair in known_interactions:
                results.append({"pair": pair, **known_interactions[pair]})
    return results
