import re

from django import forms
from django.contrib.auth.models import User
from pinax.apps.account.forms import SignupForm

import utils

class SubscriptionForm(forms.Form):
    email = forms.EmailField()
    infrastructure = forms.BooleanField(widget=forms.CheckboxInput, 
        required=False)

    def save(self, request):
        username = re.sub('[^a-zA-Z0-9_]', '', self.cleaned_data.get('email'))
        password = utils.ranpwd()

        while User.objects.filter(username=username):
            username = username + '_'

        signup = SignupForm({
            'username': username,
            'email': self.cleaned_data.get('email'),
            'password1': password,
            'password2': password,
        })

        if not signup.is_valid():
            raise Exception("Signup doesn't validate!")

        user = signup.save()
        user.profile.newsletter_subscription = True
        user.profile.infrastructure_subscription = self.cleaned_data.get(
            'infrastructure', False)
        user.profile.save()
