#overview
'''This script is designed to scrape data about various Formula 1 teams from the Pitwall website and then store the collected data into a MySQL database. 
The teams include scuderia-ferrari, mclaren-racing, mercedes-amg-f1, red-bull-racing, and williams-grand-prix-engineering
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
import sqlalchemy

# List of team names for which data will be scraped
teams = ['scuderia-ferrari','mclaren-racing','mercedes-amg-f1','red-bull-racing','williams-grand-prix-engineering']

# Loop through each team in the list
for team in teams:
    # Fetch the HTML content for the team's page
    post = requests.get(url=f'https://pitwall.app/teams/{team}')
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(post.text, 'html.parser')
    
    # Extract the headers from the first row of the table
    trow = soup.find('tr')
    headers = [i.text.strip() for i in trow.find_all('th')]
    
    # Create an empty DataFrame with the extracted headers
    df = pd.DataFrame(columns=headers)
    
    # Find the table body and extract all rows
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')
    
    # Iterate through each row to extract data
    for row in rows:
        row_data = row.find_all('td')
        data = [i.text.strip() for i in row_data]
        length = len(df)  # Get the current length of the DataFrame
        df.loc[length] = data  # Append the row data to the DataFrame
    
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        user='root',
        host='localhost',
        password='Yashwanth@7',
        database='F1'
    )
    
    # Create a SQLAlchemy engine to interact with the MySQL database
    conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:Yashwanth%407@localhost/F1')
    con = conn.connect()
    
    # Write the DataFrame to a MySQL table named after the team
    df.to_sql(f'{team}', con=con, index=False)

    # Close the database connection
    con.close()
