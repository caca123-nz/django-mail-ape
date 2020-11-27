# Mailinglist/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from mailinglist.forms import MailingListForm
from mailinglist.models import MailingList

class MailingListView(LoginRequiredMixin, ListView):
  template_name = "mailinglist/mailing-list.html"

  def get_queryset(self):
    return MailingList.objects.filter(owner=self.request.user)
  
class CreateMailingListView(LoginRequiredMixin, CreateView):
  form_class = MailingListForm
  template_name = "mailinglist/mailing-list-form.html"
  context_object_name = "mailing-list"

  def get_initial(self):
    return {
      "owner": self.request.user.id
    }