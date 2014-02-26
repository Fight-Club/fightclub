from django.conf.urls import patterns, url
from whowin.views import FightView, FighterListView, RankResultsView, FighterDetailView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', FightView.as_view(), name='fight'),
    url(r'^fighters/$', FighterListView.as_view(), name='list'),
    url(r'^results/$', RankResultsView.as_view(), name='results'),
    url(r'^fighters/(?P<slug>[\w-]+)/', FighterDetailView.as_view(), name='detail'),
    
)