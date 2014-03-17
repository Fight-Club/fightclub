from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Fighter(models.Model):
    name = models.CharField(max_length=50)
    SIDE_CHOICES = (
        ('E', 'Evil'),
        ('G', 'Good'),
        ('N', 'Neutral'),
    )
    side = models.CharField(max_length=1, choices=SIDE_CHOICES, default='N')
    description = models.TextField(default='')
    slug = models.SlugField(default=0, max_length=50, unique=True)
    rating = models.DecimalField(default=1600, max_digits=8, decimal_places=2)
    fightswon = models.IntegerField(default=0)
    fightslost = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s' % (self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Fighter, self).save(*args, **kwargs)


class Fight(models.Model):
    member1 = models.ForeignKey(Fighter, related_name='fighter_1')
    member2 = models.ForeignKey(Fighter, related_name='fighter_2')
    user = models.ForeignKey(User, null=True, blank=True)

    member1_start_rank = models.IntegerField(null=True, blank=True)
    member1_end_rank = models.IntegerField(null=True, blank=True)
    member1_start_rating = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    member1_end_rating = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    member2_start_rank = models.IntegerField(null=True, blank=True)
    member2_end_rank = models.IntegerField(null=True, blank=True)
    member2_start_rating = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    member2_end_rating = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    winner = models.ForeignKey(Fighter, related_name='winner', null=True, blank=True)
    loser = models.ForeignKey(Fighter, related_name='loser', null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __unicode__(self):
        return '%s - %s v %s' % (self.start, self.member1, self.member2)

    def rankupdate(self, win):
        if win == self.member1:
            lose = self.member2
            win = self.member1
        else:
            lose = self.member1
            win = self.member2

        winnerval = 1 / (1 + 10 ** ((lose.rating - win.rating) / 400))
        loserval = 1 - winnerval

        win.rating += 20 * (1 - winnerval)
        win.fightswon += 1
        lose.rating += 20 * (0 - loserval)
        lose.fightslost += 1
        lose.save()
        win.save()
