# Overview
'''
This Python script visualizes the championship titles won by Formula 1 drivers. It retrieves data from a MySQL database
and displays the distribution of championships won by different drivers using a pie chart. The pie chart highlights the 
two most successful drivers by slightly exploding their slices for emphasis. A legend provides additional context by 
showing the driver names, the number of races they've participated in, and their total wins.
'''

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    user='root',        # Database username
    host='localhost',   # Hostname
    password='********',# Database password (hidden for security)
    database='F1'       # Database name
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute SQL query to fetch data from the 'f1championships' table
my.execute('''SELECT * FROM f1championships''')

# Fetch all rows from the query result
info = my.fetchall()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Pos', 'Driver', 'Races', 'Wins', 'Championships'])

# Close the database connection
mydb.close()

# Create an 'explode' list to emphasize the two top drivers
explode = [0] * len(df['Driver'])   # Initialize with 0 for all drivers
explode[0:2] = [0.1, 0.1]           # Explode the slices for the top two drivers

# Create the pie chart
plt.pie(df['Championships'], 
        labels=[i for i in df['Championships']],  # Use championship counts as labels
        labeldistance=0.5,                        # Distance of labels from center
        explode=explode,                          # Explode the top two drivers
        startangle=30)                            # Rotate chart for better readability

# Add a legend to provide context (Driver, Races, Wins)
plt.legend(labels=[i for i in zip(df['Driver'], df['Races'], df['Wins'])], 
           loc='best', 
           bbox_to_anchor=(1.0, 0, 0, 0.85), 
           title='Driver, Races, Wins')

# Set the title of the chart
plt.title('Drivers Path to Victory: Races, Wins, and Championship Titles')

# Add a label in the center of the pie chart
plt.text(0, 0, "Championship Wins", ha='center', va='center', fontsize=12, color='black')

# Display the pie chart
plt.show()

