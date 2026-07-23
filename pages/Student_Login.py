import streamlit as st

st.title("👨‍🎓 Student Login")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Login"):
    st.success("Login functionality will be added in Module 4.")