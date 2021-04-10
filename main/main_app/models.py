from django.db import models


class Widgets(models.Model):
    description = models.CharField(max_length=60)
    quantity = models.IntegerField(max_length=50)


