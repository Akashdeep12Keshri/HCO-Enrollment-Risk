import streamlit as st
import pandas as pd
import pickle

# Load model
with open("enrollment_risk_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="HCO Enrollment Risk Predictor")

st.title("Health & Welfare Enrollment Risk Prediction")

st.markdown("""
This tool helps HCO operations teams identify employees at high risk
of missing benefit enrollment and take proactive action.
""")

# Input fields
age = st.slider("Age", 18, 65, 30)
monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
years_at_company = st.slider("Years at Company", 0, 40, 2)
work_life_balance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
overtime = st.selectbox("Overtime", ["Yes", "No"])

# Feature engineering
engagement_score = work_life_balance + job_satisfaction
overtime_flag = 1 if overtime == "Yes" else 0

income_band = 0
if monthly_income < 4000:
    income_band = 0
elif monthly_income <= 8000:
    income_band = 1
else:
    income_band = 2

tenure_bucket = 0
if years_at_company < 1:
    tenure_bucket = 0
elif years_at_company <= 5:
    tenure_bucket = 1
else:
    tenure_bucket = 2

input_df = pd.DataFrame([[
    age, monthly_income, job_level, years_at_company,
    work_life_balance, job_satisfaction,
    engagement_score, overtime_flag,
    income_band, tenure_bucket
]], columns=[
    "Age", "MonthlyIncome", "JobLevel", "YearsAtCompany",
    "WorkLifeBalance", "JobSatisfaction",
    "Engagement_Score", "Overtime_Flag",
    "Income_Band", "Tenure_Bucket"
])

if st.button("Predict Enrollment Risk"):
    prob = model.predict_proba(input_df)[0][1]
    st.metric("High Enrollment Risk Probability", f"{prob:.2%}")

    if prob > 0.6:
        st.error("High Risk – Proactive Outreach Recommended")
    else:
        st.success("Low Risk – No Immediate Action Needed")