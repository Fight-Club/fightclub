from django.conf.urls import patterns, url
from whowin.views import FightView, FighterListView, TopTenView, FighterDetailView, AboutView, BottomTenView, StatsView

urlpatterns = patterns('',
    url(r'^fight/(?P<id>\w+)/$', FightView.as_view(), name='fight'),
    url(r'^fighters/$', FighterListView.as_view(), name='list'),
    url(r'^topten/$', TopTenView.as_view(), name='topten'),
    url(r'^bottomten/$', BottomTenView.as_view(), name='bottomten'),
    url(r'^fighters/(?P<slug>[\w-]+)/', FighterDetailView.as_view(), name='detail'),
    url(r'^stats/$', StatsView.as_view(), name='stats'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    
)