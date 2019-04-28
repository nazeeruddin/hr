# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class application(models.Model):

    first_name = models.CharField(max_length=50, null=True, blank=True, default='N/A')
    last_name = models.CharField(max_length=10, null=True, blank=True, default='N/A')
    status = models.CharField(max_length=10, null=True, blank=True, default='N/A')