"""Unittests for views."""
from __future__ import unicode_literals

from django.contrib import auth
from django.test import TestCase, override_settings


@override_settings(ROOT_URLCONF='django_mojeid_connect.urls',
                   MIDDLEWARE=['django.contrib.sessions.middleware.SessionMiddleware'])
class TestCreateUser(TestCase):
    """Unittests for CreateUser helper view."""

    def test_post(self):
        response = self.client.post('/create_user/', {'username': 'test'})
        self.assertRedirects(response, '/oidc/authenticate/', fetch_redirect_response=False)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertEqual(user.username, 'test')
