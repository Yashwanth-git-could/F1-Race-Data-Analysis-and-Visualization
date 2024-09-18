# overview
'''This Python script connects to a MySQL database (F1) and exports data from multiple tables into a single Excel file (F1data.xlsx). 
The script uses pandas for data handling and mysql.connector for database connectivity. 
Each table's data is written to a separate sheet in the Excel file, and the xlsxwriter engine is used to handle Excel output.'''

import pandas as pd
import mysql.connector 

# Establish connection to MySQL database
mydb = mysql.connector.connect(user='root', host='localhost', username='yashwnth', password='Yashwanth@7', database='F1')
my = mydb.cursor()

# List of tables to export from the MySQL database
tables = ['drivenlaps', 'driverspodiums', 'driverspoles', 'driverswins', 'f1championships', 
          'lewisdata', 'maxdata', 'pointsscored', 'sprintrace', 'team_ferrari', 
          'team_mclaren', 'team_mercedes', 'team_redbull', 'team_williams', 'vetteldata']

# Open ExcelWriter to write multiple sheets in the same Excel file
with pd.ExcelWriter('F2data.xlsx', engine='xlsxwriter') as writer:
    for table in tables:
        # Get column names of the current table
        my.execute(f'SHOW COLUMNS FROM {table}')
        columns = my.fetchall()
        headers = [i[0] for i in columns]  # Extract column names
        
        # Fetch data from the current table
        my.execute(f'SELECT * FROM {table}')
        info = my.fetchall()
        
        # Create a DataFrame using the fetched data and column names
        df = pd.DataFrame(info, columns=headers)
        
        # Write the DataFrame to an Excel sheet, with the sheet named after the table
        df.to_excel(writer, sheet_name=table, index=False)
# To close the Connection
mydb.close()

# The script finishes, and the Excel file 'F1data.xlsx' will contain all tables.
