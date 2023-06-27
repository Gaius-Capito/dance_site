from django.contrib import admin

from schedule.models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'date',
        'lesson_materials',
        'content',
    )
    empty_value_display = '-пусто-'


admin.site.register(Schedule, ScheduleAdmin)