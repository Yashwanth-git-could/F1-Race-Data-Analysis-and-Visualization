#overview
'''
This script visualizes the historical performance of major Formula 1 teams from 2010 onward. It retrieves data from a MySQL database 
for each team, processes it into a Pandas DataFrame, and plots the positions over the years on a line chart. Each line represents a different team, 
and the script includes annotations for points achieved each year. The plot highlights performance trends and comparative analysis of teams.
'''
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to the MySQL database
mydb = mysql.connector.connect(
    user='root',  # Database username
    host='localhost',  # Database host
    password='*******',  # Database password (consider using environment variables for security)
    database='F1'  # Database name
)
my = mydb.cursor()

# Set up the plot with custom spines visibility
fig, axs = plt.subplots()
axs.spines['top'].set_visible(False)  # Hide the top spine
axs.spines['right'].set_visible(False)  # Hide the right spine

# Define teams and labels for the plot
teams = ['team_redbull', 'team_mercedes', 'team_mclaren', 'team_ferrari', 'team_williams']
labels = ['Redbull', 'Mercedes', 'McLaren', 'Ferrari', 'Williams']
columns = ['Year', 'Pos', 'Points', 'Wins', 'Podiums', 'Pole', 'Drivers']

# Loop through each team and plot their data
for team, label in zip(teams, labels):
    # Query the database for the current team's data
    my.execute(f'SELECT * FROM {team}')
    data = my.fetchall()
    
    # Convert the query results into a DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Plot the team's position over the years
    line, = plt.plot(df['Year'], df['Pos'], label=label, marker='.')
    
    # Annotate each point with the number of points achieved
    x = df['Pos']
    y = df['Year']
    for i in range(len(df)):
        plt.text(df['Year'][i], df['Pos'][i], str(df['Points'][i]), ha='right', va='bottom', color='gray')
    
    # Annotate the first point with the team label
    plt.text(y.iloc[0] + 0.2, x.iloc[0], label, fontsize=13, ha='left', va='center', color=line.get_color())

# Customize the plot with titles, labels, and limits
plt.title('Historical Performance of Major F1 Teams (Yearly Analysis) From 2010', fontdict={'fontsize': 15}, color='darkcyan', pad=50)
plt.xlabel('Year', labelpad=10, fontsize=12, color='navy')
plt.ylabel('Position', labelpad=10, fontsize=12, color='navy')
plt.ylim(0, 11)  # Set y-axis limits (positions are typically 1-10)
plt.subplots_adjust(left=0.1, right=0.85, top=0.8, bottom=0.1)
plt.gca().invert_yaxis()  # Invert y-axis to have 1 at the top
plt.show()

# Close the database connection
mydb.close()
