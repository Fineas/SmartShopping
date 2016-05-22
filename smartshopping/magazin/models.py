from __future__ import unicode_literals

from django import forms
from django.db import models
from django.contrib.auth.models import User


class LantMagazine(models.Model):
    user_owner = models.ForeignKey(User, related_name="lanturi", null=True)
    nume = models.CharField(max_length=100, null=True)
    cod = models.CharField(max_length=100, null=True)


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'required': 'required', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'required': 'required',
                                   'placeholder': 'Password'}))
    password2 = forms.CharField(label='Retype password',
                                widget=forms.PasswordInput(attrs={
                                    'required': 'required', 
                                    'placeholder': 'Confirm password'}))
    email = forms.CharField(label='Email',
                            widget=forms.EmailInput(
                                attrs={'required': 'required', 
                                       'placeholder': 'Contact email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError("This email is already taken")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if ('password' in self.cleaned_data and
            'password2' in self.cleaned_data and
            self.cleaned_data['password'] != self.cleaned_data['password2']):
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password


class LantMagazineForm(forms.ModelForm):
    nume = forms.CharField(label='U', widget=forms.TextInput(attrs={
        'required': 'required', 'placeholder': 'Numele lantului'}))
    cod = forms.IntegerField(label='Username', widget=forms.NumberInput(attrs={
        'required': 'required', 'placeholder': 'Codul de identificare'}))

    class Meta: 
        model = LantMagazine
        fields = ['nume', 'cod']


class Magazin(models.Model):
    lant = models.ForeignKey(LantMagazine, related_name='magazine', null=True)
    nume = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    adresa = models.CharField(max_length=300, null=True)


class MagazinForm(forms.ModelForm):
    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])


    class Meta:
        model = Magazin
        fields = ['nume', 'city', 'country', 'adresa']
