# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from validators import validate_min_length


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField(validators=[validate_min_length])
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
