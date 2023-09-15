import pandas as pd
import streamlit as st

# read credentials
toml_data = toml.load("secrets.toml")

# assign each credential to a variable
HOST_NAME = toml_data['mysql']['host']
DATABASE = toml_data['mysql']['database']
PASSWORD = toml_data['mysql']['password']
USER = toml_data['mysql']['user']
PORT = toml_data['mysql']['port']

# connect to database
db = connection.connect(host=HOST_NAME, database=DATABASE, user=USER, passwd=PASSWORD, use_pure=True)

#generate dataframe
df = pd.read_sql('SELECT * FROM Shippers' , db)

# configure page 
st.set_page_config(
    page_title="The Best Portfolio They Will EVER See",
    layout="wide"
)

# title of app
# st.title('')

# display dataframe
st.write(df)

with st.sidebar:
    st.write('This is the side bar!')

# conn = st.experimental_connection('mysql', type='sql')

# # Perform query.
# df = conn.query('SELECT * FROM PO_LINE;', ttl=600)

# st.title('MySQL Streamlit App Test') 

# st.write('not exactly sure what is going on here')

# st.write(df.shape)
