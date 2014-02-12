from django.conf.urls import patterns, url
from whowin.views import FightView

urlpatterns = patterns('',
    url(r'^$', FightView.as_view(), name='home'),
)