# mailinglist/forms.py
from django import forms
from django.contrib.auth import get_user_model

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
    widget=forms.TextInput(attrs={"class": "form-control"})
  )

  body = forms.CharField(
    widget=forms.Textarea(attrs={"class": "form-control"})
  )

  class Meta:
    model = Message
    fields = ["mailing_list", "subject", "body", ]

class MailingListForm(forms.ModelForm):
  owner = forms.ModelChoiceField(
    widget=forms.HiddenInput,
    queryset=get_user_model().objects.all(),
    disabled=True
  )
  name = forms.CharField(
    widget=forms.TextInput(attrs={"class": "form-control"})
  )

  class Meta:
    model = MailingList
    fields = ["owner", "name", ]