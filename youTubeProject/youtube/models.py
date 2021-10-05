from django.db import models

# Create your models here.


class Comment(models.Model):
    video_id = models.CharField(max_length=100)
    comment = models.CharField(max_length=250)
    replies = models.CharField(max_length=250)
    likes = models.IntegerField()
    dislikes = models.IntegerField()