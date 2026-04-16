import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("ann_model.h5")

st.title("🏦 Bank Churn Prediction")

# Inputs
credit_score = st.number_input("Credit Score")
age = st.number_input("Age")
balance = st.number_input("Balance")
salary = st.number_input("Estimated Salary")
# Prediction
if st.button("Predict"):
    data = np.array([[credit_score, age, balance, salary]])
    prediction = model.predict(data)

    if prediction[0][0] > 0.5:
        st.error("Customer will churn ")
    else:
        st.success("Customer will stay ")
