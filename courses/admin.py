from django.contrib import admin

from courses.models import Course, CourseVideo, Video


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'preview',
        'description',
        'slug',
    )
    empty_value_display = '-пусто-'


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'url',
        'courses',
    )
    empty_value_display = '-пусто-'

    def courses(self, obj):
        return ", ".join([course.title for course in obj.course_video.all()])

    courses.short_description = 'Курсы'


class CourseVideoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'video',
        'course',
    )
    empty_value_display = '-пусто-'


admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseVideo, CourseVideoAdmin)
