#Overview
'''
This Python script visualizes Lewis Hamilton's race performance data from a MySQL database. 
It retrieves race data, processes it into a DataFrame, and creates two plots to show finishing positions and 
points scored across races using Matplotlib.
'''
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to MySQL database
mydb = mysql.connector.connect(
    user='root', # your username
    host='localhost', #your hostname
    password='********', # your password (hidden for security)
    database='F1', # your database
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute SQL query to fetch all data from the 'lewisdata' table
my.execute('SELECT * FROM lewisdata')

# Fetch all results from the executed query
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Grandprix', 'Date', 'Car', 'RacePosition', 'Pts'])

# Extract relevant columns for plotting
x = df['Pts']  # Points scored
race = df['RacePosition']  # Finishing positions
date = df['Date']  # Date of each race

# Create a figure with two subplots
fig, axs = plt.subplots(2)

# Set the main title for the figure
fig.suptitle('Lewis Hamilton Race Performance: Finishing Positions', fontsize=16)

# Plot for Finishing Positions
axs[0].plot(race, color='Purple')  # Line color for finishing positions
axs[0].set_ylabel('Finishing Position', labelpad=10, color='green')  # Y-axis label
axs[0].grid(axis='y', color='lightgrey')  # Grid lines for y-axis
axs[0].set_title('Finishing Position of Each Race', pad=0, fontdict={'color': 'darkgreen'})  # Title for the subplot
axs[0].set_xlim(1, 350)  # Set x-axis limit
axs[0].spines['top'].set_visible(False)  #Hide the top spine (border) of the plots for a cleaner look
axs[0].spines['right'].set_visible(False)  # Hide the right spine (border) of the plots for a cleaner look

# Plot for Points Scored
axs[1].plot(x, color='Limegreen')  # Line color for points scored
axs[1].set_xlabel('Races', labelpad=1, color='navy')  # X-axis label
axs[1].set_ylabel('Points', labelpad=20, color='navy')  # Y-axis label
axs[1].grid(axis='y', color='lightgrey')  # Grid lines for y-axis
axs[1].set_title('Points Scored for Each Race', pad=0, fontdict={'color': 'navy'})  # Title for the subplot
axs[1].set_xlim(1, 350)  # Set x-axis limit
axs[1].spines['top'].set_visible(False)  #Hide the top spine (border) of the plots for a cleaner look
axs[1].spines['right'].set_visible(False)  # Hide the right spine (border) of the plots for a cleaner look

# Adjust the layout to ensure titles and labels are properly placed
plt.subplots_adjust(left=0.057, top=0.909, right=0.96, bottom=0.06)

# Display the plots
plt.show()
