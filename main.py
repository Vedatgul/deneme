# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

# Mission 1
import streamlit as st
st.title('hello')
st.sidebar.header("New customer information:")
country = st.sidebar.selectbox("Country of new user: ", {"BRA", "TUR", "USA", "CAN", "DEU","FRA"})
phone_type = st.sidebar.selectbox("Operating System of new user: ", {"Android", "IOS"})
gender = st.sidebar.selectbox("Gender of new user: ", {"Female", "Male"})
age = st.sidebar.number_input("Age of new user",value=18, step=1)

