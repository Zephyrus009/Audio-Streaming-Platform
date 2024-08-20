from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    album_title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=1000)
    cover_image = models.ImageField(blank=False)
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

class album_songs(models.Model):
    song_title = models.CharField(max_length=1000)
    album_title = models.CharField(max_length=1000)
    song = models.FileField(upload_to="media/songs")
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

