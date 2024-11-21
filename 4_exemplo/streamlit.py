import streamlit as st
import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    account=os.getenv('account_snow'), 
    user= os.getenv('user_snow'), 
    password = os.getenv('password_snow')
)

sql_query = pd.read_sql_query(
    """
    SELECT
    *
    FROM products
    """,
    conn,
)

df = pd.DataFrame(sql_query)

st.dataframe(df)