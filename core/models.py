from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "categories"


class Fighter(models.Model):
    name = models.CharField(max_length=32)
    categories = models.ManyToManyField(Category)
    description = models.CharField(max_length=1024)
    rating = models.DecimalField(default=1600, max_digits=8, decimal_places=2)
    reference = models.URLField()


class Fight(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)

    winner = models.ForeignKey(Fighter, related_name='winner')
    loser = models.ForeignKey(Fighter, related_name='loser')

    winner_start_rating = models.DecimalField(max_digits=8, decimal_places=2)
    loser_start_rating = models.DecimalField(max_digits=8, decimal_places=2)

    completed_timestamp = models.DateTimeField(auto_now_add=True)
