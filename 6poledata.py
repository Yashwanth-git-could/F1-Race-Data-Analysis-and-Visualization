# Overview
'''
This Python script scrapes data on Formula 1 drivers' pole positions from a website across multiple pages.
It uses the `requests` library to fetch the web pages and `BeautifulSoup` to parse the HTML content.
The data is then processed into a pandas DataFrame and stored in a MySQL database using the SQLAlchemy library.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize an empty list to store pole position data from multiple pages
poledata = []

# Loop through the first 5 pages of the website to gather pole position data
for i in range(1, 6):  # Pages 1 to 5
    # Send a GET request to the website and retrieve page content
    post = requests.get(url=f'https://pitwall.app/records/driver-pole-positions?page={i}')
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(post.text, 'html.parser')
    
    # Extract table headers from the first row of the table
    trow = soup.find('tr')
    headers = [i.text.strip() for i in trow.find_all('th')]
    
    # Create an empty DataFrame with the extracted headers
    df = pd.DataFrame(columns=headers)
    
    # Find all rows in the table body
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')
    
    # Iterate over each row to extract column data
    for row in rows:
        # Get all 'td' elements (table data) in each row
        row_data = row.find_all('td')
        
        # Extract the text content from each 'td' and strip whitespace
        data = [i.text.strip() for i in row_data]
        
        # Append the extracted data as a new row to the DataFrame
        length = len(df)
        df.loc[length] = data
    
    # Append the DataFrame of this page to the main list
    poledata.append(df)

# Concatenate all the DataFrames from the pages into a single DataFrame
data = pd.concat(poledata)

# Connect to the MySQL database to store the scraped data
import mysql.connector
import sqlalchemy

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

# Store the data in the 'driverpoles' table in the MySQL database
data.to_sql('driverpoles', con=con, index=False)

# Close the connection
con.close()
