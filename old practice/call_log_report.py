import logging
import pandas as pd
import os
import io
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import requests
import json
from datetime import datetime

dialpad_api = os.environ["dial_pad_key"]
connection_string = os.environ["CONNECTION_STRING"]
data = {"container": [], "folder": "KCA Call Logs"}

def upload_mp3(content, container_name, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container='keystone-activity', blob='KCA Call Logs/'+ file_name)
    blob_client.upload_blob(content, overwrite=True)

def download_mp3(group):
    if group.empty:
        return
    group['Dialpad Call Log: Created Date'] = pd.to_datetime(group['Dialpad Call Log: Created Date']).dt.strftime('%y%m%d')
    date = group['Dialpad Call Log: Created Date'].values[0]
    external_number = group['External Number'].values[0]
    rec_url = group['recording_url'].values[0]
    rec_url += f'?apikey={dialpad_api}'
    filename = f'KCA_{external_number}_{date}.mp3'
    save_path = fr'{filename}'
    response = requests.get(rec_url)

    if response.status_code == 200:
        mp3_content = io.BytesIO(response.content)
        upload_mp3(mp3_content, 'keystone-activity', filename)
        print(f"File downloaded successfully and saved as {save_path}")
        data["container"].append(filename)
    return

def extract_mp3_url(text):
    headers = {
        'Authorization': f'Bearer {dialpad_api}',
    }
    url = f"https://dialpad.com/api/v2/call/{text}"
    response = requests.get(url, headers=headers)

    rec_url = response.json()['recording_url'][0]
    print('extracted recording URL ', rec_url)
    return rec_url

def get_blob_df(container_name, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    blob_data = io.BytesIO(blob_client.download_blob().content_as_bytes())
    current_df_pd = pd.read_csv(blob_data)
    return current_df_pd


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    name = req_body.get('name')
    df = get_blob_df('sftp-content', f'Reports/KCA Call Logs/{name}')
    #df = pd.read_excel(download_url)
    df = df.sort_values(by=['Talk Time (Minutes)'], ascending=False)
    df['recording_url'] = df['CallId'].apply(extract_mp3_url)
    # Apply function to create new column
    df.groupby('recording_url').apply(download_mp3)

    return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
