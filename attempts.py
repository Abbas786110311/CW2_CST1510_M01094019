import streamlit as st
import pandas as pd
from pathlib import Path
from app.datasets import get_all_datasets_metadata
from app.db import get_db_connection

conn = get_db_connection()

DATA_FILE = Path(__file__).parent / 'DATA' / 'datasets_metadata.csv'

if not DATA_FILE.exists():
    st.error(f"Data file not found: {DATA_FILE}")
    st.stop()

data = get_all_datasets_metadata(conn)


st.set_page_config(
    page_title="Data Explorer App",
    page_icon="*",
    layout="wide"
)

st.title("* Data Explorer App")

with st.sidebar:
    st.header("About")
    st.markdown(
        """
        
        """
    )

st.selectbox(
    "Select Dataset Category",
    options=data['dataset_id'].unique()
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Rows")
    st.bar_chart(data.set_index('name')['rows'])

with col2:
    st.subheader("Dataset Columns")
    st.bar_chart(data.set_index('name')['columns'])

with st.expander("Show raw data"):
    st.write(data)

