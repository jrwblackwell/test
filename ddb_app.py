import streamlit as st
import duckdb

conn = duckdb.connect(database='witsend.duckdb', read_only=True)

st.set_page_config(layout="wide")

test = conn.execute("""
        SELECT 
            i
        FROM test_table
        ORDER BY i
    """).df()

st.write(test)
