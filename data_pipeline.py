from functions import *
import time
import datetime

import pandas as pd


print(
    "Starting data pipeline at ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)
print("----------------------------------------------------------")

# Step 1: Load data
file_url = "https://docs.google.com/spreadsheets/d/1yPQp3upG49oxvHbsKfc7cTwlAKkkUyxK4YK2yjhTyFs/export?format=csv"
df = download_excel_from_google_drive(file_url)

# Step 2 : Transform data
df["C1"] += 1


# Step 3: Export results

df.to_excel("modified_etl.xlsx")
