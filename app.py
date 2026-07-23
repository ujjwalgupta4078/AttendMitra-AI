import streamlit as st

st.set_page_config(
    page_title="AttendMitra AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AttendMitra AI")

st.subheader("AI Powered Attendance Management System")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_Student_Login.py", label="👨‍🎓 Student Login")

with col2:
    st.page_link("pages/2_Teacher_Login.py", label="👨‍🏫 Teacher Login")

with col3:
    st.page_link("pages/3_Admin_Login.py", label="👨‍💼 Admin Login")

st.divider()

st.header("🚀 Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("📸 Face Recognition")

with c2:
    st.info("🎤 Voice Recognition")

with c3:
    st.info("☁️ Cloud Database")

c4, c5, c6 = st.columns(3)

with c4:
    st.success("📊 Attendance Reports")

with c5:
    st.success("🤖 AI Verification")

with c6:
    st.success("🔒 Secure Login")

st.divider()

st.header("Why AttendMitra AI?")

st.write("""
✅ Fast Attendance

✅ AI Powered

✅ Cloud Based

✅ Secure

✅ Easy to Use
""")

st.divider()

st.caption("Made by Ujjwal Gupta")