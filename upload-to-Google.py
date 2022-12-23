from googleapiclient.http import MediaFileUpload 
from Google import Create_Service

CLIENT_SECRET_FILE ="client_secrets.json"
API_NAME ='drive'
API_VERSION='v3'
SCOPES =[ 'https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id='1AwYg-aklIfxe5GxatdDVEcuhcdcVnDz3'
file_names=['Recorded_QR.avi']
mime_types=['video/x-msvideo']

for file_name, mime_type in zip(file_names,mime_types):
    file_metadata={
        'name': file_name,
        'parent': [folder_id]
        }
    
    media = MediaFileUpload('C:/Users/Focus/.spyder-py3/Godang/AutoTube/{0}'.format(file_name), mimetype=mime_type)
    
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()