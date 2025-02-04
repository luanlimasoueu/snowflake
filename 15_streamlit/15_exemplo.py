import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from dotenv import load_dotenv
import streamlit as st
import os
import pandas as pd

load_dotenv()


connection_parameters = {
   "account": os.getenv('account_snow'),
   "user": os.getenv('user_snow'),
   "password":os.getenv('password_snow'),
   "role": "ACCOUNTADMIN",
   "database": "NEW_DB", 
   "schema": "PUBLIC"
  
}  

session = Session.builder.configs(connection_parameters).create()

employee_data = [
    [1,'TONY',101],
    [2,'STEVE',101],
    [3,'BRUCE',102],
    [4,'WANDA',102],
    [5,'VICTOR',103],
    [6,'HANK',105],
]

employee_schema = ["ID", "NAME", "DEPT_ID"]

df =session.createDataFrame(employee_data, schema=employee_schema)

df = df.to_pandas()
# Criar a interface no Streamlit
st.title("Exemplo com Streamlit e Snowflake")

# Obter os valores únicos da coluna
opcoes = df["NAME"].unique()

# Criar os botões dinamicamente com as opções do DataFrame
botao = st.radio("Escolha uma opção", opcoes)

# Exibir algo dependendo da opção escolhida
st.write(f"Você escolheu: {botao}")

# Fechar a sessão Snowflake
session.close()