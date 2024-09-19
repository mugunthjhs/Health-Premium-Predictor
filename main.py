import streamlit as st
from prediction_helper import predict

# Define the title of the application
st.title("Health Premium Predictor")

# Add some custom styling
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px;
        border: none;
    }
    .stSelectbox>div, .stNumberInput>div>input {
        color: #333;
    }
    .stMarkdown {
        margin-bottom: 20px;
    }
    .error {
        color: red;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Layout with three items per row
row1_col1, row1_col2, row1_col3 = st.columns(3)
row2_col1, row2_col2, row2_col3 = st.columns(3)
row3_col1, row3_col2, row3_col3 = st.columns(3)

with row1_col1:
    # Age (number input)
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    
with row1_col2:
    # Gender dropdown
    gender = st.selectbox("Gender", ['Male', 'Female'], index=0)
    
with row1_col3:
    # BMI (number input)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0,step=1.0)

with row2_col1:
    # BMI Category dropdown
    bmi_category = st.selectbox("BMI Category", ['Overweight', 'Underweight', 'Normal', 'Obesity'], index=0)
    
with row2_col2:
    # Marital status dropdown
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'], index=0)
    
with row2_col3:
    # Region dropdown
    region = st.selectbox("Region", ['Northeast', 'Northwest', 'Southeast', 'Southwest'], index=0)

with row3_col1:
    # Smoking status dropdown
    smoking_status = st.selectbox("Smoking Status", ['Regular', 'Occasional', 'Not Smoking'], index=0)
    
with row3_col2:
    # Employment status dropdown
    employment_status = st.selectbox("Employment Status", ['Self-Employed', 'Freelancer', 'Salaried'], index=0)
    
with row3_col3:
    # Income level dropdown
    income_level = st.selectbox("Income Level", ['> 40L', '<10L', '10L - 25L', '25L - 40L'], index=0)

with row1_col1:
    # Number of dependents (numeric input)
    num_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)

with row1_col2:
    # Income (Lakhs) (numeric input)
    income_lakhs = st.number_input("Income (Lakhs)", min_value=0.0, max_value=100.0, value=5.0,step=1.0)

with row1_col3:
    # Genetic risk dropdown
    genetic_risk = st.number_input("Genetical Risk", min_value=0, max_value=5, value=0)

with row2_col1:
    # Medical history dropdown
    medical_history = st.selectbox("Medical History", [
        'High blood pressure', 'No Disease', 'Diabetes & High blood pressure',
        'Diabetes & Heart disease', 'Diabetes', 'Diabetes & Thyroid',
        'Heart disease', 'Thyroid', 'High blood pressure & Heart disease'
    ], index=0)
    
with row2_col2:
    # Insurance plan dropdown
    insurance_plan = st.selectbox("Insurance Plan", [ 'Bronze','Silver', 'Gold'], index=0)

with row2_col3:
    # Annual premium amount (numeric input)
    annual_premium_amount = st.number_input("Annual Premium Amount", min_value=0, max_value=1000000, value=10000,step=100)

input_data = {
    "Age": age,
    "Gender": gender,
    "BMI": bmi,
    "BMI Category": bmi_category,
    "Marital Status": marital_status,
    "Region": region,
    "Smoking Status": smoking_status,
    "Employment Status": employment_status,
    "Income Level": income_level,
    "Number of Dependents": num_dependents,
    "Income (Lakhs)": income_lakhs,
    "Genetical Risk": genetic_risk,
    "Medical History": medical_history,
    "Insurance Plan": insurance_plan,
    "Annual Premium Amount": annual_premium_amount
}

if st.button("Predict"):
    prediction = predict(input_data)
    st.success(f"Predicted Premium :{prediction}")