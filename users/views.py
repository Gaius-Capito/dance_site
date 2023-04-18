from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import CreationForm

from users.models import UserAccess


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('content:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        UserAccess.objects.create(user=user)
        return response
