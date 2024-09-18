# Overview
'''
This Python script visualizes the number of laps completed by drivers in races with at least 200 races.
It retrieves data from a MySQL database, processes it into a DataFrame, and creates a horizontal bar chart
showing the laps completed by each driver, with race count annotations for each bar.
'''

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    user='root',  # Your database username
    host='localhost',  # Your database hostname
    password='********',  # Your database password (hidden for security)
    database='F1'  # The name of your database
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute SQL query to fetch data from the 'drivenlaps' table where races >= 200
my.execute('''
    SELECT * FROM drivenlaps
    WHERE Races >= 200 
    ORDER BY Races
''')

# Fetch all rows of the query result
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Pos', 'Driver', 'First Race', 'Last Race', 'Races', 'Laps'])

# Extract relevant columns for plotting
x = df['Driver']  # Driver names for the y-axis
y = df['Laps']  # Number of laps completed for the x-axis
z = df['Races']  # Number of races to be annotated on the bars

# Create a horizontal bar chart
bars = plt.barh(x, y)

# Generate a list of faded colors for the bars using a colormap
faded_colors = [plt.cm.GnBu(1 - i/len(x)) for i in range(len(x))]

# Set colors for each bar
for bar, color in zip(bars, faded_colors):
    bar.set_color(color)

# Annotate each bar with the number of races completed by the driver
for i, values in enumerate(y):
    plt.text(values, i, str(z[i]), fontdict={'size': 10, 'color': 'black'}, va='center', ha='left')

# Set the x and y labels and title of the plot
plt.xlabel('Laps Completed', labelpad=10)  # Label for x-axis
plt.ylabel('Driver', labelpad=10)  # Label for y-axis
plt.title('Laps Completed by Drivers with Race Count Annotations')  # Title of the plot

# Adjust layout of the plot to prevent overlap and ensure readability
plt.subplots_adjust(left=0.14, right=0.95, top=0.9, bottom=0.1)

# Display the plot
plt.show()
