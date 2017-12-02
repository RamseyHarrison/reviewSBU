# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class foodItem(models.Model):
    name = models.TextField()
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=200,default="east")


class foodItemComment(models.Model):
    foodItem = models.ForeignKey(foodItem)
    comment = models.CharField(max_length=500)




