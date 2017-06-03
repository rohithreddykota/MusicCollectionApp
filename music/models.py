from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    album_logo = models.FileField()
    isfavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + '-' + self.artist


class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=255)
    audio_file = models.FileField()
    isfavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
