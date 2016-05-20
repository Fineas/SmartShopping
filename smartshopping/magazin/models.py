from __future__ import unicode_literals

from django import forms
from django.db import models
from django.contrib.auth.models import User


class LantMagazine(models.Model):
    user_owner = models.ForeignKey(User, related_name="lanturi", null=True)
    nume = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    cod = models.CharField(max_length=100, null=True)


class LantMagazineForm(forms.ModelForm):
    class Meta: 
        model = LantMagazine
        fields = ['nume', 'email', 'cod']


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
