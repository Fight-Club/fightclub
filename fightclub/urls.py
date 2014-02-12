from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from fights.views import FightView, random_fight

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include("account.urls")),
    url(r'^$', random_fight, name='home'),
    url(r'^fight/(?P<fight_id>\d+)/$', FightView.as_view(), name='fight_view'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
