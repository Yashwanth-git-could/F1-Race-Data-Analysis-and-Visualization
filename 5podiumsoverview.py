# Overview
'''
This Python script retrieves driver podium data from a MySQL database, processes it, and visualizes podium percentage by driver using a bar chart.
The script calculates the percentage of podium finishes for drivers who have participated in 200 or more races, and displays this data with annotations on the chart.
'''

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to the MySQL database
mydb = mysql.connector.connect(
    user='root',  # Your database username
    host='localhost',  # Your database hostname
    password='********',  # Your database password (hidden for security)
    database='F1'  # The name of your database
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute SQL query to fetch driver podium data with podium percentage calculation
my.execute('''
    SELECT *, ROUND((Podiums / Races) * 100, 2) AS podiumPer 
    FROM driverspodiums
    WHERE Races >= 200  # Filter to include drivers with 200 or more races
    ORDER BY Podiums  # Order by the number of podiums
''')

# Fetch all rows of the query result
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Pos', 'Driver', 'First Podium', 'Last Podium', 'Races', 'Podium', 'PodiumPer'])

# Extract relevant columns for plotting
w = df['PodiumPer']  # Podium percentage for each driver
x = df['Driver']  # Driver names
y = df['Podium']  # Number of podium finishes
z = df['Races']  # Number of races

# Create a bar chart for podium percentage by driver
bars = plt.bar(x, w)

# Define a color map for the bars with a gradient effect
faded_colors = [plt.cm.Spectral(1 - i / len(x)) for i in range(len(x))]
for bar, color in zip(bars, faded_colors):
    bar.set_color(color)  # Apply color gradient to bars

# Add annotations to each bar showing the number of races and podium finishes
for i, (y_val, z_val) in enumerate(zip(y, z)):
    plt.text(i, w[i], f'({z_val}, {y_val})', ha='center', va='top', rotation=90)

# Set labels and title for the plot
plt.xlabel('Driver', labelpad=10)
plt.ylabel('Podium Percentage', labelpad=10)
plt.title('Analyzing Driver Success: Race Count, Podium Finishes, and Podium Percentage')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Adjust the layout of the plot to prevent clipping of labels and titles
plt.subplots_adjust(left=0.1, right=0.9, top=0.94, bottom=0.25)

# Display the plot
plt.show()
