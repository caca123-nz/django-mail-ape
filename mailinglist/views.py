# Mailinglist/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from mailinglist.models import MailingList

class MailingListView(LoginRequiredMixin, ListView):
  context_object_name = "mailing-list"
  template_name = "mailinglist/mailing-list.html"

  def get_queryset(self):
    return MailingList.objects.filter(owner=self.request.user)