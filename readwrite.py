import streamlit as st
import pandas as pd
from google.oauth2.service_account import Credentials
from gspread_pandas import Spread, Client
import numpy as np

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file('./ecmganalystdashboard-151feef86862.json', scopes=scope)


client = Client(scope=scope, creds=credentials)
spread = Spread("ReadWrite", client=client)

stock_df = pd.DataFrame(np.array([[1, 2, 2], [4, 5, 6], [7, 8, 9]]), columns=['a', 'z', 'on'])

spread.df_to_sheet(stock_df)

stock_df = spread.sheet_to_df()

st.write(stock_df)