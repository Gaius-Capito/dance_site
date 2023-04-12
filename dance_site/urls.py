from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('', include('content.urls', namespace='content')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('courses/', include('courses.urls', namespace='courses'))
]
