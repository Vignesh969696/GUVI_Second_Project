Cricket Match Data Analysis Project
-----------------------------------

This project does data analysis of cricket matches using data from Cricsheet.org. The objective was to collect, clean, store, analyze, and visualize data from ODI, T20, and Test matches using Python, SQLite, and PowerBI.

Project Structure:

GUVI_Second_Project/
│
├── ODI_full_dataset.csv            # Merged and cleaned ODI match data
├── load_all_data.py                # Loads ODI, T20, and Test data into SQLite
├── all_queries.py                  # Runs 20 SQL queries across ODI, T20, and Test matches
├── visualize.py                    # Contains 10 different visualizations using matplotlib and seaborn
├── scrape_cricksheet.py            # Downloads data from Cricsheet using requests and BeautifulSoup
├── cricket_data.db                 # SQLite database file with 3 tables: odi_matches, t20_matches, test_matches
└── README.txt                      # This file

Features:

Data Downloading
   - Downloaded ODI, T20, and Test datasets automatically from Cricsheet.org
   - Used `requests` and `BeautifulSoup` for scraping download links

Data Storage
   - Loaded data into a local SQLite database using sqlite3
   - Three separate tables for ODI, T20, and Test matches

Data Cleaning
   - Cleaned and merged ODI data into a single CSV
   - Handled missing values, inconsistent columns, and types

SQL Analysis
   - 20 SQL queries total (7 ODI, 7 T20, 6 Test)
   - Queries included match outcomes, toss decisions, venues, top players, powerplay stats, etc.

Data Visualization
   - 10 visualizations using `matplotlib` and `seaborn`
   - Charts included bar plots, pie charts, histograms, and line plots
   - One seaborn-styled chart for variety

Power BI Dashboard
   - Imported `ODI_full_dataset.csv` into Power BI
   - Created 10 different visualizations (bar, donut, clustered, etc.)
   - Included filters and slicers to explore batting/bowling teams, venues, dismissals, and more



Dataset Source:

All match data was downloaded from:
https://cricsheet.org/downloads/

Cricsheet is an open-source project providing data for international cricket matches.

How to Run:

1. Run `scrape_cricksheet.py` to download the zip files and extract them into subfolders
2. Run `load_all_data.py` to populate the `cricket_data.db` SQLite file
3. Run `visualize.py` to generate visual insights
4. Run `all_queries.py` to execute 20 SQL queries and view the results
5. Open Power BI → Import `ODI_full_dataset.csv` → Start creating visuals


Requirements:

- Python 3.x
- pandas
- matplotlib
- seaborn
- requests
- beautifulsoup4
- sqlite3 
