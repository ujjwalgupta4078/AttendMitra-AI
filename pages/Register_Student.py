import streamlit as st

st.title("🎓 Student Registration")

with st.form("student_form"):

    name = st.text_input("Full Name")

    roll = st.text_input("Roll Number")

    email = st.text_input("Email")

    mobile = st.text_input("Mobile Number")

    department = st.selectbox(
        "Department",
        [
            "AIML",
            "CSE",
            "IT",
            "ECE",
            "ME",
            "Civil"
        ]
    )

    semester = st.selectbox(
        "Semester",
        [1,2,3,4,5,6,7,8]
    )

    photo = st.file_uploader(
        "Upload Photo",
        type=["jpg","jpeg","png"]
    )

    submit = st.form_submit_button("Register")