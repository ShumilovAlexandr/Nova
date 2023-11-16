from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class FileUpload:

    g_auth = GoogleAuth()

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def create_and_upload_file(self, name: str, data: str) -> dict:
        try:
            drive = GoogleDrive(g_auth)
            my_file = drive.CreateFile({"title": name})
            my_file.SetContentString(data)
            my_file.Upload()

            return {"name": name,
                    "data": data}
        except Exception as e:
            return {"message": "Unexpected error. Check your code!"}

# TODO скрипт рабочий. Понять, почему не вызывается