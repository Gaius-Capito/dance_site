from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from courses.models import Course, Video
from users.models import UserAccess


def courses(request):
    if request.user.is_anonymous:
        courses = Course.objects.all()
        return render(request, 'courses/courses.html',
                      {'courses': courses,
                       'available_courses': []
                       })
    courses = Course.objects.all()
    user_access = UserAccess.objects.filter(user=request.user).first()
    if not user_access:
        courses = Course.objects.all()
        return render(request, 'courses/courses.html',
                      {'courses': courses,
                       'available_courses': []
                       })
    available_courses = user_access.available_courses.all()
    available_courses = Course.objects.filter(
        id__in=available_courses.values_list('id', flat=True))
    context = {'courses': courses,
               'available_courses': available_courses,
               }
    return render(request, 'courses/courses.html', context)


def video(request, slug):
    if request.user.is_anonymous:
        videos = Video.objects.filter(course_video__title='Панда')
        return render(
            request,
            'courses/videolessons.html',
            {'videos': videos}
        )
    user_access = UserAccess.objects.filter(user=request.user).first()
    if not user_access:
        videos = Video.objects.filter(course_video__title='Панда')
        return render(
            request,
            'courses/videolessons.html',
            {'videos': videos}
        )
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
