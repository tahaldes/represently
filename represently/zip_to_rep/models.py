# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.forms import forms

from . import calculator

# Create your models here.
class Zipcode(models.Model):
    zip = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.zip

    def get_absolute_url(self):
        return reverse('zip_to_rep:index')
    #('zip_to_rep:zipcode_detail',kwargs={'zip':self.zip})
    #('zip_to_rep:index')
    #('zip_to_rep:zipcode_detail', kwargs={'zip': self.zip})

class District(models.Model):
    zip_code = models.ForeignKey(Zipcode)
    dist_state = models.CharField(max_length=5)
    dist_num = models.IntegerField()

    def __str__(self):
        return self.dist_state + str(self.dist_num)


class Rep(models.Model):
    dist = models.ForeignKey(District)
    rep_name = models.CharField(max_length=250)
    recent_bill = models.CharField(max_length=250)
    how_voted = models.CharField(max_length=15)

    def __str__(self):
        return self.rep_name
