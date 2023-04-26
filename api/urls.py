from django.urls import path, include
from rest_framework import routers
from api.views import ScheduleViewSet

router = routers.DefaultRouter()
router.register('schedules', ScheduleViewSet, basename='schedules')

urlpatterns = [
    path('', include(router.urls)),
]
