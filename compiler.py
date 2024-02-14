import pandas as pd
import os

# Assuming all files are in the 'data_directory' and are CSVs
data_directory = "/Users/varunsharma/Desktop/BCI_Car/final"
all_files = os.listdir(data_directory)

# Create an empty list to store the data from each file
all_dataframes = []

# Loop through each file and read the data
for file_name in all_files:
    if file_name.endswith('.csv'):  # Check if the file is a CSV
        file_path = os.path.join(data_directory, file_name)
        df = pd.read_csv(file_path)
        all_dataframes.append(df)

# Concatenate all the dataframes into one
combined_dataframe = pd.concat(all_dataframes)

# Save the combined dataframe to a new CSV file
combined_dataframe.to_csv("final_compiled.csv", index=False)
