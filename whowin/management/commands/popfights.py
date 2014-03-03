from django.core.management.base import BaseCommand
from whowin.models import Fight, Fighter

class Command(BaseCommand):

	def handle(self, *args, **options):
		all_fights = Fight.objects.all()
		for fight in all_fights:
			fight.delete()
			
		all_fighters = Fighter.objects.all()
		for fighter1 in all_fighters:
			for fighter2 in all_fighters:
				if fighter1 != fighter2:
					fight = Fight(member1=fighter1, member2=fighter2)
					fight.save()

		total = 0
		for member in all_fighters:
			total += member.fightswon
			total += member.fightslost

		print total/2
