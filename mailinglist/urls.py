# /mailinglist/urls.py
from django.urls import path
from mailinglist import views

app_name="mailinglist"

urlpatterns=[
  path("", views.MailingListView.as_view(), name="mailing-list"),
  path("new/", views.CreateMailingListView.as_view(), name="create-mailing-list")
]