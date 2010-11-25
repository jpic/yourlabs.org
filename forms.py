import re

from django import forms
from django.contrib.auth.models import User, Group
from pinax.apps.account.forms import SignupForm
from django.utils.translation import ugettext as _

import utils

class SubscriptionForm(forms.Form):
    email = forms.EmailField()
    infrastructure = forms.BooleanField(widget=forms.CheckboxInput, 
        required=False)

    def clean_email(self):
        value = self.cleaned_data.get('email')
        if User.objects.filter(email=value).count():
            raise forms.ValidationError(_('this email is already subscribed!'))
        return value

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
        group, created = Group.objects.get_or_create(name=u'optin')
        user.groups.add(group)

        return user
