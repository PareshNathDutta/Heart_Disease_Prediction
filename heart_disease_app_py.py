# -*- coding: utf-8 -*-
"""heart_disease_app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12SCS6FFOYRGd1jch4_0p0-2rgy3nUvFO
"""

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

# Title
st.title('Heart Disease Prediction App')

# User input
age = st.slider('Age', 20, 80, 30)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type (0-3)', [0,1,2,3])
trestbps = st.number_input('Resting Blood Pressure', 80, 200, 120)
chol = st.number_input('Cholesterol', 100, 400, 200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0,1])
restecg = st.selectbox('Resting ECG (0-2)', [0,1,2])
thalach = st.number_input('Max Heart Rate Achieved', 60, 220, 150)
exang = st.selectbox('Exercise Induced Angina', [0,1])
oldpeak = st.number_input('Oldpeak', 0.0, 6.0, 1.0)
slope = st.selectbox('Slope (0-2)', [0,1,2])
ca = st.selectbox('Number of major vessels (0-3)', [0,1,2,3])
thal = st.selectbox('Thal (0 = normal; 1 = fixed defect; 2 = reversable defect)', [0,1,2])

# Prepare data for prediction
input_data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == 'Male' else 0],
    'cp': [cp],
    'trestbps': [trestbps],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [restecg],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal]
})

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error('You may be at risk of heart disease. Please consult a doctor.')
    else:
        st.success('You are unlikely to have heart disease.')