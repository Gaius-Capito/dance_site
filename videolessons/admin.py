from django.contrib import admin

from videolessons.models import Course, CourseVideo, Video


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'preview',
        'description',
    )
    empty_value_display = '-пусто-'


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'url',
    )
    empty_value_display = '-пусто-'


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
