from django.db import models

# Create your models here.
class Things(models.Model):
    name = models.CharField(blank=False, max_length=12, unique=True)
    description = models.CharField(blank=True, max_length=30)
    quantity = models.IntegerField(blank=True)