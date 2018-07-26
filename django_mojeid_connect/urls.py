"""Urls for django_mojeid_connect."""
from __future__ import unicode_literals

from django.conf.urls import include, url

from django_mojeid_connect.views import CreateUser

urlpatterns = [
    # Basic templates
    url(r'^create_user/$', CreateUser.as_view(), name='create_user'),
    # Mozilla-django-oidc views
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
]
