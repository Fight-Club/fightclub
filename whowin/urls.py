from django.conf.urls import patterns, url

from whowin import views

urlpatterns = patterns('',
    url(r'^match/$', views.MatchView.as_view()),
    url(r'^results/$', views.RankResultsView.as_view()),
)