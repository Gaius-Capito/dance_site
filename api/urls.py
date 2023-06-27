from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ScheduleViewSet

router = DefaultRouter()
router.register('schedules', ScheduleViewSet, basename='schedules')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
