from django.urls import path

from courses import views


app_name = 'courses'


urlpatterns = [
    path('', views.courses, name='courses'),
    path('lessons/<slug:slug>/', views.video, name='lessons'),
]
