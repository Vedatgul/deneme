# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

# Mission 1
import streamlit as st
st.title('hello')

st.sidebar.header("New user information:")
st.sidebar.radio('Gender of new user:', options=['Female', 'Male'],  horizontal=True)
Pregnancies = st.sidebar.number_input("Pregnanciesof",value=17, step=1)
age = st.slider('How old are you?', 0, 90, 25)
Glucose = st.slider('Glucose', 0, 199, 50)
BloodPressure = st.slider('BloodPressure', 0, 122, 45)
DiabetesPedigreeFunction = st.slider('DiabetesPedigreeFunction', 0, 122, 45)
SkinThickness = st.sidebar.number_input("SkinThickness",value=99, step=0)
Insulin = st.sidebar.number_input("Insulin",value=846, step=0)
BMI = st.sidebar.number_input("BMI",value=67, step=0)



