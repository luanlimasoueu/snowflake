import streamlit as st
import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd
from snowflake.snowpark import Session

connection_parameters = {
   "account": os.getenv('account_snow'),
   "user": os.getenv('user_snow'),
   "password":os.getenv('password_snow')
}

new_session = Session.builder.configs(connection_parameters).create()
print(new_session)
#new_session = new_session.sql("select * from SNOW1.SCHEMA1SNOW1.BUG_REPORT_DATA").collect()
#print(new_session)