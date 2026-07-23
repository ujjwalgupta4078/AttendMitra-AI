import streamlit as st

st.title("👨‍🏫 Teacher Login")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Login"):
    st.success("Teacher Login Coming Soon.")