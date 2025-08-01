Cricket Match Data Analysis Project
-----------------------------------

This project does data analysis of cricket matches using data from Cricsheet.org. The objective was to collect, clean, store, analyze, and visualize data from ODI, T20, and Test matches using Python, SQLite, and PowerBI.

Project Structure:

GUVI_Second_Project/
│
├── scrape_cricksheet.py            # Scrapes and extracts raw data from Cricksheet.org
├── odi.py                          # Converts raw csv files into clean data
├── t20.py                          # Converts raw json files into clean data
├── test.py                         # Converts raw json files into clean data
├── load_all_data.py                # Loads all clean data into SQLite database
├── all_queries.py                  # Runs SQL queries across ODI, T20, and Test matches
├── visualize.py                    # Contains 10 different visualizations using matplotlib and seaborn
├── Cricket_Analytics.pbix          # PowerBi Dashboard(connects to SQLite Database)
├── cricket_data.db                 # SQLite database file with 3 tables: odi_matches, t20_matches, test_matches
└── README.txt                      # This file

Features:

Data Downloading
   - Downloaded ODI, T20, and Test datasets automatically from Cricsheet.org
   - Used Selenium for scraping download links

Data Storage
   - Loaded data into a local SQLite database using sqlite3
   - Three separate tables for ODI, T20, and Test matches

Data Cleaning
   - Cleaned and merged ODI data into a single CSV
   - Handled missing values, inconsistent columns, and types

SQL Analysis
   - 20 SQL queries total 
   - Queries included match outcomes, toss decisions, venues, top players, powerplay stats, etc.

Data Visualization
   - 10 visualizations using `matplotlib` and `seaborn`
   - Charts included bar plots, pie charts, histograms, and line plots
   - One seaborn-styled chart for variety

Power BI Dashboard
   - Imported `cricket_data` into Power BI
   - Created 13 different visualizations (bar, pie, clustered, etc.)
   - Included filters and slicers to explore batting/bowling teams, venues, dismissals, and more



Dataset Source:

All match data was downloaded from:
https://cricsheet.org/downloads/

How to Run:

1. Run `scrape_cricksheet.py` to download the zip files and extract them into subfolders
2. Run `load_all_data.py` to populate the `cricket_data.db` SQLite file
3. Run `visualize.py` to generate visual insights
4. Run `all_queries.py` to execute 20 SQL queries and view the results
5. Open the .pbix file in Power BI Desktop
6. If visuals don't load, go to Transform Data → Data Source Settings → Change Source
7. Point it to your local path of cricket_data.db (SQLite database)
8. Click OK → Close & Apply to refresh the visuals


Requirements:

- Python 3.x
- pandas
- selenium
- matplotlib
- seaborn
- PowerBi
- sqlite3 
