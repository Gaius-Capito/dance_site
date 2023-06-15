from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ScheduleListView

router = DefaultRouter()
# router.register('schedules', ScheduleListView, basename='schedules')

urlpatterns = [
    # path('', include(router.urls)),
    path('schedules/', ScheduleListView.as_view()),
    path('', include('djoser.urls.jwt')),
]