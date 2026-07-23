import streamlit as st

st.title("👨‍💼 Admin Login")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Login"):
    st.success("Admin Login Coming Soon.")