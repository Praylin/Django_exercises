from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length = 30)
    album_title = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 20)
    album_logo = models.CharField(max_length = 250)

    def __str__(self):
        return self.artist + ' : ' + self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    song_title = models.CharField(max_length = 100)
    file_type = models.CharField(max_length = 10)
