from django.db import models
import datetime


class Date(models.Model):
    date_time = models.DateTimeField(null=True)
