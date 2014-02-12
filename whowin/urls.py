from django.conf.urls import patterns, url
from whowin.views import FightView, random_fight, RankResultsView

urlpatterns = patterns('',
    url(r'^$', random_fight, name='home'),
    url(r'^fight/(?P<fight_id>\d+)/$', FightView.as_view(), name='fight_view'),
    url(r'^results/$', RankResultsView.as_view()),
)