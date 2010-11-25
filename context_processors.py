from datetime import date

from fanzine.models import *

from forms import SubscriptionForm

def global_context(request):
    context = {}

    context['subscription_form'] = SubscriptionForm()

    return context
