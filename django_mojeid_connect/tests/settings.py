from __future__ import unicode_literals

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_oidc_sub',
    'mozilla_django_oidc',
    'django_mojeid_connect',
)

MIDDLEWARE = []

AUTH_USER_MODEL = 'auth.User'

SECRET_KEY = 'TOP_SECRET_DO_NOT_SHARE'
