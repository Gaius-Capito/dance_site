from django.shortcuts import render

from content.models import Content, Images


def index(request):
    content = Content.objects.get(pk=1)
    images = Images.objects.last()
    context = {
        'content': content,
        'images': images,
    }
    return render(request, 'content/index.html', context)
