from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Email', 'class': 'form-control'}
        )
    )
