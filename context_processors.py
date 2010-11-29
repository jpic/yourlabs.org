from datetime import date
from datetime import datetime

from django.utils.translation import ugettext as _

from fanzine.models import *
from pinax.apps.blog.models import *

from forms import SubscriptionForm


def previous_posts(request):
    context = {}
    qs = Post.objects.filter(publish__lte=datetime.now())
    qs = qs.select_related()
    context['previous_posts'] = qs.all()[:7]
    return context

def next_posts(request):
    context = {}
    qs = Post.objects.filter(publish__gt=datetime.now())
    qs = qs.select_related()
    if request.user.is_staff and qs.count():
        context['next_posts'] = qs.all()[:7]
    return context

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
