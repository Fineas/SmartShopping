from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import md5
from django.core.urlresolvers import reverse



class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    telefon = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    cod = models.CharField(max_length=100,null=True, blank=True)


    def gravatar_photo(self):
        usshash = md5.new()
        usshash.update(self.user.email)
        return usshash.hexdigest()