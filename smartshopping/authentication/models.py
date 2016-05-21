from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse



class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    telefon = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=36, null=True)
    address = models.CharField(max_length=100, null=True)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def clean_password(self): 
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError("Incorrect username or password")
        return password
        
    

