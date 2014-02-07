from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template.response import TemplateResponse

from whowin.models import Fight

class MatchView(generic.TemplateView):
	model = Fight
	template_name = 'whowin/templates/whowin/match.html'