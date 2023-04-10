from django.shortcuts import render

from videolessons.models import Course, Video


def courses(request):
    content = Course.objects.all()
    return render(request, 'videolessons/courses.html', {'courses': content})


def video(request):
    content = Video.objects.all()
    return render(
        request,
        'videolessons/videolessons.html',
        {'videos': content}
    )



