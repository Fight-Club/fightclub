from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from whowin.views import FightView, RankResultsView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include("account.urls")),
    url(r'^$', include('whowin.urls')),
    url(r'^results/$', RankResultsView.as_view()),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
