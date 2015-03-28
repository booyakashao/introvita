from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^', include('introvita_user_interact.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
