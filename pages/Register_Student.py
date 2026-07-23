import streamlit as st

from utils.validator import validate_student
from services.student_service import register_student

st.title("🎓 Student Registration")

with st.form("student_form"):

    name = st.text_input("Full Name")

    roll_no = st.text_input("Roll Number")

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

    if submit:

        valid, message = validate_student(
            name,
            roll_no,
            email,
            mobile
        )

        if not valid:

            st.error(message)

        else:

            student_data = {

                "name": name,

                "roll_no": roll_no,

                "email": email,

                "mobile": mobile,

                "department": department,

                "semester": semester

            }

            success, response = register_student(student_data)

            if success:

                st.success("✅ Student Registered Successfully!")

            else:

                st.error(response)