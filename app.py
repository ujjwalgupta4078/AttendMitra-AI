import streamlit as st

st.set_page_config(
    page_title="AttendMitra AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎓 AttendMitra AI")

st.markdown("## AI Powered Attendance Management System")

st.divider()

st.write("""
Welcome to **AttendMitra AI**.

This application will provide:

- 📸 Face Recognition Attendance
- 🎤 Voice Recognition Attendance
- 👨‍🎓 Student Login
- 👨‍🏫 Teacher Login
- 👨‍💼 Admin Panel
- ☁️ Supabase Cloud Database
- 📊 Attendance Reports
- 🤖 AI Verification
""")

st.success("Module 2 Started Successfully 🚀")