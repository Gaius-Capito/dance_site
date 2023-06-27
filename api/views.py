from rest_framework import viewsets
from api.permissions import IsAdminOrReadOnly


from api.serializers import ScheduleSerializer
from schedule.models import Schedule


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        user_id = self.request.user.id
        return Schedule.objects.filter(user=user_id)
