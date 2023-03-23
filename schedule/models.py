from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Schedule(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Ученик'
    )
    date = models.CharField('Дата занятия', max_length=40)
    content = models.TextField('Содержание')
    lesson_materials = models.TextField('Материалы к занятию')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
