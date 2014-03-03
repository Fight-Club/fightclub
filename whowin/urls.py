from django.conf.urls import patterns, url
from whowin.views import FightView, FighterListView, RankResultsView, FighterDetailView
from whowin import views

urlpatterns = patterns('',
    url(r'^fight/(?P<id>\w+)/$', FightView.as_view(), name='fight'),
    url(r'^fighters/$', FighterListView.as_view(), name='list'),
    url(r'^results/$', RankResultsView.as_view(), name='results'),
    url(r'^fighters/(?P<slug>[\w-]+)/', FighterDetailView.as_view(), name='detail'),
    url(r'^stats/$', views.stats_view, name='stats'),
    
)