import pymysql
import pandas as pd
import streamlit as st

connection = pymysql.connect(host='localhost',
                            # port=3306,
                            user='root',
                            passwd='gemini98'),
                            db='test_data')

sql_query = f'SELECT * FROM salary_journey;' 

with connection.cursor() as cursor:
    cursor.execute(sql_query)

    # Connection is not autocommit by default, so we must commit to save changes
    connection.commit()
    
    # Fetch all the records from SQL query output
    results = cursor.fetchall()
    
    # Convert results into pandas dataframe
    df = pd.DataFrame(results)                                     

st.write(df.shape)


# import mysql.connector as connection
# import pandas as pd
# import streamlit as st
# import toml

# # read credentials
# toml_data = toml.load("secrets.toml")

# # assign each credential to a variable
# HOST_NAME = toml_data['mysql']['host']
# DATABASE = toml_data['mysql']['database']
# PASSWORD = toml_data['mysql']['password']
# USER = toml_data['mysql']['user']
# PORT = toml_data['mysql']['port']

# # connect to database
# db = connection.connect(host=HOST_NAME, database=DATABASE, user=USER, passwd=PASSWORD, use_pure=True)

# #generate dataframe
# df = pd.read_sql('SELECT * FROM Shippers' , db)

# # configure page 
# st.set_page_config(
#     page_title="The Best Portfolio They Will EVER See",
#     layout="wide"
# )

# # title of app
# # st.title('')

# # display dataframe
# st.write(df)

# with st.sidebar:
#     st.write('This is the side bar!')

# conn = st.experimental_connection('mysql', type='sql')

# # Perform query.
# df = conn.query('SELECT * FROM PO_LINE;', ttl=600)

# st.title('MySQL Streamlit App Test') 

# st.write('not exactly sure what is going on here')

# st.write(df.shape)
