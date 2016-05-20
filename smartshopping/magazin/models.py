from __future__ import unicode_literals

from django.db import models
from django import forms


class LantMagazine(models.Model):
    nume = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    cod = models.CharField(max_length=100, null=True)

class LantMagazineForm(forms.ModelForm):


    class Meta: 
        model = LantMagazine
        fields = ['nume', 'email', 'cod']

