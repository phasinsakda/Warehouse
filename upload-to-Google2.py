from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

upload_file_list = ['Recorded_MobileApp.avi']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1bbF4m3RZOJC3_eJeafXsEnFU4Il0OgAq'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.
    

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1bbF4m3RZOJC3_eJeafXsEnFU4Il0OgAq')}).GetList()
for file in file_list:
    print('title: %s, id: %s, Link: %s' % (file['title'], file['id'], file['alternateLink']));
    
