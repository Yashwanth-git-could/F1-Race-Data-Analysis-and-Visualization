# overview
'''
This script connects to a MySQL database to retrieve data from the pointsscored table, 
specifically focusing on drivers who have scored more than 1000 points. It then processes this data into a 
Pandas DataFrame and visualizes the distribution of points using a pie chart. 
The pie chart highlights the proportion of total points for each driver, with specific emphasis on the first slice.
'''
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to the MySQL database
mydb = mysql.connector.connect(
    user='root',  # Database username
    host='localhost',  # Database host
    password='********',  # Database password (note: consider using environment variables for security)
    database='F1'  # Database name
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute an SQL query to fetch data from the 'pointsscored' table where Points > 1000
my.execute('''SELECT * FROM pointsscored WHERE Points > 1000 and Races>150;''')

# Fetch all rows from the query result
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Pos', 'Driver', 'f', 'l', 'Races', 'Points'])

# Prepare the explode parameter for the pie chart, which highlights slices
explode = [0] * len(df['Driver'])  # Initialize explode list with zeros
explode[0] = 0.05  # Highlight the first slice

# Create a pie chart to visualize the distribution of points
plt.pie(
    df['Points'],  # Data to plot
    labels=[f'points: {i}' for i in df['Points']],  # Labels for each slice showing the points
    autopct='%1.1f%%',  # Format for displaying percentages
    labeldistance=1.04,  # Distance of labels from the center
    explode=explode,  # Slices to explode (highlight)
    startangle=30  # Angle to start the pie chart
)

# Add a legend to the pie chart
plt.legend(
    labels=[i for i in zip(df['Driver'], df['Races'])],  # Legend showing driver names and number of races
    loc='best',  # Position of the legend
    bbox_to_anchor=(1.1, 0, 0, 0.85),  # Adjust the position of the legend
    title='Driver, Races,'  # Title for the legend
)

# Set the title for the pie chart
plt.title('Drivers Performance: Races and Points Distribution')

# Display the pie chart
plt.show()
