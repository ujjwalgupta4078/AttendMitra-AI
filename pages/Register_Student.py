import streamlit as st

st.title("📝 Student Registration")

st.text_input("Student Name")

st.text_input("Roll Number")

st.text_input("Department")

st.file_uploader("Upload Student Photo")

if st.button("Register"):
    st.success("Registration Module Coming Soon.")