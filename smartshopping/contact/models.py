from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact(models.Model):
    frist_name = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)
    message = models.CharField(max_length=1000, null=True)
