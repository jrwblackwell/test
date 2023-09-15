import streamlit as st
import pymongo
from pymongo.mongo_client import MongoClient
import pandas as pd 


uri = "mongodb+srv://jrwblackwell1998:gemini98@cluster0.zdpbyk2.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a new client and connect to the server
@st.cache_resource
client = MongoClient(uri)

# Send a ping to confirm a successful connection

try:
    client.admin.command('ping')
    st.write("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    st.write(e)

def get_data():
    db = client.sample_guides #establish connection to the 'sample_guide' db
    items = db.planets.find() # return all result from the 'planets' collection
    items = list(items)        
    return items

data = get_data()

# df = pd.read_json(data)

# st.write(df)

df = pd.DataFrame(data)

st.write(df)

st.write(data)
