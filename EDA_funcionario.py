import streamlit as st
import pandas as pd
import base64

file = st.file_uploader("Choose a XLSX file", type="xlsx")

if file:
    df = pd.read_excel(file, sheet_name = 'bd')

    st.dataframe(df)
    st.table(df)