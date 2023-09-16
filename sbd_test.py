import pandas as pd
import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.experimental_connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="salary", ttl="10m").execute()

st.write(rows)

df = pd.DataFrame.from_dict(data)

st.write(df)
