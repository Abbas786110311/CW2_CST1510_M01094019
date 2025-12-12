import streamlit as st
from app.incidents import migrating_cyber_incidents
from app.db import get_db_connection
import pandas as pd
import os
from openai import OpenAI
from app.env_loader import load_env

load_env()


with st.sidebar:
    st.subheader("I am AI ")
    user_msg = st.text_input("I will assist you if you want help:")
    if st.button("Send") and user_msg:
        with st.spinner("generating response..."):
            api_key = os.getenv("OPEN_AI_KEY")
            if not api_key:
                st.error("OpenAI API key not found in .env file")
            else:
                try:
                    api_key = api_key.strip()
                    client = OpenAI(api_key=api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": user_msg}]
                    )
                    st.success(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"OpenAI Error: {str(e)}")

st.header("cyber incidents dashboard")
st.write("welcome to the home page of the application.")

# Initialize session state key if missing so page can be opened directly
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


conn = get_db_connection() 
data = migrating_cyber_incidents(conn)  

st.set_page_config(
    page_title="Home Page",
    page_icon="🏠",
    layout="wide"
)

if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()



conn = get_db_connection()
data = migrating_cyber_incidents(conn) 


with st.sidebar:

    st.header("Cyber severity Overview")
    severity_ = st.selectbox('severity', data['severity'].unique())


filtered_data = data[data['severity'] == severity_]

col1, col2 = st.columns(2)

with col1:
    st.subheader("number of categories")
    st.bar_chart(filtered_data['category'].value_counts())

with col2:
    st.subheader("filtered cyber incidents data")
    st.line_chart(filtered_data, x= 'timestamp', y='incident_id')
    st.bar_chart(filtered_data['incident_id'].value_counts())


st.dataframe(filtered_data)
