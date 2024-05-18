from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import mysql.connector
import google.generativeai as genai

# Configure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query as response
def get_gemini_response(question, prompt):
    api_key = os.getenv("GOOGLE_API_KEY")
    print("API Key:", api_key)  # Print API key
    genai.configure(apey=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt_str = "\n".join(prompt)  # Convert prompt list to string
    response = model.generate_content(prompt_str + "\n" + question)  # Concatenate prompt and question
    return response.text

# Function to retrieve query from SQL database
def read_sql_query(sql):
    print("SQL Query:", sql)  # Print the SQL query being executed
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="ronaldocr7",
        database="student"
    )
    cur = conn.cursor()
    cur.execute(sql)
    
    # Fetch all rows from the result set
    rows = cur.fetchall()
    
    # Close the cursor and connection
    cur.close()
    conn.close()
    
    # Debugging: Print the fetched rows
    print("Fetched rows:", rows)
    
    # Return the fetched rows
    return rows

# Define prompt - Give information to model about how it should behave
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit app
st.set_page_config(page_title="Gemini App to Retrieve SQL Data")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("The SQL Query Generated is:")
    st.code(response, language='sql')
    
    # Fetch data from the database based on the generated SQL query
    data = read_sql_query(response)
    
    # Display the fetched data
    st.subheader("The Retrieved Data is:")
    if data:
        for row in data:
            st.write(row)
    else:
        st.write("No data retrieved from the database.")
