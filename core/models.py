from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)


class Fighter(models.Model):
    name = models.CharField(max_length=32)
    categories = models.ManytoManyField(Category)
    description = models.CharField(max_length=1024)
    rating = models.DecimalField(default=1600, max_digits=8, decimal_places=2)


class Fight(models.Model):
    Fighter1 = models.ForeignKey(Fighter)
    Fighter2 = models.ForeignKey(Fighter)
