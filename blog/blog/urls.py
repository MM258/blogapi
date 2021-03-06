from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    url(r'^blogapi/', include('blogapi.urls', namespace='blogapi')),

    url(r'^admin/', include(admin.site.urls)),
    # api
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

    url(r'^api/', include('api.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
