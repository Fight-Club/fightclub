from django.conf.urls import patterns, url

from whowin import views

urlpatterns = patterns('',
    url(r'^$', views.MatchView.as_view()),
    url(r'^results/$', views.MatchResultsView.as_view()),
)