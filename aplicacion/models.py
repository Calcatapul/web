from django.conf import settings
from django.db import models
from django.utils import timezone


class Modelo(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=200)


