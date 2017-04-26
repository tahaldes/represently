# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Zipcode,Rep, District

# Register your models here.

admin.site.register(Zipcode)
admin.site.register(Rep)
admin.site.register(District)