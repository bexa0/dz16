from django.db import models


class VideoCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AudioCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Screenshot(models.Model):
    image = models.ImageField(upload_to='screenshot')


class Video(models.Model):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video')

    def __str__(self):
        return f'{self.pk} - video - {self.category}'


class Audio(models.Model):
    category = models.ForeignKey(AudioCategory, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio')

    def __str__(self):
        return f'{self.pk} - audio - {self.category}'
