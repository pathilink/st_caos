import streamlit as st
import pandas as pd
from pathlib import Path
#import base64

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.title("Engajamento")
st.subheader("Análise Exploratória de Dados")

file = st.file_uploader("Choose a XLSX file", type="xlsx")

if file:
    df = pd.read_excel(file, sheet_name = 'bd')
    st.markdown('**Número de linhas:**')
    st.markdown(df.shape[0])
    st.markdown('**Número de colunas:**')
    st.markdown(df.shape[1])
    intro_markdown = read_markdown_file("variaveis.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    st.markdown('**Dataframe:**')
    number = st.slider('Escolha o número de linhas para ver:', min_value=1, max_value=20)
    st.dataframe(df.head(number))

    #st.table(df)