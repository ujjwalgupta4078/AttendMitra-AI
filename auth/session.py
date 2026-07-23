import streamlit as st

def login_user(role, email):

    st.session_state["logged_in"] = True

    st.session_state["role"] = role

    st.session_state["email"] = email


def logout_user():

    st.session_state.clear()