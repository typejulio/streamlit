import streamlit as st
import pandas as pd
import requests as req

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
cotacoes = req.get(link).json()

# criando um DataFrame com os dados da API
data = []
for key, value in cotacoes.items():
    data.append(value)
df = pd.DataFrame(data)

# exibindo o DataFrame como uma tabela usando o Streamlit
st.write("Tabela de Cotações:", df)

st.table(df)

st.dataframe(df)

st.line_chart(df)
