from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

gauth = GoogleAuth()
scope = ["https://www.googleapis.com/auth/drive"]
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name("drivezipper_sa.json", scope)
drive = GoogleDrive(gauth)

def uploadFile(file, dir):
    pass

def getFolders():
    f = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    folders = dict()
    for file in f:
        if(file['mimeType'] == "application/vnd.google-apps.folder"):
            folders[file['title']] = file['id']
    return folders