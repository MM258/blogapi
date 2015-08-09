from django.conf.urls import patterns, include, url
from blogapi import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blogapi.urls')),
    url(r'^$',views.index),
    # url(r'^blog/$',views.blog),
    # url(r'^about_us/$',views.about_us),
    # url(r'^contact_us/$',views.contact_us),
    # url(r'^case/$',views.case),

)
