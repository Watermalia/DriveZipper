from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

class Google_Drive:
    def __init__(self, folder_id):
        self.gauth = GoogleAuth()
        self.scope = ["https://www.googleapis.com/auth/drive"]
        self.gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name("drivezipper_sa.json", self.scope)
        self.drive = GoogleDrive(self.gauth)
        self.folder_id = folder_id

    def uploadFile(self, filename, parent):
        newFile = self.drive.CreateFile({'title': filename, 'parents': [{'id': parent}]})
        newFile.Upload()

    def getFolders(self):
        f = self.drive.ListFile({"q": "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        folders = dict()
        for file in f:
            if(file['mimeType'] == "application/vnd.google-apps.folder"):
                folders[file['title']] = file['id']
        return folders

    def create_folder(self, folderName):
        file_metadata = {
            'title': folderName,
            'parents': [{'id': self.folder_id}], #parent folder
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = self.drive.CreateFile(file_metadata)
        folder.Upload()

    def delete_folder(self, folderName):
        f = self.drive.ListFile({"q": "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        folders = dict()
        for file in f:
            if(file['mimeType'] == "application/vnd.google-apps.folder" and file['title'] == folderName):
                file.Delete()

drive = Google_Drive("1vNKiSTNI8RtQNnwQw8xGyCkwghJhvUGq")
drive.delete_folder("Poop")