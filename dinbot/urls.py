from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'bot.views.index', name='index'),  # noqa
    url(r'^admin/', include(admin.site.urls)),
)
