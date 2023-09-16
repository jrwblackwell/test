import pandas as pd
import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.experimental_connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="salary", ttl="10m").execute()

st.write(rows)

rows = conn.query("Client, Orders, Total", table="salary", ttl="10m").eq(
        "Client", "Rudiger Pharmacy"
    ).execute()

# sql =  "select * from salary where client like 'Rock%'"

# rows = conn.query(sql, table="salary", ttl="10m").execute()

df = pd.DataFrame(rows.data)

st.write(df)

with st.sidebar:
  st.write('Finally!')
