import requests
import pandas as pd
from io import BytesIO


def download_excel_from_google_drive(file_url):
    # Construct the Google Drive download URL
    download_url = f"{file_url}"

    # Send a GET request to fetch the file content
    df = pd.read_csv(download_url)
    return df
    # else:
    #     print(f"Failed to download file. Status code: {response.status_code}")
    #     return None
