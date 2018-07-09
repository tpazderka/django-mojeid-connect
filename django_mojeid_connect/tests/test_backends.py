"""Unittests for backends."""
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.backends.cache import SessionStore
from django.test import RequestFactory, TestCase, override_settings
from django_oidc_sub.models import OidcUserSub

from django_mojeid_connect.backends import MojeidOidcBackend


@override_settings(OIDC_OP_AUTHORIZATION_ENDPOINT='http://example/oidc/authorization',
                   OIDC_OP_TOKEN_ENDPOINT='http://example/oidc/token',
                   OIDC_OP_USER_ENDPOINT='http://example/oidc/user',
                   OIDC_RP_CLIENT_ID='clientid',
                   OIDC_RP_CLIENT_SECRET='client_secret')
class TestMojeidOidcBackend(TestCase):
    """Unittests for MojeidOidcBackend."""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='test')
        request = RequestFactory().get('/')
        request.session = SessionStore()
        request.user = AnonymousUser()
        cls.backend = MojeidOidcBackend()
        cls.backend.request = request

    def test_no_user(self):
        queryset = self.backend.filter_users_by_claims({'sub': 'aaa'})
        self.assertQuerysetEqual(queryset.values_list('username'), [], transform=tuple)

    def test_match_sub(self):
        OidcUserSub.objects.create(user=self.user, sub='aaa')
        queryset = self.backend.filter_users_by_claims({'sub': 'aaa'})
        self.assertQuerysetEqual(queryset.values_list('username'), [('test',)], transform=tuple)

    def test_pairing(self):
        self.backend.request.user = self.user
        queryset = self.backend.filter_users_by_claims({'sub': 'aaa'})
        self.assertQuerysetEqual(queryset.values_list('username'), [('test',)], transform=tuple)
        self.assertQuerysetEqual(OidcUserSub.objects.filter(sub='aaa').values_list('user__username'),
                                 [('test',)], transform=tuple)
