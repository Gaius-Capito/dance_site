from django.db import models


class Course(models.Model):
    title = models.CharField(
        'Название курса',
        max_length=120
    )
    preview = models.CharField('ссылка на картинку', max_length=32)
    description = models.TextField('Описание курсов')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(
        'Название видеоурока',
        max_length=120
    )
    url = models.CharField('ссылка на видео', max_length=32)
    course_video = models.ManyToManyField(Course, through='CourseVideo')

    class Meta:
        verbose_name = 'Видеоурок'
        verbose_name_plural = 'Видеоуроки'

    def __str__(self):
        return self.title


class CourseVideo(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course} {self.video}'



