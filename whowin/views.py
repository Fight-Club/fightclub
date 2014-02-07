from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from whowin.models import Fight

class MatchView(generic.MatchView):
	model = Fight
	template_name = 'fight/match.html'