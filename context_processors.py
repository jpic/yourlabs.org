from datetime import date

from django.utils.translation import ugettext as _

from fanzine.models import *

from forms import SubscriptionForm

def global_context(request):
    context = {}

    form_class = SubscriptionForm
    context['subscription_form_status'] = None

    if request.method == 'POST' and \
        request.POST.get('subscription_form', False):
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save(request)
            context['subscription_form_status'] = 'passed'
            context['messages'] = (
                _('your subscription was saved, thanks for choosing yourlabs.org'),
            )
        else:
            context['subscription_form_status'] = 'failed'

    else:
        form = form_class()

    context['subscription_form'] = form

    return context
