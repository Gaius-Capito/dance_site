from django.contrib.auth import get_user_model
from django.db import models

from courses.models import Course


User = get_user_model()


class UserAccess(models.Model):
    user = models.OneToOneField(
        User,
        related_name='access_user',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    available_courses = models.ForeignKey(
        Course,
        related_name='available_courses',
        verbose_name='Доступные курсы',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = 'Доступ к курсам'
        verbose_name_plural = 'Доступ к курсам'

    def __str__(self):
        return f'{self.user}_{self.available_courses}'
