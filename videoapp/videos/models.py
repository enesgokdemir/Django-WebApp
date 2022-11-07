from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)

class Video(models.Model):
    video_adi=models.CharField(max_length=200)
    aciklama=models.TextField()
    resim=models.CharField(max_length=100)
    video_video=models.CharField(max_length=100)
    anasayfa=models.BooleanField(default=False)
    