from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

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