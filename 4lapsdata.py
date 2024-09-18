# Overview
'''
This Python script extracts driver lap data from a web page, processes it into a DataFrame, and stores it into a MySQL database. 
It then retrieves data from the database for drivers who have participated in more than 150 races and updates another table with this filtered data.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
import sqlalchemy

# Fetch data from the web page
post = requests.get(url='https://pitwall.app/records/driver-laps-driven')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(post.text, 'html.parser')

# Extract table headers
trow = soup.find('tr')
headers = [i.text.strip() for i in trow.find_all('th')]

# Create a DataFrame to store the data
df = pd.DataFrame(columns=headers)

# Extract table body and rows
tbody = soup.find('tbody')
rows = tbody.find_all('tr')

# Populate DataFrame with data from each row
for row in rows:
    row_data = row.find_all('td')
    data = [i.text.strip() for i in row_data]
    length = len(df)
    df.loc[length] = data

# Connect to MySQL database
mydb = mysql.connector.connect(
    user='root',  # Your database username
    host='localhost',  # Your database hostname
    password='********',  # Your database password (hidden for security)
    database='F1'  # The name of your database
)

# Create an SQLAlchemy engine
conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost/F1')
con = conn.connect()

# Save DataFrame to 'drivenlaps' table in the database
df.to_sql('drivenlaps', con=con, if_exists='replace', index=False)

# Close the database connection
mydb.close()