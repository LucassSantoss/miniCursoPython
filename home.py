import streamlit as st
import pandas as pd

st.text("Hello World")
print("Hello World")

caminhoDoArquivo = r"C:\Programacao\EngSoft\3oSemestre\cursoPython\dados\capacidade_das_escolas.csv"
df = pd.read_csv(caminhoDoArquivo)
st.table(df)
