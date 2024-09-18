# overview
'''This script scrapes data about driver points scored from the Pitwall website and saves it to a MySQL database. 
It uses requests and BeautifulSoup to extract data from an HTML table on a webpage. 
After processing the data into a Pandas DataFrame, it writes this data to a MySQL table named pointscored using SQLAlchemy.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the driver points scored page on Pitwall
post = requests.get(url='https://pitwall.app/records/driver-points-scored')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(post.text, 'html.parser')

# Extract the table header (column names)
trow = soup.find('tr')  # Find the first row containing headers
headers = [i.text.strip() for i in trow.find_all('th')]  # Clean up header text

# Create an empty DataFrame with the specified columns
df = pd.DataFrame(columns=['Pos', 'Driver', 'First Points', 'Last Points', 'Races', 'Points'])

# Extract the table body and iterate through the rows
tbody = soup.find('tbody')
rows = tbody.find_all('tr')  # Get all rows from the table

# Loop through each row, extract data, and add it to the DataFrame
for row in rows:
    row_data = row.find_all('td')  # Get all cells from the row
    data = [i.text.strip() for i in row_data]  # Clean up the text data
    length = len(df)  # Get the current length of the DataFrame
    
    # Append the data to the DataFrame
    df.loc[length] = data

# MySQL connection setup
import mysql.connector
import sqlalchemy

# Connect to MySQL database
mydb = mysql.connector.connect(
    user='root',  # Database username
    host='localhost',  # Database host
    password='*********',  # Database password (note: consider using environment variables for security)
    database='F1'  # Database name
)

# Create a SQLAlchemy engine for connecting to the MySQL database
conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost/F1')
con = conn.connect()

# Write the DataFrame to the MySQL table 'pointscored'
df.to_sql('pointsscored', con=con, index=False)

# Close the database connection
con.close()
