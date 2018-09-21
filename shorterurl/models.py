# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class URLs(models.Model):
    shortedURL = models.CharField(max_length=15, primary_key=True)
    targetURL = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True, blank=True)
