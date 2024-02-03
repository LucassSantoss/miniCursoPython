import streamlit as st
import pandas as pd
import plotly.express as px

print("Iniciando Programa...")
st.title("Capacidade das escolas")
st.text("Prefeitura de Bauru")

caminhoDoArquivo = r"C:\Programacao\EngSoft\3oSemestre\cursoPython\dados\capacidade_das_escolas.csv"
df = pd.read_csv(caminhoDoArquivo, sep=';', encoding="utf-8")
st.table(df)

eixoX = df['Unidade'].nunique()
eixoY = df['Capacidade'].sum()

fig = px.bar(df, x='Unidade', y='Capacidade')
st.plotly_chart(fig)