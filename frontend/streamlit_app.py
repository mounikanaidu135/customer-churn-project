import streamlit as st
import requests

st.title("Customer Churn Prediction")

tenure = st.number_input("Customer Tenure (months)")
monthly = st.number_input("Monthly Charges")

if st.button("Predict"):

    response = requests.post(
        "http://localhost:5000/predict",
        json={
            "tenure":tenure,
            "monthly":monthly
        }
    )

    result = response.json()

    st.success(result["prediction"])