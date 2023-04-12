from django.shortcuts import get_object_or_404, render

from courses.models import Course, Video


def courses(request):
    content = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': content})


def video(request, slug):
    content = Video.objects.filter(
        course_video__slug=slug).prefetch_related('course_video').all()
    return render(
        request,
        'courses/videolessons.html',
        {'videos': content}
    )
