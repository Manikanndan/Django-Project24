from django import forms
from django.forms import fields
from django.forms.models import _Labels
from app.models import *
from django.forms import widgets
from django.utils.translation import gettext_lazy as gt


class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['topic_name']
        widgets={'name':forms.PasswordInput,'url':forms.Textarea(attrs={'cols':5,'rows':5})}
        help_texts={'name':gt('enter url')}
       # label={'name':gt('FirstName')}


class AccessForm(forms.ModelForm):
    class Meta():
        model=Access_Records
        fields='__all__'