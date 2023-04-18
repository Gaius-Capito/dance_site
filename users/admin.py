from django.contrib import admin

from users.models import UserAccess


class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'get_available_courses')
    fields = ('user', 'available_courses')

    def get_available_courses(self, obj):
        return "\n".join(
            [course.title for course in obj.available_courses.all()])

    get_available_courses.short_description = 'Доступные курсы'


admin.site.register(UserAccess, UserAccessAdmin)
