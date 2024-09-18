# overview 
'''
This script queries data from a MySQL database about Formula 1 drivers' sprint race performances. 
It calculates the percentage of sprint wins for each driver and visualizes this information using a bar chart. 
The script employs pandas for data manipulation, mysql.connector for database access, and matplotlib for plotting the results.
'''
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to the MySQL database
mydb = mysql.connector.connect(
    user='root',  # Database username
    host='localhost',  # Database host
    password='**********',  # Database password (consider using environment variables for security)
    database='F1'  # Database name
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute a SQL query to retrieve sprint race data and calculate the percentage of sprint wins
my.execute('''
    SELECT Driver, Sprint_races, Sprint_Wins,
           ROUND((Sprint_Wins/Sprint_races)*100, 2) AS Sprintper
    FROM sprintrace
    ORDER BY Sprint_Wins
''')

# Fetch all results from the query
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame with the retrieved data
df = pd.DataFrame(info, columns=['Driver', 'Sprint_races', 'Sprint_Wins', 'Sprintper'])

# Plot a bar chart showing the percentage of sprint wins for each driver
bars = plt.bar(df['Driver'], df['Sprintper'], label=[f'Sprint Wins: {i}' for i in df['Sprint_Wins']])

# Apply color gradient to bars
x = df['Sprintper']
y = df['Driver']
faded = [plt.cm.Greens(1 - i / len(x)) for i in range(len(x))]
for bar, color in zip(bars, faded):
    bar.set_color(color)

# Annotate each bar with its value
for i, values in enumerate(x):
    plt.text(i, values, f'{x[i]:.2f}%', ha='center')

# Set plot labels and title
plt.xlabel('Driver', labelpad=15, fontdict={'fontsize': 12})
plt.ylabel('Sprint Wins Percentage', labelpad=10, fontdict={'fontsize': 12})
plt.title('Sprint Race Analysis: Drivers, Wins, and Winning Percentages')
plt.legend()
plt.show()
