# coding: utf-8
from django.db import models

class Contribution(models.Model):
    name = models.CharField(max_length=200, verbose_name='Navn')
    amount = models.FloatField(default=200.0, verbose_name='Beløp')
