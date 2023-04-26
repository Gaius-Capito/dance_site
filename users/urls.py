from django.contrib.auth.views import (
    LogoutView, LoginView,
    PasswordResetCompleteView, PasswordResetDoneView
)
from django.urls import path

from users import views
from users.views import CustomPasswordResetView, CustomPasswordResetConfirmView

app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        views.SignUp.as_view(template_name='users/signup.html'),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'password_reset/',
        CustomPasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'reset/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

]
