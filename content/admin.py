from django.contrib import admin

from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title_main',
        'content_main',
        'title_about',
        'content_about',
        'image_about_us',
    )
    empty_value_display = '-пусто-'
    exclude = ('image_about_us',)


admin.site.register(Content, ContentAdmin)
