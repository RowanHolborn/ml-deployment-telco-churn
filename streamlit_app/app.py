from config.settings import config
import streamlit as st
import requests


# ---------------------------
# Churn Prediction Function
# ---------------------------
def predict_churn(input_data: dict) -> dict:
    try:
        response = requests.post(config.api_url, json=input_data)
        if response.status_code == 200:
            return {"success": True, "result": response.json()}
        else:
            return {"success": False, "error": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}


# ---------------------------
# Streamlit App Interface
# ---------------------------
st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("📉 Customer Churn Predictor")

with st.form("prediction_form"):
    st.subheader("Customer Profile")

    # Default values aligned to the JSON sample
    tenure = st.slider("Tenure (months)", 0, 72, value=12)
    monthly_charges = st.number_input("Monthly Charges", min_value=10.0, max_value=150.0, value=75.5)
    total_charges = st.number_input("Total Charges", min_value=10.0, max_value=8000.0, value=906.0)

    gender = st.selectbox("Gender", ["Male", "Female"], index=0)
    senior = st.checkbox("Senior Citizen", value=False)
    partner = st.checkbox("Has Partner", value=True)
    dependents = st.checkbox("Has Dependents", value=False)
    phone_service = st.checkbox("Phone Service", value=True)

    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"], index=1)
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], index=1)
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"], index=0)
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"], index=2)
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"], index=0)
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"], index=1)
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"], index=1)
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"], index=0)

    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"], index=0)
    paperless_billing = st.checkbox("Uses Paperless Billing", value=True)
    payment_method = st.selectbox("Payment Method", [
        "Bank transfer (automatic)", "Credit card (automatic)",
        "Electronic check", "Mailed check"
    ], index=2)

    submitted = st.form_submit_button("Predict")

# ---------------------------
# Make Prediction
# ---------------------------
if submitted:
    # Build one-hot encoded request
    input_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "gender_Male": 1 if gender == "Male" else 0,
        "SeniorCitizen_1": int(senior),
        "Partner_Yes": int(partner),
        "Dependents_Yes": int(dependents),
        "PhoneService_Yes": int(phone_service),

        "MultipleLines_No": int(multiple_lines == "No"),
        "MultipleLines_No phone service": int(multiple_lines == "No phone service"),
        "MultipleLines_Yes": int(multiple_lines == "Yes"),

        "InternetService_DSL": int(internet_service == "DSL"),
        "InternetService_Fiber optic": int(internet_service == "Fiber optic"),
        "InternetService_No": int(internet_service == "No"),

        "OnlineSecurity_No": int(online_security == "No"),
        "OnlineSecurity_No internet service": int(online_security == "No internet service"),
        "OnlineSecurity_Yes": int(online_security == "Yes"),

        "OnlineBackup_No": int(online_backup == "No"),
        "OnlineBackup_No internet service": int(online_backup == "No internet service"),
        "OnlineBackup_Yes": int(online_backup == "Yes"),

        "DeviceProtection_No": int(device_protection == "No"),
        "DeviceProtection_No internet service": int(device_protection == "No internet service"),
        "DeviceProtection_Yes": int(device_protection == "Yes"),

        "TechSupport_No": int(tech_support == "No"),
        "TechSupport_No internet service": int(tech_support == "No internet service"),
        "TechSupport_Yes": int(tech_support == "Yes"),

        "StreamingTV_No": int(streaming_tv == "No"),
        "StreamingTV_No internet service": int(streaming_tv == "No internet service"),
        "StreamingTV_Yes": int(streaming_tv == "Yes"),

        "StreamingMovies_No": int(streaming_movies == "No"),
        "StreamingMovies_No internet service": int(streaming_movies == "No internet service"),
        "StreamingMovies_Yes": int(streaming_movies == "Yes"),

        "Contract_Month-to-month": int(contract == "Month-to-month"),
        "Contract_One year": int(contract == "One year"),
        "Contract_Two year": int(contract == "Two year"),

        "PaperlessBilling_Yes": int(paperless_billing),

        "PaymentMethod_Bank transfer (automatic)": int(payment_method == "Bank transfer (automatic)"),
        "PaymentMethod_Credit card (automatic)": int(payment_method == "Credit card (automatic)"),
        "PaymentMethod_Electronic check": int(payment_method == "Electronic check"),
        "PaymentMethod_Mailed check": int(payment_method == "Mailed check"),
    }

    # API call
    result = predict_churn(input_data)

    if result["success"]:
        churn = result["result"]["churn_prediction"]
        churn_message = f"🔎 Prediction: {'Will Churn' if churn == 1 else 'Will Not Churn'}"
        if churn == 1:
            st.warning(churn_message)
        else:
            st.success(churn_message)
    else:
        st.error(f"❌ Error: {result['error']}")
