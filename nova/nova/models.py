from django.db import models
from gdstorage.storage import GoogleDriveStorage


gd_storage = GoogleDriveStorage()


class File(models.Model):
    data = models.TextField()
    name = models.CharField(max_length=20)
    map_data = models.FileField(upload_to='files', storage=gd_storage)

