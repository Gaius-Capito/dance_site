from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from schedule.models import Schedule


@login_required
def schedule(request):
    content = Schedule.objects.filter(user=request.user).all()
    return render(request, 'schedule/schedule.html', {'schedule': content})
