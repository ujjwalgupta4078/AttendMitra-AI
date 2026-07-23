import streamlit as st

st.title("📊 Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Students", "0")

col2.metric("Teachers", "0")

col3.metric("Attendance", "0%")