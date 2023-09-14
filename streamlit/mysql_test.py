import pandas as pd
import streamlit as st

# conn = st.experimental_connection('mysql', type='sql')

# # Perform query.
# df = conn.query('SELECT * FROM PO_LINE;', ttl=600)

st.title('MySQL Streamlit App Test') 

st.write('not exactly sure what is going on here')

st.write(df.shape)
