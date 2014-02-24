from django.conf.urls import patterns, url
from whowin.views import FightView, FighterListView, RankResultsView

urlpatterns = patterns('',
    url(r'^$', FightView.as_view(), name='home'),
    url(r'fighters/', FighterListView.as_view()),
    url(r'results/', RankResultsView.as_view(), name='results'),
    
)