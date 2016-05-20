from __future__ import unicode_literals

from django.db import models

class Magazin(models.Model):
    nume = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    cod = models.CharField(max_length=100, null=True)
