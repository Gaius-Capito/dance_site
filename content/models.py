from django.db import models


class Content(models.Model):
    title_main = models.CharField(
        'Название заглавной странички',
        max_length=120
    )
    content_main = models.TextField()
    title_about = models.CharField(max_length=120)
    content_about = models.TextField()
    price = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Содержание главной страницы'
        verbose_name_plural = 'Содержание главной страницы'

class Images(models.Model):
    image_about_us = models.ImageField(
        'картинка "about_us"',
        upload_to='static/img/content/'
    )
    image_about_them = models.ImageField(
        'картинка "about_them"',
        upload_to='static/img/content/'
    )

    class Meta:
        verbose_name = 'Изображение на главной странице'
        verbose_name_plural = 'Изображения на главной странице'
