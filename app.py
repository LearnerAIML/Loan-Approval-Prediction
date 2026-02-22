import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load('loan_approval_model.pkl')

st.title("🏦 Loan Approval Predictor")
st.write("Fill in the details below to check loan approval status")

# Input fields
no_of_dependents = st.slider("Number of Dependents", 0, 10, 2)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
income_annum = st.number_input("Annual Income (₹)", min_value=0, value=500000)
loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=1000000)
loan_term = st.slider("Loan Term (months)", 2, 20, 12)
cibil_score = st.slider("CIBIL Score", 300, 900, 700)
residential_assets_value = st.number_input("Residential Assets Value (₹)", min_value=0, value=1000000)
commercial_assets_value = st.number_input("Commercial Assets Value (₹)", min_value=0, value=500000)
luxury_assets_value = st.number_input("Luxury Assets Value (₹)", min_value=0, value=300000)
bank_asset_value = st.number_input("Bank Asset Value (₹)", min_value=0, value=200000)

# Convert categorical inputs
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

if st.button("Predict Loan Status"):
    # Basic validation rules
    if income_annum <= 0:
        st.warning("⚠️ Annual income must be greater than 0!")
    elif loan_amount > income_annum * 20:
        st.warning("⚠️ Loan amount is too high compared to your income!")
    elif cibil_score < 300:
        st.warning("⚠️ CIBIL score is invalid!")
    else:
        input_data = pd.DataFrame([[no_of_dependents, education, self_employed,
                                    income_annum, loan_amount, loan_term, cibil_score,
                                    residential_assets_value, commercial_assets_value,
                                    luxury_assets_value, bank_asset_value]],
                                  columns=['no_of_dependents', 'education', 'self_employed',
                                           'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
                                           'residential_assets_value', 'commercial_assets_value',
                                           'luxury_assets_value', 'bank_asset_value'])
        
        result = model.predict(input_data)[0]
        
        if result == 1:
            st.success("✅ Loan Approved!")
        else:
            st.error("❌ Loan Rejected!")