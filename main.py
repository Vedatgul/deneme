# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

# Mission 1

# Q1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Rule Based Classification of Customer's Data", page_icon="🖖")
# st.title("Rule Based Classification of Customer's Data")
st.markdown("<h2 style='text-align: center; color: grey;'>Rule Based Classification of Customer's Data </h2>", unsafe_allow_html=True)
"""
This application is developed to find out Segment and Price of the New Customer' informations for the company.
This way, company can predict the income by new customers

To use the app you should choose at the following steps below:

    1- Country of the new customer,
    2- Operating system of the new customer,
    3- Gender 
    4- Age

After these choices this app will give the Segment and Price for the new user.

"""
st.subheader("Analysis of the variables")


# Mission 8

st.sidebar.header("New customer information:")
country = st.sidebar.selectbox("Country of new user: ", {"BRA", "TUR", "USA", "CAN", "DEU","FRA"})
phone_type = st.sidebar.selectbox("Operating System of new user: ", {"Android", "IOS"})
gender = st.sidebar.selectbox("Gender of new user: ", {"Female", "Male"})
age = st.sidebar.number_input("Age of new user",value=18, step=1)

input_dataframe = [[country, phone_type, gender, age]]
input_dataframe = pd.DataFrame(input_dataframe, columns = ["COUNTRY", "SOURCE", "SEX", "AGE"])

st.sidebar.markdown(("New Customer Definition:"))
new_user_3 = (country + "_"+ phone_type +"_"+ gender+ "_"+age_cat).upper()
price = new_df[new_df["customers_level_based"] == new_user_3].reset_index(drop=True)
st.sidebar.markdown(new_user_3)

st.info("New Customer ID: " + str(new_user_3))
st.success("Mean Price for New Customer: " + str(format(price["PRICE"][0], ".2f")) + "$")
st.success("Segment for New Customer: " + str(price["SEGMENT"][0]))

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
