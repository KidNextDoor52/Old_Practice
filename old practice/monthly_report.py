import logging
import pandas as pd
import numpy as np
import os
import io
import re
from datetime import datetime, timedelta
import azure.functions as func
from azure.storage.blob import BlobServiceClient

def get_blob_df(container_name, file_name, sheet_name=None):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    blob_data = io.BytesIO(blob_client.download_blob().content_as_bytes())
    try:
        if sheet_name:
            current_df_pd = pd.read_excel(blob_data, sheet_name=sheet_name, index_col=None)
        else:
            current_df_pd = pd.read_excel(blob_data, index_col=None)
    except:
        current_df_pd = pd.read_csv(blob_data, index_col=None)
    return current_df_pd

def upload_file(df,container_name, file_name):
    new_blob_data = io.BytesIO()
    df.to_excel(new_blob_data, index=False)
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    blob_client.upload_blob(new_blob_data.getvalue(), overwrite=True)
    return
    
def format_time_column(df, column_name):
    try:
        df[column_name] = pd.to_datetime(df[column_name]) - timedelta(hours=5)
        df[column_name] = df[column_name].dt.strftime('%-m/%-d/%Y %-I:%M %p')
    except Exception as e:
        logging.error(f"Error formatting column {column_name}: {e}")
    return df

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    global connection_string
    connection_string = os.environ["CONNECTION_STRING"]

    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime('%m-%d-%y')

    req_body = req.get_json()
    file_name = req_body.get('file_name')
    logging.info(f'{file_name}')

    ma_raw = get_blob_df('sftp-content', f'Reports/Magnitude Monthly Reports/Raw/{file_name}') 
    ma_df = ma_raw.copy()
    ma_df = format_time_column(ma_df, "Time of Call")
    ma_df = format_time_column(ma_df, "Call End Time")
    ma_raw['Connected Duration'] = pd.to_datetime(ma_df['Connected Duration'], unit='s').dt.strftime('%H:%M:%S')



    report_name = f'Magnitude Media ACA Call Log Monthly {formatted_date}.xlsx'

    upload_file(ma_df, f'sftp-content', f"Reports/Magnitude Monthly Reports/Production/{report_name}")
    return func.HttpResponse(report_name, status_code=200)
