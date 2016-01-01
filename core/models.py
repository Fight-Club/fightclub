import random
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class FighterManager(models.Manager):
    def sample_two_fighters(self):
        last = self.all().count()
        index1, index2 = random.sample(range(last), 2)

        Fighter1 = self.all()[index1]
        Fighter2 = self.all()[index2]

        return Fighter1, Fighter2


class Fighter(models.Model):
    name = models.CharField(max_length=32)
    categories = models.ManyToManyField(Category)
    description = models.CharField(max_length=1024)
    rating = models.DecimalField(default=1600, max_digits=8, decimal_places=2)
    reference = models.URLField()

    objects = FighterManager()

    def __str__(self):
        return self.name


class Fight(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)

    winner = models.ForeignKey(Fighter, related_name='winner')
    loser = models.ForeignKey(Fighter, related_name='loser')

    winner_start_rating = models.DecimalField(max_digits=8, decimal_places=2)
    loser_start_rating = models.DecimalField(max_digits=8, decimal_places=2)

    completed_timestamp = models.DateTimeField(auto_now_add=True)
