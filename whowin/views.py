from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template.response import TemplateResponse

from whowin.models import Fight, Fighter

class MatchView(generic.TemplateView):
	model = Fight
	template_name = 'whowin/match.html'

class RankResultsView(generic.ListView):
	queryset = Fighter.objects.order_by('-rating')
	context_object_name = 'fighter_list'
	template_name = 'whowin/results.html'

