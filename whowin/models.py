from django.db import models
from elo import rate_1vs1

class Fighter(models.Model):
	name = models.CharField(max_length=50)
	rating = models.DecimalField(default=1600, max_digits=8, decimal_places=2)
	url = models.URLField(default='')

	def __unicode__(self):
	    return unicode(self.name)

class Fight(models.Model):
	member1 = models.ForeignKey(Fighter, related_name='fighter_1')
	member2 = models.ForeignKey(Fighter, related_name='fighter_2')

	def __unicode__(self):
		return unicode(self.member1)

	def fight(self):
		rate_1vs1(member1.rating(), member2.rating())
