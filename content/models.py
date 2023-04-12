from django.db import models


class Content(models.Model):
    title_main = models.CharField(
        'Название заглавной странички',
        max_length=120
    )
    content_main = models.TextField()
    title_about = models.CharField(max_length=120)
    content_about = models.TextField()

    class Meta:
        verbose_name = 'Содержание главной страницы'
        verbose_name_plural = 'Содержание главной страницы'
