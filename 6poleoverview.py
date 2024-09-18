# Overview
'''
This Python script visualizes the percentage of pole positions achieved by drivers in a series of races.
It retrieves data from a MySQL database, processes it into a DataFrame, and creates a horizontal bar chart
showing the pole percentage for each driver along with annotations for each driver’s races and pole positions.
'''

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    user='root', # Your database username
    host='localhost', # Your database hostname
    password='********', # Your database password (hidden for security)
    database='F1' # The name of your database
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute SQL query to fetch data from 'driverspoles' table and calculate the percentage of poles
my.execute('''
    SELECT *, ROUND((Poles/Races)*100, 2) AS PolesPer 
    FROM driverspoles
    ORDER BY Poles;
''')

# Fetch all rows of the query result
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Pos', 'Driver', 'First Pole', 'Last Pole', 'Races', 'Poles', 'PolesPer'])

# Extract relevant columns for plotting
w = df['Races'] # Number of races
x = df['Driver'] # Driver names
y = df['PolesPer'] # Percentage of poles
z = df['Poles'] # Number of poles

# Combine driver, races, and poles into a single list for x-axis labels
x1 = [f'{driver} ({race}, {pole})' for driver, race, pole in zip(x, w, z)]

# Create a horizontal bar chart
bars = plt.barh(x1, y)

# Generate a list of faded colors for the bars
faded_colors = [plt.cm.coolwarm(1 - i/len(x)) for i in range(len(x))]

# Set colors for each bar
for bar, color in zip(bars, faded_colors):
    bar.set_color(color)

# Annotate each bar with the percentage of poles
for i, value in enumerate(y):
    plt.text(value, i, f'{value:.2f}%', ha='left', va='center')

# Set the x and y labels and title of the plot
plt.xlabel('Pole Percentage', labelpad=10, fontdict={'fontsize': 12})
plt.ylabel('(Driver, Races, Poles)', labelpad=10, fontdict={'fontsize': 12})
plt.title('Driver Success Metrics: Races, Pole Positions, and Poles Percentages', pad=13, fontdict={'fontsize': 15})

# Add gridlines to the x-axis
plt.grid(axis='x', color='silver', linestyle='--')

# Adjust layout of the plot to prevent overlap
plt.subplots_adjust(left=0.208, right=0.968, top=0.9, bottom=0.1)

# Display the plot
plt.show()
