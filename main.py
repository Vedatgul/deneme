# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

# Mission 1
import streamlit as st
st.title('hello')
st.sidebar.header("New user information:")
st.sidebar.radio('Gender of new user:', options=['Female', 'Male'],  horizontal=True)

Pregnancies = st.sidebar.number_input("Pregnanciesof",value=17, step=1)
Glucose = st.sidebar.number_input("Glucose",value=199, step=0)
BloodPressure = st.sidebar.number_input("BloodPressure",value=122, step=0)
SkinThickness = st.sidebar.number_input("SkinThickness",value=99, step=0)
Insulin = st.sidebar.number_input("Insulin",value=846, step=0)
BMI = st.sidebar.number_input("BMI",value=67, step=0)
DiabetesPedigreeFunction = st.sidebar.number_input("DiabetesPedigreeFunction",value=2, step=0) 
Age = st.sidebar.number_input("Age",value=67.1, step=0)

st.set_page_config(layout="wide")






