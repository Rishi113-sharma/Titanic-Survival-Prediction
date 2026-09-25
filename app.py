import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Logistic Regression.pkl")
scaler = joblib.load("scalar.pkl")
columns = joblib.load("columns.pkl")

st.title("Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class", [1, 2, 3])

sex = st.selectbox("Sex", ["Male", "Female"])

age = st.number_input("Age", min_value=0, max_value=100, value=30)

sibsp = st.number_input("Siblings / Spouses", min_value=0, max_value=10, value=0)

parch = st.number_input("Parents / Children", min_value=0, max_value=10, value=0)

fare = st.number_input("Fare", min_value=0.0, value=30.0)

embarked = st.selectbox("Embarked", ["C", "Q", "S"])

alone = st.selectbox("Travelling Alone", ["No", "Yes"])

if sex == "Male":
    sex = 1
else:
    sex = 0

if embarked == "C":
    embarked = 0
elif embarked == "Q":
    embarked = 1
else:
    embarked = 2

if alone == "Yes":
    alone = 1
else:
    alone = 0

if st.button("Predict"):

    input_data = pd.DataFrame([[
        pclass,
        sex,
        age,
        sibsp,
        parch,
        fare,
        embarked,
        alone
    ]], columns=columns)

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("Passenger is predicted to SURVIVE")
    else:
        st.error("Passenger is predicted NOT to survive")