from django.db import models


class File(models.Model):
    data = models.TextField()
    name = models.CharField(max_length=20)

