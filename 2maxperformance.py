# Overview
'''
This Python script visualizes Max Verstappen's race performance over multiple races using data from
a MySQL database. It retrieves race data, processes it, and creates a visual representation of 
finishing positions and points scored using Matplotlib.
'''

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    user='root', # Your database username
    host='localhost', # Your database hostname
    password='********', # Your database password
    database='F1', # The name of your database
)

# Create a cursor object to interact with the database
my = mydb.cursor()

# Execute SQL query to fetch data from the 'maxdata' table
my.execute('SELECT * FROM maxdata')

# Fetch all rows from the query result
info = my.fetchall()

# Close the database connection
mydb.close()

# Create a DataFrame from the fetched data
df = pd.DataFrame(info, columns=['Grandprix', 'Date', 'Car', 'RacePosition', 'Pts'])

# Extract relevant columns for plotting
x = df['Pts'] # Points scored in each race
race = df['RacePosition'] # Finishing positions in each race
date = df['Date'] # Dates of the races

# Create a figure with two subplots
fig, axs = plt.subplots(2)

# Set the overall title for the figure
fig.suptitle('Max Verstappen Race Performance: Finishing Positions', fontsize=16)

# Plot Finishing Positions
axs[0].plot(race, color='brown') # Plot finishing positions with brown color
axs[0].set_ylabel('Finishing Position', labelpad=10, color='green') # Set the y-axis label
axs[0].grid(axis='y', color='lightgrey') # Add a grid on the y-axis
axs[0].set_title('Finishing Position of Each Race', pad=0, fontdict={'color': 'darkgreen'}) # Set the title for this subplot
axs[0].set_xlim(1, 203)  # Set x-axis limit for the finishing positions plot
axs[0].spines['top'].set_visible(False)  # Hide the top spine (border) of the plot for a cleaner look
axs[0].spines['right'].set_visible(False)  # Hide the right spine (border) of the plot for a cleaner look

# Plot Points Scored
axs[1].plot(x, color='Olive') # Plot points scored with olive color
axs[1].set_xlabel('Races', labelpad=5, color='navy') # Set the x-axis label
axs[1].set_ylabel('Points', labelpad=20, color='navy') # Set the y-axis label
axs[1].grid(axis='y', color='lightgrey') # Add a grid on the y-axis
axs[1].set_title('Points Scored for Each Race', pad=0, fontdict={'color': 'navy'}) # Set the title for this subplot
axs[1].set_xlim(1, 203)  # Set x-axis limit for the points scored plot
axs[1].spines['top'].set_visible(False)  # Hide the top spine (border) of the plot for a cleaner look
axs[1].spines['right'].set_visible(False)  # Hide the right spine (border) of the plot for a cleaner look

# Adjust the layout of the plots
plt.subplots_adjust(left=0.057, top=0.909, right=0.96, bottom=0.08)

# Display the plots
plt.show()
