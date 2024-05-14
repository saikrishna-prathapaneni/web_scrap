import pandas as pd

# Read the exit companies from 'plugnplay_exit.csv'
exit_df = pd.read_csv('plugnplay_exit.csv')

# Read the unicorn companies from 'plugnplay_unicorn.csv'
unicorn_df = pd.read_csv('plugnplay_unicorn.csv')

# Combine the exit and unicorn company names
removed_companies = pd.concat([exit_df['Company Name'], unicorn_df['Company Name']])

# List to store individual DataFrames
dataframes = []

# Loop through the range of file numbers
for n in range(1, 15):
    filename = f"plugnplay{n}.csv"
    
    # Read each CSV file into a DataFrame
    df = pd.read_csv(filename)
    
    # Remove companies based on the merged 'Company Name' column
    df = df[~df['Company Name'].isin(removed_companies)]
    
    # Append the DataFrame to the list
    dataframes.append(df)

# Merge all DataFrames into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("merged_plugnplay_fine.csv", index=False)
