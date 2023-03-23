from django.db import models


class Content(models.Model):
    title_main = models.CharField(max_length=120)
    content_main = models.TextField()
    title_about = models.CharField(max_length=120)
    content_about = models.TextField()
