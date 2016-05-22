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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(attrs={
                                   'required': 'required'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'required': 'required'}),
                               label='Password')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(
                                   attrs={'required': 'required'}))
    email = forms.CharField(max_length=100, label='Email',
                            widget=forms.EmailInput(attrs=
                                                    {'required': 'required'}))
    password = forms.CharField(max_length=160, label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'required': 'required'}))
    password2 = forms.CharField(max_length=160,
                                label='Retype password',
                                widget=forms.PasswordInput(
                                    attrs={'required': 'required'}))
    address = forms.CharField(max_length=100, label='address',
                               widget=forms.TextInput(
                                   attrs={'required': 'required'}))
    country = forms.CharField(max_length=100, label='country',
                              widget=forms.TextInput(
                                  attrs={'required': 'required'}))
    city = forms.CharField(max_length=100, label='city',
                              widget=forms.TextInput(
                                  attrs={'required': 'required'}))

    phone = forms.IntegerField(label='Phone number', widget=forms.NumberInput(
        attrs={'required': 'required'}))

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#
#     def clean_password(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         user = authenticate(username=username,password=password)
#         if user is None:
#             raise forms.ValidationError("Incorrect username or password")
#         return password
        
    

