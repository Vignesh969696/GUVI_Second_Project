import sqlite3
import pandas as pd
import os

# Dataset Paths
odi_path = r"D:\guvi_fourth_project\ODI_Match\The_ODI_full_dataset.csv"
t20_path = r"D:\guvi_fourth_project\T20_Match\T20_combined_data.csv"
test_path = r"D:\guvi_fourth_project\Test_Match\Test_full_data.csv"

# SQLite database file
sqlite_db = r"D:\guvi_fourth_project\cricket_data.db"

# Connecting to SQLite
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Loading and inserting ODI data
odi_df = pd.read_csv(odi_path)
odi_df.to_sql("odi_matches", conn, if_exists="replace", index=False)
print("ODI data loaded into 'odi_matches' table.")

# Loading and inserting T20 data
t20_df = pd.read_csv(t20_path)
t20_df.to_sql("t20_matches", conn, if_exists="replace", index=False)
print("T20 data loaded into 't20_matches' table.")

# Loading and inserting Test data
test_df = pd.read_csv(test_path)
test_df.to_sql("test_matches", conn, if_exists="replace", index=False)
print("Test data loaded into 'test_matches' table.")

# Closing connection
conn.close()
print("\nData loaded into SQLite db.")
