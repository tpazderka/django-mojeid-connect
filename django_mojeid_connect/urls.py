"""Urls for django_mojeid_connect."""
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.views.generic import TemplateView

from django_mojeid_connect.views import CreateUser

urlpatterns = [
    # Basic templates
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    url(r'^failed_login/$', TemplateView.as_view(template_name='login_fail.html'), name='fail_login'),
    url(r'^result/$', TemplateView.as_view(template_name='login_results.html'), name='login_result'),
    url(r'^create_user/$', CreateUser.as_view(), name='create_user'),
    # Mozilla-django-oidc views
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
]
