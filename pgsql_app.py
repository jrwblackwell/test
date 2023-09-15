import streamlit as st

# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM "public"."cosmetics_invoices" LIMIT 15', ttl="10m")

# Print results.
st.write(df)
