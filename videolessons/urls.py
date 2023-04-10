from django.urls import path

from videolessons import views


app_name = 'videolessons'


urlpatterns = [
    path('', views.courses, name='courses'),
    path('lessons/', views.video, name='videolessons'),
]
