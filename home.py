import streamlit as st
from log_hash import hash_password, validate_hash
from app.users import add_user, get_user, ensure_user_table
from app.db import get_db_connection


st.set_page_config(page_title="Home Page", page_icon="🏠", layout="wide")

st.header("Home page")
st.write("Welcome to the home page of the application.")



if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False



conn = get_db_connection()
ensure_user_table(conn)


tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    login_name = st.text_input("Username", key="login_name")
    login_password = st.text_input("Password", type="password", key="login_password")
    if st.button("Log in"):
        user = get_user(conn, login_name)
        if user is None:
            st.error("User not found. Please register first.")
        else:
            _id, name, pw_hash = user
            if validate_hash(login_password, pw_hash):
                st.session_state['logged_in'] = True
                st.success("You are now logged in")
            else:
                st.error("Invalid credentials")

with tab_register:
    st.info("Registration")
    reg_name = st.text_input("Choose a username", key="reg_name")
    reg_password = st.text_input("Choose a password", type="password", key="reg_password")
    if st.button("Register"):
        if not reg_name or not reg_password:
            st.error("Please provide username and password")
        else:
            hashed_password = hash_password(reg_password)
            try:
                add_user(conn, reg_name, hashed_password)
                st.success("You have registered successfully. Go to the Login tab to log in.")
            except Exception as e:
                st.error(f"Registration failed: {e}")