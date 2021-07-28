from numpy.lib.function_base import _median_dispatcher
import pandas as pd
import streamlit as st
from datetime import datetime
# nome da aplciação
st.write(
    """
    **Ações WEB App
    """
)
# criar sidebar
st.sidebar.header('Escolha dua Ação: ')

# Ler arquivo de ações:
def get_data():
    path = 'C:\Users\mawri\Downloads\COTAHIST_A2020.TXT'
    return pd.read_csv(path)

df = get_data()

df_data = pd.to_datetime(df['data_pregao'].dt.date.drop_duplicaes())

min_date = min(df_data)
max_date = max(df_data)
stock = df['sigla_acao'].drop_duplicates()
stock_choices = st.didebar.selectbox("Escolha uma ação", stock)