from django.db import models


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
    Fighter1 = models.ForeignKey(Fighter, related_name='fighter1')
    Fighter2 = models.ForeignKey(Fighter, related_name='fighter2')

    Fighter1_start_rating = models.DecimalField(max_digits=8, decimal_places=2)
    Fighter2_start_rating = models.DecimalField(max_digits=8, decimal_places=2)

    winner = models.ForeignKey(Fighter, related_name='winner')
    loser = models.ForeignKey(Fighter, related_name='loser')
    completed_datetime = models.DateTimeField(auto_now_add=True)
