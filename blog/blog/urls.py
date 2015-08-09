from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    url(r'^blog/', include('blogapi.urls', namespace='api')),

    url(r'^admin/', include(admin.site.urls)),
)
