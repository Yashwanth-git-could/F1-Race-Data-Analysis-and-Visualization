# Overview
'''
This Python script visualizes the win percentage of Formula 1 drivers who have participated in at least 200 races. 
It retrieves the data from a MySQL database, processes it into a DataFrame, and generates a bar chart showing 
the win percentage of each driver. The chart uses color gradients to differentiate between drivers, 
and it also displays the number of races and wins for each driver along with the win percentage.
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

# Execute SQL query to fetch data on drivers with 200 or more races, including calculated win percentage
my.execute('''
    SELECT *, ROUND((Wins/Races)*100, 2) as WinsPer 
    FROM driverswins 
    WHERE Races >= 200 
    ORDER BY Wins
''')

# Fetch all rows from the query result
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Pos', 'Driver', 'First Win', 'Last Win', 'Races', 'Wins', 'WinsPer'])

# Extract relevant columns for plotting
w = df['Races']     # Number of races
x = df['Driver']    # Driver names
y = df['WinsPer']   # Win percentage
z = df['Wins']      # Number of wins

# Create combined labels for each bar (Driver, Races, Wins)
x1 = [str(i) for i in zip(x, w, z)]

# Create a bar chart
bars = plt.bar(x1, y, width=0.5)

# Generate a list of faded colors for the bars using the Oranges colormap
faded_colors = [plt.cm.Oranges(1 - i / len(x)) for i in range(len(x))]

# Set the color for each bar
for bar, color in zip(bars, faded_colors):
    bar.set_color(color)

# Annotate each bar with the win percentage
for i, values in enumerate(y):
    plt.text(i, values, str(y[i]), ha='center', va='bottom')

# Set x and y labels and chart title
plt.xlabel('(Driver, Races, Wins)', labelpad=10, fontdict={'fontsize': '12'})
plt.ylabel('Win Percentage', labelpad=10, fontdict={'fontsize': '12'})
plt.title('Analyzing Driver Achievements: Races Completed, Wins, and Win Percentage', pad=13, fontdict={'fontsize': '15'})

# Rotate the x-axis labels for better readability
plt.xticks(rotation=85)

# Add gridlines on the y-axis
plt.grid(axis='y', color='silver', linestyle='--')

# Adjust layout to prevent label overlap
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.37)

# Remove the top and right spines to clean up the chart
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Display the plot
plt.show()
