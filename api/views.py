from rest_framework.generics import ListAPIView
from schedule.models import Schedule
from api.serializers import ScheduleSerializer


class ScheduleListView(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Schedule.objects.filter(user=user_id)
