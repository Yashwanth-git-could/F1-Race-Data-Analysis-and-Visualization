 ## Overview

'''
The script performs the following tasks:
1. **Scrape Data**: Retrieves race results for Sebastian Vettel from the Formula 1 website for each year from 2007 to 2024.
2. **Data Processing**: Extracts relevant information and stores it in a pandas DataFrame.
3. **Database Insertion**: Inserts the consolidated data into a MySQL database table named `lewisdata`.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
import sqlalchemy

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    user='root', # your username
    host='localhost', #your hostname
    password='********', # your password (hidden for security)
    database='F1', # your database
)
conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:yourpassword@localhost/F1')
con = conn.connect()

# Initialize a list to store DataFrames for each year
alldata = []

# Loop through the years from 2007 to 2022
for year in range(2007, 2023):
    # Request the HTML content of the page for the given year
    post = requests.get(url=f'https://www.formula1.com/en/results/{year}/drivers/SEBVET01/sebastian-vettel')
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(post.text, 'html.parser')
    
    # Find the table headers
    trow = soup.find('tr')
    headers = [i.text.strip() for i in trow.find_all('th')]
    
    # Create an empty DataFrame with the headers
    df = pd.DataFrame(columns=headers)
    
    # Find the table body and iterate over each row
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')
    for row in rows:
        row_data = row.find_all('td')
        data = [cell.text.strip() for cell in row_data]
        
        # Append the data to the DataFrame
        length = len(df)
        df.loc[length] = data
    
    # Append the DataFrame for this year to the list
    alldata.append(df)

# Concatenate all DataFrames into a single DataFrame
all = pd.concat(alldata)

# Insert the consolidated DataFrame into the MySQL database table 'lewisdata'
all.to_sql('vetteldata', con=con, index=False)

# Close the database connection
con.close()
