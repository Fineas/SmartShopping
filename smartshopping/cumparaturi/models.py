from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User

from magazin.models import Magazin


class Cumparaturi(models.Model):
    magazin = models.OneToOneField(Magazin, primary_key=True, default=None)
    user = models.OneToOneField(User, primary_key=True, default=None)
