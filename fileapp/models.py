from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class File_Upload(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    file_field = models.FileField(upload_to="")

    def __str__(self):
        return self.title