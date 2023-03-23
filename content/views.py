from django.shortcuts import render

from content.models import Content


def index(request):
    content = Content.objects.get(pk=1)
    return render(request, 'content/index.html', {'content': content})
