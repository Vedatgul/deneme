# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

# Mission 1
import streamlit as st  
st.set_page_config(page_title="Diabetes Prediction App")

st.title('Diabetes Prediction')
st.sidebar.header("New user information:")
st.sidebar.radio('Gender of new user:', options=['Female', 'Male'],  horizontal=True)
Pregnancies = st.sidebar.number_input("Pregnancies",value=17, step=1)
age = st.slider('How old are you?', 0, 90, 25)
Glucose = st.slider('Glucose', 0, 199, 50)
BloodPressure = st.slider('BloodPressure', 0, 122, 45)
DiabetesPedigreeFunction = st.slider('DiabetesPedigreeFunction', 0, 122, 45) 
SkinThickness = st.sidebar.number_input("SkinThickness",value=99, step=0)
Insulin = st.sidebar.number_input("Insulin",value=846, step=0)
BMI = st.sidebar.number_input("BMI",value=67, step=0)

