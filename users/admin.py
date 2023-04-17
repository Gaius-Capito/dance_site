from django.contrib import admin

from users.models import UserAccess


class UserAccessAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'available_courses',
    )
    empty_value_display = '-пусто-'


admin.site.register(UserAccess, UserAccessAdmin)
