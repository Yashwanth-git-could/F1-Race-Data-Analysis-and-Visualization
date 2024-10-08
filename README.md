# F1-Race-Data-Analysis-and-Visualization

## Overview

This project analyzes Formula 1 race data using **Python** and **MySQL**, with visualizations generated by **Matplotlib**. The goal is to create various graphs that offer insights into different aspects of Formula 1, focusing on historical performance, consistency, and achievements.

## Features

-- Comprehensive Race Data Analysis: Analyze race performances for drivers like Lewis Hamilton, Max Verstappen, and Sebastian Vettel.
-- Visualizations: Generate clear, insightful visualizations including bar charts, pie charts, and line graphs for various metrics like podium finishes, laps completed, pole positions, and championships.
-- Historical Team Performance: Plot the performance of major F1 teams over time.
-- Data Management: Utilizes both MySQL for database management and Pandas for data manipulation.

## Requirements

1. Software Requirements
-- **Python 3.x**: The primary programming language for writing scripts, data manipulation, and visualization.
-- **MySQL Server**: To store, query, and manage Formula 1 data, which will be dynamically fetched in the Python scripts.
-- **MySQL Workbench** (Optional): For easier management of databases and queries in a GUI-based environment.
-- **IDE/Code Editor**: Tools like PyCharm, Visual Studio Code, or Jupyter Notebook to write and execute Python code.

2. Python Libraries
-- **pandas**: For data manipulation and transformation, especially to convert SQL query results into DataFrames for analysis.
-- **mysql-connector-python**: To establish a connection between Python and MySQL, allowing the fetching of data.
-- **matplotlib**: For creating the various plots and visualizations (line plots, bar charts, pie charts, etc.).
-- **SQLAlchemy**: If you're using SQLAlchemy for managing database connections and queries with an ORM (Object-Relational Mapping) approach, you'll need to install the library. It allows you to interact with the MySQL database in a more abstract, Pythonic way.
-- **Requests API**: For making HTTP requests, this is essential if you're fetching live data from APIs related to Formula 1, such as race schedules, driver statistics, or team standings. This library is commonly used to interact with web APIs.
-- **Beautiful Soup**: If you're using web scraping to gather Formula 1 data from websites, this library is useful for parsing HTML and XML documents.

-- Required Python packages and their install:
```bash
pip install pandas
pip install matplotlib
pip install SQLAlchemy
pip install requests
pip install beautifulsoup4

## Tasks
-- Task 1,2,3:
These tasks involve generating performance graphs for top drivers such as Lewis Hamilton, Max Verstappen, and Sebastian Vettel. The process involves:

    -- Task 1: Querying the database to retrieve Sebastian Vettel’s race performance data, including race positions and points.
    -- Task 2: Querying for Lewis Hamilton's data, focusing on his points and race positions for analysis.
    -- Task 3: Similar to Task 1, but for Max Verstappen, plotting race positions and points for each race.

-- Task 4:
    -- Goal: Analyze drivers based on the number of laps completed and their race count.
    -- Insight: This helps track driver longevity and consistency across different races.

-- Task 5:
    -- Goal: Analyze the podium finishes for drivers who have competed in more than 200 races.
    -- Insight: Visualizes which drivers consistently finish in the top 3 over their careers, highlighting race count and podium success.

-- Task 6 :
    -- Goal: Visualize drivers based on their pole positions and the percentage of poles they secured across their career.
    -- Insight: Highlights how effective each driver has been at securing pole positions relative to their career races.

-- Task 7:
    -- Goal: Plot the win percentages of drivers with more than 200 races.
    -- Insight: This reveals drivers’ win rates compared to their total career races, helping to identify those with the highest success rates.

-- Task 8:
    -- Goal: Display the number of championship titles won by drivers using a pie chart.
    -- Insight: Highlights the dominance of specific drivers in terms of championship titles won throughout their careers.

-- Task 9:
    -- Goal: Analyze drivers who have scored over 1000 points in their careers.
    -- Insight: Displays the drivers’ consistency and ability to score points over their career, with drivers accumulating over 1000 points highlighted.

-- Task 10:
    -- Goal: Analyze drivers based on their sprint race wins and winning percentages.
    -- Insight: Visualizes the success rate of drivers in sprint races, showing which drivers are strongest in this format.

-- Task 11:
    -- Goal: Analyze the historical performance of top F1 teams (Red Bull, Mercedes, McLaren, Ferrari, Williams) from 2010 onwards.
    -- Insight: This allows for the visualization of teams' historical performances, revealing trends of dominance or decline over time.
