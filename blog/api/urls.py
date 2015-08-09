from django.conf.urls import patterns, url, include

from rest_framework import routers
# from api.routers import CustomAPIRouter

from blogapi.rest.views import blogapiset

router = routers.DefaultRouter()
router.register(r'blogapi',blogapiset)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)