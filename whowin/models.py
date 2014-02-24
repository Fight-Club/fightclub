from django.db import models
from django.template.defaultfilters import slugify


class Fighter(models.Model):
	name = models.CharField(max_length=50)
	rating = models.DecimalField(default=1600, max_digits=8, decimal_places=2)
	fightswon = models.IntegerField(default=0)
	fightslost = models.IntegerField(default=0)
	slug = models.SlugField(max_length=50, unique=True)

	def __unicode__(self):
	    return unicode(self.name)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(self).save(*args, **kwargs)

class Fight(models.Model):
	member1 = models.ForeignKey(Fighter, related_name='fighter_1')
	member2 = models.ForeignKey(Fighter, related_name='fighter_2')
	
	def __unicode__(self):
		return '%s v %s' % (self.member1, self.member2)

	def rankupdate(self, winner):
		if winner == self.member1:
			loser = self.member2
		else:
			loser = self.member1

		winnerval = 1 / (1 + 10 ** ((loser.rating - winner.rating)/400))
		loserval = 1 - winnerval

		winner.rating += 20 * (1 - winnerval)
		winner.fightswon += 1
		loser.rating += 20 * (0 - loserval)
		loser.fightslost += 1
		
		loser.save()
		winner.save()