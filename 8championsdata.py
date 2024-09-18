# Overview
'''
This script scrapes data related to Formula 1 driver championships from the Pitwall website and filters the data to include only 
drivers with more than 1 championship. The data is processed into a Pandas DataFrame and then saved into a MySQL table named f1championships. 
The script uses BeautifulSoup for web scraping and SQLAlchemy for interacting with the MySQL database.
'''

# Import necessary libraries
import requests  # To send HTTP requests to the website
from bs4 import BeautifulSoup  # For parsing HTML content
import pandas as pd  # To manipulate and analyze data

# Send a GET request to the driver championships page on Pitwall
post = requests.get(url='https://pitwall.app/records/driver-championships')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(post.text, 'html.parser')

# Extract the table header (column names)
trow = soup.find('tr')  # Find the first row containing headers
headers = [i.text.strip() for i in trow.find_all('th')]  # Clean up header text

# Create an empty DataFrame with the extracted headers
df = pd.DataFrame(columns=headers)

# Extract the table body and iterate through the rows
tbody = soup.find('tbody')  # Locate the table body
rows = tbody.find_all('tr')  # Get all rows from the table

# Loop through each row, extract data and add it to the DataFrame
for row in rows:
    row_data = row.find_all('td')  # Get all cells from the row
    data = [i.text.strip() for i in row_data]  # Clean up the text data by stripping extra spaces
    length = len(df)  # Get the current length of the DataFrame (used for appending new data)
    
    # Append the data to the DataFrame
    df.loc[length] = data

# Filter the DataFrame to keep only drivers with more than 1 championship
results = df[df['Championships'] > '1']

# Import MySQL connector and SQLAlchemy for database interaction
import mysql.connector  # To connect to the MySQL database
import sqlalchemy  # For SQLAlchemy engine to work with MySQL

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    user='root',  # Your database username
    host='localhost',  # Your database hostname
    password='********',  # Your database password (hidden for security)
    database='F1'  # The name of your database
)

# Create an SQLAlchemy engine to interact with MySQL
conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost/F1')

# Open a connection using SQLAlchemy
con = conn.connect()

# Write the filtered DataFrame to the MySQL table 'f1championships'
results.to_sql('f1championships', con=con, index=False)  # Exporting the DataFrame to MySQL table without the index column

# Close the database connection
con.close()  # Safely close the connection after writing data
