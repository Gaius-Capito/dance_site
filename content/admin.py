from django.contrib import admin

from content.models import Content, Images


class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title_main',
        'content_main',
        'title_about',
        'content_about',
    )
    empty_value_display = '-пусто-'


class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'image_about_us',
        'image_about_them',
    )


admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
