from django.db import models
from django.http import JsonResponse

class ontel(models.Model):
    nama = models.PositiveIntegerField(default=0)
    