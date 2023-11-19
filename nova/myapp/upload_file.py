from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class FileUpload:

    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.g_auth = GoogleAuth()
        self.g_auth.LocalWebserverAuth()

    def create_and_upload_file(self) -> dict:
        try:
            drive = GoogleDrive(self.g_auth)
            my_file = drive.CreateFile({"title": self.name})
            my_file.SetContentString(self.data)
            my_file.Upload()

            return {"name": self.name,
                    "data": self.data}
        except Exception as e:
            print(e)
            return {"message": "Unexpected error. Check your code!"}

