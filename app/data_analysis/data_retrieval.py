# app/data_analysis/retrieve_data.py

import psycopg2
import pandas as pd

def get_data():
    """
    Retrieves data from the sports_data table and returns it as a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing all records from the sports_data table.
    """
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="sports_db", 
        user="your_username", 
        password="your_password", 
        host="localhost"
    )
    
    # SQL query to select all data from the table
    query = "SELECT * FROM sports_data"
    
    # Read the SQL query result into a DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    return df

df = get_data()
print(df.head())
