from django.urls import path

from content import views


app_name = 'content'


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
]
