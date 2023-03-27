from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from users.models import User
from users.forms import CreationForm


class SignUp(FormView):
    form_class = CreationForm
    template_name = 'users/signup.html'

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        raw_password = form.cleaned_data['password1']
        usesrname = first_name+last_name
        user = User.objects.create_user(
            username=usesrname,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=raw_password
        )
        login(self.request, user)
        return HttpResponseRedirect(reverse('content:index'))
