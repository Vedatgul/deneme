import streamlit as st
from predict_page4 import show_predict_page
from explore_page2 import show_explore_page
from chat_page import show_chat_page

page = st.sidebar.selectbox("Explore Or Predict Or Chat", ("Predict", "Explore", "Chat"))

if page == "Predict":
    show_predict_page()
elif page == "Chat":
    show_chat_page()
else:
    show_explore_page()