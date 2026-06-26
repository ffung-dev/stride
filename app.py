import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="STRIDE",
    page_icon="🩺",
    layout="centered"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
            
.stButton > button {
    border-radius: 4px !important;
    height: 3rem;
    font-weight: 600;
}
            
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

.card {
    background-color: white;
    padding: 1.2rem;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    margin-bottom: 1rem;
}

.risk-title {
    font-size: 2rem;
    font-weight: 700;
}

.small-text {
    color: #6B7280;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# load models
lr_model = joblib.load("models/logreg_model.joblib")
rf_model = joblib.load("models/rf_model.joblib")

# app 
st.markdown("""
<h1>STRIDE</h1>
<p class='small-text'>
Type 2 Diabetes Risk Assessment Tool
</p>
""", unsafe_allow_html=True)
st.subheader("Patient Information")

# get patient info
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0.0, step=1.0)
    bmi = st.number_input("BMI", min_value=0.0, step=1.0)
with col2: 
    hypertension = st.radio("Hypertension", ["Yes", "No"])
    glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=0.0, step=1.0)
    hba1c = st.number_input("HbA1c Level (%)", min_value=0.0, step=0.01)

with st.expander("Clinical Reference Ranges"):

    st.markdown("""
    **HbA1c Level**
    - Normal: < 5.7%
    - Prediabetes: 5.7–6.4%
    - Diabetes: ≥ 6.5%

    **BMI**
    - Healthy: 18.5–24.9
    - Overweight: 25–29.9
    - Obese: ≥ 30
    """)

# gender and hypertension to num
gender_val = 1 if gender == "Female" else 0
hypertension_val = 1 if hypertension == "Yes" else 0

def assign_risk(prob):
    if prob < 0.2:
        return "Low"
    elif prob < 0.5:
        return "Medium"
    elif prob < 0.7:
        return "High"
    else:
        return "Very High"

# stylize
def color_risk(risk):
    if risk == "Low":
        return "#317628"
    elif risk == "Medium":
        return "#CFBD18"
    elif risk == "High":
        return "#EE8F37"
    else:
        return "#72130D"
 
if st.button("Predict Risk"):
    # input DataFrame 
    input_data = pd.DataFrame([{
        'gender': gender_val,
        'age': age,
        'bmi': bmi,
        'blood_glucose_level': glucose,
        'hypertension': hypertension_val,
        'hbA1c_level': hba1c
    }])

    # Logistic Regression
    prob_log = lr_model.predict_proba(input_data)[:,1][0]
    risk_log = assign_risk(prob_log)

    # Random Forest
    prob_rf = rf_model.predict_proba(input_data)[:,1][0]
    risk_rf = assign_risk(prob_rf)

    # display results
    st.subheader("Results")

    st.markdown(f"""
    <div style="padding:15px; border-radius:10px; background-color:#1E293B;">
    <b>Logistic Regression</b><br>
    Probability: {prob_log:.2f}<br>
    <span style="color:{color_risk(risk_log)}; font-weight:600;">
    Risk Level: {risk_log}
    </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="padding:15px; border-radius:10px; background-color:#1E293B; margin-top:10px;">
    <b>Random Forest</b><br>
    Probability: {prob_rf:.2f}<br>
    <span style="color:{color_risk(risk_rf)}; font-weight:600;">
    Risk Level: {risk_rf}
    </span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<p style="font-size:13px; color:#6B7280; text-align:center">
Developed for WUHC '26, AI/ML. <br>
EDIFICIENT: Fiona F. and Kevin L.<br>
<a href="https://docs.google.com/document/d/14f32zCMk3zQ0UXC47A2HAiY8emfwXXBnlXtwO9ZE1hM/edit?usp=sharing" target="_blank">View Full Research Paper</a><br>
<a href="https://github.com/ffung-dev/t2d-risk-predictor" target="_blank">GitHub Repository</a><br>
This tool is intended for educational purposes only and is not a medical diagnostic device.
</p>
""", unsafe_allow_html=True)