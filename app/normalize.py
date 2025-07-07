def normalize_medications(med_list):
    # Fuzzy match or lookup dictionary
    mapping = {
        "lipitor": "atorvastatin",
        "panadol": "acetaminophen",
        "aspirin": "aspirin",
        "warfarin": "warfarin"
    }
    return [mapping.get(m.lower(), m.lower()) for m in med_list]
