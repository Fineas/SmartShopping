from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from django.core.urlresolvers import reverse



class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    telefon = models.IntegerField(null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=36, null=True)
    address = models.CharField(max_length=100, null=True)
    cod = models.CharField(max_length=100, null=True, blank=True)
