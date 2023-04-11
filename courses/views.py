from django.shortcuts import render

from courses.models import Course, Video


def courses(request):
    content = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': content})


def video(request):
    content = Video.objects.all()
    return render(
        request,
        'courses/videolessons.html',
        {'videos': content}
    )



