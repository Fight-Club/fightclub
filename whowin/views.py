from django.views import generic
from django.template.response import TemplateResponse
from random import randint

from whowin.models import Fight, Fighter


class MatchView(generic.DetailView):
	model = Fight
	template_name = 'whowin/match.html'
	
	def get_object(self):
		return Fight.objects.order_by('?')[0]

	context_object_name = 'fight'
	

class RankResultsView(generic.ListView):
	queryset = Fighter.objects.order_by('-rating')
	context_object_name = 'fighter_list'
	template_name = 'whowin/results.html'

