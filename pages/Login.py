import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)

st.title("🔐 Login")

role = st.selectbox(
    "Select Role",
    [
        "Student",
        "Teacher",
        "Admin"
    ]
)

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

login = st.button("Login")