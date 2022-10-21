# Django Imports
from django.db import models


class Errorcode(models.Model):
    status_code = models.CharField(max_length=150)
    message = models.CharField(max_length=500)
