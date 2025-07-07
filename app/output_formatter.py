def format_alerts(interactions):
    formatted = []
    for item in interactions:
        formatted.append({
            "interaction": list(item["pair"]),
            "severity": item["severity"],
            "risk": item["risk"],
            "suggestion": item["suggestion"]
        })
    return formatted
