import datetime
from django.db import models


class Date(models.Model):
    date_time = models.DateTimeField(null=False)



