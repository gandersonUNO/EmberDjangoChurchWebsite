from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^churchevents/(?P<pk>[0-9]+)', csrf_exempt(controllers.ChurchEventDetail.as_view())),
    url(r'^alerts/(?P<pk>[0-9]+)', csrf_exempt(controllers.AlertDetail.as_view())),
	url(r'^churchevents', csrf_exempt(controllers.ChurchEventList.as_view())),
    url(r'^alerts', csrf_exempt(controllers.AlertList.as_view())),
    url(r'^', include(router.urls)),
]
