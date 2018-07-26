"""Views for django_mojeid_connect."""
from __future__ import unicode_literals

from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import CreateView


class CreateUser(CreateView):
    """
    View for creating and pairing user to mojeID.

    This is intended as a demonstration view for pairing of an existing user.
    If user is logged in, then the only requested attribute is `sub` which is then used to create the binding.
    """

    model = get_user_model()
    fields = ['username']
    template_name = 'create_user.html'
    success_url = reverse_lazy('oidc_authentication_init')

    def form_valid(self, form):
        """Log user in and initiate pairing."""
        response = super(CreateUser, self).form_valid(form)
        login(self.request, self.object)
        return response
