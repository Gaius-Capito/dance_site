from django.conf import settings
from django.shortcuts import render

from content.models import Content, Images


def index(request):
    content = Content.objects.get(pk=1)
    images = Images.objects.last()
    tel_number = settings.TEL_NUMBER
    work_email = settings.WORK_EMAIL
    context = {
        'content': content,
        'images': images,
        'tel_number': tel_number,
        'work_email': work_email,
    }
    return render(request, 'content/index.html', context)


def contacts(request):
    return render(request, 'content/contacts.html')
