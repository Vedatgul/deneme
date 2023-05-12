# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

# Mission 1
import streamlit as st
left, right = st.columns(2)   
with left:     
  st.title('Diabetes Prediction')

st.sidebar.header("New user information:")
st.sidebar.radio('Gender of new user:', options=['Female', 'Male'],  horizontal=True)
Pregnancies = st.number_input("Pregnancies",value=17, step=1)
age = st.slider('How old are you?', 0, 90, 25)
Glucose = st.slider('Glucose', 0, 199, 50)
BloodPressure = st.slider('BloodPressure', 0, 122, 45)
DiabetesPedigreeFunction = st.slider('DiabetesPedigreeFunction', 0, 122, 45)
with right:     
SkinThickness = st.number_input("SkinThickness",value=99, step=0)
Insulin = st.number_input("Insulin",value=846, step=0)
BMI = st.number_input("BMI",value=67, step=0)
st.set_page_config(layout="wide")



