from django.core.management.base import BaseCommand
from whowin.models import Fight, Fighter

class Command(BaseCommand):

	def handle(self, *args, **options):
		all_fighters = Fighter.objects.all()
		for fighter1 in all_fighters:
			for fighter2 in all_fighters:
				if fighter1 != fighter2:
					fight = Fight(member1=fighter1, member2=fighter2)
					fight.save()
