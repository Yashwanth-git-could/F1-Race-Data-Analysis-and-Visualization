# overview
'''
This script is intended to scrape data about Formula 1 drivers' sprint race wins from the Pitwall website. It uses BeautifulSoup to parse HTML 
and extract relevant data from a table. The processed data is stored in a Pandas DataFrame and then uploaded to a MySQL database table named sprintrace. 
The script utilizes requests for fetching the webpage and SQLAlchemy for database interactions.
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the driver sprint wins page on Pitwall
post = requests.get(url='https://pitwall.app/records/driver-sprint-wins')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(post.text, 'html.parser')

# Extract the table header (column names) from the first row
trow = soup.find('tr')  # Locate the header row
headers = [i.text.strip() for i in trow.find_all('th')]  # Clean up header text

# Create an empty DataFrame with the specified columns
df = pd.DataFrame(columns=['Pos', 'Driver', 'First sprint win', 'Last sprint win', 'Sprint_Races', 'Sprint_Wins'])

# Extract the table body and iterate through each row
tbody = soup.find('tbody')
rows = tbody.find_all('tr')  # Get all rows from the table

# Loop through each row, extract the data, and append it to the DataFrame
for row in rows:
    row_data = row.find_all('td')  # Get all cells in the row
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
    password='***********',  # Database password (note: consider using environment variables for security)
    database='F1'  # Database name
)

# Create a SQLAlchemy engine for connecting to the MySQL database
conn = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost/F1')
con = conn.connect()

# Write the DataFrame to the MySQL table 'sprintrace'
df.to_sql('sprintrace', con=con, index=False)

# Close the database connection
con.close()
