from __future__ import print_function


import io
import os
from PIL import Image
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from oauth2client import client, file, tools

store = file.Storage('token.json')


def get_drive_creds():
    SCOPES = "https://www.googleapis.com/auth/drive.readonly"
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)
    return creds

def download_file(id, creds, section_index, img_index):
# def download_file(id):
    """Downloads a file
    Args:
        id: List of file IDs to download
    Returns : IO object with location.

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # SCOPES = "https://www.googleapis.com/auth/drive.readonly"
    # flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    # creds = tools.run_flow(flow, store)
    creds = creds

    # Get the current directory
    current_directory = os.getcwd()


    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds, static_discovery=False)

        # Generate a unique filename based on the section and img index 
        filename = f'image_{section_index}_{img_index}.jpg'
        save_path = os.path.join(current_directory, filename)

        # pylint: disable=maybe-no-member
        request = service.files().get_media(fileId=id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')
        # Save the downloaded file to the specified path
        with open(save_path, 'wb') as f:
            f.write(file.getvalue())
        print(f'Successfully saved the file at: {save_path}')
        image = Image.open(filename)
        image.thumbnail((320, 320))
        image.save(filename)

    except HttpError as error:
        print(F'An error occurred: {error}')

    return filename


if __name__ == '__main__':
    creds = get_drive_creds()
    download_file(id, creds, 1)
    # download_file(id, creds, 2)
    # download_file(id, creds, 3)
    # download_file(id)
