from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from courses.models import Course, Video
from users.models import UserAccess


def courses(request):
    user_access = UserAccess.objects.filter(user=request.user).first()
    available_courses = user_access.available_courses.all()
    courses = Course.objects.filter(
        id__in=available_courses.values_list('id', flat=True))
    return render(request, 'courses/courses.html', {'courses': courses})


def video(request, slug):
    user_access = UserAccess.objects.filter(user=request.user).first()
    available_courses = user_access.available_courses.all()
    courses = Course.objects.filter(
        id__in=available_courses.values_list('id', flat=True))
    content = Video.objects.filter(
        course_video__slug=slug,
        course_video__in=courses
    ).prefetch_related('course_video').all()
    if not content:
        raise PermissionDenied
    return render(
        request,
        'courses/videolessons.html',
        {'videos': content}
    )
