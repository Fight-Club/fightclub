from django.db import models


class Fighter(models.Model):
	name = models.CharField(max_length=50)
	rating = models.DecimalField(default=1600, max_digits=8, decimal_places=2)
	fightswon = models.IntegerField(default=0)
	fightslost = models.IntegerField(default=0)

	def __unicode__(self):
	    return unicode(self.name)

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
		loser.rating += 20 * (0 - loserval)
		
		loser.save()
		winner.save()