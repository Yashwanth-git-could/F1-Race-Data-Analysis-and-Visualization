# Overview
'''
This Python script scrapes driver podium data from multiple pages of a website and stores it in a MySQL database.
The script uses requests and BeautifulSoup for web scraping and pandas for data manipulation. 
Data is fetched from multiple pages, combined into a single DataFrame, and then saved to a MySQL database.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(page):
    '''
    Fetches podium data from a specific page of the driver podiums records.
    
    Parameters:
    page (int): The page number to fetch data from.
    
    Returns:
    pd.DataFrame: DataFrame containing the scraped podium data from the page.
    '''
    # Send a GET request to the specified page URL
    post = requests.get(url=f'https://pitwall.app/records/driver-podiums?page={page}')
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(post.text, 'html.parser')
    
    # Extract headers from the first row of the table
    trow = soup.find('tr')
    headers = [i.text.strip() for i in trow.find_all('th')]
    
    # Initialize an empty DataFrame with the extracted headers
    df = pd.DataFrame(columns=headers)
    
    # Find the table body and all rows in the table
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')
    
    # Iterate through each row and extract data
    for row in rows:
        row_data = row.find_all('td')
        data = [i.text.strip() for i in row_data]
        length = len(df)
        df.loc[length] = data
    
    return df

# Fetch data from multiple pages (1 to 5)
page_data = [get_data(page) for page in range(1,2)]

# Concatenate all DataFrames into a single DataFrame
data = pd.concat(page_data)


import mysql.connector
import sqlalchemy

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    user='root',  # Your database username
    host='localhost',  # Your database hostname
    password='**********',  # Your database password (hidden for security)
    database='F1'  # The name of your database
)

# Create an SQLAlchemy engine for MySQL
conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost/F1')
con = conn.connect()

# Save the combined DataFrame to a MySQL table
data.to_sql('driverspodiums', con=con, index=False)

# Close the database connection
con.close()
