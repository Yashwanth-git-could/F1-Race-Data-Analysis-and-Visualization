# overview
'''
This script scrapes data on Formula 1 drivers' race wins from the Pitwall website using the requests and BeautifulSoup libraries. 
It processes the scraped data into a Pandas DataFrame, then uploads the data to a MySQL database. 
The final data is stored in a table called driverswins, containing driver details like position, name, number of races, wins, and win percentage.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data from a specific page number
def get_data(i):
    # Send a GET request to the website's driver wins page for page 'i'
    post = requests.get(url=f'https://pitwall.app/records/driver-wins?page={i}')
    
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(post.text, 'html.parser')
    
    # Extract the table header (column names)
    trow = soup.find('tr')  # Finds the first row containing headers
    headers = [i.text.strip() for i in trow.find_all('th')]  # Clean header text
    
    # Create an empty DataFrame with the headers
    df = pd.DataFrame(columns=headers)
    
    # Find the table body and extract each row's data
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')  # Finds all rows in the table
    
    # Loop through each row and extract individual cell data
    for row in rows:
        row_data = row.find_all('td')  # Find all table data cells
        data = [i.text.strip() for i in row_data]  # Clean up each data point
        length = len(df)  # Get the current length of the DataFrame
        
        # Insert the row data into the DataFrame
        df.loc[length] = data
    
    return df  # Return the DataFrame for the specific page

# Combine data from all 5 pages into a single DataFrame
winsdata = [get_data(i) for i in range(1, 6)]
data = pd.concat(winsdata)  # Concatenate the DataFrames for all pages
print(data.shape)  # Print the shape of the combined data

# MySQL connection setup
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

# Insert the DataFrame into the MySQL table 'driverswins'
data.to_sql('driverswins', con=con, index=False)

# Close the database connection
con.close()
