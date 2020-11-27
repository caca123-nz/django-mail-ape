# /user/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.forms import CustomAuthenticationForm
from user import views

app_name = "user"
urlpatterns=[
  path("register/", views.RegisterView.as_view(), name="register"),
  path("login/", LoginView.as_view(authentication_form=CustomAuthenticationForm), name="login"),
  path("logout/", LogoutView.as_view(), name="logout")
]