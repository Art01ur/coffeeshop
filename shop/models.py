from django.db import models
from django.utils import timezone


class Type(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    country = models.CharField(max_length=50)
    roast = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
