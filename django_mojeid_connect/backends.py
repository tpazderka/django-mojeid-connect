"""Backend for django_mojeid_connect with pairing capability."""
from __future__ import unicode_literals

from django_oidc_sub.backends import OidcSubBackend
from django_oidc_sub.models import OidcUserSub


class MojeidOidcBackend(OidcSubBackend):
    """Backend that pairs mojeid users to currently logged user."""

    def filter_users_by_claims(self, claims):
        """Retrieve and pair user."""
        query = super(MojeidOidcBackend, self).filter_users_by_claims(claims)
        self.request.session['oidc_claims'] = claims
        if query.exists():
            # Sub-User pairing found, continue with login
            return query
        elif self.request.user.is_authenticated:
            # No Sub-User pairing found but user is logged in -> pair
            OidcUserSub.objects.create(sub=claims['sub'], user=self.request.user)
            return super(MojeidOidcBackend, self).filter_users_by_claims(claims)
        return query
