from __future__ import unicode_literals

from django.db import models
from django import forms
from magazin.models import Magazin

class Oferta(models.Model):
    magazin = models.ForeignKey(Magazin, related_name="oferte", null=True)
    titlu = models.CharField(max_length=100, null=True)
    descriere = models.CharField(max_length=300, null=True)
    data_inceperii = models.DateTimeField(null=True)
    data_sfarsirii = models.DateTimeField(null=True)


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['titlu', 'descriere', 'data_inceperii', 'data_sfarsirii']
