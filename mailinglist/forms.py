# mailinglist/forms.py
from django import forms

from mailinglist.models import Subscriber, MailingList, Message

class SubscriberForm(forms.ModelForm):
  mailing_list = forms.ModelChoiceField(
    widget = forms.HiddenInput,
    queryset = MailingList.objects.all(),
    disabled = True
  )
  email = forms.EmailField(
    widget=forms.EmailInput(attrs={"class": "form-control"})
  )

  class Meta:
    models = Subscriber
    fields = ["mailing_list", "email", ]
  
class MessageForm(forms.ModelForm):
  mailing_list = forms.ModelChoiceField(
    widget = forms.HiddenInput,
    queryset = MailingList.objects.all(),
    disabled = True
  )
  subject = forms.CharField(
    widget=forms.TextInput(attr={"class": "form-control"})
  )

  body = forms.CharField(
    widget=forms.Textarea(attr={"class": "form-control"})
  )

  class Meta:
    model = Message
    fields = ["mailing_list", "subject", "body", ]