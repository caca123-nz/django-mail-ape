# /user/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.forms import CustomAuthenticationForm

app_name = "user"
urlpatterns=[
  path("login/", LoginView.as_view(authentication_form=CustomAuthenticationForm), name="login")
]