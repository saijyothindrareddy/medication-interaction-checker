import streamlit as st
import requests

st.set_page_config(page_title="Medication Interaction Checker", layout="centered")

st.title("💊 Medication Interaction Checker")
st.markdown("Check for possible drug interactions with patient-specific info.")

with st.form("interaction_form"):
    meds = st.text_area("Enter medications (comma separated)", "Aspirin, Warfarin, Lipitor")
    age = st.number_input("Patient Age", min_value=0, max_value=120, value=60)
    weight = st.number_input("Patient Weight (kg)", min_value=1, max_value=300, value=65)
    conditions = st.text_input("Pre-existing Conditions (comma separated)", "stroke")

    submitted = st.form_submit_button("Check Interactions")

if submitted:
    # 🔄 Process inputs
    med_list = [m.strip() for m in meds.split(",")]
    cond_list = [c.strip() for c in conditions.split(",")]

    payload = {
        "medications": med_list,
        "age": age,
        "weight": weight,
        "conditions": cond_list
    }

    # 📡 Send request to FastAPI backend
    try:
        response = requests.post("http://localhost:8000/check", json=payload)
        if response.status_code == 200:
            interactions = response.json()
            if interactions:
                st.subheader("🚨 Interactions Found")
                for item in interactions:
                    st.error(f"""
**Drugs**: {', '.join(item['interaction'])}  
**Severity**: `{item['severity']}`  
**Risk**: {item['risk']}  
**Suggestion**: {item['suggestion']}
""")
            else:
                st.success("✅ No significant interactions found!")
        else:
            st.warning(f"Server error: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Could not connect to backend.\n\n{e}")
