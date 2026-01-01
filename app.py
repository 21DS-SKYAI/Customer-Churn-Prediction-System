import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------
# Load trained model
# ---------------------------
model = joblib.load("model.joblib")

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered"
)

# ---------------------------
# UI Header
# ---------------------------
st.image("Customer_chur_banner.png", use_column_width=True)
st.title("📉 Customer Churn Prediction App")
st.markdown("Predict whether a customer is likely to churn using Machine Learning.")

# ---------------------------
# Sidebar Inputs
# ---------------------------
st.sidebar.header("Customer Details")

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges (₹)", 20, 150, 70)
total_charges = st.sidebar.slider("Total Charges (₹)", 0, 10000, 1000)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

tech_support = st.sidebar.selectbox(
    "Tech Support",
    ["No", "Yes"]
)

# ---------------------------
# Encode inputs (MATCH training)
# ---------------------------
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
tech_support_map = {"No": 0, "Yes": 1}

input_data = pd.DataFrame([{
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Contract": contract_map[contract],
    "InternetService": internet_map[internet_service],
    "TechSupport": tech_support_map[tech_support]
}])

# ---------------------------
# Prediction
# ---------------------------
if st.button("🔮 Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer is likely to CHURN\n\nRisk Score: **{probability:.2%}**")
    else:
        st.success(f"✅ Customer is NOT likely to churn\n\nRisk Score: **{probability:.2%}**")

st.markdown("---")
st.caption("Built using Machine Learning & Streamlit | 21DS_SkYAI")
