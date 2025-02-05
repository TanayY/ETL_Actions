from functions import *
import time
import datetime
import random
import pandas as pd


print(
    "Starting data pipeline at ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)
print("----------------------------------------------------------")

# Step 1: Load data
file_url = "modified_etl.xlsx"
df = pd.read_excel(file_url)
df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
print(df)

# Step 2 : Transform data
# Get current timestamp
new_row = {"C1": [random.randint(1, 100)]}
df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)
print(df)

# Step 3: Export results

df.to_excel("modified_etl.xlsx")
