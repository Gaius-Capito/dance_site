from django.contrib import admin

from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title_main',
        'content_main',
        'title_about',
        'content_about',
    )
    empty_value_display = '-пусто-'


admin.site.register(Content, ContentAdmin)
