import os
import pandas as pd

# Ensure script runs relative to its own location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Confirm working directory
print("Current working directory:", os.getcwd())

# Set the path to the folder containing the CSVs
csv_dir = os.path.join(os.getcwd(), "odis_csv2")

# Parsing match info files (_info.csv) 

match_summaries = []

for file in os.listdir(csv_dir):
    if not file.endswith("_info.csv"):
        continue

    match_id = file.replace("_info.csv", "")
    file_path = os.path.join(csv_dir, file)

    data = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',', 2)
            if len(parts) == 3 and parts[0] == 'info':
                key = parts[1].strip()
                value = parts[2].strip().strip('"')
                data[key] = value

    data['match_id'] = match_id
    match_summaries.append(data)

df_matches = pd.DataFrame(match_summaries)

# 2: Parsing CSV files  

ball_data_frames = []

for file in os.listdir(csv_dir):
    if file.endswith("_info.csv") or not file.endswith(".csv"):
        continue

    file_path = os.path.join(csv_dir, file)

    try:
        df = pd.read_csv(file_path, low_memory=False)
    except Exception as e:
        print(f"Error reading {file}: {e}")
        continue

    match_id = file.replace(".csv", "")
    df['match_id'] = match_id

    ball_data_frames.append(df)

df_balls = pd.concat(ball_data_frames, ignore_index=True)

# 3: Merge and export full dataset 

df_matches.fillna("N/A", inplace=True)

# Preventing duplicate column conflict by making pandas handle overlapping names
merged_df = pd.merge(df_balls, df_matches, on='match_id', how='left', suffixes=('', '_info'))

# Save to same folder as script
output_path = os.path.join(os.getcwd(), "ODI_full_dataset.csv")
merged_df.to_csv(output_path, index=False)

print("ODI data processing complete. Output saved as ODI_full_dataset.csv")







